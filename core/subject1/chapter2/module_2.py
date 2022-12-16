import random
from core.subject1.chapter2.solver import Kmap,utils


str_terms = []
terms_not_care = []


no_minterms=random.randint(4,8)
minterm_range=[i for i in range(16)]
random.shuffle(minterm_range)


for i in range(no_minterms):
    min_t=bin(minterm_range[i])[2:]
    
    if(len(min_t)<4):
        rem_zero=4-len(min_t)
        min_t='0'*rem_zero+min_t
    str_terms.append(min_t)

t_min=minterm_range[:no_minterms]
t_min.sort()
print("Minterms: ",t_min)
t_minterms = [utils.Term(term) for term in str_terms]
not_cares = [utils.Term(term) for term in terms_not_care]

minterms = Kmap.Minterms(t_minterms, not_cares)
res=[]
res=minterms.simplify()
#print(res)
alph=['A','B','C','D','E']
print("Minimized Boolean expression: ",end='')
for i in range(4):
    if res[0][i]=='*':
        continue
    elif res[0][i]=='0':
        print(alph[i]+"'",end='')
    else:
        print(alph[i],end='')

for _exp in res[1:]:
    print(" + ",end='')
    for i in range(4):
        if _exp[i]=='*':
            continue
        elif _exp[i]=='0':
            print(alph[i]+"'",end='')
        else:
            print(alph[i],end='')

print()