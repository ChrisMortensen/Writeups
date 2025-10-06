# Stego 100-3 Low Tide at Midnight
## Introduction
In the 2023 contest, we had a stego challenge that utilized an image from Jeff Lee Johnson called "Blue Plate Special." Well, this year we couldn't resist adding some of the Missouri illustrators new work. The trick with this one might be finding a clear way to extract the flag, but if you know then you know. 

## Files
* [stego100-3.jpg](stego100-3.jpg)

## Investigation
![stego100-3.jpg](stego100-3.jpg)

Picture seems to be inversed so lets fix that.

![non-inverse.jpg](non-inverse.jpg)

Seems like there is a hidden QR-code

![qr.png](qr.png)

## Flag
<details>
<summary>Click to reveal the flag</summary>

```text
poctf{uwsp_f0r3v3r_bl0w1n6_bubbl35}
```