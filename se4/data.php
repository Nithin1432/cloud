
<?php

function get_Rooms($name, $Rooms)
{
        /* Database INFO */
	$servername = "localhost";
	$username = "julakann1";
	$password = "38sfi7";
	$dbname = "julakann1_db";

        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);
        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
       }

       $sql = "SELECT Rooms FROM details WHERE House = '$name'";
       $result = $conn->query($sql);

        if ($result->num_rows > 0) {
             // output data of each row
             while($row = $result->fetch_assoc()) {
                      $p = $row["Rooms"];
      }
    } else {
                     $p = null;
        }

    $conn->close();

if ($p == $Rooms) 
  {
    return "true";
  }
else 
 {
  return "false";

 }

}

?>
