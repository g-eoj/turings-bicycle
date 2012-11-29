# todos:
# calculate if chain will never fall off
# format print output widths
# give users common bike info hints to questions?
# input tests

from math import pi

# introduction
print "Turing's bicycle has a rear rim with a bent spoke and a chain with a weak link. When the bent spoke and weak link come in contact with each other the chain falls off. Input some information about the bicycle to calculate how far it can be ridden before the chain falls off."

# get information about the bike
tire_diameter = float(raw_input("What's the rear tire's outer diameter in milimeters?: "))
chain_total_links = int(raw_input("How many links in the chain?: "))
sprocket_total_teeth = int(raw_input("How many teeth on the sprocket?: "))
chain_position = int(raw_input("The bent spoke is now touching the the chain. How many chain links away is the weak link?: ")) % chain_total_links

tire_circumference = tire_diameter * pi # milimeters
sprocket_revolutions = 0
distance_traveled = 0.0
units = 'milimeters'
chain_on = True

# calculate distance the bike can travel before the chain falls off, up to 500 sprocket revolutions
while sprocket_revolutions < 501:
  sprocket_revolutions += 1
  chain_position = (chain_position + sprocket_total_teeth) % chain_total_links
  distance_traveled += tire_circumference
  if chain_position == 0:
    chain_on = False
    break

# convert distance traveled to meters or kilometers if needed
if distance_traveled > 1000:
  units = 'meters'
  distance_traveled /= 1000
if distance_traveled > 1000:
  units = 'kilometers'
  distance_traveled /= 1000

# give user the result
if chain_on == True:
  print 'The bike can travel at least %.2f %s before the chain falls off.' % (distance_traveled, units)
else:
  print 'The bike can travel %.2f %s before the chain falls off.' % (distance_traveled, units)
  #print 'The chain fell off after %d sprocket revolutions' % sprocket_revolutions
