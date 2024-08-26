def linear_search(arr,N,X):
    for i in range(0,N):
        if (arr[i] == X):
            return i
    return -1    


if __name__ =="__main__":
    arr=[2,3,4,6,87,34]
    X=87
    N=len(arr)
    
    result =linear_search(arr,N,X)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is prsent at index",result)  