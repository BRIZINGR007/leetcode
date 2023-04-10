def sortColors(self, elements):
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
        return elements
elements = [2,0,2,1,1,0]
print("Unsorted list is,") 
print( elements)

sortColors(elements)
print("Sorted Array is, ")
print(elements)