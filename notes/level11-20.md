## natas11

```php
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

...

if($data["showpassword"] == "yes") {
    print "The password for natas12 is <censored><br>";
}

```
obveriously we need to change the "showpassword" to "yes"

```php
function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}
```

and what we set will also be sent back as cookie

this is good as

```php

$tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
...

function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
```

as here the magic `xor_encrypt` "key" is censored, we need to fingure it out using the plain text we know

and be careful `$outText .= $text[$i] ^ $key[$i % strlen($key)]` the key is not that long long text you get, it is just the repulation of it.



