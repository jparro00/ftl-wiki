# Bulk-pull FTL Fandom event pages as wikitext into raw/wiki/.
# Uses the MediaWiki API (api.php), not HTML scraping.
$ErrorActionPreference = 'Stop'
$ProgressPreference    = 'SilentlyContinue'

$base = 'https://ftl.fandom.com/api.php'

# Derived from where this script sits, not from where it was written: $PSScriptRoot is
# tools/, so its parent is the repo root wherever the repo happens to be cloned.
$out  = Join-Path (Split-Path -Parent $PSScriptRoot) 'raw\wiki'

# The MediaWiki API asks for a contact in the User-Agent. It should name whoever is
# making the requests, so it follows git's configured address rather than naming the
# person this script was written by.
$contact = (git config user.email) 2>$null
if (-not $contact) { $contact = 'unknown' }
$ua   = "ftl-event-wiki/1.0 (personal knowledge base; contact $contact)"

$today = '2026-08-09'

$cats = @(
  'Random_Events','Unique_Events','Ship_Unlocking_Events',
  'Trading_Events','Filler_Events','Events:_Rewards_and_Opportunities'
)

if (-not (Test-Path $out)) { New-Item -ItemType Directory -Path $out | Out-Null }

# --- 1. collect titles, with the categories each belongs to ---
$pages = @{}
foreach ($cat in $cats) {
  $cont = ''
  do {
    $u = "$base`?action=query&list=categorymembers&cmtitle=Category%3A$cat&cmlimit=500&cmprop=title&format=json&formatversion=2"
    if ($cont) { $u += "&cmcontinue=$cont" }
    $r = Invoke-RestMethod -Uri $u -UserAgent $ua -TimeoutSec 60
    foreach ($m in $r.query.categorymembers) {
      if ($m.ns -ne 0) { continue }
      if (-not $pages.ContainsKey($m.title)) { $pages[$m.title] = New-Object System.Collections.ArrayList }
      [void]$pages[$m.title].Add($cat)
    }
    $cont = $r.continue.cmcontinue
    Start-Sleep -Milliseconds 150
  } while ($cont)
  Write-Host ("category {0,-34} running total: {1} unique pages" -f $cat, $pages.Count)
}

Write-Host "`n=== $($pages.Count) unique pages to fetch ===`n"

# --- 2. fetch wikitext for each ---
$manifest = New-Object System.Collections.ArrayList
$ok = 0; $fail = 0; $i = 0

foreach ($title in ($pages.Keys | Sort-Object)) {
  $i++
  $slug = $title.ToLower() -replace '[^a-z0-9]+','-' -replace '(^-|-$)',''
  if ($slug.Length -gt 80) { $slug = $slug.Substring(0,80).TrimEnd('-') }
  $file = Join-Path $out "$slug.md"

  try {
    $enc = [uri]::EscapeDataString($title)
    $u = "$base`?action=parse&page=$enc&prop=wikitext|revid&format=json&formatversion=2"
    $r = Invoke-RestMethod -Uri $u -UserAgent $ua -TimeoutSec 60
    $wt = $r.parse.wikitext
    if (-not $wt) { throw "empty wikitext" }

    $cl  = ($pages[$title] -join ', ')
    $url = 'https://ftl.fandom.com/wiki/' + ($title -replace ' ','_')
    $hdr = @(
      "<!-- Retrieved from the FTL Fandom wiki via api.php on $today. Source layer: do not edit. -->",
      "Title: $title",
      "URL: $url",
      "Categories: $cl",
      "Revision: $($r.parse.revid)",
      "Retrieved: $today",
      "",
      "---",
      ""
    ) -join "`n"

    Set-Content -Path $file -Value ($hdr + $wt) -Encoding utf8
    $null = $manifest.Add([pscustomobject]@{
      Title = $title; File = "$slug.md"; Revision = $r.parse.revid; Categories = $cl
    })
    $ok++
  } catch {
    Write-Host ("  FAIL  {0} :: {1}" -f $title, $_.Exception.Message)
    $fail++
  }

  if ($i % 50 -eq 0) { Write-Host ("  ... {0}/{1} fetched" -f $i, $pages.Count) }
  Start-Sleep -Milliseconds 150
}

$manifest | Sort-Object Title | Export-Csv -Path (Join-Path $out '_manifest.csv') -NoTypeInformation -Encoding utf8

Write-Host "`n=== DONE: $ok pages written, $fail failed -> $out ==="
