import turtle

###################################################
## Change the variable values to draw a pentagon ##
###################################################

screen = 500
sides = 5
length = 100

window = turtle.Screen()
window.setup(screen, screen)
my_ttl = turtle.Turtle()

for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360 / sides)