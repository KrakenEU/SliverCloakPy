# SliverCloakPy
Bypass common signature detections such as the ones from elastic.
Python script that does the job of slivercloak against armysick's sliver fork
slivercloak -> https://github.com/thelikes/slivercloak
armysick's sliver -> https://github.com/armysick/sliver

## Usage

Right now the script covers the Elastic Module, but you can replace whatever you want to be honest.
I did this small script because I have a hard time understanding all the work behind go, and I wanted to use armysick's fork, since it implements the ekko sleep module.

Just download the script and run `python3 builder.py`

## armory problems fix
Since this is replacing strings, including the ones of armory, you wont be able to install armory packages straight forard, here is a quick fix

```
armory add -u https://api.github.com/repos/sliverarmory/armory/releases -k "RWSBpxpRWDrD7Fe+VvRE3c2VEDC2NK80rlNCj+BX0gz44Xw07r6KQD9L" armory

armory install all
```
