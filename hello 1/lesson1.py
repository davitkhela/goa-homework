from turtle import *
#start drawing the square
width(7)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


forward(200)
left(90)
end_fill()
#the square is done

#start drawing the door
begin_fill()
forward(70)
left(90)

color("yellow")
forward (90)
right(90)

forward(60)
right(90)

forward(90)
end_fill()
#the door is constructed

#it is time for the roof
penup()
goto(200,200)
pendown()

begin_fill()
color("red")
right(150)
forward(200)

left(120)
forward(200)
end_fill()
#the roof is finished too

#time for some windows

penup()
goto(5,180)
pendown()
begin_fill()
color("cyan")
left(120)
forward(50)

right(90)
forward(25)

right(90)
forward(50)

right(90)
forward(25)
end_fill()

#2nd window
penup()
goto(195,180)
pendown()
begin_fill()
left(90)
forward(50)

left(90)
forward(25)

left(90)
forward(50)

left(90)
forward(25)
end_fill()
#done

#lets add some extra stuff

penup()
goto(6,178)
color("white")
pendown()
right(90)
forward(10)

penup()
goto(147,178)
pendown()

forward(10)

#the door needs a knob

penup()
goto(120,30)
color("brown")
pendown()

width(20)
forward(1)
#its done!! yippie!!