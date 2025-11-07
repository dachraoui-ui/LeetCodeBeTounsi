t = int(input())
while t>0 :
   t-=1
   n = int(input())
   str = input()
   res = []
   for i,num  in enumerate(str) :
      if num == '0':
         str = str[:i] + str[i+1:]
         res.append(i)
   print(len(res))
   print(*res)



   
   