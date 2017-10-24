import random
randomSet=set([])
for i in range (0,11413224, 234):
    randomSet.add(random.random()*12312)
    if len(randomSet) >= 200:
        break
print(randomSet)
