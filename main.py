from associate.fpgrowth import *
T = [[1,   3, 4  ],
     [   2, 3,  5],
     [ 1,2,3,   5],
     [  2,      5]]
itemsets = frequent_itemsets(T,2)
print(itemsets)
print(np.__file__)