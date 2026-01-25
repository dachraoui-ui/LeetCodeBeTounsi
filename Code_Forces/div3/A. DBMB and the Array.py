t = int(input())
while (t>0):
   t-=1
   n , s , x = map(int , input().split())
   arr = list(map(int,input().split()))
   tot = sum(arr)
   if ((tot == s) or (s - tot) % x == 0) and (s - tot >= 0) : 
      print("YES")
   else : 
      print("NO")
      
   
