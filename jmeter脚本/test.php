<?php
$appKey    = 'asdafas';
$timestamp = 1892367612;
$requestId = 'aksjhdufifbxuhdy';
$arr = [
     $appKey,
     $timestamp,
     $requestId
];
sort($arr, SORT_STRING);
$implodeString = implode($arr);
$signature     = sha1($implodeString);
var_dump($signature);
