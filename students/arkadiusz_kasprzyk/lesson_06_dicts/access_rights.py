# access_right.py

symbols = {'execute': 'X', 'read': 'R', 'write': 'W'}

N = int(input("Give N: "))
rights = dict()

for k in range(N):
    file_k = input("{}: ".format(k + 1)).split(" ")
    rights[file_k[0]] = set(file_k[1:])

M = int(input("Give M: "))
commands = [''] * M

for k in range(M):
    commands[k] = input("{}: ".format(k + 1)).split(" ")

<<<<<<< HEAD
print("")  # just aesthetics for testing in Snakify
=======
print("")  # just aestethics for testing in Snakify
>>>>>>> 20508ca4668bf458c74a7d554f4bab5ad0bf3736

for k in range(M):
    if symbols[commands[k][0]] in rights[commands[k][1]]:
        print("OK")
    else:
        print("Access denied!")
