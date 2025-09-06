# wave
## Introduction
not a steg challenge i promise

We get the following:
* [wave.wav](wave.wav)

## Investigation
It's one of the easy challenges so the first thing we do is search its contents.

```bash
$ strings wave.wav | grep ictf{
```

This returns the flag.

```
ictf{obligatory_metadata_challenge}
```