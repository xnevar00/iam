import sys

if (len(sys.argv) != 2):
    print("Chybny zapis argumentu!")
    exit()

n = sys.argv[1]
n = int(n)

output = ""
lineCount = 0

# na kazdem radku musi byt alespon jedna dama
for i in range(0, n):
    line=""
    for j in range(1, n+1):
        num = i*n+j
        line +=str(num)+" "
    
    output += line+" 0\n"
    lineCount+=1

#v kazdem loupci musi byt alespon jedna dama
for i in range(1, n+1):
    line = ""
    for j in range(0, n):
        num = j*n+i
        line += str(num)+" "
    
    output += line+" 0\n"
    lineCount+=1

#na kazdem radku nesmi byt 2 a vice dam
for i in range(0, n):
    for j in range(1, n+1):
        for k in range(j, n+1):
            if (j != k):
                line = "-"+str(i*n+j)+" -"+str(i*n+k)
                output += line+" 0\n"
                lineCount+=1


#v kazdem sloupci nesmi byt 2 a vice dam
for i in range(1, n+1):
    for j in range(0, n):
        for k in range(0, n):
            if (j != k):
                line = "-"+str(j*n+i)+" -"+str(k*n +i)
                output += line+" 0\n"
                lineCount+=1

#pro lepsi manipulaci s uhlopricky = pole
array = [[0 for j in range(n)] for i in range(n)]

num = 1
for i in range(n):
    for j in range(n):
        array[i][j] = num
        num += 1

#diagonaly zleva doprava shora dolu
#max 1 dama na kazde diagonale
for i in range (0, n):
    for j in range (0, n):
        staticElement = array[i][j]
        for k in range(1, n):
            if (i+k < n and j+k < n):
                dynamicElement = array[i+k][j+k]
                line =  "-"+str(staticElement)+" -"+str(dynamicElement)
                output += line+" 0\n"
                lineCount+=1


#diagonaly zleva doprava sdola nahoru
#max 1 dama na kazde diagonale
for i in range (0, n):
    for j in range (0, n):
        staticElement = array[i][j]
        for k in range(1, n):
            if (i-k >= 0 and j+k < n):
                dynamicElement = array[i-k][j+k]
                line =  "-"+str(staticElement)+" -"+str(dynamicElement)
                output += line+" 0\n"
                lineCount+=1

#pridani hlavicky
header = "c queens\n"
header += "p cnf "+ str(n*n)+" "+str(lineCount)+"\n"
output = header + output
print(output)