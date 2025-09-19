def PalindromeIndex(n,k):
  for i in range(1,k+1):
    rev = int(str(n)[::-1])
    s = n + rev
    if str(s) == str(s)[::-1]:
      return [i,s]
    n = s
  return[-1,-1]     
print(PalindromeIndex(89,30))
