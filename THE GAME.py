A = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

def move(l,s,c,r,f):
            if (l[f][c] != 0) and (l[r][s] == 0):
                l[r][s]=l[f][c]
                l[f][c]=0
            elif l[f][c] == l[r][s]:
                l[r][s] = l[r][s]*2
                l[f][c] = 0 

def right (l):
    for y in range(3):
        i = 3-y
        for x in range (i):
            s = 3-x 
            for r in range(4):
                c = s -1
                move(l,s,c,r,r)

def left (l):
    for i in range (3):
        y = 3-i
        for s in range (y):
            c = s +1
            for r in range(4):
                move(l,s,c,r,r)         

def down (l):
    for i in range (3):
        y = 3 - i
        for x in range (y):
            r = 3-x
            f = r - 1
            for s in range (4):
                move(l,s,s,r,f)

def up (l):
    for i in range (3):
        y = 3 - i
        for r in range(3):
            f = r + 1
            for s in range (4):
                move(l,s,s,r,f)           

import random

while True:
    WhyWouldAnyoneDoThis = True
    while WhyWouldAnyoneDoThis:
        WhyWouldAnyoneDoThis = False
        inp = input("Command:")
        if inp == 'w':
            up(A)
        elif inp == 'd':
            right(A)
        elif inp == 's':
            down(A)
        elif inp == 'a':
            left(A)
        elif inp == 'reset':
            if input('Are you sure?:')=='yes':
                A = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]
        else:
            WhyWouldAnyoneDoThis = True
            
            
    while True:
        x = random.randint(0,3)
        y = random.randint(0,3)
        if A[y][x] == 0:
            A[y][x] = 2
            break
    print(A[0])
    print(A[1])
    print(A[2])
    print(A[3])