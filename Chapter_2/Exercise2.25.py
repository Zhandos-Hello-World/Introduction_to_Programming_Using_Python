import turtle

centerX, centerY, width, height = eval(input('Enter a centerX and centerY, width and height of the rectangle: '))
turtle.penup()
turtle.goto(centerX, centerY)
turtle.pendown()
turtle.write('(' + str(centerX) + ', ' + str(centerY) + ')')

turtle.penup()
turtle.goto(centerX + (width / 2), centerY + (height / 2))
turtle.pendown()
turtle.goto(centerX + (width / 2), centerY - (height / 2))

turtle.goto(centerX - (width / 2), centerY - (height / 2))

turtle.goto(centerX - (width / 2), centerY + (height / 2))

turtle.goto(centerX + (width / 2), centerY + (height / 2))

turtle.done()
