## natas0

quite easy, just look at html source code and you can find

## natas1

similar with level0, password hidding in the html

## natas2

there is a "files" in it's source, let's check what's in it, a "users.txt" and there is the password

## natas3

"not even google will help" ok check the "robots.txt"!

## natas4

Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"

ok change the headers

## natas5

Access disallowed. You are not logged in

well check the cookies
loggedin=0

good just set it to 1

## natas6

from the "Source Code" we can find that there is a magic page "/includes/secret.inc", just post secret from it

## natas7

good hint from html "hint: password for webuser natas8 is in /etc/natas_webpass/natas8"

## natas8

good still from source code

```php
$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret)
```

## natas9

```php
if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
```

hmm I am not interested in this dictionary.txt of course!, using ; to do whatever we need

## natas10

ok "Input contains an illegal character!" this time

```php
if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
```

then we just match every thing