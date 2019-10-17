#something to understanding scoping and nested functions
def f(x):
  def g():
    x = 'abc'
    print 'function x=', x
  def h():
    z = x
    print 'hz =', z
  x = x + 1
  print 'x plus 1 =', x
  h()
  g()
  print 'gx=', x
  return g
 
x = 3
z = f(x)
print 'zx=', x
