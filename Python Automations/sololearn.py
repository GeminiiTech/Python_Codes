
from itertools import permutations


letters = 'kenny'
p_letters = permutations(letters)
l_letters = list(p_letters)

a = 0
for i in l_letters:
    print(i)
    first_letter = i[0]
    if first_letter == 'a':
       a+=1

