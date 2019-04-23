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

## natas12

well I tried shellcode.php.jpg not working

```php
if(array_key_exists("filename", $_POST)) { 
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]); 
```

there is a "filename" in post data?!

```html
<input type="hidden" name="filename" value="7wtb2zypwn.jpg">
```
ah it is hidden

```php
function makeRandomPath($dir, $ext) { 
    do { 
    $path = $dir."/".genRandomString().".".$ext; 
    } while(file_exists($path)); 
    return $path; 
} 

```
so I just need to change the ext of filename to "php" then we can do something evil

## natas13

```php
else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) { 
        echo "File is not an image"; 
```

hmm ok this time I "have to" upload a image, but still simple to bypass it right, just add a special header


## natas14

```php
$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\""; 
```

SQLInject

## natas15

```php
 $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\""; 
    if(array_key_exists("debug", $_GET)) { 
        echo "Executing query: $query<br>"; 
    } 

    $res = mysql_query($query, $link); 
    if($res) { 
    if(mysql_num_rows($res) > 0) { 
        echo "This user exists.<br>"; 
    } else { 
        echo "This user doesn't exist.<br>"; 
    } 
    } else { 
        echo "Error in query.<br>"; 
    } 

```

well first I check user natas16 exists, good, then we can use SQLInject to exam(guess/bruteforce) the password

## natas16

```php
if(preg_match('/[;|&`\'"]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i \"$key\" dictionary.txt");
    }
```

no more illegal characters and with "" round. but we can still using `$()` do something

## natas17

similar with natas15, but this time without output
```php
 if(mysql_num_rows($res) > 0) { 
        //echo "This user exists.<br>"; 
    } else { 
        //echo "This user doesn't exist.<br>"; 
    } 
    } else { 
        //echo "Error in query.<br>"; 
    } 
```
this can be a "Time-Based Blind SQL Injection Attacks"
