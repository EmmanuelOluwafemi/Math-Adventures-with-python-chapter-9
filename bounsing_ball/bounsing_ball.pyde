x = 100
y = 100
xspeed = 1
yspeed = 3.3

def setup():
  size(200,200)
  smooth()
  background(255)

def draw():
  global x, y, xspeed, yspeed
  noStroke()
  fill(255)
  rect(0,0,width,height)
  
  # Add the current speed to the location.
  x += xspeed
  y += yspeed

  # Check for bouncing
  if ((x > width) or (x < 0)):
    xspeed = xspeed * -1
    
  if ((y > height) or (y < 0)):
    yspeed = yspeed * -1

  # Display at x,y location
  stroke(0)
  fill(175)
  ellipse(x,y,16,16)
