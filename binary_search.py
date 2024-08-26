def binary_search(arr,low,high,X):
    while low <= high:
        mid =(low+high)//2
        
        if arr[mid] == X:
            return mid
        elif arr[mid] < X:
            low =mid+1
        else:
            high =mid-1
    return -1
if __name__ =="__main__":
    arr=[8,2,10,22,34]
    X=8
    
    result =binary_search(arr,0,len(arr)-1,X)
    if result != -1:
        print("Show",result)
    else:
        print("Desnot Found")
            
        