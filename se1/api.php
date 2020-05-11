<?php
header("Content-Type:application");
require "../se1/data.php";

if(!empty($_GET['name']))
{
	$name=$_GET['name'];
	$Rooms = get_Rooms($name);
	
	if(empty($Rooms))
	{
		response(NULL);
	}
	else
	{
		response($Rooms);
	}	
}
else
{
	response(NULL);
}

function response($data)
{
	header("HTTP/1.1 ");
	
	echo $data;
}

?>
