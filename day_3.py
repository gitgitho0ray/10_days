# probabilities
dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]
combinations = []
six = []
overnine = []
for i in dice1:
    for d in dice2:
        combinations.append([i, d])
        if i + d == 6 and i != d:
            six.append([i, d])
        elif i + d > 9:
            overnine.append([i, d])

print(len(six) / len(combinations))
print(1 - len(overnine) / len(combinations))


#compound probabs
bin1=['r']*4 + ['b']*3
bin2=['r']*5 + ['b']*4
bin3=['r']*4 + ['b']*4

combos=[]
for i in bin1:
    for i2 in bin2:
        for i3 in bin3:
            combos.append([i,i2,i3])

len(combos)

r2b1=[]
for i in test1:
    if ''.join(i) == 'rrb' or ''.join(i) == 'brr' or ''.join(i) == 'rbr':
        r2b1.append(i)
# r2b1=[i for i in test1 if ''.join(i) == 'rrb' or ''.join(i) == 'brr' or ''.join(i) == 'rbr']
len(r2b1)
len(r2b1)/len(combos)


def hcfnaive(a, b):
    if (b == 0):
        return a
    else:
        return hcfnaive(b, a % b)


a = 204
b = 504

print(hcfnaive(a, b))

## 52 card deck
suits = 'a b c d'.split()
cards =  [i for i in range(2,15)]

deck=[[c,s] for s in suits for c in cards]
deck2=[i for i in suits for n in range(2,15)]


numbers = [10, 20, 30, 40]
ggg = numbers.remove(10)
print(numbers)
ten = numbers.pop(-1)

print(numbers)
