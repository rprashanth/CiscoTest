import numpy as np

def mergeSortShuffling(alist): # complex shufling alogorithm in mergesort way
    print(alist)
    np.random.shuffle(alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSortShuffling(lefthalf)
        mergeSortShuffling(righthalf)

        i=0
        j=0
        k=0
        found = False

        while i < len(lefthalf) and j < len(righthalf):
            if found:
                alist[k]=righthalf[j]
                found = False
                j=j+1
            else:
                alist[k]=lefthalf[i]
                found = True
                i=i+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
