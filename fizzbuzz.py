# First FizzBuzz program
# Hardcoded limit is 100

limit = 20
counter = 1

print "Fizz buzz counting up to %s" % limit
while counter <= limit:
    if counter % 3 == 0 and counter % 5 == 0:
        print "FizzBuzz"
    elif counter % 3 == 0:
        print "Fizz"
    elif counter % 5 == 0:
        print "Buzz"
    else:
        print str(counter)
    counter += 1