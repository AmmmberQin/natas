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

## natas26


```php
$drawing=unserialize(base64_decode($_COOKIE["drawing"]));
```
unserialize good!

```php
class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct($file){
            // initialise variables
            $this->initMsg="#--session started--#\n";
            $this->exitMsg="#--session end--#\n";
            $this->logFile = "/tmp/natas26_" . $file . ".log";
      
            // write initial message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$initMsg);
            fclose($fd);
        }                       
      
        function log($msg){
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$msg."\n");
            fclose($fd);
        }                       
      
        function __destruct(){
            // write exit message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$this->exitMsg);
            fclose($fd);
        }                       
    }
```

this is a useful class, as it write something whatever, what we need is to construct a instance at first


## natas27

mysql_real_escape_string() calls MySQL's library function mysql_real_escape_string, which prepends backslashes to the following characters: \x00, \n, \r, \, ', " and \x1a.

so using ' to have a sql injection is not working

```sql
/* 
CREATE TABLE `users` ( 
  `username` varchar(64) DEFAULT NULL, 
  `password` varchar(64) DEFAULT NULL 
); 
*/ 
```

varchar will  remove the characters over the length limit, and remove space in the end.

So we can create another "natas28" user

## natas28

interesting search, look at the url carefully, this is a cipher+Sql injection attack