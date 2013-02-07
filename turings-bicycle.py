# todos:
# cmd line controls
# detect states where chain never falls off
# specify wheel start position
# readme - give users common bike info hints to questions?

from math import pi
from sys import exit

# function to ask user a question, test that the answer is a number, and return that number
def ask(question, valueType):
  while True:
    try:
      answer = valueType(raw_input(question))
      if answer < 0:
        raise ValueError
      return answer
    except ValueError:
      if valueType == int:
        print "  ^ Enter a positive whole number..."
      else:
        print "  ^ Enter a positive number..."

# function to calculate total distance bike can be ridden before chain falls off or if chain will never falll off
def calcDistance(tire_diameter, chain_position, sprocket_total_teeth, chain_total_links, max_sprocket_revolutions):
  tire_circumference = tire_diameter * pi # milimeters
  sprocket_revolutions = 0
  distance_traveled = 0.0
  chain_on = 1 # 0 - chain will fall off, 1 - chain may fall off eventually, 2 - chain will never fall off
  
  # determine if the bent spoke and weak link will never come in contact, does it catch all scenarios?
  if chain_total_links % 2 == 0 and sprocket_total_teeth % 2 == 0 and chain_position % 2 != 0:
    chain_on = 2
  elif chain_total_links % sprocket_total_teeth == 0:
    positions = []
    for i in range(chain_total_links / sprocket_total_teeth):
      positions.append(i * sprocket_total_teeth + chain_position)
    if 0 not in positions:
      chain_on = 2

  # calculate distance the bike can travel before the chain falls off, limited by max_sprocket_revolutions
  while sprocket_revolutions <= max_sprocket_revolutions and chain_on == 1:
    sprocket_revolutions += 1
    chain_position = (chain_position + sprocket_total_teeth) % chain_total_links
    distance_traveled += tire_circumference
    if chain_position == 0:
      chain_on = 0
  
  return distance_traveled, chain_on

# function to convert distance traveled to meters or kilometers if needed
def metricConversion(distance_traveled):
  units = 'milimeters'
  if distance_traveled > 1000:
    units = 'meters'
    distance_traveled /= 1000
  if distance_traveled > 1000:
    units = 'kilometers'
    distance_traveled /= 1000
  return distance_traveled, units

# function to return result of calculations in readable format
def result(chain_on, distance_traveled, units):
  if chain_on == 1:
    return "\nThe bike can be ridden at least %.2f %s before the chain falls off.\n" % (distance_traveled, units)
  elif chain_on == 0:
    return "\nThe bike can be ridden %.2f %s before the chain falls off.\n" % (distance_traveled, units)
    #print "The chain fell off after %d sprocket revolutions" % sprocket_revolutions
  else:
    return "\nThe chain will never fall off.\n"

# interactive shell
# introduction
print """
Turing's bicycle has a rear rim with a bent spoke and a chain with a weak link.
When the bent spoke and weak link come in contact with each other the chain
falls off. Input some information about the bicycle to calculate how far 
it can be ridden before the chain falls off:
"""

while True:
  # get information about the bike from user
  tire_diameter = ask("  What's the rear tire's outer diameter in milimeters?: ", float)
  chain_total_links = ask("  How many links in the chain?: ", int)
  sprocket_total_teeth = ask("  How many teeth on the sprocket?: ", int)
  chain_position = ask("  The bent spoke is now touching the the chain. How many chain links away \n  is the weak link?: ", int) % chain_total_links

  # calculate total distance bike can be ridden before chain falls off, 500 max_sprocket_revolutions is arbitrary
  distance_traveled, chain_on = calcDistance(tire_diameter, chain_position, sprocket_total_teeth, chain_total_links, 500)

  # convert distance traveled to meters or kilometers if needed
  distance_traveled, units = metricConversion(distance_traveled)

  # give user the result
  print result(chain_on, distance_traveled, units)

  # check if user wants to try again
  do_again = raw_input("Press enter to continue or type 'e' to exit: ")
  if do_again == 'e':
    exit(0)
  print "\r"
