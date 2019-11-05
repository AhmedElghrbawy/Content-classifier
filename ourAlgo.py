def BubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i][1] < alist[i+1][1]:
               exchanges = True
               alist[i], alist[i+1] = alist[i+1], alist[i]
       passnum = passnum-1
    return alist


def insertionSort(arr):
    for i in range(1, len(arr)): 
        key_value = arr[i][1] 
        key = arr[i]
        j = i-1
        while j >=0 and key_value > arr[j][1]: 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key
    return arr


def selectionSort(alist):
    n = len(alist)
    for i in range(n-1):
        max = alist[i][1]
        maxposition = i
        for j in range(i+1, n):
            if alist[j][1] > max:
                max = alist[j][1]
                maxposition = j
        alist[i],alist[maxposition] = alist[maxposition],alist[i]
    return alist


def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][1] >= righthalf[j][1]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return alist


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
    return alist
def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)
        
def partition(alist,first,last):
    pivotvalue = alist[first][1]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark][1] >= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark][1] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]
    alist[first],alist[rightmark] = alist[rightmark],alist[first]
    return rightmark

def get_category(categories):
    maxi = categories[0][1]
    pos = 0
    for i in range(1,len(categories)):
        if categories[i][1] > maxi:
            maxi = categories[i][1]
            pos = i
    print (categories[pos][0])