<?php

function get_Rooms($name)
{
	$products = [
		"Bliss"=>12,
		"Gage"=>16,
		"Ridgeview"=>24		
	];
	
	foreach($products as $product=>$Rooms)
	{
		if($product==$name)
		{
			return $Rooms;
			break;
		}
	}
}

?>
