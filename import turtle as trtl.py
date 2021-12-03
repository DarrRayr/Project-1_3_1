
#----imports----
import turtle as trtl
import random as rand
import time 

#----initialize turtles----
player = trtl.Turtle() 
wn = trtl.Screen()
point = trtl.Turtle()
writer = trtl.Turtle()
player.setheading(90)
player.penup()

#sets point shape and color
point.shape("square")
point.color("yellow")
#identifies shapes
sprite_1 = "sprite_1.gif" 
sprite_2 = "sprite_2.gif" 
sprite_3 = "sprite_3.gif" 
sprite_4 = "sprite_4.gif" 
bullet = "bullet.gif"

#adds shapes to turtle list
wn.addshape(sprite_1) 
wn.addshape(sprite_2) 
wn.addshape(sprite_3) 
wn.addshape(sprite_4) 
wn.addshape(bullet)



#----variables----
score = 0
min_bullets = 0
max_bullets = 0
font_setup = ("Arial", 20, "normal")



#----functions----

#gives the player a random character
def random_char():
	player_shapes = ["sprite_1.gif", "sprite_2.gif", "sprite_3.gif", "sprite_4.gif"]
	chosen_sprite = str(player_shapes[rand.randint(0,3)])
	print (chosen_sprite)
	player.shape(chosen_sprite)

#asks the player for what difficulty they want.
def pick_difficulty():
	global min_bullets
	global max_bullets

	difficulty = input("Hard | Medium | Easy: ")
	difficulty.lower()
	if difficulty == "easy":
		print("You chose easy.")
		min_bullets = 1
		max_bullets = 2
	elif difficulty == "medium":
		print("You chose medium!")
		min_bullets = 2
		max_bullets = 3

	elif difficulty == "hard":
		print("YOU CHOSE HARD!")
		min_bullets = 3
		max_bullets = 4
	else:
		pick_difficulty()


	

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

def make_border():
	writer.penup()
	writer.setposition(-300,-300)
	writer.pendown()
	for x in range(2):
		writer.left(90)
		writer.forward(300)
		writer.left(90)
		writer.forward(300)

	

#moves player back to 0,0 if they try and get out of the border






#----event/calls----

#listens for movement then activates the move functions accordingly.
wn.onkey(move_forward, 'w')
wn.onkey (move_backward, 's')
wn.onkey(move_left, 'a')
wn.onkey(move_right, 'd')
wn.listen()
make_border()
random_char()
pick_difficulty()





wn.mainloop()
