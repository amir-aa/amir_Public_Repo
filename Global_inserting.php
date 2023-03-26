<?php
$servername="ip:port";
$username="username";
$password="pass";
$DBNAME="DB";
$date = date('d-m-y h:i:s');
$con = new mysqli($servername, $username, $password, $DBNAME);
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql="insert into ";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}




$conn->close();
?>