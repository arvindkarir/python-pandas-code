poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''
# The above phrase is used to input text in the file poem.txt which
# goes to the default directory \exercies in this case
# Open for 'w'riting
f = open('poem.txt', 'w')
# Write text, which is the string above, to file
f.write(poem)
# Close the file
f.close()
# If no mode is specified,
# 'r'ead mode is assumed by default
f = open('poem.txt')
while True:
  line = f.readline()
  if len(line) == 0:   # Zero length indicates EOF
    break
  # The `line` already has a newline
  # at the end of each line
  # since it is reading from a file.
  print(line, end='')
  # close the file
f.close()
