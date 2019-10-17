first_input = str(raw_input('Enter first string\n'))
second_input = str(raw_input('Enter second string?\n'))
print 'This is what you entered\n', first_input, second_input

    
set_one = set(first_input)
set_two = set(second_input)
intersect = set_one & set_two #or s intersection(t)
exclusion = set_one ^ set_two #or symmetric_difference(t)
a_minus_b = set_one - set_two #or s.difference(t)
b_minus_a = set_two - set_one #or t.difference(s)
print intersect, 'are common'
print exclusion, 'are not common'
print a_minus_b, 'first string less second string'
print b_minus_a, 'second string less first string'
