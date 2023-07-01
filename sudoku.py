import sys

output = ""
lineCount = 0

#load given numbers from stdin
for line in sys.stdin:
    line = line.strip()
    numbers = line.split()
    result = ''.join(numbers)
    output += result + " 0\n"
    lineCount +=1


# na kazdem radku musi byt 1-9
for value in range(1, 10):
    for row in range(1, 10):
        line=""
        for column in range(1, 10):
            line +=str(row)+str(column)+str(value)+ " "
        
        output += line+" 0\n"
        lineCount+=1

# v kazdem sloupci musi byt 1-9
for value in range(1, 10):
    for column in range(1, 10):
        line=""
        for row in range(1, 10):
            line +=str(row)+str(column)+str(value)+ " "
        
        output += line+" 0\n"
        lineCount+=1


#na kazdem radku nesmi byt 2 a vice stejnych cisel
for row in range(1, 10):
    for value in range(1, 10):
        for column in range(1, 10):
            for column2 in range(column+1, 10):
                if (column != column2):
                    line = "-"+str(row)+str(column)+str(value)+" -"+str(row)+str(column2)+str(value)
                    output += line+" 0\n"
                    lineCount+=1

#v kazdem sloupci nesmi byt 2 a vice stejnych cisel
for column in range(1, 10):
    for value in range(1, 10):
        for row in range(1, 10):
            for row2 in range(row+1, 10):
                if (row != row2):
                    line = "-"+str(row)+str(column)+str(value)+" -"+str(row2)+str(column)+str(value)
                    output += line+" 0\n"
                    lineCount+=1

#v kazdem ctverci, jehoz levy horni roh je na pozici [square_row, square_column], muze byt kazda cislice 1-9 max jednou
for square_row in range(1, 8, 3):
    for square_column in range(1, 8, 3):
        for value in range(1, 10):
            for row in range(square_row, square_row+3):
                for column in range(square_column, square_column+3):
                    line = str(row)+str(column)+str(value)
                    for row2 in range(square_row, square_row +3):
                        for column2 in range(square_column, square_column+3):
                            if (not((column2 == column) and (row2 == row)) and ((column2 >= column) or(row2 >= row))):
                                line2 = "-" +line+" " + "-" + str(row2)+str(column2)+str(value)
                                output +=line2+ " 0\n"
                                lineCount+=1

#na kazdem policku muze byt pouze jedno cislo
for row in range(1, 10):
    for column in range(1, 10):
        for i in range(1, 10):
            for j in range(i+1, 10):
                line = " -" + str(row) + str(column) +str(i) + " -" + str(row) + str(column) + str(j)
                output +=line+ " 0\n"
                lineCount+=1


#pridani hlavicky
header = "c sudoku\n"
header += "p cnf "+ str(81)+" "+str(lineCount)+"\n"
output = header + output
print(output)