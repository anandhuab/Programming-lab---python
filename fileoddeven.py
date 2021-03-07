with open('main.txt','r',encoding='utf-8') as f:
    #print(f.read())
    for i in f:
        s=i.split()
        print(s)
    for i in s:
        x=int(i)
        if x%2==0:
            with open("even.txt",'a',encoding='utf-8') as e:
                e.write(i)
                e.write("\n")
        else:
            with open("odd.txt",'a',encoding='utf-8') as e:
                e.write(i)
                e.write("\n")
