def bubble_sort(array):
    for i in range(0,len(array)-1):
        has_swaped=False #THIS PART HELPS IN IDENTIFYING WHEN A ARRAY IS ALREADY SORTED 
        for j in range(len(array) -1, i, -1):
            if array[j]<array[j-1]:
                array[j], array[j-1]= array[j-1], array[j]
                has_swaped=True
        if not has_swaped:
            break
    
    return array

print(bubble_sort([1,2,3,4,5,6]))

