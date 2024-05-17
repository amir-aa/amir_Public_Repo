<?php
class DB{
    protected $conn_instance;
    public function __construct($host,$username,$password,$dbname){    
       $this->conn_instance=new mysqli();
       $this->conn_instance->options(MYSQLI_OPT_CONNECT_TIMEOUT,120);
       $this->conn_instance->connect($host,$username,$password,$dbname);
    }

    public function runQuery($query){
        $this->conn_instance->query($query);
        $this->conn_instance->close();
    }
}
$con=new DB("localhost","test","1234","phptest");
$con->runQuery("insert into users(name,email) VALUES('ali','ali@a.com')");

