# Written by Kamran Saifullah
# https://linkedin.com/in/KamranSaifullah
# https://github.com/CyDefOps/project-killchain
# https://cydefops.com
# 17-October-23

# Change the IPAddr.txt to the file name of your choice which holds the data.

$list = Get-Content "IPAddr.txt"

foreach ($comp in $list) {

    # Change the 443 to 80 to test for HTTP. 
    
    $pingTest = Test-NetConnection -ComputerName $comp -Port 443

    if($pingTest) {

    Write-Host($comp + " is online")

    }

    else {

    Write-Host($comp + " is offline")

    }

}
