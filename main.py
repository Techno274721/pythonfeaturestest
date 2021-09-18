import sys, os, curses
import time 

st = 0.2
def sp(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(st)
  print()

sp("hi how u doing \n")
sp("IT WORKS")