def selection_sort(arr):
    n=len(arr)
    
    for i in range(n-1):
        mini =i
        for j in range(i+1,n):
            if arr[mini] > arr[j]:
               mini = j
            
        arr[mini],arr[i]=arr[i],arr[mini]
            
if __name__ =="__main__":
     arr=[2,32,4,1,20]
     selection_sort(arr)
    
     print("Sorted array")
     for i in range(len(arr)):
       print(arr[i])       
