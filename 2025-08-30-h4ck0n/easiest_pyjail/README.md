# Easiest Pyjail
## Introduction
We get the following:
* nc h4ckc0n.d4rkc0de.in 33209

## Exploitation
When running `nc h4ckc0n.d4rkc0de.in 33209` we find ourselves inside a python interpreter. Since its called Easiest Pyjail i expect minimal restrictions.
We start by trying to gain some information about how Python was invoked.

```pycon
>>> print(open('/proc/self/cmdline').read())
python3 challenge.py
```
Here we get the exact command-line arguments used. Since we know have the name of the file we can try to open and read it.

```pycon
>>> print(open("challenge.py").read())
```

This returned the entire files' code. Meaning, we can now see everything going on in the pyjail.
Her we see a file called 'flag.txt' was accessed and read from. Since the pyjail is supposed to be easy we can just try and read from it in order to see if there are any restrictions.

```pycon
>>> print(open("flag.txt").read())
d4rkc0de{ezZ_f0r_pyth0n_lvrs_huh?}
```
