from random import shuffle

flag = b'ipb.link/z3-zolve-huh (not flag btw $^$)'

idx_flag = list(range(len(flag)))
shuffle(idx_flag)

flag_format = ["(flag[%d]+flag[%d]+flag[%d]+flag[%d]+flag[%d])", "(flag[%d]-flag[%d]-flag[%d]-flag[%d]-flag[%d])", "(flag[%d]+flag[%d]-flag[%d]+flag[%d]-flag[%d])", "(flag[%d]-flag[%d]+flag[%d]-flag[%d]+flag[%d])", "(flag[%d]+flag[%d]+flag[%d]-flag[%d]-flag[%d])", "(flag[%d]-flag[%d]-flag[%d]+flag[%d]+flag[%d])", "(flag[%d]+flag[%d]-flag[%d]-flag[%d]+flag[%d])", "(flag[%d]-flag[%d]+flag[%d]+flag[%d]-flag[%d])"]

idx_format = [i for i in range(len(flag_format))]
idx = []

for i in range(0, len(idx_flag), 5):
    idx.append(idx_flag[i:i+5])

# print(idx)
# print(idx_format)
out = ''

for j in idx_format:
    for i in idx:
        cond = flag_format[j]%tuple(i)
        val = eval(cond)
        print('s.add(%s==%d)'%(cond,val))
        frmt = '(%s==%d)and(%s)'%(cond,val,out)
        out = frmt
        # print(eval('(%s==%d)'%(cond,val)))
        # print('(%s==%d)'%(cond,val))

# print()
out = out.replace('and()','')
print(out)
print(eval(out))
