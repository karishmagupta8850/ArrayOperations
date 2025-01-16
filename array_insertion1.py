import array as array;
class arrays:
    array=[]
    array2=[]
    array3=[]
    array4=[]

    
    def __init__(self):
        self.size=int(input("enter the size of ur array:"))
        self.arry=int(input("Enter the number of values u want to enter:"))

        while self.arry > self.size:
            print("invalid no. of value")
            self.arry=int(input("Enter the number of values u want to enter:"))
            
        for i in range(0,self.arry):
            value=int(input("enter value: "))
            self.array.append(value)

        for i in range(self.arry,self.size):
            self.array.append(0)
        print(self.array)               

    def traversal(self):
        for i in self.array:
            print(i)
            
    def insert(self):
        index=int(input("Enter the index at which u want to insert a value:"))
        vlu=int(input("Enter the value which you want to insert"))

        if index < 0 or index >=self.size:
            print("Invalid index")
            return 
        i=self.size-1
        self.array.append(0)
        while(i>=index):
            self.array[i+1]=self.array[i]
            i=i-1
            
        self.array[index]=vlu
        self.size=self.size+1
        print(self.array)
        
    def delete(self):
        pos=int(input("Enter the index from where you want to delte the element"))

        if pos < 0 or pos >= self.size:
            print("Invalid index")
            return
        i=pos
        while(i < self.size - 1):
            self.array[i]=self.array[i+1]
            i=i+1
        self.array.pop()
        print(self.array)


    def linear_search(self):
        seach=int(input("enter a element or value you want to search: "))
        for i in range(len(self.array)):
            if self.array[i]==seach:
                print("Element found at index ",i)
                return
        print("Element not found")


    def binary_search(self):
        self.array.sort()
        print("sorted array",self.array)
        search=int(input("Enter the element you want to search for: "))
        start,end=0,self.size-1
        while start<=end:
            middle= (start+end)//2
            if self.array[middle]==search:
                print("elment found at index ",middle)
                return
            elif self.array[middle] < search:
                start = middle+1
            else:
                end=middle-1
        print("Element not found")

    def bubble_sort(self):
        n=self.arry
        i=0
        while(i<n-1):
            j=0
            while(j<n-1):
                if(self.array[j]>self.array[j+1]):
                    temp=self.array[j]
                    self.array[j]=self.array[j+1]
                    self.array[j+1]=temp
                j=j+1
            i=i+1
        print("Array after sorting",self.array)

    def merging(self):
        self.array2=[]
        self.array3=[]
        self.array4=[]
        self.sizee=int(input("Enter the size of your first array: "))
        self.arr=int(input("Enter the elements for array: "))

        while self.arr > self.sizee:
            print("invalid no. of value")
            self.arr=int(input("Enter the number of values u want to enter: "))
            
        for i in range(0,self.arr):
            value=int(input("enter value: "))
            self.array2.append(value)

        for i in range(self.arr,self.sizee):
            self.array2.append(0)
        print("Array 1",self.array2)

        self.szee=int(input("Enter the size of your second array: "))
        self.arrys=int(input("Enter the elements for array: "))

        while self.arrys > self.szee:
            print("invalid no. of value")
            self.arrys=int(input("Enter the number of values u want to enter: "))
            
        for i in range(0,self.arrys):
            valuee=int(input("enter value: "))
            self.array3.append(valuee)

        for i in range(self.arrys,self.szee):
            self.array3.append(0)
        print("Array 2",self.array3)
        
        print("Select the operation")
        print("1. Merging of unsorted array")
        print("2. Merging of sorted array")
        print("3. Exit")
        choicee=int(input("Enter the type of array u want to merge: "))

        if choicee == 1:
            self.unsorted_array_merging()
        elif choicee == 2:
            self.sorted_array_merging()
        else:
            print("Invalid input")
        
    def unsorted_array_merging(self):
        m=self.sizee+self.szee
        self.array4 = [None]*m
        
        i=0
        while(i<self.sizee):
            self.array4[i]=self.array2[i]
            i=i+1

        j=0
        while(j<self.szee):
            self.array4[self.sizee + j]=self.array3[j]
            j=j+1
            
        print("Merging of unsorted array is",self.array4)

    def sorted_array_merging(self):
        index=0
        index_first=0
        index_second=0
        m=self.sizee + self.szee
        self.array4 = [None]*m
        
        while index_first < self.sizee and index_second < self.szee:
            if self.array2[index_first] < self.array3[index_second]:
                self.array4[index] = self.array2[index_first]
                index_first=index_first +1
                
            else:
                self.array4[index]=self.array3[index_second]
                index_second=index_second+1
            index=index+1
            
        while index_first< self.sizee:
            self.array4[index]=self.array2[index_first]
            index_first=index_first+1
            index=index+1

        while index_second < self.szee:
            self.array4[index]=self.array3[index_second]
            index_second=index_second+1
            index=index+1
        print("Merging of sorted array",self.array4)
            
    def choice(self):
        while True:
            print("operations")
            print("1. Traversal")
            print("2. Insertion")
            print("3. Deletion")
            print("4. linear search")
            print("5. Binary search")
            print("6. Bubble sort")
            print("7. Merging")
            print("8. Exit")
            choose=int(input("choose the operation u want to perform: "))


            if choose == 1:
                self.traversal()
                
            elif choose == 2:
                self.insert()
                
            elif choose == 3:
                self.delete()
                
            elif choose == 4:
                self.linear_search()
                
            elif choose == 5:
                self.binary_search()
                
            elif choose == 6:
                self.bubble_sort()
                
            elif choose == 7:
                self.merging()
                
            elif choose == 8:
                print("Exit")
                break
            else:
                print("Invalid input please try again")

p1=arrays()
p1.choice()
        
    
        

