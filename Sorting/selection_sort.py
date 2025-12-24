#first scans entire array and then swaps in single function
#run one main loop
#USE INDICES TO SWAP AND KEEP TRACK OF SMALELST

def selection(array):
    for i in range(0, len(array)):
        smallest= i
        for j in range(i+1, len(array)):
            if array[smallest]>array[j]:
                smallest=j
        temp=array[i]
        array[i]=array[smallest]
        array[smallest]=temp
    
    return array

print(selection([1,3,2,8,5,6,9,7]))
             