def front3(str):
  a=list(str)
  if len(str)<3:
    b=str+str+str
    return b
  else:
    c=a[0]+a[1]+a[2]
    result=c*3
    return result
