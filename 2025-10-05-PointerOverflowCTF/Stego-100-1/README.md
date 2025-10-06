# Stego 100-1 Ink Between the Lines
## Introduction
Sweet Gentlepersons, I have forsaken my life as a humble educator and have decided henceforth to become a bard. I am certain you will agree that I have what it takes when you witness my genius, thusly. Now, I am certain that you will doubt that it is my own creation. So, to eschew any accusations, I provide you a commemorative copy of this poem, secured and verified by digital means. 

## Files
* [leaflet.txt](leaflet.txt)

## Investigation
The txt file contains a poem. From it we can deduce there are hidden chars which we need to interpret. Highlighting the text we can see each line has a suffix consisting of tabs and spaces. Since there are two types we try converting them to binary values.

```python
binary = ""
with open("input.txt", "r") as f:
    for line in f:
        if '.' in line:
            after_dot = line.split('.')[-1].rstrip('\n')
            for char in after_dot:
                if char == ' ':
                    binary += '0'
                elif char == '\t':
                    binary += '1'
```
```text
01110011011101110110010101100101011101000110100001100101011000010111001001110100001000000110100101110011001000000111010001101000011110010010000001100011011000010110110001101100
```

From here we can convert it into ASCII.

```python
decoded = ''.join(
    chr(int(binary[i:i+8], 2))
    for i in range(0, len(binary), 8)
)
```
```text
sweetheart is thy call
```

Can't really see what to do with this phrase from here. So we assume this is the flag and apply the formatting specified in the rules.


```python
substitutions = {
    " ": "_",
    'a': '4',
    'e': '3',
    'i': '1',
    'o': '0',
    's': '5',
    't': '7'
}

leet_phrase = ''.join(substitutions.get(c, c) for c in decoded)
flag = f"poctf{{uwsp_{leet_phrase}}}"
```

This prints out the flag.

## Flag
<details>
<summary>Click to reveal the flag</summary>

```text
poctf{uwsp_5w337h34r7_15_7hy_c4ll}
```