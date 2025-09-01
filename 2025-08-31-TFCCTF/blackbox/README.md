# Blackbox
## Introduction
Some friend of mine sent me this firmware for me to analyze. There should be some flag hidden around here...

### Files
* [ELF-File](firmware.elf)

## Exploitation
First up i want to know some information:

```bash
$ file firmware.elf
firmware.elf: ELF 32-bit LSB executable, Atmel AVR 8-bit, version 1 (SYSV), statically linked, with debug_info, not stripped
```
After a quick google search ´Atmel AVR 8-bit´ seems to be some kind of microcontroller. 

I want to try at just searching for any signs of the flag.

```bash
$ strings firmware.elf | grep 'TFC'
```

This doesn't return anything. 

From here i want to explore the contents of the file closer.

```bash
$ readelf -S firmware.elf
There are 14 section headers, starting at offset 0x1fe4:

Section Headers:
  [Nr] Name              Type            Addr     Off    Size   ES Flg Lk Inf Al
  [ 0]                   NULL            00000000 000000 000000 00      0   0  0
  [ 1] .data             PROGBITS        00800100 000378 00004e 00  WA  0   0  1
  [ 2] .text             PROGBITS        00000000 000094 0002e4 00  AX  0   0  2
  [ 3] .bss              NOBITS          0080014e 0003c6 000009 00  WA  0   0  1
  [ 4] .comment          PROGBITS        00000000 0003c6 000011 01  MS  0   0  1
  [ 5] .note.gnu.av[...] NOTE            00000000 0003d8 000040 00      0   0  4
  [ 6] .debug_aranges    PROGBITS        00000000 000418 000060 00      0   0  8
  [ 7] .debug_info       PROGBITS        00000000 000478 0007f5 00      0   0  1
  [ 8] .debug_abbrev     PROGBITS        00000000 000c6d 0005de 00      0   0  1
  [ 9] .debug_line       PROGBITS        00000000 00124b 00019a 00      0   0  1
  [10] .debug_str        PROGBITS        00000000 0013e5 000208 00      0   0  1
  [11] .shstrtab         STRTAB          00000000 001f56 00008e 00      0   0  1
  [12] .symtab           SYMTAB          00000000 0015f0 000580 10     13  28  4
  [13] .strtab           STRTAB          00000000 001b70 0003e6 00      0   0  1
[...]
```

I look for anything weird in the different sections using `avr-objdump`. But i dont find anything interesting.

At this point i believe the flag has to be hidden using some easily guessable obfuscation method somewhere inside the file. The easiest method is using XOR with a single byte.

For this i create a python file that brute forces its way to the correct key. 


In this case the key is a byte which can be any of the values 0-255. I then XOR the key with all bytes in the file and search the new file for the flag using a custom regular expression.

```python
pattern = re.compile(rb"(TFCCTF)\{[A-Za-z0-9_\-]{5,100}\}")
```

From here it loops through and print any strings that furfill the regular expression. We assume this string is a flag. However, to account for fake flags like `TFCCTF{not_the_flag}` it prints all found flags for every key.  

```python
import re

with open("firmware.elf", "rb") as f:
    data = f.read()

pattern = re.compile(rb"(TFCCTF)\{[A-Za-z0-9_\-]{5,100}\}")

for k in range(0, 2**8):
    decoded = bytes(b ^ k for b in data)
    for match in pattern.finditer(decoded):
        m = match.group()
        try:
            flag = m.decode("ascii")
        except UnicodeDecodeError:
            flag = m.decode("utf-8", errors="replace")
        print(f"Flag: {flag}")
```

This returns:

```
Flag: TFCCTF{Th1s_1s_som3_s1mpl3_4rdu1no_f1rmw4re}
```