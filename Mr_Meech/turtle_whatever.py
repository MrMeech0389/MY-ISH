import turtle


turtle.speed(0)

def turnleft():
    turtle.left(90)

turtle.onkeypress(turnleft, "a")
turtle.listen()



def doTickActions():
    turtle.forward(50)
    
    
def handleTick():
    doTickActions()
    turtle.ontimer(handleTick, 200)
    
handleTick()
    

turtle.mainloop()