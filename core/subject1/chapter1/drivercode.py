# Driver Code
n = 4
str1 = rand_key👎
str2=rand_key👎
print("Desired length random binary string is: ", str1)
print("Desired length random binary string is: ", str2)
op=random.randint(1,3)
sign1=random.randint(0,1)
sign2=random.randint(0,1)
def add(a,b):
    
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
     
    
    result = ''
     
    
    carry = 0
     
    
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
     
        
        carry = 0 if r < 2 else 1
     
    if carry != 0:
        result = '1' + result
     
    return result
res=add(str1,str2)
print("sum is ",res)
