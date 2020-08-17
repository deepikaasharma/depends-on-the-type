# define your function here
def depends_on_the_type(x):
  if type(x)is bool:
    return False
#if str
  elif type(x) is str:
    return x+x
#if float
  elif type(x) is float:
    return x*1.5
#if int
  elif type(x) is int:
    #if obj=0
    if x==0:
        return "Zero"
    elif x%2==0:
      return x*x
    else:
      return x*x*x
  else:
    return None

print(depends_on_the_type(True))
      

#none of them