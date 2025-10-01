# Spam Test
## Introduction
Time to do some careful Googling... what's the MD5 hash of the Generic Test for Unsolicited Bulk Email (GTUBE) string?

Submit the hash wrapped within the flag{ prefix and } suffix to match the standard flag format.

## Investigation
This should be easy. Lets search up the `Generic Test for Unsolicited Bulk Email (GTUBE) string`.

````text
XJS*C4JDBQADN1.NSBN3*2IDNEN*GTUBE-STANDARD-ANTI-UBE-TEST-EMAIL*C.34X
```
```bash
$ echo -n 'XJS*C4JDBQADN1.NSBN3*2IDNEN*GTUBE-STANDARD-ANTI-UBE-TEST-EMAIL*C.34X' | md5sum 
6a684e1cdca03e6a436d182dd4069183
```

We format this as specified in the introduction.

## Flag
<details>
<summary>Click to reveal the flag</summary>

```text
flag{6a684e1cdca03e6a436d182dd4069183}
```