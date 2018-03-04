#google tech code challenge available at
# https://techdevguide.withgoogle.com/paths/advanced/compress-decompression/

import sys

def recur(string):
	#first iteration until we find a number
    i=0
    while (i < len(string) and not string[i].isdigit()):
        i+=1
    
    #we stop when we don't find any more items "nr[stufftorepeat]" 
    if i == len(string):
        return string
        
    #second iteration to get the number
    k=i
    while string[k].isdigit():
        k+=1
    number = int(string[i:k])

    #third iteration to get the string to repeat
    count = False
    start = k+1
    j = k
    while True:
        if string[j] == "[":
            flag = True
            count+=1
        elif string[j] == "]":
            count-=1
        j+=1
        if (count == 0):
            break
    
    #we recur with the repeated string
    return recur(string[0:i] + string[start:j-1]*number + string[j:])

print(recur(sys.argv[1]))



