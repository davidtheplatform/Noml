#!/usr/bin/env python3

import sys
if getattr(sys, 'frozen', False):
  from noml.commands import echo, clear, tput
  from noml.editor import run
from os import system

tput("civis")
echo("Noml")
clear()
run()
tput("cnorm")
echo("")
clear()
