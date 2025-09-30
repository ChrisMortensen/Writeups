# Pretty Delicious Food - Forensics
## Introduction
This cake is out of this world! :DDDDDDD

omnomonmonmonmonm

...

something else is out of place too.

Note: This is not a steganography challenge

## Files
* [prettydeliciouscakes.pdf](prettydeliciouscakes.pdf)

## Investigation
First we run some basic investigatory commands on the provided file.

```bash
$ file prettydeliciouscakes.pdf 
prettydeliciouscakes.pdf: PDF document, version 1.4, 2 page(s)
```

```bash
$ exiftool prettydeliciouscakes.pdf 
ExifTool Version Number         : 13.25
File Name                       : prettydeliciouscakes.pdf
Directory                       : .
File Size                       : 4.4 MB
File Modification Date/Time     : 2025:09:28 07:57:05-04:00
File Access Date/Time           : 2025:09:30 08:29:23-04:00
File Inode Change Date/Time     : 2025:09:28 07:58:07-04:00
File Permissions                : -rwxrw-rw-
File Type                       : PDF
File Type Extension             : pdf
MIME Type                       : application/pdf
PDF Version                     : 1.4
Linearized                      : No
Producer                        : Skia/PDF m142 Google Docs Renderer
Title                           : prettycakes
Language                        : en
Tagged PDF                      : Yes
Page Count                      : 2
```

```bash
 binwalk prettydeliciouscakes.pdf 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PDF document, version: "1.4"
1500          0x5DC           Zlib compressed data, default compression
1630          0x65E           Zlib compressed data, default compression
2259          0x8D3           Zlib compressed data, default compression
2016258       0x1EC402        Zlib compressed data, default compression
2016664       0x1EC598        Zlib compressed data, default compression
4380767       0x42D85F        Zlib compressed data, default compression
4381068       0x42D98C        Zlib compressed data, default compression
4381993       0x42DD29        Zlib compressed data, default compression
```

Jackpot. There seems to be files hidden inside the pdf. Lets extract them and take a look.

Next we search for the flag in the extracted directory.

```bash
$ grep -rnw -e 'sun' 
```

It doesn't return anything. Thus, we start looking at the files manually.

Inside the binary file `5DC` we find the following which looks like base64:

```text
const data = 'c3Vue3AzM3BfZDFzX2ZsQGdfeTAhfQ==';
```

This turns out to be the flag.

## Flag
<details>
<summary>Click to reveal the flag</summary>

```text
sun{p33p_d1s_fl@g_y0!}
```