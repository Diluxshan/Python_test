from array import *

l1 = [1,2,3,4,5]
l2 = [2,3,4,5,6]
l3 = [3,4,5,6,7]

l4 = [l1,l2,l3]

print("col1 col2 col3 col4 col5")
for i in l4:
    for c in i:
        print(" ",c, end="  ")
    print()
