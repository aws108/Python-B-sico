salir = false

while salir == False:

	print "You enter a dark room with two doors. Do you go through door #º or door @?"

	door = raw_input("> ")

	if door == "1":
		print "There's a giant bear here eating a cheese cake. What do you do?"
		print "·1. take the cake"
		print "2. Scream at the bear"
	
		bear= raw_input("> ")
	
		if bear =="1":
			print "The bear eats your face off. Good job!"
		elif bear =="2":
			print "The bear eats your legs off. Good job!"
		else:
	elif door=="2":
		print "You stare into the endless abyss at Thulu's retina"
		print "1 blueberries"
		print "2 Yellow jacket clothespins"
		print"3 Undertanding revolvers yelling melodies"
	
		insanity = raw_input("> ")
	
		if insanity =="1" or insanity =="2":
			print "Your body survives powered by a mind of jello. Good job!"
		else:
			print "The insanity rots your eyes into a pool of muck. Good job!"
	else:
		print "You stumble around and fall on a knife and die. Good job!"
	
	salir = raw_input("Desea salir del programa?. Escriba S o N")
	
	if salir =="S":
		salir=True
	else:
		salir=False
