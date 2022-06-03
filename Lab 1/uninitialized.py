#Uninitialized variables problem.
f = 10
g = 2
g *= f
g += f*5
print(g)
