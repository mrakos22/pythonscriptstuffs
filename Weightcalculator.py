import sys

name = raw_input('What is your name:')
weight = int(input('How much your weight(in Kg):'))
height = float(input ('How much your height(in Meter) :'))

print 'Hello dear %s' %name
print 'Your weight is %s' %weight
print 'Your height is %s' %height
calculate =float (height*height/weight)

if calculate<19:
	print 'Your body is Skinny'
elif calculate<25:
	print 'Your body is Normal'
elif calculate<27:
	print 'Your body is Overweight'
elif calculate<30:
	print 'Your body is have  little Overweight'
elif calculate<40:
	print 'Your body is have a middle Overweight'
else:
	print 'Your body is have a diseased Overweight'


print " ______ __  __"
print "|__ ___|\ \/ /"
print "  |_|    |__|"
print "created by:R.Akos"

