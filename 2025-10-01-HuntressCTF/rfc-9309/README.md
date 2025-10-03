# RFC 9309
## Introduction
Sorry. You know every CTF has to have it. 🤷

- We are given a temporarily accesible website.

## Investigation
RFC 9309 is the Robots Exclusion Protocol. So lets go investigate in `/robots.txt`.

````text
User-Agent: *
Disallow: /
```

Doesnt seem like there is anything here...

That is untill you realise you can scroll and the flag is hidden further down along the right side of the screen.

## Flag
<details>
<summary>Click to reveal the flag</summary>

```text
flag{aec1142c199aa5d8ad0f3ae3fa82e13c}
```