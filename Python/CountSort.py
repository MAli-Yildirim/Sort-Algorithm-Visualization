#Mehmet Ali Yıldırım
#160403008
#Homework 5
#Counting Sort

def CountSort(array,maxvalue):
    
    size = len(array)
    sortedarray = []
    storage = []
    
    #Creating blank array to hold sortedarray
    for i in range(0,size):
        sortedarray.append(0)
    #Creating storage to hold index values
    for i in range(0,maxvalue+1):
        storage.append(0)
    #Counting elements of array
    for i in range(0,size):
        storage[array[i]] = storage[array[i]] + 1
    #Adding elements of storage
    for i in range(1,maxvalue+1):
        storage[i] = storage[i]+storage[i-1]
    #Filling sorted array 
    for i in range(size-1,-1,-1):       
        sortedarray[storage[array[i]]-1] = array[i]
        storage[array[i]] = storage[array[i]] - 1

    return sortedarray
    

