# todos:
# detect states where chain never falls off
# specify wheel start position
# give users common bike info hints to questions?
# loop program

from math import pi

# introduction
print """
Turing's bicycle has a rear rim with a bent spoke and a chain with a weak link.
When the bent spoke and weak link come in contact with each other the chain
falls off. Input some information about the bicycle to calculate how far 
it can be ridden before the chain falls off:
"""
# function to test user input to questions is a number
def answerEval(question, valueType):
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

# get information about the bike from user
tire_diameter = answerEval("  What's the rear tire's outer diameter in milimeters?: ", float)
chain_total_links = answerEval("  How many links in the chain?: ", int)
sprocket_total_teeth = answerEval("  How many teeth on the sprocket?: ", int)
chain_position = answerEval("  The bent spoke is now touching the the chain. How many chain links away \n  is the weak link?: ", int) % chain_total_links

tire_circumference = tire_diameter * pi # milimeters
sprocket_revolutions = 0
distance_traveled = 0.0
units = 'milimeters'
chain_on = 1 # 0 - chain will fall off, 1 - chain may fall off eventually, 2 - chain will never fall off

# determine if the bent spoke and weak link will never come in contact, does it catch all scenarios?
if chain_total_links % sprocket_total_teeth == 0:
  positions = []
  for i in range(chain_total_links / sprocket_total_teeth):
    positions.append(i * sprocket_total_teeth + chain_position)
  if 0 not in positions:
    chain_on = 2

if chain_total_links % 2 == 0 and sprocket_total_teeth % 2 == 0 and chain_position % 2 != 0:
  chain_on = 2

# calculate distance the bike can travel before the chain falls off, up to 500 sprocket revolutions
while sprocket_revolutions < 501 and chain_on != 2:
  sprocket_revolutions += 1
  chain_position = (chain_position + sprocket_total_teeth) % chain_total_links
  distance_traveled += tire_circumference
  if chain_position == 0:
    chain_on = 0
    break

# convert distance traveled to meters or kilometers if needed
def metricConversion(distance_traveled, units):
  if distance_traveled > 1000:
    units = 'meters'
    distance_traveled /= 1000
  if distance_traveled > 1000:
    units = 'kilometers'
    distance_traveled /= 1000
  return distance_traveled, units

distance_traveled, units = metricConversion(distance_traveled, units)

# give user the result
if chain_on == 1:
  print '\nThe bike can be ridden at least %.2f %s before the chain falls off.\n' % (distance_traveled, units)
elif chain_on == 0:
  print '\nThe bike can be ridden %.2f %s before the chain falls off.\n' % (distance_traveled, units)
  #print 'The chain fell off after %d sprocket revolutions' % sprocket_revolutions
else:
  print "\nThe chain will never fall off.\n"
