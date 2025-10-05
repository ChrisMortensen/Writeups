# Web 100-1 All Paths Lead Home
## Introduction
A simple little challenge to start off the Web category. We have a site here that will read the contents of a text file hosted on the server. Unfortunately, there's also a file in /secret/ that you're not supposed to see. All you have to do is work out how to get there. There is one little twist, but I've left plenty of clues on that.

## Links
Your Target: REDACTED

## Investigation
First lets have a look at the main page of the website.

![alt text](main-path.png)

Clicking open:

```text
Welcome traveler.
Only text files are available here.
```

Lets have a look at common paths. First up, `robots.txt`.

```text
User-agent: *
Disallow:

# Compatibility note:
# Some historical clients used a non-UTF-8 decoder.
# See /docs/legacy.html for details on enabling legacy mode.
```

Well lets have a look at `/docs/legacy.html`.

```text
Legacy Mode

&legacy=1

Some older clients relied on a legacy decoding pipeline. The server still supports a compatibility path for archival reasons. If you suspect your payload requires it, include the query-string to enable legacy decoding.

Hint: This compatibility path uses a mailbox-safe character encoding (see RFC 2152). Certain characters must be supplied in shifted sequences of the form +...- rather than literal bytes.

# Legacy clients note
# Charset: UTF-7
# Example of shifted form:
#   "<"  => +ADw-
#   ">"  => +AD4-
# Use the same approach for other disallowed characters.
```

Given the introduction the flag is likely in `../secret/flag.txt`. Lets encode it as UTF-7 using CyberChef.

```text
../secret/flag.txt -> ../secret/flag.txt
```

Seems like all none of the characters need to be encoded, but that cannot be right. Lets be sure and try it like this.

```text
404 – Not Found

This path doesn’t exist. If you’re experimenting with encodings, consult the docs.

Hint: legacy compatibility is documented at /docs/legacy.html.
```

Same hint as earlier. Follwing this i researched [RFC 1642](https://www.rfc-editor.org/rfc/rfc2152.html). Here i learned some basic rules for UTF-7 encoding. First wrapping is added starting with `+` and ending with `-`. From here i got lost so i asked AI for the rules and a [python script](encoding.py) which could encode the `.` and `/` with these rules. From here i just needed to modify it to suit the challenge.

Running the scirpt returns:

```text
REDACTED.com/view?file=%2BAC4-%2BAC4-%2BAC8-secret%2BAC8-flag.txt&legacy=1
```

Going to the website returns the flag.


## Flag
<details>
<summary>Click to reveal the flag</summary>

```text
poctf{uwsp_c4nc3l_m3_0rd3r5}
```