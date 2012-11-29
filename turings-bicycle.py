from math import pi

tire_diameter = float(raw_input("What's the rear tire's outer diameter in milimeters?: "))
chain_total_links = int(raw_input("How many links on the chain?: "))
sprocket_total_teeth = int(raw_input("How many teeth on the sprocket?: "))
chain_position = int(raw_input("The bent spoke is now touching the the chain. How many chain links away is the weak link?: ")) % chain_total_links

tire_circumference = tire_diameter * pi # milimeters
sprocket_revolutions = 0
distance_traveled = 0.0
units = 'milimeters'
chain_on = True

while sprocket_revolutions < 501:
  sprocket_revolutions += 1
  chain_position = (chain_position + sprocket_total_teeth) % chain_total_links
  distance_traveled += tire_circumference
  if chain_position == 0:
    chain_on = False
    break

if distance_traveled > 1000:
  units = 'meters'
  distance_traveled /= 1000
if distance_traveled > 1000:
  units = 'kilometers'
  distance_traveled /= 1000

if chain_on == True:
  print 'The bike can travel at least %.2f %s before the chain falls off.' % (distance_traveled, units)
else:
  print 'The bike can travel %.2f %s before the chain falls off.' % (distance_traveled, units)
  #print 'The chain fell off after %d sprocket revolutions' % sprocket_revolutions
