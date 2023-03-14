words = ["Hello","Alaska","Dad","Peace"]
aa=["qwertyuiop","asdfghjkl","zxcvbnm"]
lst = list()

for z in aa:
    for i in words:
        count = 0
        for j in range(len(i)):
            if i[j].lower() in z:
                count+=1 
        if count == len(i):
            lst.append(i)       

print(lst)