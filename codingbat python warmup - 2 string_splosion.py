def string_splosion(str):
  b=""
  if len(str)<=1:
    return str
  for i in range(0,len(str)+1):
    a=str[:i]
    b=b+a
  return b
