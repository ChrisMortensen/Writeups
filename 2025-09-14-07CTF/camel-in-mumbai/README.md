#  Camel in Mumbai (forensics)
## Introduction
Stuck and stranded in the traffic of mumbai...

We get the following:
* [camel_in_mumbai](camel_in_mumbai)

## Investigation
First we check the filetype and architecture.

```bash
file ./camel_in_mumbai
camel_in_mumbai: ELF 64-bit LSB pie executable, x86-64, [...]
```

A 64-bit ELF binary means we need to run it on Linux. I choose to use Kali Linux.

We run the binary to see behaviour.

```bash
$ ./camel_in_mumbai 
zsh: permission denied: ./camel_in_mumbai
```
Since binary is not executable we change its permissions.

```bash
chmod +x ./camel_in_mumbai
```

We try to run the binary again.

```bash
$ ./camel_in_mumbai         
camels are lovely aren't they?
```

There is nothing interactive.

From here we search the binary for any strings containing the prefix of the flag, that being `07CTF`.
```bash
strings camel_in_mumbai | grep '07CTF' 
```

Nothing is returned.

We make the binary print its use of library calls during runtime using `ltrace`. 

`ltrace` writes to `stderr`. So we redirect `stderr` into `stdout` before piping to `grep`.

```bash
$ ltrace ./camel_in_mumbai 2>&1 | grep '07CTF'          
memmove(0x7f9704bfea38, "07CTF{C4m3ls_4r3_Tr4sh_As_Hell}", 31) = 0x7f9704bfea38
```

## Flag
<details>
<summary>Click to reveal the flag</summary>

```text
07CTF{C4m3ls_4r3_Tr4sh_As_Hell}
```