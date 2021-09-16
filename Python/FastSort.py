#MehmetAli Yıldırım
#160403008
#Homework 4
#QuickSort

def partition(array,p,q):
    #pivot
    x = array[p-1]
    #index
    i = p-1
       
    for j in range(p,q):
        #Arranging numbers by pivot 
        if array[j] < x:
            i = i + 1
            blank    = array[j]
            array[j] = array[i]
            array[i] = blank
    #Writing value of pivot to make pivot right size bigger , left size lower than itself 
    blank    = array[p-1]
    array[p-1] = array[i]
    array[i] = blank
    return i+1
    
#Main recursion function
def quickSort(array,p,r):
    if r > p:
        q = partition(array,p,r)
        #Sorting recursively right and left side of pivot
        quickSort(array,p,q-1)
        quickSort(array,q+1,r)
        
    return array




def makeheap(array, size, i):
    #Left part of node
    left  = 2 * i + 1 
    #Right part of node
    right = 2 * i + 2
    #Main node which is biggest
    highest = i

    #If left is bigger than node keep index and prevent to out of size
    if left < size and array[left] > array[highest]:
        highest = left
        
    #If right is bigger than node keep index and prevent to out of size
    if right < size and array[right] > array[highest]:
        highest = right  
    
    #If node index does not match highest value of left or right index swap index values
    if highest != i:
        blank    = array[i]
        array[i] = array[highest]
        array[highest] = blank          
        #After that re-Sort heap 
        makeheap(array,size,highest)


def heapSort(array):
    size = len(array)
    
    #For all nodes, sort-heap to last to start
    for i in range(size, -1, -1): 
        makeheap(array, size, i) 

    #Swap highest value on index 0 to last index currently
    for i in range(size-1,0,-1): 
        blank    = array[i]
        array[i] = array[0]
        array[0] = blank 
        #Re-Sort the heap because 0 index is no longer highest
        makeheap(array,i,0)
        
    return array








