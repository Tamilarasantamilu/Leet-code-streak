sys.stdout = open('user.out', 'w')
a= tuple(i for i in map(loads, stdin))
for i in range(0,len(a),2):
    hand=a[i]
    groupSize=a[i+1]
    m=collections.defaultdict(lambda: 0)
    for i in hand:
        m[i]+=1
    v=list(m.keys())
    v.sort()
    flag=0
    for i in v:
        while m[i]:
            for j in range(groupSize):
                if m[i+j]==0:
                    print("false")
                    flag=1
                    break
                m[i+j]-=1
            if flag:break
        if flag:break
    if flag:continue
    print("true")
            
