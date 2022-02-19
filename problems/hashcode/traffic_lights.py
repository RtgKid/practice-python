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
    

D, I, S, V, F, dfstreets, dfpaths = read_file('qualification_round_2021.in/d.txt')
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
        for i in range(len(path) - 1):
            ss = path[i]
            if ss in d:
                d[ss] = d[ss] + 1
            else:
                d[ss] = 1

        # for ss in path:
        #     if ss in d:
        #         d[ss] = d[ss] + 1
        #     else:
        #         d[ss] = 1

    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))      

def start_car_count(dfpaths):
    d = {}

    for path in dfpaths["streets"]:
        if path[0] in d:
            d[path[0]] = d[path[0]] + 1
        else:
            d[path[0]] = 1
    return d        

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
    car_count = start_car_count(dfpaths)
    
    # print(dfstreets)
    # print(dfpaths)
    # print(busy_streets)
    print(I)
    for interId in intersections:
        print(interId)
        streets = sorted(intersections[interId], key = lambda x: car_count.get(x, 0),reverse=True)


        #print(streets)
        #print(len(intersections[interId]))
        print(len(streets))
        #for ss in intersections[interId]:
        for ss in streets:
            if ss in busy_streets:
                print(str(ss) + " " + str(busy_streets[ss]))
            else:
                print(str(ss) + " " + str(1))    
                    
    
        
def write_to_file():
    busy_streets = sort_streets_by_busiest(dfpaths)
    intersections = in_streets_of_inter(dfstreets)
    car_count = start_car_count(dfpaths)
    
    #print(busy_streets)
    file = open("qualification_round_2021.in/d_ans_car_count.txt", "w")
    #print(I)
    file.write(str(I) + "\n")
    for interId in intersections:
        #print(interId)
        file.write(str(interId) + "\n")
        streets = sorted(intersections[interId], key = lambda x: car_count.get(x, 0),reverse=True)
        #print(len(intersections[interId]))
        file.write(str(len(streets)) + "\n")

        iter_strs = []
        for ss in streets:
            if ss in busy_streets:
                iter_strs.append(busy_streets[ss])
        w_streets = [str(i / min(iter_strs)) for i in iter_strs]        

        for ss in streets:
            i = 0
            if ss in busy_streets:
                #print(str(ss) + " " + str(busy_streets[ss]))
                file.write(str(ss) + " " + str(w_streets[i]) + "\n")
            else:
                file.write(str(ss) + " " + "1" + "\n")
            i = i + 1    
                    
    file.close()            


write_to_file()

from scoring import scoring
print(scoring(input_file='qualification_round_2021.in/d.txt',output_file='qualification_round_2021.in/d_ans_car_count.txt'))

    
  