def front_back(str):#str 문자열 받기
  if len(str)<=1:
    return str
    exit()
  a=list(str)
  b=a[:]
  result=""
  del b[0]
  del b[len(b)-1]
  for i in range(0,len(b)):
    c="%s" % b[i]
    result=result+c
  output=a[len(a)-1]+result+a[0]
  return output
