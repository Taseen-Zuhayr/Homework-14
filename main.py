import turtle

pen = turtle.Screen()
pen.bgcolor("tan")
pen.title("Square")

cursor = turtle.Turtle()
size = 0
for i in range(4):
    turtle.forward(100)
    turtle.right(90)