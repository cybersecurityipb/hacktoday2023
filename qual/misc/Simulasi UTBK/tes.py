
r = open("tes.txt", "r").readlines()
database = {}

s = 0
double = []
for i in r:
    temp = i.split('?')
    if temp[0] in database.keys():
        print(s)
        double.append(s)
    database[temp[0]] = temp[1]
    s += 1

print(len(database))
print(len(double))

def delete_lines(file_path, lines_to_delete):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = [line for i, line in enumerate(lines) if i not in lines_to_delete]

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)


file_path = 'tes.txt'
lines_to_delete = [2, 5, 7]  # Specify the line numbers you want to delete

delete_lines(file_path, double)

# def recover(file_path, lines_to_delete):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
        
    
#     modified_lines = []
#     for i in lines:
#         if 'Hitunglah' in i:
#             if '?' not in i: 
#                 print('hm')
#                 temp = i.index('.')
#                 s = list(i)
#                 s[temp] = '?'
#                 s = ''.join(s)
#                 print(s)
#                 modified_lines.append(s)
#             else:
#                 modified_lines.append(i)
#         else:
#             modified_lines.append(i)

#     with open(file_path, 'w') as file:
#         file.writelines(modified_lines)

# recover("tes.txt", 0)