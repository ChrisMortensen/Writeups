# BigMak - Misc
## Introduction
I tried typing out the flag for you, but our Astronaut Coleson seems to have changed the terminal's keyboard layout? He went out to get a big mak so I guess we're screwed. Whatever, here's the flag, if you can somehow get it back to normal.

rlk{blpdfp_iajylg_iyi}

## Investigation
First we find a website that can do keyboard layout mapping, that being [AWSM](https://awsm-tools.com/keyboard-layout).

Then we input our encoded flag `rlk{blpdfp_iajylg_iyi}` and try all options for mapping to QWERTY.

When [mapping using Colemak](https://awsm-tools.com/keyboard-layout?form%5Bfrom%5D=colemak&form%5Btext%5D=rlk%7Bblpdfp_iajylg_iyi%7D&form%5Bto%5D=qwerty) the flag is decoded. Turns out the `"mak"` in the introduction was a hint.

## Flag
<details>
<summary>Click to reveal the flag</summary>

```text
sun{burger_layout_lol}
```