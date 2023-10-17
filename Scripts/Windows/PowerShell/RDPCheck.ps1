# Written by Kamran Saifullah
# https://linkedin.com/in/KamranSaifullah
# https://github.com/CyDefOps/project-killchain
# https://cydefops.com
# 17-October-23

# Change the RDPSystems.txt to the file name of your choice which holds the data.
$comp = $list = Get-Content "RDPSystems.txt"

foreach ($comp in $list) {

    $pingTest = New-Object System.Net.Sockets.TCPClient -ArgumentList $comp,3389

    if($pingTest) {

    Write-Host($comp + " is online")

    }

    else {

    Write-Host($comp + " is offline")

    }

}
