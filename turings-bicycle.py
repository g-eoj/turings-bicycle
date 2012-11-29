from math import pi

tire_diameter = float(raw_input("What's the rear tire's outer diameter in milimeters?: "))
chain_total_links = int(raw_input("How many links on the chain?: "))
sprocket_total_teeth = int(raw_input("How many teeth on the sprocket?: "))
#chain_weak_link = 0 # starting position of the weak link relative to the sprocket
#rim_bent_spoke = 0 # starting position of the bent spoke in degrees relative to the sprocket
tire_circumference = tire_diameter * pi
chain_position = 0
sprocket_revolutions = 0
distance_traveled = 0.0
units = 'milimeters'
while sprocket_revolutions < 201:
  sprocket_revolutions += 1
  chain_position = (chain_position + sprocket_total_teeth) % chain_total_links
  distance_traveled += tire_circumference
  if chain_position == 0:
    if distance_traveled > 1000:
      units = 'meters'
      distance_traveled /= 1000
    if distance_traveled > 1000:
      units = 'kilometers'
      distance_traveled /= 1000
    print 'The bike can travel %.2f %s before the chain will fall off.' % (distance_traveled, units)
    #print 'The chain fell off after %d sprocket revolutions' % sprocket_revolutions
    break
