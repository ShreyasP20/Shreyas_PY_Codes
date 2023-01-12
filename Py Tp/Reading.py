class Reading:
    windspeed = input("Enter The Windspeed:")
    temperature = input("Enter The Temperature:")
    
    
list1 = []

def main():
    no_obj=input("Enter The Number Of Objects:")
    for i in range(no_obj):
        obj = Reading()
        list1[i]=obj

    choice=input("Enter Which Sorting Algorithm U Would like To perform: \n1.Selection Sort \n2.Merge Sort \n3.Bubble Sort")
    sort(list1, choice)
    
def sort(list1, choice):
    if choice == '1':
        for i in list1:
            min=i
            for j in range(i+1, len(list1)):
                if list1[j] < list1[min]:
                    min=j
                
            (list1[i],list1[min])=(list1[min],list1[i])

    elif choice == '2':
        mergeSort(list1)
       
    elif choice == '3':
          bubbleSort(list1)





def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              myList[k] = left[i]
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1
            
            
            
def bubbleSort(arr):
    n = len(arr)
    
    swapped = False
    for i in range(n-1):
        
        for j in range(0, n-i-1):
 
            
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
        
            return