#!/usr/bin/env python3

from noml.editor import run
from os import system

system("tput civis")
system('echo -n -e "\033]0;Noml\007"')
system("clear")
run()
system("tput cnorm")
system('echo -n -e "\033]0;\007"')
system("clear")