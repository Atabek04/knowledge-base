# Builds the wiki locally with Quartz and serves it at
# http://localhost:8080/knowledge-base/ (the same subpath as GitHub Pages, so
# explorer links, which are built from baseUrl, resolve exactly as in production).
# Mirrors .github/workflows/publish.yml. Quartz is cloned once into
# %LOCALAPPDATA%\quartz-kb and reused; pass -Update to pull the latest v5.
#
#   .\scripts\site-preview.ps1            # build + serve
#   .\scripts\site-preview.ps1 -BuildOnly # build into %LOCALAPPDATA%\quartz-kb\preview\knowledge-base
#   .\scripts\site-preview.ps1 -Update    # git pull Quartz first
#   .\scripts\site-preview.ps1 -Port 9000
param(
    [switch]$BuildOnly,
    [switch]$Update,
    [int]$Port = 8080
)

$ErrorActionPreference = "Stop"
$vault = Split-Path -Parent $PSScriptRoot
$quartz = Join-Path $env:LOCALAPPDATA "quartz-kb"
$preview = Join-Path $quartz "preview"
$subpath = "knowledge-base"   # must match the last segment of baseUrl in site/quartz.config.yaml
$out = Join-Path $preview $subpath

if (-not (Test-Path $quartz)) {
    git clone --depth 1 -b v5 https://github.com/jackyzha0/quartz.git $quartz
    Push-Location $quartz; npm ci; Pop-Location
} elseif ($Update) {
    Push-Location $quartz; git pull; npm ci; Pop-Location
}

# overlay: config, overrides, styles, fonts, landing page
Copy-Item (Join-Path $vault "site\quartz.config.yaml") $quartz -Force
Copy-Item (Join-Path $vault "site\quartz.ts") $quartz -Force
Copy-Item (Join-Path $vault "site\custom.scss") (Join-Path $quartz "quartz\styles\custom.scss") -Force
New-Item -ItemType Directory -Force (Join-Path $quartz "quartz\static\fonts") | Out-Null
Copy-Item (Join-Path $vault "site\fonts\*") (Join-Path $quartz "quartz\static\fonts") -Force
Copy-Item (Join-Path $vault "site\favicon\icon.png") (Join-Path $quartz "quartz\static\icon.png") -Force
Copy-Item (Join-Path $vault "site\index.md") (Join-Path $vault "index.md") -Force

New-Item -ItemType Directory -Force $preview | Out-Null
Push-Location $quartz
try {
    npx quartz plugin install --from-config
    node (Join-Path $vault "site\patch-graph.mjs")
    if ($LASTEXITCODE -ne 0) { throw "graph patch failed" }
    npx quartz build -d $vault -o $out
} finally {
    Pop-Location
    Remove-Item (Join-Path $vault "index.md") -Force -ErrorAction SilentlyContinue
}

if ($BuildOnly) { return }

# root redirect to the subpath
Set-Content -Path (Join-Path $preview "index.html") -Encoding utf8 -Value "<meta http-equiv=`"refresh`" content=`"0; url=/$subpath/`">"

Write-Host ""
Write-Host "  Preview: http://localhost:$Port/$subpath/" -ForegroundColor Green
Write-Host ""
npx --yes serve $preview -l $Port
