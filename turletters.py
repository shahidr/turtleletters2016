import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        tur.setpos(40, 0)
    elif letter == "B":
	    pass
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":
	    pass		
	elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
	    pass
    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":
	turtle.pu()
        turtle.fd(10)
        turtle.right(90)
        turtle.fd(15)
        turtle.pd()
        turtle.circle(10)
        turtle.pu()
        turtle.left(90)
        turtle.fd(10)
        turtle.pd()
        turtle.right(45)
        turtle.fd(15)
        turtle.pu()
        turtle.fd(15)
        turtle.left(135)
        turtle.fd(35)
        tur.setheading(0,0,0)
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
	    pass
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	turtle.pu()
        turtle.fd(7)
        turtle.right(90)
        turtle.fd(10)
        turtle.pd()
        turtle.left(45)
        turtle.fd(20)
        turtle.left(90)
        turtle.fd(20)
        turtle.right(180)
        turtle.fd(20)
        turtle.left(45)
        turtle.fd(20)
        turtle.pu()
        turtle.left(90)
        turtle.fd(17)
        turtle.left(90)
        turtle.fd(45)
        turtle.right(90)
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)
	







window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(1)
turtleLetter("box",tur)
turtleLetter("A",tur)


window.exitonclick()
