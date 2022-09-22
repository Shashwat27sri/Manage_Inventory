####################### manage the inventory ########################
t=int(input())
for j in range (t):
    n=int(input())
    l = [[],[]]
    for _ in range (n):
        item = input().split()
        item_name=item[0]
        item_quantity=int (item[1])
        l[0].append(item_name)
        l[1].append(item_quantity)

    m=int(input())
    for _ in range(m):
        op = input()
        a=op.find(" ")
        b=op[a+1:]
        b=b.split(" ")
        name =b[0]
        num = int (b[1])
        op=op[:a]
        if op == "ADD":                    ##ADD operation 
            if name not in l[0]:
                l[0].append(name )
                l[1].append(num)
                print(f"ADDED Item {name}")
            else:
                new=l[0].index(name)
                l[1][new]+=num
                print(f"UPDATED Item {name}")
        

        elif op=="DELETE":                 ##DELETE OPERATION 
            if name not in l[0]:
                print(f"Item {name } does not exist")
            else:
                new=l[0].index(name)
                if num <= l[1][new]:
                    l[1][new] -= num
                    print(f"DELETED Item {name}")
                else:
                    print(f"Item {name} could not be DELETED")
            

    total = sum(l[1])
    print(f"Total Items in Inventory: {total}")