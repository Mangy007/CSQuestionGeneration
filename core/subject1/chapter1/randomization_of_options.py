import random
from operator import*
 

def rand_key(p):
   
    
    key1 = ""
 
    
    for i in range(p):
         
        
        temp = str(random.randint(0, 1))
 
        key1 += temp
         
    return(key1)
