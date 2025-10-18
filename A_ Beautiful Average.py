t = int(input())
while t>0 :
   t-=1
   n = int(input())
   arr = list(map(int, input().split()))
   
   avg = arr[0]
   for i in range(1 , n) : 
      if arr[i] > avg :
         avg = arr[i]

   print(avg)



