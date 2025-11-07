t=int(input())
while(t):
   t-=1
   x=int(input())
   p=1
   l=[]
   while(x>0):
      if(x%10>0):
         l.append((x%10)*p)
      x//=10
      p*=10
   print(len(l))
   for i in l : print(i)
   