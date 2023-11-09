#for One_Twenty in range(1,21):
    #print(One_Twenty)

#for One_Twenty in range(1,1000001):
    #print(One_Twenty)   

Millie = list(range(1,1000000))
print(min(Millie))
print(max(Millie))
print(sum(Millie))

odd = list(range(1,20,2))
print(odd)

even = list(range(2,21,2))
print(even)

threes = [value*3 for value in range(3,30)]
print(threes)

expthrees3 = []
for value in range(1,10): 
    expthrees3.append(value**3)
    print(expthrees3)
    
expthrees2 = [value**3 for value in range(1,10)]
print(expthrees2)

