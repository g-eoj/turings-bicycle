#wheel_diameter = raw_input("What's the rear wheel's diameter in meters?: ")
chain_total_links = int(raw_input("How many links on the chain?: "))
sprocket_total_teeth = int(raw_input("How many teeth on the sprocket?: "))
#chain_weak_link = 0 # starting position of the weak link relative to the sprocket
#wheel_bent_spoke = 0 # starting position of the bent spoke in degrees
chain_position = 0
sprocket_revolutions = 0
#distance_traveled = # kilometers?
#if distance_traveled > 1.0:
#  units = 'kilometers'
#else:
#  units = 'meters'
#  distance_traveled *= 100
while sprocket_revolutions < 201:
  sprocket_revolutions += 1
  chain_position = (chain_position + sprocket_total_teeth) % chain_total_links
  if chain_position == 0:
  #  print 'The bike can travel %d %s before the chain will fall off.' % (distance_traveled, units)
    print 'The chain fell off after %d sprocket revolutions' % sprocket_revolutions
    break
