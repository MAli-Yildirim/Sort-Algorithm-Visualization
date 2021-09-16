# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project#1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import random,FastSort,SortFuncs,time,CountSort,RadixSort,BucketSort,math,sys

import numpy as np
random.seed(28)

from PyQt5 import QtCore, QtGui, QtWidgets ,uic
from PyQt5.QtWidgets import*





class ProjectClient(QtWidgets.QMainWindow):
    def __init__(self):
        super(ProjectClient, self).__init__()
        uic.loadUi("ProjectClient.ui",self)
        self.show()
        
    
        self.array = random.sample(list(np.arange(int(self.lineEdit.text())+1)),int(self.lineEdit_2.text()))        
        self.MplWidget.canvas.axes.bar(np.linspace(1,len(self.array),len(self.array)),self.array)
        for x,y in enumerate(self.array):
            self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
                
    
        
        self.SortButton.clicked.connect(self.update_graph)
        self.pushButton_9.clicked.connect(self.ChangeArray)
        self.pushButton_11.clicked.connect(self.Exit)
        self.pushButton_10.clicked.connect(self.Stop)
        
        #1       
        self.pushButton_7.clicked.connect(self.InsertionAnimation)
        #2
        self.pushButton_5.clicked.connect(self.MergeAnimation)
        #3
        self.pushButton.clicked.connect(self.BubbleAnimation)
        #4
        self.pushButton_2.clicked.connect(self.QuickAnimation)
        #5
        self.pushButton_3.clicked.connect(self.HeapAnimation)
        #6
        self.pushButton_4.clicked.connect(self.CountAnimation)
        #7
        self.pushButton_6.clicked.connect(self.RadixAnimation)
        #8
        self.pushButton_8.clicked.connect(self.BucketAnimation)
        
        self.stop = 0
    def Stop(self):
        self.stop = 1
        
    def Exit(self):
        app.quit()
        sys.exit()
        

    
    
    def ChangeArray(self):
        self.array = random.sample(list(np.arange(int(self.lineEdit.text())+1)),int(self.lineEdit_2.text()))  
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.bar(np.linspace(1,len(self.array),len(self.array)),self.array)  
        for x,y in enumerate(self.array):
            self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
        self.MplWidget.canvas.axes.set_title('Sorting Simulation')
        self.MplWidget.canvas.draw()
        

    def InsertionAnimation(self):
        
             
        size = int(len(self.array))
        #Starting loop from second unit
        for j in range(1,size):
            #assign next unit to blank unit
            blank = self.array[j]
            #returning to first unit for compare
            i=j-1
            #Changing values of array[i+1] if it's larger than next values
            while i > -1 and self.array[i] > blank:
                self.array[i+1]=self.array[i]
                
                
                self.MplWidget.canvas.axes.clear()                
                for x,y in enumerate(self.array):
                    self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
                self.MplWidget.canvas.axes.bar(np.linspace(1,len(self.array),len(self.array)),self.array)  
                self.MplWidget.canvas.axes.bar([i+2, i+1],[self.array[i+1],self.array[i]] ,color = "red")
                
                self.MplWidget.canvas.axes.set_title('Sorting Simulation')
                self.MplWidget.canvas.draw()
                speed = 1/self.horizontalSlider.value()
                time.sleep(speed)
                QApplication.processEvents()
                i=i-1
                
                
            self.array[i+1]=blank
            
            self.MplWidget.canvas.axes.clear()
            for x,y in enumerate(self.array):
                self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
            self.MplWidget.canvas.axes.bar(np.linspace(1,len(self.array),len(self.array)),self.array)  
            self.MplWidget.canvas.axes.bar([i+2, i+1],[blank,self.array[i]] ,color = "red")
            self.MplWidget.canvas.axes.set_title('Sorting Simulation')
            self.MplWidget.canvas.draw()
            speed = 1/self.horizontalSlider.value()
            
            time.sleep(speed)
            self.MplWidget.canvas.axes.clear()
            for x,y in enumerate(self.array):
                self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
            self.MplWidget.canvas.axes.bar(np.linspace(1,len(self.array),len(self.array)),self.array)
            self.MplWidget.canvas.draw()
            if self.stop == 1:
                self.stop = 0
                return
            QApplication.processEvents()
           
            
    def MergeAnimation(self):
        #Blank arrays to hold divided arrays
        tempArray1=[]
        tempArray2=[]
        Holder = []
        #Counters
        a=0
        b=0
        size = int(len(self.array))
        k = (size-math.floor(size/2))
        
        #First assignment
        for x in range(0,math.floor(size/2)):
            #First array
            tempArray1.append(self.array[x])
        #Second assignment
        for x in range(math.floor(size/2),size):
            #Second array
            tempArray2.append(self.array[x])
        #Sorting by using insertion method 
        size = int(len(tempArray1))
        #Starting loop from second unit
        for j in range(1,size):
            #assign next unit to blank unit
            blank = tempArray1[j]
            #returning to first unit for compare
            i=j-1
            #Changing values of array[i+1] if it's larger than next values
            while i > -1 and tempArray1[i] > blank:
                tempArray1[i+1]=tempArray1[i]
                
                
                self.MplWidget.canvas.axes.clear()
                Holder = tempArray1[:]
                Holder.extend(tempArray2)
                self.MplWidget.canvas.axes.bar(np.linspace(1,len(Holder),len(Holder)),Holder)  
                for x,y in enumerate(Holder):
                    self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
                self.MplWidget.canvas.axes.bar([i+2, i+1],[tempArray1[i+1],tempArray1[i]] ,color = "red")
                self.MplWidget.canvas.axes.set_title('Sorting Simulation')
                self.MplWidget.canvas.draw()
                speed = 1/self.horizontalSlider.value()
                time.sleep(speed)
                QApplication.processEvents()
                i=i-1
                Holder = []
                                    
            tempArray1[i+1]=blank                
            self.MplWidget.canvas.axes.clear()
            Holder = tempArray1[:]
            Holder.extend(tempArray2)
            self.MplWidget.canvas.axes.bar(np.linspace(1,len(Holder),len(Holder)),Holder)    
            for x,y in enumerate(Holder):
                self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
            
            self.MplWidget.canvas.axes.set_title('Sorting Simulation')
            self.MplWidget.canvas.draw()
            speed = 1/self.horizontalSlider.value()
            time.sleep(speed)
            QApplication.processEvents()
            if self.stop == 1:
                self.stop = 0
                return
            Holder = []
            
        
        size = int(len(tempArray2))
        #Starting loop from second unit
        for j in range(1,size):
            #assign next unit to blank unit
            blank = tempArray2[j]
            #returning to first unit for compare
            i=j-1
            #Changing values of array[i+1] if it's larger than next values
            while i > -1 and tempArray2[i] > blank:
                tempArray2[i+1]=tempArray2[i]
                i=i-1
                
                self.MplWidget.canvas.axes.clear()
                Holder = tempArray1[:]
                Holder.extend(tempArray2)
                self.MplWidget.canvas.axes.bar(np.linspace(1,len(Holder),len(Holder)),Holder)
                for x,y in enumerate(Holder):
                    self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
                self.MplWidget.canvas.axes.bar([k+i+2, k+i+1],[Holder[k+i+1],Holder[k+i]] ,color = "red")
                self.MplWidget.canvas.axes.set_title('Sorting Simulation')
                self.MplWidget.canvas.draw()
                speed = 1/self.horizontalSlider.value()
                time.sleep(speed)
                QApplication.processEvents()
                Holder = []
                                    
            tempArray2[i+1]=blank                
            self.MplWidget.canvas.axes.clear()
            Holder = tempArray1[:]
            Holder.extend(tempArray2)
            self.MplWidget.canvas.axes.bar(np.linspace(1,len(Holder),len(Holder)),Holder) 
            for x,y in enumerate(Holder):
                    self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
            self.MplWidget.canvas.axes.set_title('Sorting Simulation')
            self.MplWidget.canvas.draw()
            speed = 1/self.horizontalSlider.value()
            time.sleep(speed)
            QApplication.processEvents()
            if self.stop == 1:
                self.stop = 0
                self.array = Holder
                return
            Holder = []
        
        #Merging two temporary arrays
        for x in range(0,len(self.array)): 
            #If first temporary array is out of size add rest of the variables to array  
            #Avoding the out of range controlling size of temparray2 
            if a == len(tempArray1) and b != len(tempArray2):                   
                self.array[x]=tempArray2[b]
                b+=1
            #If second temporary array is out of size add rest of the variables to array    
            #Avoding the out of range controlling size of temparray1
            if b == len(tempArray2) and a != len(tempArray1):                   
                self.array[x]=tempArray1[a]
                a+=1
            #Avoiding out of range 
            if a != len(tempArray1) and b != len(tempArray2):            
                #If first is smaller add to array
                if tempArray1[a]<=tempArray2[b]:
                    self.array[x]=tempArray1[a]
                    a+=1                
                #If second is smaller add to array
                elif tempArray1[a]>tempArray2[b]:
                    self.array[x]=tempArray2[b]
                    b+=1
           
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.bar(np.linspace(1,len(self.array),len(self.array)),self.array)
            for x,y in enumerate(self.array):
                    self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
            self.MplWidget.canvas.axes.set_title('Sorting Simulation')
            self.MplWidget.canvas.draw()
            speed = 1/self.horizontalSlider.value()
            time.sleep(speed)
            QApplication.processEvents()
            
            
        
    def BubbleAnimation(self):
    
        size=int(len(self.array))
        #Comparing side by side values in two for loop 
        for x in range (1,size-1):
            for y in range (0,size-x):
                #Swapping values then next two swapping with higher values
                if self.array[y]>self.array[y+1]:
                    blank=self.array[y]
                    self.array[y]=self.array[y+1]
                    self.array[y+1]=blank
                    self.MplWidget.canvas.axes.clear()
                    self.MplWidget.canvas.axes.bar(np.linspace(1,len(self.array),len(self.array)),self.array)
                    self.MplWidget.canvas.axes.bar(y+2,self.array[y+1] ,color = "red")
                    for x,y in enumerate(self.array):
                            self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
                    
                    self.MplWidget.canvas.axes.set_title('Sorting Simulation')
                    self.MplWidget.canvas.draw()
                    speed = 1/self.horizontalSlider.value()
                    time.sleep(speed)
                    if self.stop == 1:
                        self.stop = 0
                        self.MplWidget.canvas.axes.clear()
                        self.MplWidget.canvas.axes.bar(np.linspace(1,len(self.array),len(self.array)),self.array)
                        for x,y in enumerate(self.array):
                                self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
                        self.MplWidget.canvas.axes.set_title('Sorting Simulation')
                        self.MplWidget.canvas.draw()
                        return
                    QApplication.processEvents()
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.bar(np.linspace(1,len(self.array),len(self.array)),self.array)
        for x,y in enumerate(self.array):
                self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
        self.MplWidget.canvas.axes.set_title('Sorting Simulation')
        self.MplWidget.canvas.draw()
        speed = 1/self.horizontalSlider.value()
        time.sleep(speed)
        QApplication.processEvents()
        
            
            
    def partition(self,array,p,q):
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
                self.MplWidget.canvas.axes.clear()
                
                self.MplWidget.canvas.axes.bar(np.linspace(1,len(array),len(array)),array)
                self.MplWidget.canvas.axes.set_title('Sorting Simulation')
                #for x,y in enumerate(array):
                 #       self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
               
                self.MplWidget.canvas.draw()
                speed = 1/self.horizontalSlider.value()
                time.sleep(speed)
                QApplication.processEvents()
        #Writing value of pivot to make pivot right size bigger , left size lower than itself 
        blank    = array[p-1]
        array[p-1] = array[i]
        array[i] = blank
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.bar(np.linspace(1,len(array),len(array)),array)
        for x,y in enumerate(array):
                self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
        self.MplWidget.canvas.axes.set_title('Sorting Simulation')
        self.MplWidget.canvas.draw()
        speed = 1/self.horizontalSlider.value()
        time.sleep(speed)
        QApplication.processEvents()
        return i+1
        
        #Main recursion function
    def quickSortt(self,array,p,r):
        if r > p:
            q = self.partition(array,p,r)
            if self.stop == 1:
                self.stop = 0
                return
            #Sorting recursively right and left side of pivot
            array = self.quickSortt(array,p,q-1)
            array = self.quickSortt(array,q+1,r)
            
            
        return array        
    
         
    def QuickAnimation(self):
        self.quickSortt(self.array,1,len(self.array))
     
    def makeheap(self, array, size, i):
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
            self.makeheap(array,size,highest)
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.bar(np.linspace(1,len(array),len(array)),array)
        self.MplWidget.canvas.axes.bar(highest,array[highest-1] ,color = "red")
        for x,y in enumerate(array):
                self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')    
        self.MplWidget.canvas.axes.set_title('Sorting Simulation')
        self.MplWidget.canvas.draw()
        speed = 1/self.horizontalSlider.value()
        time.sleep(speed)
        QApplication.processEvents()
        


    def heapSort(self, array):
        size = len(array)
        
        #For all nodes, sort-heap to last to start
        for i in range(size, -1, -1): 
            self.makeheap(array, size, i) 
    
        #Swap highest value on index 0 to last index currently
        for i in range(size-1,0,-1): 
            blank    = array[i]
            array[i] = array[0]
            array[0] = blank 
            #Re-Sort the heap because 0 index is no longer highest
            self.makeheap(array,i,0)
            if self.stop == 1:
                self.stop = 0
                self.MplWidget.canvas.axes.clear()
                self.MplWidget.canvas.axes.bar(np.linspace(1,len(array),len(array)),array)
                for x,y in enumerate(array):
                        self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
                self.MplWidget.canvas.axes.set_title('Sorting Simulation')
                self.MplWidget.canvas.draw()
                return
            
            
        
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.bar(np.linspace(1,len(array),len(array)),array)
        for x,y in enumerate(array):
                self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
        self.MplWidget.canvas.axes.set_title('Sorting Simulation')
        self.MplWidget.canvas.draw()
        speed = 1/self.horizontalSlider.value()
        time.sleep(speed)
        QApplication.processEvents()
        
        return array
        
    def HeapAnimation(self):
        self.heapSort(self.array)
        
    def CountAnimation(self):
        
        maxvalue = int(self.lineEdit.text())
        size = len(self.array)
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
            storage[self.array[i]] = storage[self.array[i]] + 1
        #Adding elements of storage
        for i in range(1,maxvalue+1):
            storage[i] = storage[i]+storage[i-1]
        #Filling sorted array 
        for i in range(size-1,-1,-1):       
            sortedarray[storage[self.array[i]]-1] = self.array[i]
            storage[self.array[i]] = storage[self.array[i]] - 1
            
            
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.bar(np.linspace(1,len(sortedarray),len(sortedarray)),sortedarray)
            for x,y in enumerate(sortedarray):
                    self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
            self.MplWidget.canvas.axes.set_title('Sorting Simulation')
            self.MplWidget.canvas.draw()
            speed = 1/self.horizontalSlider.value()
            time.sleep(speed)
            QApplication.processEvents()
            
    def RadixAnimation(self):
        blank = 0
        size = len(self.array)
        #Taking max digit value to use on iteration of each coulum
        largest = len(str(max(self.array)))    
        #Iteration start
        for x in range(0,largest):
            #Insertion sort modified to use it on radix sort
            for j in range(1,size):
                #assign next unit to blank unit
                blank = self.array[j]
                #returning to first unit for compare
                i=j-1
                #Changing values of array[i+1] if it's larger than next values
                # and taking digit coulums last to first
                while i > -1 and int(self.array[i]/10**x)%10 > int(blank/10**x)%10:
                    self.array[i+1]=self.array[i]
                    i=i-1
                                
                self.array[i+1]=blank
        
                
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.bar(np.linspace(1,len(self.array),len(self.array)),self.array)
            for x,y in enumerate(self.array):
                    self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
            self.MplWidget.canvas.axes.set_title('Sorting Simulation')
            self.MplWidget.canvas.draw()
            speed = 1/self.horizontalSlider.value()
            time.sleep(speed)
            QApplication.processEvents()
            
            
            
            
            
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.bar(np.linspace(1,len(self.array),len(self.array)),self.array)
        for x,y in enumerate(self.array):
                self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
        self.MplWidget.canvas.axes.set_title('Sorting Simulation')
        self.MplWidget.canvas.draw()
        speed = 1/self.horizontalSlider.value()
        time.sleep(speed)
        QApplication.processEvents()
        
    

        
    
        
        
    def BucketAnimation(self):
        
        size = len(self.array)
        bucket = []
        
        #Dividing into 10 pieces of bucket
        seperator = (math.ceil((max(self.array)+1)/10))
        k = 0
        
        #Creating Buckets
        for i in range(0,10):
            bucket.append([])
        #Filling buckets
        for i in range(0,size):
            j = math.floor(self.array[i]/seperator)
            bucket[j].append(self.array[i])
            
            #Sorting buckkets
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.bar(np.linspace(1,len(bucket[j]),len(bucket[j])),bucket[j])
            for x,y in enumerate(bucket[j]):
                    self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
            self.MplWidget.canvas.axes.set_title('Sorting Simulation Bucket {}'.format(j))
            self.MplWidget.canvas.draw()
            speed = 1/self.horizontalSlider.value()
            time.sleep(speed)
            QApplication.processEvents()
        
        
        
        
        
        for i in range(0,10):
            SortFuncs.insertionsort(bucket[i])[0]
        #Taking items from buckets first to last
        for i in range(0,10): 
            for j in range(len(bucket[i])): 
                self.array[k] = bucket[i][j] 
                k += 1
                self.MplWidget.canvas.axes.clear()
                self.MplWidget.canvas.axes.bar(np.linspace(1,len(self.array),len(self.array)),self.array)
                for x,y in enumerate(self.array):
                        self.MplWidget.canvas.axes.text(x+1,y,str(y), color = 'black', ha = 'center', va = 'center',fontweight='bold')
                self.MplWidget.canvas.axes.set_title('Sorting Simulation')
                self.MplWidget.canvas.draw()
                speed = 1/self.horizontalSlider.value()
                time.sleep(speed)
                QApplication.processEvents()
    
        
        
        
        
        
        
        


    def update_graph(self):
        
        
        maxvalue  = int(self.MaxlineEdit.text())
        size      = int(self.ArraySizelineEdit.text())
        iteration = int(self.IterationlineEdit.text())
        itnumber  = int(self.IterationNumberlineEdit.text())
        array = []
        insertiontime=[]
        mergetime=[]
        bubbletime=[]
        quicktime=[]
        heaptime=[]
        countingtime=[]
        radixtime=[]
        buckettime=[]
        name=[]
        
        
        
        
        
        
        if size <= maxvalue:
            
            #Making array with no double
            
            
            
            array = random.sample(list(np.arange(maxvalue+1)),size)
            
                
            for x in range(iteration):
                
                #In this area code keeps the time values on each unique array by desire check value
                holder = array[:]
                    #1 
                if self.Insertioncheck.isChecked():  
                    insertiontime.append(SortFuncs.insertionsort(array)[1])
                array = holder[:]              
                    #2
                if self.Mergecheck.isChecked():
                    mergetime.append(SortFuncs.mergesort(array)[1])
                array = holder[:]
                    #3
                if self.Bubblecheck.isChecked():
                    bubbletime.append(SortFuncs.bubblesort(array)[1])
                array = holder[:]
                    #4
                if self.Quickcheck.isChecked():    
                    size = len(array)
                    start = time.time()
                    FastSort.quickSort(array,1,size)
                    end = time.time()
                    quicktime.append(end-start)
                array = holder[:]
                    #5
                if self.Heapcheck.isChecked():    
                    start1 = time.time()
                    FastSort.heapSort(array)
                    end1=time.time()
                    heaptime.append(end1-start1)
                array = holder[:]
                    #6
                if self.checkBox.isChecked():    
                    start1 = time.time()
                    CountSort.CountSort(array,max(array))
                    end1=time.time()
                    countingtime.append(end1-start1)
                array = holder[:]
                    #7
                if self.checkBox_2.isChecked():    
                    start1 = time.time()
                    RadixSort.RadixSort(array)
                    end1=time.time()
                    radixtime.append(end1-start1)
                array = holder[:]
                    #8
                if self.checkBox_3.isChecked():    
                    start1 = time.time()
                    BucketSort.BucketSort(array)
                    end1=time.time()
                    buckettime.append(end1-start1)
                array = holder[:]
                
                
                size = len(array)
                array = random.sample(list(np.arange(maxvalue+1)),size+itnumber)
                
                
                
                
                #Following running situation
                self.Errorlabel.setText("{0:.2f}% completed".format(((x+1)/iteration)*100))
                QApplication.processEvents()
                
            
            
            
        else:
            self.Errorlabel.setText("There are'nt enough int values to fill array")
            
            
        t = np.linspace(0,iteration,iteration)
        
        #With time arrays plotting graphs by desire checked value 
        self.MplWidget.canvas.axes.clear()
        #1
        if self.Insertioncheck.isChecked():           
            self.MplWidget.canvas.axes.plot(t,insertiontime)
            name.append('Insertion Sort')
        #2
        if self.Mergecheck.isChecked():      
            self.MplWidget.canvas.axes.plot(t,mergetime)
            name.append('Merge Sort')
        #3
        if self.Bubblecheck.isChecked():      
            self.MplWidget.canvas.axes.plot(t,bubbletime)
            name.append('Bubble Sort')
        #4
        if self.Quickcheck.isChecked():
            self.MplWidget.canvas.axes.plot(t,quicktime)
            name.append('Quick Sort')
        #5
        if self.Heapcheck.isChecked():      
            self.MplWidget.canvas.axes.plot(t,heaptime)
            name.append('Heap Sort')
        #6
        if self.checkBox.isChecked():      
            self.MplWidget.canvas.axes.plot(t,countingtime)
            name.append('Counting Sort')
        #7
        if self.checkBox_2.isChecked():      
            self.MplWidget.canvas.axes.plot(t,radixtime)
            name.append('Radix Sort')
        #8
        if self.checkBox_3.isChecked():      
            self.MplWidget.canvas.axes.plot(t,buckettime)
            name.append('Bucket Sort')
            
            
            
            
        #Name of the graphs
        self.MplWidget.canvas.axes.legend(name,loc='upper left')
        self.MplWidget.canvas.axes.set_title('Sorting Times')
        #draw
        self.MplWidget.canvas.draw()






app = QtWidgets.QApplication(sys.argv)

window = ProjectClient()
app.exec_()