import random
import math

#1. an outer loop decreases in size each time
#2. The goal is to have the largest number at the end of the list when the outer loop completes 1 cycle
#3. The inner loop starts comparting indexes at the beginning of the loop
#4 Check if list[Index] > list[Index + 1]
#5. If so, swap list[Index] and list[Index + 1]
#6. When the innner loop completes the largest nuber is at the end of the list
#7. Decrement the outer loop by 1

numlist = []

for i in range(5):
    numlist.append(random.randint(1, 10))

i = len(numlist) - 1

while i > 1:
    
    j = 0
    
    while j < i:
        print("\nIs {} > {}".format(numlist[j], numlist[j + 1]))
        
        if numlist[j] > numlist[j + 1]:
            
            print("Switch")
            
            temp = numlist[j]
            numlist[j] = numlist[j + 1]
            numlist[j + 1] = temp
        else:
            print("Don't switch")
            
        j += 1
        
        for k in numlist:
            print(k, end = ", ")
        print()
       
    print("END OF ROUND")
    i -= 1

for k in numlist:
    print(k, end = ", ")
print()
