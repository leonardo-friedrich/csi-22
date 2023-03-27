import turtle
window = turtle.Screen()
fred= turtle.Turtle()
fred.up()
fred.goto(-200,0)
fred.down()
k=0
for j in range (100):
        fred.forward(k)
        fred.right(90)
        k=k+2
fred.up()
fred.goto(200,0)
fred.down()
k=0
for j in range (100):
        fred.forward(k)
        fred.right(89)
        k=k+2
window.mainloop()