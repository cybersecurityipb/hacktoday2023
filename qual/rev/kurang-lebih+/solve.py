from z3 import *

flag = [Int(f'x_{i}') for i in range(40)]

s = Solver()

s.add(flag[0] == ord('h'))
s.add(flag[1] == ord('a'))
s.add(flag[2] == ord('c'))
s.add(flag[3] == ord('k'))
s.add(flag[4] == ord('t'))
s.add(flag[5] == ord('o'))
s.add(flag[6] == ord('d'))
s.add(flag[7] == ord('a'))
s.add(flag[8] == ord('y'))
s.add(flag[9] == ord('{'))
s.add(flag[-1] == ord('}'))
s.add([i < 128 for i in flag])
s.add((flag[28]+flag[19]+flag[18]+flag[17]+flag[39])==414)
s.add((flag[4]+flag[29]+flag[20]+flag[8]+flag[30])==576)
s.add((flag[31]+flag[27]+flag[25]+flag[22]+flag[2])==528)
s.add((flag[33]+flag[24]+flag[26]+flag[15]+flag[13])==497)
s.add((flag[36]+flag[0]+flag[11]+flag[35]+flag[7])==430)
s.add((flag[37]+flag[1]+flag[21]+flag[32]+flag[6])==460)
s.add((flag[5]+flag[38]+flag[9]+flag[16]+flag[10])==417)
s.add((flag[3]+flag[12]+flag[23]+flag[34]+flag[14])==509)
s.add((flag[28]-flag[19]-flag[18]-flag[17]-flag[39])==-234)
s.add((flag[4]-flag[29]-flag[20]-flag[8]-flag[30])==-344)
s.add((flag[31]-flag[27]-flag[25]-flag[22]-flag[2])==-284)
s.add((flag[33]-flag[24]-flag[26]-flag[15]-flag[13])==-317)
s.add((flag[36]-flag[0]-flag[11]-flag[35]-flag[7])==-250)
s.add((flag[37]-flag[1]-flag[21]-flag[32]-flag[6])==-216)
s.add((flag[5]-flag[38]-flag[9]-flag[16]-flag[10])==-195)
s.add((flag[3]-flag[12]-flag[23]-flag[34]-flag[14])==-295)
s.add((flag[28]+flag[19]-flag[18]+flag[17]-flag[39])==62)
s.add((flag[4]+flag[29]-flag[20]+flag[8]-flag[30])==142)
s.add((flag[31]+flag[27]-flag[25]+flag[22]-flag[2])==150)
s.add((flag[33]+flag[24]-flag[26]+flag[15]-flag[13])==117)
s.add((flag[36]+flag[0]-flag[11]+flag[35]-flag[7])==138)
s.add((flag[37]+flag[1]-flag[21]+flag[32]-flag[6])==158)
s.add((flag[5]+flag[38]-flag[9]+flag[16]-flag[10])==35)
s.add((flag[3]+flag[12]-flag[23]+flag[34]-flag[14])==95)
s.add((flag[28]-flag[19]+flag[18]-flag[17]+flag[39])==118)
s.add((flag[4]-flag[29]+flag[20]-flag[8]+flag[30])==90)
s.add((flag[31]-flag[27]+flag[25]-flag[22]+flag[2])==94)
s.add((flag[33]-flag[24]+flag[26]-flag[15]+flag[13])==63)
s.add((flag[36]-flag[0]+flag[11]-flag[35]+flag[7])==42)
s.add((flag[37]-flag[1]+flag[21]-flag[32]+flag[6])==86)
s.add((flag[5]-flag[38]+flag[9]-flag[16]+flag[10])==187)
s.add((flag[3]-flag[12]+flag[23]-flag[34]+flag[14])==119)
s.add((flag[28]+flag[19]+flag[18]-flag[17]-flag[39])==58)
s.add((flag[4]+flag[29]+flag[20]-flag[8]-flag[30])==144)
s.add((flag[31]+flag[27]+flag[25]-flag[22]-flag[2])==140)
s.add((flag[33]+flag[24]+flag[26]-flag[15]-flag[13])==117)
s.add((flag[36]+flag[0]+flag[11]-flag[35]-flag[7])==56)
s.add((flag[37]+flag[1]+flag[21]-flag[32]-flag[6])==80)
s.add((flag[5]+flag[38]+flag[9]-flag[16]-flag[10])==177)
s.add((flag[3]+flag[12]+flag[23]-flag[34]-flag[14])==85)
s.add((flag[28]-flag[19]-flag[18]+flag[17]+flag[39])==122)
s.add((flag[4]-flag[29]-flag[20]+flag[8]+flag[30])==88)
s.add((flag[31]-flag[27]-flag[25]+flag[22]+flag[2])==104)
s.add((flag[33]-flag[24]-flag[26]+flag[15]+flag[13])==63)
s.add((flag[36]-flag[0]-flag[11]+flag[35]+flag[7])==124)
s.add((flag[37]-flag[1]-flag[21]+flag[32]+flag[6])==164)
s.add((flag[5]-flag[38]-flag[9]+flag[16]+flag[10])==45)
s.add((flag[3]-flag[12]-flag[23]+flag[34]+flag[14])==129)
s.add((flag[28]+flag[19]-flag[18]-flag[17]+flag[39])==206)
s.add((flag[4]+flag[29]-flag[20]-flag[8]+flag[30])==90)
s.add((flag[31]+flag[27]-flag[25]-flag[22]+flag[2])==158)
s.add((flag[33]+flag[24]-flag[26]-flag[15]+flag[13])==117)
s.add((flag[36]+flag[0]-flag[11]-flag[35]+flag[7])==152)
s.add((flag[37]+flag[1]-flag[21]-flag[32]+flag[6])==178)
s.add((flag[5]+flag[38]-flag[9]-flag[16]+flag[10])==67)
s.add((flag[3]+flag[12]-flag[23]-flag[34]+flag[14])==139)
s.add((flag[28]-flag[19]+flag[18]+flag[17]-flag[39])==-26)
s.add((flag[4]-flag[29]+flag[20]+flag[8]-flag[30])==142)
s.add((flag[31]-flag[27]+flag[25]+flag[22]-flag[2])==86)
s.add((flag[33]-flag[24]+flag[26]+flag[15]-flag[13])==63)
s.add((flag[36]-flag[0]+flag[11]+flag[35]-flag[7])==28)
s.add((flag[37]-flag[1]+flag[21]+flag[32]-flag[6])==66)
s.add((flag[5]-flag[38]+flag[9]+flag[16]-flag[10])==155)
s.add((flag[3]-flag[12]+flag[23]+flag[34]-flag[14])==75)

if s.check() == sat:
    model = s.model()
    flag_values = [model.eval(f) for f in flag]
    flag_string = ''.join(chr(int(str(f))) for f in flag_values)
    print(f"Flag: {flag_string}")
else:
    print("No solution found.")