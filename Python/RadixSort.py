#Mehmet Ali Yıldırım
#160403008
#Homework 5
#Radix Sort


def RadixSort(array):    
    size = len(array)
    #Taking max digit value to use on iteration of each coulum
    largest = len(str(max(array)))    
    #Iteration start
    for x in range(0,largest):
        #Insertion sort modified to use it on radix sort
        for j in range(1,size):
            #assign next unit to blank unit
            blank = array[j]
            #returning to first unit for compare
            i=j-1
            #Changing values of array[i+1] if it's larger than next values
            # and taking digit coulums last to first
            while i > -1 and int(array[i]/10**x)%10 > int(blank/10**x)%10:
                array[i+1]=array[i]
                i=i-1
            array[i+1]=blank         
    return array