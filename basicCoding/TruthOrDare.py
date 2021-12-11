from random import choice
players_size = int(input('Number of Players:'))
players = []
print("Enter Players Names:")

for i in range(1, players_size+1):
	name = input(f"Player {i}:")
	#Appending each name in players List.
	players.append(name)

truth_questions = [
	'Describe the perfect date for you?',
	'Have you ever been kissed?',
	'Pick three people present now to spend the rest of your\
	 life on an island with. Why them?',
	'Stare into the eyes of the person you like the most for 1 minute.',
	'Which celebrity would you go out with?'
]

dare_questions = [
	'Ask the person you like the most to dance with you.',
	'Stare into the eyes of the person you like the most for 1 minute.',
	'Wear your shirt inside out.',
	'Pretend and act to be someone’s pet dog and sit on their lap.',
	'Go outside and shout the name of your crush.'
]

print("Playes in Game:",players)

while True:
	spin = input('Spin the bottle?(y/n)\n')
	if spin == 'y':
		player = choice(players)
		#Choice method randomly selects a player
		print(f"{player}'s turn")
		ch = input("Truth or Dare?(t/d)\n")
		if ch == 't':
			print(choice(truth_questions))
			#Prints Random Question from truth list.
		else:
			print(choice(dare_questions))
			#Prints Random Question from dare list.
	print()