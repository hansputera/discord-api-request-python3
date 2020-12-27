#!/bin/python3

# Kustomisasi print() dengan berwarna
from sty import fg, bg

"""
 [ KETERANGAN ]

 fg = font color
 bg = background color

"""

def fatal(text):
  if (isinstance(text, str)) == False:
    print(f"{bg.red}Error: Invalid type!{bg.rs}")
  else:
    print(f"{bg.red}[FATAL]: {text}{bg.rs}")

def error(text):
  if (isinstance(text, str)) == False:
    print(f"{bg.red}Error: Invalid type!{bg.rs}")
  else:
    print(f"{bg.red}[ERROR]: {text}{bg.rs}")

def info(text):
  if (isinstance(text, str)) == False:
    print(f"{bg.red}Error: Invalid type!{bg.rs}")
  else:
    print(f"{bg.cyan}[INFO]: {text}{bg.rs}")

def success(text):
  if (isinstance(text, str)) == False:
    print(f"{bg.red}Error: Invalid type!{bg.rs}")
  else:
    print(f"{bg.green}[SUCCESS]: {text}{bg.rs}")

def warn(text):
  if (isinstance(text, str)) == False:
    print(f"{bg.red}Error: Invalid type!{bg.rs}")
  else:
    print(f"{bg.yellow}[WARNING]: {text}{bg.rs}")