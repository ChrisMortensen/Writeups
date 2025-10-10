# Snooze
## Introduction
Don't bug me, I'm sleeping! Zzzz... zzz... zzzz....

Uncover the flag from the file presented.

## File
* [snooze](snooze)

## Investigation
We try to get some info about the file:

```bash
$ file snooze 
snooze: compress'd data 16 bits
```

We try to decompress the file using different programs:
- `tar`   : This does not return anything.
- `GNOME` : An error occurred while extracting files.
- `7zip`  : Creates a file called `snooze~`.

Inside `snooze~` is the flag in plaintext.

## Flag
<details>
<summary>Click to reveal the flag</summary>

```text
flag{c1c07c90efa59876a97c44c2b175903e}
```