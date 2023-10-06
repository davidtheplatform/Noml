#!/usr/bin/env python3

from commands import echo, clear, tput
from editor import run
from os import system

tput("civis")
echo("Noml")
clear()
run()
tput("cnorm")
echo("")
clear()
