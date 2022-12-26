import random
from core.subject1.chapter2.solver import k_map_solver,utils

alph=['A','B','C','D','E']

def minimized_expression():
    str_terms = []
    terms_not_care = []

    #Generating random number of minterms
    no_minterms=random.randint(4,8)
    minterm_range=[i for i in range(16)]
    random.shuffle(minterm_range)

    all_opt_min=[]
    #Converting the minterms into binary
    #it is used as input to quine mccluskey algo
    for i in range(no_minterms):
        min_t=bin(minterm_range[i])[2:]
    
        if(len(min_t)<4):
            rem_zero=4-len(min_t)
            min_t='0'*rem_zero+min_t
        str_terms.append(min_t)

    all_opt_min.append(str_terms)
    #Minterms for option 1
    min_t=bin(minterm_range[no_minterms])[2:]
    opt1=str_terms
    if(len(min_t)<4):
        rem_zero=4-len(min_t)
        min_t='0'*rem_zero+min_t
    
    opt1.append(min_t)
    all_opt_min.append(opt1)

    #Minterms for option 2
    min_t=bin(minterm_range[no_minterms+1])[2:]
    opt2=opt1
    if(len(min_t)<4):
        rem_zero=4-len(min_t)
        min_t='0'*rem_zero+min_t
    
    opt2.append(min_t)
    all_opt_min.append(opt2)

    #Minterms for option 3
    min_t=bin(minterm_range[no_minterms+2])[2:]
    opt3=opt2
    if(len(min_t)<4):
        rem_zero=4-len(min_t)
        min_t='0'*rem_zero+min_t
    
    opt3.append(min_t)
    all_opt_min.append(opt3)

    t_min=minterm_range[:no_minterms]
    t_min.sort()

    print("Which of the following is the minimized SOP for the minterms: ",t_min)

    opts=[[],[],[],[]]
    for i in range(4):
        str_terms=all_opt_min[i]
        t_minterms = [utils.Term(term) for term in str_terms]
        not_cares = [utils.Term(term) for term in terms_not_care]

        minterms = k_map_solver.Minterms(t_minterms, not_cares)
        res=[]
        res=minterms.simplify()
        for _exp in res:
        # print(" + ",end='')
            opts[i].append('')
            for j in range(4):
                if _exp[j]=='0':
                    opts[i][-1]=opts[i][-1]+alph[j]+"'"
                else:
                    opts[i][-1]=opts[i][-1]+alph[j]
        print("Option ",i+1," + ".join(opts[i]))
        #print(res)


    print("Correct answer:"," + ".join(opts[0]))