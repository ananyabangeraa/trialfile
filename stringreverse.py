lep = "banana"
new = ''
new1 = ''
n = 1
print(lep[::-1])
# with while loop
while(n<=len(lep)):
  new = new + lep[len(lep)-n]
  n+=1
print(new)
# with for loop
for n in range(len(lep)):
  new1 = new1 + lep[len(lep)-1-n]
print(new1)
