#!/bin/python3

import math
import os
import random
import re
import sys

def printweird():
    print("Weird")
    
def printnotweird():
    print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        printweird()
    else:
        if 2<=n<=5:
            printnotweird()
        elif 6 <=n<=20:
            printweird()
        else:
            printnotweird()
        
            
