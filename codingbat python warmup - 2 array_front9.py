def array_front9(nums):
  if len(nums)<4:
    for i in range(0,len(nums)):
      if nums[i]==9:
        return True
    return False
  else:
    for i in range(0,4):
      if nums[i]==9:
        return True
    return False
