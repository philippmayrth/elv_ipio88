<?php
	/* 
		This code uses the shellapi.py to read the portvalues of the "ELV IPIO88" and provide either 
		the HEX value of all Ports compined or the BIN value of the IN and OUT Ports seperatly in 2 Lines
		
		Requests should look like this:
			./webapi.php?ip=192.168.1.100&out=HEX
		or:
			./webapi.php?ip=192.168.1.100&out=BIN
	*/
	
	$DeviceIP = $_GET['ip'];
	
	// Set the Default IP if not given in the $_GET['ip'];
	if (empty($DeviceIP) == TRUE) {
		$DeviceIP = '192.168.1.100'; // Default is 192.168.1.100
	}
		
	$PathToShellAPI = "~/Desktop/dev/GitHub/elv_ipio88/shellapi.py"; //"../shellapi.py";
	$EXEC = "python $PathToShellAPI -a $DeviceIP -o HEX";
	
	// echo "Executing this: $EXEC"; // 4 debuging
	echo exec($EXEC, $OutLineByLine);
?>