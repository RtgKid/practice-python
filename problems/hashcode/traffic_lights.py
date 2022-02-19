# Street
# 1. unique name
# 2. i1 -> i2
# 3. L is the time to get from the beginning to the end 

# Intersection
# 1. unique id
# 2. -> i ->

# Traffic lights
# 1. Red - stop!
# 2. Green - go!

# On intersection max one traffic light is green

# Car -> sequence of streets

from sqlite3 import InternalError
import numpy as np
import pandas as pd


def read_file(path):
    with open(path) as file:
        D, I, S, V, F = file.readline().split(' ')
        df = []
        cols = ['inter_start', 'inter_end', 'street_name', 'street_time']
        for line in range(int(S)):
            df.append(file.readline().strip().split(' '))
        dfstreets = pd.DataFrame(df, columns=cols)
        
        df = []
        cols = ['P_num_of_streets', 'streets']
        for line in range(int(V)):
            temp = file.readline().strip().split(' ')
            
            df.append([temp[0], temp[1:]])
        dfpaths = pd.DataFrame(df, columns= cols)
        return int(D), int(I), int(S), int(V), int(F), dfstreets, dfpaths
    

D, I, S, V, F, dfstreets, dfpaths = read_file('qualification_round_2021.in/a.txt')
# print("D :", D)
# print("I :", I)
# print("S :", S)
# print("V :", V)
# print("F :", F)
#print( dfstreets)
#print("dfpaths : ", dfpaths)


# For each intersection, calculate incoming streets usability percantage.

def sort_streets_by_busiest(dfpaths):
    d = {}

    for path in dfpaths["streets"]:
        for ss in path:
            if ss in d:
                d[ss] = d[ss] + 1
            else:
                d[ss] = 1

    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))      

def in_streets_of_inter(dfstreets):
    d = {}
    for i in range(len(dfstreets['inter_end'])):
        inter_end = dfstreets['inter_end'][i]
        street = dfstreets['street_name'][i]
        
        if inter_end in d:
            d[inter_end].append(street)
        else:
            d[inter_end] = [street]    
    return d


def main():
    busy_streets = sort_streets_by_busiest(dfpaths)
    intersections = in_streets_of_inter(dfstreets)
    
    print(busy_streets)
    print(I)
    for interId in intersections:
        print(interId)
        print(len(intersections[interId]))
        for ss in intersections[interId]:
            print(str(ss) + " " + str(busy_streets[ss]))
        
    
        

    
main()    