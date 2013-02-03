# todos:
# detect states where chain never falls off
# specify wheel start position
# give users common bike info hints to questions?
# input tests

from math import pi

# introduction
print """
Turing's bicycle has a rear rim with a bent spoke and a chain with a weak link.
When the bent spoke and weak link come in contact with each other the chain
falls off. Input some information about the bicycle to calculate how far it can
be ridden before the chain falls off:
"""

# get information about the bike from user
tire_diameter = float(raw_input("  What's the rear tire's outer diameter in milimeters?: "))
chain_total_links = int(raw_input("  How many links in the chain?: "))
sprocket_total_teeth = int(raw_input("  How many teeth on the sprocket?: "))
chain_position = int(raw_input("  The bent spoke is now touching the the chain. How many chain links away is \n  the weak link?: ")) % chain_total_links

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
# def metric_conversion
if distance_traveled > 1000:
  units = 'meters'
  distance_traveled /= 1000
if distance_traveled > 1000:
  units = 'kilometers'
  distance_traveled /= 1000

# give user the result
if chain_on == 1:
  print '\nThe bike can be ridden at least %.2f %s before the chain falls off.\n' % (distance_traveled, units)
elif chain_on == 0:
  print '\nThe bike can be ridden %.2f %s before the chain falls off.\n' % (distance_traveled, units)
  #print 'The chain fell off after %d sprocket revolutions' % sprocket_revolutions
else:
  print "\nThe chain will never fall off.\n"
