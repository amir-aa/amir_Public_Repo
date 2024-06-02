<?php
set_time_limit(0);
$mystring="SALAM THIS IS MY LOG";
$length=strlen($mystring);

$socket=socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($socket===false) { echo "WOW I can Not Make socket";}
$conn_result=socket_connect($socket, "127.0.0.1", 10000);
if ($conn_result===false) { echo "Connection Aborted";}
while ($length>0){
$sent_len= socket_write($socket, $mystring,$length);
if ($sent_len===false) { echo "ERROR on Writing DATA on SOCKET ". socket_strerror(socket_last_error($socket));break;}
$length-=$sent_len;
