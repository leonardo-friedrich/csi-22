import turtle
window = turtle.Screen()
fred= turtle.Turtle()
k=0
for j in range (5):
    for i in range(4):
        fred.forward(20-2*k)
        fred.left(90)
    k=k-10
    fred.up()
    fred.goto(k,k)
    fred.down()
window.mainloop()




