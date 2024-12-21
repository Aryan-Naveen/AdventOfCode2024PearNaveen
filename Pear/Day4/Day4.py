#create a grid 2D of the characters
#search for x 
#take the remaining 8 digits look for a M, if no M search for next X
#If M is in correct spot, use same direction to search for A, if not search for next X
# If A is in correct spot, use same direction to search for S, if not search for next X
#If S in in the correct spot, +1 to "xmas" counter
import numpy as np
with open ("Input4.txt" , "r") as file:
    lines = file.readlines()
grid = []


for line in lines:
    row = line.strip().split()
    grid.append(list(row[0]))

grid = np.array(grid)
n_rows, n_cols = grid.shape

#search for x 
x_row , x_col = np.where(grid == "X")

directions = np.array([[-1, 1], [0,1], [1, 1] , [1, 0] , [1,-1] , [0,-1] , [-1 ,-1] , [-1 , 0] ])
count = 0
for index in range(len(x_row)):
    x_coord = np.array([x_row[index], x_col[index]])
    for direction in directions:
        m_coord = direction + x_coord
        a_coord = (2 * direction) + x_coord
        s_coord = (3 * direction) + x_coord
        if s_coord[0] >= 0 and s_coord[0] < n_rows and s_coord[1] >= 0 and s_coord[1] < n_cols:
            x_val = grid[x_coord[0], x_coord[1]]
            m_val = grid[m_coord[0] , m_coord[1]]
            a_val = grid[a_coord[0] , a_coord[1]]
            s_val = grid[s_coord[0] , s_coord[1]]
            if m_val == "M" and a_val == "A" and s_val == "S":
                count +=1


#print (count)
a_row, a_col = np.where(grid == "A")
counter = 0
for index in range(len(a_row)):
    a_coord = np.array([a_row[index] , a_col[index]])
    if a_coord[0] >= 1 and a_coord[1] >= 1 and a_coord[0] < n_rows - 1 and a_coord[1] < n_cols - 1:
        tl = grid[a_coord[0] - 1 , a_coord[1] + 1]
        tr =  grid[a_coord[0] + 1 , a_coord[1] + 1] 
        bl =  grid[a_coord[0] - 1 , a_coord[1] - 1]
        br =  grid[a_coord[0] + 1 , a_coord[1] - 1]
        d1 = [tl, br]
        d2 = [tr, bl]
        if (d1 == ["M" , "S"] or d1 == ["S" , "M"]) and (d2 == ["M" , "S"] or d2 == ["S" , "M"]):
            counter += 1
print (counter)



#replace anchor of x_coord with a_coord
#check to see if A is in a valid location if a_coord[0] >= 1 and a_coord[1] >= 1 and a_coord[0] <= n_rows - 1 and a_coord[1] <= n_cols - 1  
#topleftcorner = grid[a-coord[0] - 1 , a-coord[1] + 1]
#toprightcorner =  grid[a-coord[0] + 1 , a-coord[1] + 1] 
#bottomleftcorner =  grid[a-coord[0] - 1 , a-coord[1] - 1]
#bottomrightcorner =  grid[a-coord[0] + 1 , a-coord[1] - 1]
#check diagnals 
#if diagnals satisfied  counter =+ 1