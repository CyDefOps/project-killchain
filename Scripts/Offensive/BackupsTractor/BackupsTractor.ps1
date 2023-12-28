param (
    [string]$keyword
)

function Search-Files {
    param (
        [string]$searchPath,
        [string]$keyword
    )

    Get-ChildItem -Recurse $searchPath |
        ForEach-Object {
            try {
                $content = Get-Content $_.FullName -Raw
                if ($content -match $keyword) {
                    Write-Host "Found '$keyword' in: $($_.FullName)"
                }
            } catch {
                Write-Host "Error reading $($_.FullName): $_"
            }
        }
}

function Show-Banner {
    $banner = @"
    ____             __                   ______                __            
   / __ )____ ______/ /____  ______  ____/_  __/________ ______/ /_____  _____
  / __  / __ `/ ___/ //_/ / / / __ \/ ___// / / ___/ __ `/ ___/ __/ __ \/ ___/
 / /_/ / /_/ / /__/ ,< / /_/ / /_/ (__  )/ / / /  / /_/ / /__/ /_/ /_/ / /    
/_____/\__,_/\___/_/|_|\__,_/ .___/____//_/ /_/   \__,_/\___/\__/\____/_/     
                           /_/                                                

Coded By: Kamran Saifullah, Umar Javed
https://cydefops.com
https://github.com/CyDefOps/project-killchain

Usage: BackupsTractor.ps1 <Search String>
"@
    Write-Host $banner
}

Show-Banner

$usersFolder = "C:\Users"
foreach ($userFolder in Get-ChildItem $usersFolder -Directory) {
    $backupPath = Join-Path $userFolder.FullName "AppData\Roaming\Notepad++\backup"

    if (Test-Path $backupPath) {
        Write-Host "Searching in $backupPath for '$keyword'"
        Search-Files -searchPath $backupPath -keyword $keyword
    }
}
