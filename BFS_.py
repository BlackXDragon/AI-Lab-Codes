dict={}
queue=[]
visited=[]
origin={}

dict={'A':['F','C','B'],
      'B':['G','C'],
      'C':['F'],
      'D':['C'],
      'E':['D','C','J'],
      'F':['D'],
      'G':['C','E'],
      'J':['D','K'],
      'K':['E','G']}

for i in dict:
    visited.append(i)
    origin[i]=0
    break

while len(visited)!=0:
    n=visited.pop(0)
    queue.append(n)
    for i in queue:
        for j in dict[i]:
            if n==j:
                origin[n]=i

            
    for i in dict[n]:
        if i not in queue:
            visited.append(i)


print("queue:",queue)
print("origin:",origin)


        
value='K'        
while value in origin:
     print(value)
     value=origin[value]
     
    
'''             
value='K'
listt=[]
for i in origin:
    listt.append(i)
print(listt)  #['A', 'F', 'C', 'B', 'D', 'G', 'E', 'J', 'K']


for j in range(0,len(listt)):
    i=listt[j]
    if i==value:
        print(value)
        value=origin[i]
        print(i,"->",value)
        print(value)
        j=0
 
'''
        
        
        
