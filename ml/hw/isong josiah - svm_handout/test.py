dna = "CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA"
dic = {}
index = [a for a in range(0,len(dna), 3)]
print(index)

for i in index:
    seg = dna[i:i+3]
    if seg in dic:
        dic[seg] += 1
    elif seg not in dic:
        dic[seg] = 1
print(dic)