# pwgen
## Introduction
MyPassword policies aren't always great. That's why we generate passwords for our users based on a strong master password!

We get the following:
* http://52.59.124.14:5003

## Investigation
When opening the webstite we are greeted with some text and telling us to have a look at the [source code for the website](source.php).

The site works by taking the flag, shuffelling the characters, and displaying those as the password for the user.

```php
include "flag.php";

$shuffle_count = abs(intval($_GET['nthpw']));

[...]

srand(0x1337); // the same user should always get the same password!

for($i = 0; $i < $shuffle_count; $i++) {
    $password = str_shuffle($FLAG);
}

if(isset($password)) {
    echo "Your password is: '$password'";
}
```

The vulnerability here is that the randomness is seeded, meaning we can reproduce the shuffeling using the same seed.

## Exploitation

First we get a shuffle of the flag by setting the query string parameter `nthpw`, in this case I chose `2`. We can now set these values as known variables in our script.

```php
$shuffled = "7F6_23Ha8:5E4N3_/e27833D4S5cNaT_1i_O46STLf3r-4AH6133bdTO5p419U0n53Rdc80F4_Lb6_65BSeWb38f86{dGTf4}eE8__SW4Dp86_4f1VNH8H_C10e7L62154";
$shuffle_count = 2;
$seed = 0x1337;
```

We solve the challenge by first creating a token string using unique bytes. 

```php
$len = strlen($shuffled);
$tokens = "";
for ($i = 1; $i <= $len; $i++) {
    $tokens .= chr($i);
}
```

We can then shuffle these bytes using the seed we were given.

```php
srand($seed);
$perm = $tokens;
for ($i = 0; $i < $shuffle_count; $i++) {
    $perm = str_shuffle($tokens);
}
```

Now we know the former location of each byte based on their value, and their current one based on their position in the string. So, from here we basically have maped the shuffeling of the characters. Meaning, we can take this map of shuffeling in the opposite direction on the shuffled flag in order to unshuffel it.

```php
$original = array_fill(0, $len, '');
for ($j = 0; $j < $len; $j++) {
    $k = ord($perm[$j]) - 1;
    $original[$k] = $shuffled[$j];
}
$flag = implode('', $original);
echo "Flag: $flag\n";
```

Running [the script](seeded_anti_shuffle.php) returns:

```
Flag: ENO{N3V3r_SHUFFLE_W1TH_STAT1C_S333D_OR_B4D_TH1NGS_WiLL_H4pp3n:-/_0d68ea85d88ba14eb6238776845542cf6fe560936f128404e8c14bd5544636f7}
```
