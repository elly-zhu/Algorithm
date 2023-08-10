#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque
def hasPath(maze, start, destination):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    def isValid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] != 1
    
    queue = deque([start])
    visited = set()

    while queue:
        x, y = queue.popleft()
        if [x, y] == destination:
            return True
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        for dx, dy in directions:
            newX, newY = x + dx, y + dy
            
            # Keep rolling in the same direction until you hit a wall or go out of bounds
            while isValid(newX, newY):
                newX += dx
                newY += dy
            
            # Roll back one step to the last valid cell
            newX -= dx
            newY -= dy
            
            if (newX, newY) not in visited:
                queue.append([newX, newY])
    return False


# In[2]:


# Test data
maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]

print(hasPath(maze, start, destination))  # Output: true


# In[3]:


# Test data
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [3,2]
print(hasPath(maze, start, destination))  # Output: false


# In[4]:


# Test data
maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
start = [4,3]
destination = [0,1]
print(hasPath(maze, start, destination))  # Output: false

