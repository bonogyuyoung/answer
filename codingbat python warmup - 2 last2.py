def last2(str):
  count=0
  a=list(str)
  for i in range(1,len(a)-1):
    if a[i] == a[len(a)-1] and a[i-1] == a[len(a)-2]:
      count=count+1
  return count

