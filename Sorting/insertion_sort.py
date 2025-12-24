### BEST= O(N), AVERAGE= O(N2), WORST= O(N2)
#if only few elements not sorting- practicaly O(n)

#two loops: one going forward, one going backward to compare against all previous elements

def insertion_sort(array):
    for i in range(1,len(array)):
        j=i
        while array[j-1]>array[j] and j>0:
            prev_one=array[j-1]
            array[j-1]=array[j]
            array[j]=prev_one
            j-=1
    
    return array



print(insertion_sort([1,4,6,3,2,5,7,9,2,15,12]))