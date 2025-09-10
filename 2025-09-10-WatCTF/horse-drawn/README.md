#  horse-drawn 
## Introduction
This is how it must have felt in the Year of Our Ford.


We get the following:
* [main.py](main.py)
* [dockerfile](Dockerfile)
* ssh hexed@challs.watctf.org -p 8022

## Investigation
The first thing we do is just have a look at the python file since these often contain the code we need to exploit. Then we try to connect using ssh and get get the following output.

```console
lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you lmao no flag for you
Connection to challs.watctf.org closed.
```
In [the python file]((main.py)) we can see that the flag itself is supposed to be printed before the string `lmao no flag for you` is printed 32 times. 

## Exploitation
To get the flag we just need to send the output to a txt-file instead of showing it in our terminal.

```bash
ssh hexed@challs.watctf.org -p 8022  > output.txt
```

From here we open the file using notepad and extract the flag:

```
watctf{im_more_of_a_tram_fan_personally}
```
