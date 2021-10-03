def childs(node, ignore=0):
    for el in d[node]:
        if el != ignore:
            yield el
            
def path(node, ignore=0):    
    arr = childs(node, ignore)
    
    flag = False
    max_p = 0
    
    for child in arr:
        flag = True
        p = path(child, ignore=node)
        
        if p > max_p:
            max_p = p
    
    return max_p+1 if flag else 1

with open('input.txt') as f:
    n = int(f.readline())
    d = dict()
    
    for _ in range(n-1):
        num1, num2 = map(int, f.readline().split())
        
        if num1 in d:
            d[num1].add(num2)
        else:
            d[num1] = {num2}
            
        if num2 in d:
            d[num2].add(num1)
        else:
            d[num2] = {num1}
            
ones = []

for k in d:
    if len(d[k]) == 1:
        ones += [k]
        
if n == 1:
    print(1)
elif len(ones) == 2:
    print(n)
else:
    max_path = 0

    for start in ones:
        p = path(start)

        if p > max_path:
            max_path = p
    print(max_path if n > 1 else 1)
