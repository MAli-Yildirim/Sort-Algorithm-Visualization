#Mehmet Ali Yıldırım
#160403008
#Homework 5
#Bucket Sort

from math import ceil,floor
import SortFuncs

def BucketSort(array):
    
    size = len(array)
    bucket = []
    #Dividing into 10 pieces of bucket
    seperator = (ceil((max(array)+1)/10))
    k = 0
    
    #Creating Buckets
    for i in range(0,10):
        bucket.append([])
    #Filling buckets
    for i in range(0,size):
        j = floor(array[i]/seperator)
        bucket[j].append(array[i])
    #Sorting buckkets
    for i in range(0,10):
        SortFuncs.insertionsort(bucket[i])[0]
    #Taking items from buckets first to last
    for i in range(0,10): 
        for j in range(len(bucket[i])): 
            array[k] = bucket[i][j] 
            k += 1
    
    return array


