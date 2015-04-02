# Second FizzBuzz program
# Accepts one argument from user at run time; if no argument provided, asks for argument on run

import sys

limit = 0

while limit == 0:
  try:
    limit = int(sys.argv[1])
  except (IndexError, ValueError):
    try:
      limit = int(raw_input("How high do you want FizzBuzz to count? (enter a number): "))
    except (IndexError, ValueError):
      print "Looks like that wasn't a number."


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