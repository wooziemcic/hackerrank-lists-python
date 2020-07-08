li = []
if __name__ == '__main__':
    for _ in range(int(input())):
        x = input().split(" ")
        if x[0] == "insert":
            li.insert(int(x[1]), int(x[2]))
        elif x[0] == "remove":
            li.remove(int(x[1]))
        elif x[0] == "reverse":
            li.reverse()
        elif x[0] == "pop":
            li.pop()
        elif x[0] == "sort":
            li.sort()
        elif x[0] == "append":
            li.append(int(x[1]))
        elif x[0] == "print":
            print(li)
        else:
            print("Error")
