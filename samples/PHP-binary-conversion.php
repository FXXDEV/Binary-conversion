
<?php 

function string_to_binary($string){
	return base_convert($string[1], 16, 2);	 
}

function binary_to_string($binary){	
	return pack('H*', base_convert($binary, 2, 16));
}


var_dump(binary_to_string('01101000 01100101 01101100 01101100 01101111'));
var_dump(binary_to_string('Hello World'));


?>