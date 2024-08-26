def bubble_short(arr):
    n =len(arr)
    
    for i in range(n):
        swapped =False
        #print("print i value",i)
        
        
        for j in range(0,n-i-1):
            print(j) # pass number 
            
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                #print(arr[j])
                #print(arr[j+1])
                swapped =True
                
        if(swapped ==False):
            break


if __name__ =="__main__":
    arr=[12,34,2,40,7,33,4]
    bubble_short(arr)
    
    print("Sorted array")
    for i in range(len(arr)):
      print(arr[i])