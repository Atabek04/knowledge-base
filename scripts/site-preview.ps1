# Builds the wiki locally with Quartz and serves it at http://localhost:8080.
# Mirrors .github/workflows/publish.yml. Quartz is cloned once into
# %LOCALAPPDATA%\quartz-kb and reused; pass -Update to pull the latest v5.
#
#   .\scripts\site-preview.ps1            # build + serve
#   .\scripts\site-preview.ps1 -BuildOnly # build into %LOCALAPPDATA%\quartz-kb\public
#   .\scripts\site-preview.ps1 -Update    # git pull Quartz first
param(
    [switch]$BuildOnly,
    [switch]$Update
)

$ErrorActionPreference = "Stop"
$vault = Split-Path -Parent $PSScriptRoot
$quartz = Join-Path $env:LOCALAPPDATA "quartz-kb"

if (-not (Test-Path $quartz)) {
    git clone --depth 1 -b v5 https://github.com/jackyzha0/quartz.git $quartz
    Push-Location $quartz; npm ci; Pop-Location
} elseif ($Update) {
    Push-Location $quartz; git pull; npm ci; Pop-Location
}

Copy-Item (Join-Path $vault "site\quartz.config.yaml") $quartz -Force
Copy-Item (Join-Path $vault "site\quartz.ts") $quartz -Force
Copy-Item (Join-Path $vault "site\custom.scss") (Join-Path $quartz "quartz\styles\custom.scss") -Force
Copy-Item (Join-Path $vault "site\index.md") (Join-Path $vault "index.md") -Force

Push-Location $quartz
try {
    npx quartz plugin install --from-config
    if ($BuildOnly) {
        npx quartz build -d $vault
    } else {
        npx quartz build --serve -d $vault
    }
} finally {
    Pop-Location
    Remove-Item (Join-Path $vault "index.md") -Force -ErrorAction SilentlyContinue
}
