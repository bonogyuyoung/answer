def string_match(a, b):
  count=0
  result1=[]
  result2=[]
  first=list(str(a))
  second=list(str(b))
  for i in range(0,len(a)-1):
    result1.append(first[i]+first[i+1])
  for i in range(0,len(b)-1):
    result2.append(second[i]+second[i+1])
  if len(a)>=len(b):
    for i in range(0,len(result2)):
      if result1[i]==result2[i]:
        count=count+1
  else:
    for i in range(0,len(result1)):
      if result1[i]==result2[i]:
        count=count+1
  return count
