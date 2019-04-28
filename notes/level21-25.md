## natas21

```php
if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1)
```

another session exploit

haha so easy

```php
if(array_key_exists("submit", $_REQUEST)) { 
    foreach($_REQUEST as $key => $val) { 
    $_SESSION[$key] = $val; 
    } 
} 
```

## natas22

```php
<? 
session_start(); 

if(array_key_exists("revelio", $_GET)) { 
    // only admins can reveal the password 
    if(!($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1)) { 
    header("Location: /"); 
    } 
} 
?> 
```
...

```php
<? 
    if(array_key_exists("revelio", $_GET)) { 
    print "You are an admin. The credentials for the next level are:<br>"; 
    print "<pre>Username: natas23\n"; 
    print "Password: <censored></pre>"; 
    } 
?> 
```

hmm not allow redirect??

## natas23

```php
if(strstr($_REQUEST["passwd"],"iloveyou") && ($_REQUEST["passwd"] > 10 )){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas24 Password: <censored></pre>";
        }
```
hmm php Type juggling

## natas24

```txt
If I set $_GET['password'] equal to an empty array, then strcmp would return a NULL. Due to some unherent weaknesses in PHP's comparisons, NULL == 0 will return true (more info)).
```

## natas25

```php
$log=$log . " " . $_SERVER['HTTP_USER_AGENT'];
$log=$log . " \"" . $message ."\"\n"; 
$fd=fopen("/var/www/natas/natas25/logs/natas25_" . session_id() .".log","a");
```

inject something in User-Agent, and then read from the log file
