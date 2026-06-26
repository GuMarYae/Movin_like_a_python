table = [] 
#creates a table

ROWS = 5;
COLUMNS = 10;
for i in range(ROWS):   #so, i is in range up to 5
    row = [0] * COLUMNS #row is declared and its value is 0 across 10 colums in each row so ROWS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    table.append(row)
    #we're appending [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] to table and we're gonna do that 4 more times 
    
def check_table():
    for i in table:
        print(i)
print(check_table())

table[3][9] = "tony"
print(check_table())
table [3][9] = 0
print(check_table())

index = 0
for index in table:
    table[index] = index
    print (index)
    index+=1