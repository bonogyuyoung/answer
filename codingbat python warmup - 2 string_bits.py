def string_bits(str):
  result=""
  if len(str)<2:
    return str
  a=list(str)
  for i in range(0,len(a)):
    if i % 2 == 0:
      result=result+a[i]
  return result
