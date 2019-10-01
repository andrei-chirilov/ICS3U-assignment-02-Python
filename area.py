#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: Oct 2019
# This program calculates the perimeter of a square where user puts in values

import math


def main():
    print("We will be calculating the Perimiter of a square")
    SideLength = int(input("Enter the sidelength (mm): "))
    perimeter = SideLength * 4
    print("Perimeter is {} mm".format(perimeter))


if __name__ == "__main__":
    main()
