from util.grammar import is_allowed_true, get_answer_as_number

r = None

print("You need to get to new york now you can:")
print("1. Go to the subway")
print("2. Go to the airport again.")
r = get_answer_as_number([1, 2])

if r == 1:
	print("You go and buy a sandwich, nobody said you would go to a train station or the sandwich shop")
	exit("You die of diabetes")

print("On your way there you see a monke on the road and have 2 choices:")
print("1.Take de monke")
print("2.Leave de monke")
print("3.Watch then laugh at it getting run over by a car")
r = get_answer_as_number([1, 2, 3])

if r == 1:
	print("You took de monke and now he will just follow you around")

if r == 2:
	print("you leave de monke and then carry on with your pathetic boring life")
	exit("zzzzzzz oh died of bordom lol")

if r == 3:
	print("you get run over by a car")
	exit("karma")