import turtle as trtl
#----initialize turtles----
player = trtl.Turtle() 
player.setheading(90)
player.penup()

#----variables----
score = 0



#----functions----

#moves player forward
def move_forward():
	player.forward(100)

#moves player backward
def move_backward():
	player.backward(100)

#moves player left
def move_left():
	cur_xcor = player.xcor()
	cur_ycor = player.ycor()
	player.setposition(cur_xcor-100,cur_ycor)

#moves player right
def move_right():
	cur_xcor = player.xcor()
	cur_ycor = player.ycor() 
	player.setposition(cur_xcor+100,cur_ycor)
	


wn = trtl.Screen()

#----event/calls----

#listens for movement then activates the move functions accordingly.
wn.onkey(move_forward, 'w')
wn.onkey (move_backward, 's')
wn.onkey(move_left, 'a')
wn.onkey(move_right, 'd')
wn.listen()

wn.mainloop()