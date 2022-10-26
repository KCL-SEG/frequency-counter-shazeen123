def frequencies(items):
    frequencies = {}
    if len(items)!=0:
        list = []
        for value in items:
            y = str(value)
            list.append(y)
        list.sort()
        x = list[0]
        i = 1
        count = 1
        while i < len(list):
            if x!=list[i]:
                frequencies[x]=count
                count=1
            elif x==list[i]:
                count += 1
            x=list[i]
            i +=1
        else:
            frequencies[x]=count
    return frequencies
