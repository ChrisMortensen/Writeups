<?php

# known variables
$shuffled = "_S2N36Ni524_D1b3a6_1_SL_dV-pf4f_T4440664Hb30E85H0F6G_S95TCHF71e3f83p:1ac25O6eec3nABO{3DHRL8344e4b_S4}75W6_f1Er_N7865/Td88LWT8Ud183";
$shuffle_count = 2;
$seed = 0x1337;

$len = strlen($shuffled);

// build a token string with unique single-byte tokens
$tokens = "";
for ($i = 1; $i <= $len; $i++) {
    $tokens .= chr($i);
}

// reproduce the exact shuffle sequence
srand($seed);
$perm = $tokens;
for ($i = 0; $i < $shuffle_count; $i++) {
    $perm = str_shuffle($tokens);
}

// map the shuffled string back to the original
$original = array_fill(0, $len, '');
for ($j = 0; $j < $len; $j++) {
    $k = ord($perm[$j]) - 1;
    $original[$k] = $shuffled[$j];
}
$flag = implode('', $original);
echo "Flag: $flag\n";
