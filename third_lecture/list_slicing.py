'''      0   1    2   3   4'''
marks = [94, 87, 95, 66, 45]
'''      -5  -4   -3  -2  -1'''
marks[ 1: 4 ] #is [87, 95, 66]
marks[ : 4] #is same as marks[0:4]
marks[ 1 : ] #is same as marks[1: len(marks)]
marks[-3 : -1] #is [95, 66]