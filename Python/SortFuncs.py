import math
import time

#Insertion Sort
def insertionsort(array):
    start=time.time()
#Determine the size to code    
    size = int(len(array))
    #Starting loop from second unit
    for j in range(1,size):
        #assign next unit to blank unit
        blank = array[j]
        #returning to first unit for compare
        i=j-1
        #Changing values of array[i+1] if it's larger than next values
        while i > -1 and array[i] > blank:
            array[i+1]=array[i]
            i=i-1
        array[i+1]=blank
        #returning to sorted array
    deltatime=time.time()-start
    return array,deltatime

#Merge Sort
def mergesort(array):
    start = time.time()
    #Blank arrays to hold divided arrays
    tempArray1=[]
    tempArray2=[]
    #Counters
    a=0
    b=0
    size = int(len(array))
    #First assignment
    for x in range(0,math.floor(size/2)):
        #First array
        tempArray1.append(array[x])
    #Second assignment
    for x in range(math.floor(size/2),size):
        #Second array
        tempArray2.append(array[x])
    #Sorting by using insertion method 
    tempArray1=insertionsort(tempArray1)[0]
    tempArray2=insertionsort(tempArray2)[0]
    
    #Merging two temporary arrays
    for x in range(0,size): 
        #If first temporary array is out of size add rest of the variables to array  
        #Avoding the out of range controlling size of temparray2 
        if a == len(tempArray1) and b != len(tempArray2):                   
            array[x]=tempArray2[b]
            b+=1
        #If second temporary array is out of size add rest of the variables to array    
        #Avoding the out of range controlling size of temparray1
        if b == len(tempArray2) and a != len(tempArray1):                   
            array[x]=tempArray1[a]
            a+=1
        #Avoiding out of range 
        if a != len(tempArray1) and b != len(tempArray2):            
            #If first is smaller add to array
            if tempArray1[a]<=tempArray2[b]:
                array[x]=tempArray1[a]
                a+=1                
            #If second is smaller add to array
            elif tempArray1[a]>tempArray2[b]:
                array[x]=tempArray2[b]
                b+=1
        
    deltatime=time.time()-start
    return array,deltatime
    
#Bubble Sort
def bubblesort(array):
    start = time.time()
    size=int(len(array))
    #Comparing side by side values in two for loop 
    for x in range (1,size-1):
        for y in range (0,size-x):
            #Swapping values then next two swapping with higher values
            if array[y]>array[y+1]:
                blank=array[y]
                array[y]=array[y+1]
                array[y+1]=blank  
    deltatime=time.time()-start
    return array,deltatime
    
    
    
    
    
    
    
    
    
    
    
    