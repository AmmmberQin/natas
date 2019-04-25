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

## natas18

```php
$maxid = 640;
...
if(my_session_start()) { 
    print_credentials(); 
    $showform = false; 
} else { 
    if(array_key_exists("username", $_REQUEST) && array_key_exists("password", $_REQUEST)) { 
    session_id(createID($_REQUEST["username"])); 
    session_start(); 
    $_SESSION["admin"] = isValidAdminLogin(); 
    debug("New session started"); 
    $showform = false; 
    print_credentials(); 
    } 
}  
```

```php
function my_session_start() { /* {{{ */ 
    if(array_key_exists("PHPSESSID", $_COOKIE) and isValidID($_COOKIE["PHPSESSID"])) { 
    if(!session_start()) { 
        debug("Session start failed"); 
        return false; 
    } else { 
        debug("Session start ok"); 
        if(!array_key_exists("admin", $_SESSION)) { 
        debug("Session was old: admin flag set"); 
        $_SESSION["admin"] = 0; // backwards compatible, secure 
        } 
        return true; 
    } 
    } 

    return false; 
} 
```
we need find the magic sessionid for admin, just 640 try, easy bruteforce

## natas19

This page uses mostly the same code as the previous level, but session IDs are no longer sequential

analysis the cookie "PHPSESSID" when I input admin as username "3334322d61646d696e" hex of course, convert based on ascii table "342-admin" good

## natas20

well from debug mode, I hit "Session file doesn't exist" all the time

so what will happen if the session file exist

```php
function myread($sid) {  
    ...
    if(!file_exists($filename)) { 
        debug("Session file doesn't exist"); 
        return ""; 
    } 
    debug("Reading from ". $filename); 
    $data = file_get_contents($filename); 
    $_SESSION = array(); 
    foreach(explode("\n", $data) as $line) { 
        debug("Read [$line]"); 
    $parts = explode(" ", $line, 2); 
    if($parts[0] != "") $_SESSION[$parts[0]] = $parts[1]; 
    } 
    return session_encode(); 
} 
```
it will set `$_SESSION[$parts[0]] = $parts[1]` hmm good what is $parts[0] is admin and $parts[1] is 1 then we can get the password

then set "name" = "admin 1" let's try, ah "DEBUG: Read [name admin 1]" not right as `$data .= "$key $value\n";`. but easy to by pass 
