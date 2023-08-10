#!/usr/bin/env python
# coding: utf-8

# In[5]:


def hasPath(maze, start, destination):
    rows, cols = len(maze), len(maze[0])
    visited = set()

    def dfs(x, y):
        if [x, y] == destination:
            return True
        
        if (x, y) in visited:
            return False

        visited.add((x, y))

        # Move up
        i, j = x, y
        while i > 0 and maze[i - 1][j] != 1:
            i -= 1
        if dfs(i, j):
            return True

        # Move down
        i, j = x, y
        while i < rows - 1 and maze[i + 1][j] != 1:
            i += 1
        if dfs(i, j):
            return True

        # Move left
        i, j = x, y
        while j > 0 and maze[i][j - 1] != 1:
            j -= 1
        if dfs(i, j):
            return True

        # Move right
        i, j = x, y
        while j < cols - 1 and maze[i][j + 1] != 1:
            j += 1
        if dfs(i, j):
            return True

        return False

    return dfs(start[0], start[1])




# In[6]:


# Test data
maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]

print(hasPath(maze, start, destination))  # Output: true


# In[7]:


# Test data
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [3,2]
print(hasPath(maze, start, destination))  # Output: false


# In[8]:


# Test data
maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
start = [4,3]
destination = [0,1]
print(hasPath(maze, start, destination))  # Output: false

