#!/usr/bin/env bash
sudo apt install -y cowsay
cowsay -f dragon "I am a dragon. You are gonna feel my rage. RWWWW!!!!" > dragon.txt
if grep -i "dragon" dragon.txt
then
    echo "Found dragon! Kill him"
    cat dragon.txt
else
    echo "No dragon found."
fi
