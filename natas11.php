<?php

function xor_encrypt($in, $key) {
    $key = $key;
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function get_key(){

    $defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
    $data = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=";
    $key = json_encode($defaultdata);
    return xor_encrypt(base64_decode($data), $key);

}

$key = get_key();
$key = substr($key, 0, 4);

$defaultdata = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
$cookie = base64_encode(xor_encrypt(json_encode($defaultdata), $key));

echo $cookie;


?>