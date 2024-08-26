def insertion_sort(arr):
    for i in range(1,len(arr)):
        print(i)
        key = arr[i]
        j=i-1
        
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j -=1
            arr[j+1]=key
            
if __name__ =="__main__":
    arr=[12,34,2,40,7,33,4]
    insertion_sort(arr)
    
    print("Sorted array")
    for i in range(len(arr)):
      print(arr[i])
        