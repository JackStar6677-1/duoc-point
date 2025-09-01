Set-StrictMode -Version Latest

if (-not (Test-Path ".venv")) {
    python -m venv .venv
}

. .\.venv\Scripts\Activate.ps1

pip install -r server/requirements.txt

if ((Test-Path "infra/.env.example") -and -not (Test-Path "infra/.env")) {
    Copy-Item "infra/.env.example" "infra/.env"
}

$envPath = "infra/.env"
if (Test-Path $envPath) {
    Get-Content $envPath | ForEach-Object {
        if ($_ -match '^\s*$' -or $_ -match '^\s*#') { return }
        $pair = $_.Split('=',2)
        if ($pair.Length -eq 2) {
            $name = $pair[0]
            $value = $pair[1]
            Set-Item -Path "env:$name" -Value $value
        }
    }
}

# Enable demo mode for exploring APIs without auth
$env:DEMO_MODE = "1"

python server/manage.py migrate --noinput
python server/manage.py runserver 8000
