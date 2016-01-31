import random
import time
import sys
import math

def bubblesort(list):
    n = len(list)
    for i in range(0,n):
       for j in range(n-1,i, -1):
           if list[j] < list[j-1]:
               tmp = list[j]
               list[j] = list[j-1]
               list[j-1] = tmp

def insertionsort(list):
    for j in range(1,len(list)):
        key = list[j]
        i = j-1
        while i >= 0 & list[i] > key:
            list[i+1] = list[i]
            i -= 1

def merge(list,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = list[p:p+n1]
    R = list[q:q+n2]
    i = 0
    j = 0
    for k in range(p,r):
        if L[i] <= R[i]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1

def mergesort(list, p=0,r=-1):
    if r == -1:
        r = len(list) - 1
    if p < r:
        q = math.floor((p+r) / 2)
        mergesort(list,p,q)
        mergesort(list,q+1,r)
        merge(list,p,q,r)

def checkSorted(list):
    return all(list[i] <= list[i+1] for i in range(len(list)-1))
        

def timeSort(sortFunc = insertionsort, length=1000000):
    list = [random.randint(0,length) for r in range(length)]
    start = time.time()
    sortFunc(list)
    end = time.time()
    timeTaken = end - start
    if checkSorted(list):
        print('sorted')
    else:
        print('not sorted')
    return timeTaken

def main(argv):
    timeTaken = timeSort(mergesort,5)
    print('Time taken: ', timeTaken)
    
main(sys.argv)

