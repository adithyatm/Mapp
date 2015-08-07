<?php

$url = "https://tenmilesadithya.happyfox.com/api/1.1/json/tickets/";
$api_key = "43d5e36d980541cc88ce838b54365207";
$auth_code = "9bb36ea082ce4c15839c934218c6bc4c";

//$filePath = "/Users/adithya/Desktop/rajni.jpg";
//$file1 = '@/' . realpath($filePath);

$data = array (
    "subject"=> "Test subject",
    "text"=> "Test message",
    "category"=> 1,
    "priority"=> 1,
    "email"=> "adithya.pk@tenmiles.com",
    "name"=> "Adithya",
   // "attachments"=> $file1
);

$headers = array("Content-Type:multipart/form-data");
$ch = curl_init();
$options = array(
    CURLOPT_URL => $url,
    CURLOPT_HEADER => true,
    CURLOPT_POST => 1,
    CURLOPT_HTTPHEADER => $headers,
    CURLOPT_POSTFIELDS => $data,
    CURLOPT_INFILESIZE => $filesize,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_BINARYTRANSFER => true,
    CURLOPT_USERPWD => $api_key . ":" . $auth_code
);

curl_setopt_array($ch, $options);
$result = curl_exec($ch);
if(!curl_errno($ch))
{
    $info = curl_getinfo($ch);
    echo $info['http_code'];

    if($info['http_code'] == 500){
        error_log(var_dump($info));
    }else{
        echo json_decode($result,true);
    }

    if ($info['http_code'] == 200) {
        $errmsg = "File uploaded successfully";
    }
}
else
{
    $errmsg = curl_error($ch);
}
curl_close($ch);

echo $errmsg

?>