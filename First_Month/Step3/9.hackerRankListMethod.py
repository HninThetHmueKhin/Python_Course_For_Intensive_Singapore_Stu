N = int(input("N : "))
L = []
for i in range(N):
    cmd = input("Enter command: ").split()#insert 0 5
    if cmd[0] == "insert":
        L.insert(int(cmd[1],int(cmd[2])))
    elif cmd[0] == "append":
        pass
    elif cmd[0] == "pop":
        pass
    elif cmd[0] == "print":
        pass
    elif cmd[0] == "remove":
        pass
    elif cmd[0] == "sort":
        pass
    elif cmd[0] == "reverse":
        pass
#insert 0 5  ---> cmd
# 0     1 2