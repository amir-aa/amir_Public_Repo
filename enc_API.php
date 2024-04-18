<?php

require_once 'vendor/autoload.php';

use \Defuse\Crypto\Crypto;
use \Defuse\Crypto\Key;


function encryptData($data, $key) {
    $cipher = Crypto::encrypt($data, $key);
    return $cipher;
}


function decryptData($cipher, $key) {
    $plain_text = Crypto::decrypt($cipher, $key);
    return $plain_text;
}

//Endpoint for enc
if ($_SERVER['REQUEST_METHOD'] === 'POST' && $_SERVER['REQUEST_URI'] === '/encrypt') {
    $requestData = json_decode(file_get_contents('php://input'), true);
    $key = hex2bin($requestData['key']);
    $data = base64_decode($requestData['data']);
    
    try {
        $cipher = encryptData($data, $key);
        echo base64_encode($cipher);
    } catch (\Exception $e) {
        http_response_code(400);
        echo $e->getMessage();
    }
    exit;
}

//Endpoint for dec
if ($_SERVER['REQUEST_METHOD'] === 'POST' && $_SERVER['REQUEST_URI'] === '/decrypt') {
    $requestData = json_decode(file_get_contents('php://input'), true);
    $key = hex2bin($requestData['key']);
    $cipher = base64_decode($requestData['data']);

    try {
        $plain_text = decryptData($cipher, $key);
        echo base64_encode($plain_text);
    } catch (\Exception $e) {
        http_response_code(400);
        echo $e->getMessage();
    }
    exit;
}

// Respond with 404 for invalid routes
http_response_code(404);
echo "Not Found";
?>
