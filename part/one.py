from util.grammar import is_allowed_true, get_answer_as_number
r = None

r = input("Do you want to go to the Airport ✈ ? ")

if is_allowed_true(r):
	print("You go to the ✈️  Airport and think of what flight to go on")

else:
	print("You died to a seagull flying at 30,000,000 miles a second")
	exit(1)
print("You can go on a flight with Le Bron James as captain on flight #43")
print("You can go on a flight with a stranger as a captain on flight #86")
print("1. #43")
print("2. #86")

r = get_answer_as_number([1, 2])

if r == 1:
	print("You forgot to check where the flight takes you and land in north korea where you get shot down durring landing")
	exit("You died in North Korea.\nThats probably not good.")

print("You are in the flight.")
print("You are thrown into the cockpit by people with guns.")
print("You are now given a knife.  🗡️")
print("You are told by the people with guns to kill the pilot with the weapon, to survive.")
if not is_allowed_true(input("Do you want to kill the poor pilot? ")):
  exit("You died")

print("Now comes the tricky part - you have to pilot the plane")
print("You have two options:")
print("""
1. Glide the plane down to the ground safely
2. Turn off all the engines and systems
""")

r = get_answer_as_number([1, 2])

if r == 1:
	print("You try to glide down safely but then accidentaly turn on the blinkers and a plane nearby thought you were gonna turn so kept going straight and crashed into you")
	exit("You committed homicide")

elif r == 2:
	print("You turn off all of the engines and think your gonna die but then the plane lands in a vat of orange juice and everyone survived exept Jeff but nobody cares about jeff")
print("now you smell like oranges and have 2 choices")
print("1. Jump into a lake")
print("2. Go to hospital")
r = get_answer_as_number([1, 2])

if r == 1:
	print("You jumped into the lake and it turns out that the kracken lives there and he ate you.")
	exit("At least you cleaned your clothes")
else:
	print("You go to the hospital and a doctor comes to clean your cloths because it is a laundry house")