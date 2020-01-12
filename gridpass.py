#!/usr/bin/python3
from string import ascii_lowercase as lowercase
from string import ascii_uppercase as uppercase
from string import digits,punctuation
from random import choice
from re import sub
from os import path
from argparse import ArgumentParser
#----------------------------------------------
#replaced , in punction so I could parse the file
punctuation = sub(',', '', punctuation)
parser = ArgumentParser(description='Translate a simple password into a complex one')
parser.add_argument('-p', '--passwd', type=str, help='simple password', required=True)
parser.add_argument('-g', '--generate', default=False, type=str, help='Any value to make true', required=False)
args = parser.parse_args()
fname = '.gridcache'


def square_gen():
    random = choice(uppercase)
    random+= choice(lowercase)
    random+= choice(digits)
    random+= choice(punctuation)
    return random

def grid_gen():
    squares = {}
    for alpha in lowercase:
      squares[alpha] = square_gen()
    with open(fname, 'w') as f:
      f.write('\n'.join(str(v) + str(",") + str(squares[v]) for v in squares))
    return squares

def read_grid(grid):
  squares = {}
  if path.isfile(grid):
    f = open(grid, 'r')
    file = f.readlines()
    for line in file:
      x,y = line.rstrip().split(',')
      squares[x] = y
  return squares

def main(grid, passwd):
  print(passwd)
  print(''.join(str(grid[v]) for v in passwd))

if args.generate:
  grid = grid_gen()
elif path.isfile(fname):
  grid = read_grid(fname)
else:
  grid = grid_gen()



main(grid, args.passwd)
