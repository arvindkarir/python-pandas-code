solution = []
ans = int(raw_input('Enter a positive integer'))
for root in range(0,ans+1):
    for pwr in range(1,6):
        if root ** pwr == ans:
          solution.append([root, pwr])
if (solution == []):
  print "No solution found."
else:
  print solution 
