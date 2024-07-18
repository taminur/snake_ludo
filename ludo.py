import random


class Board():
	def __init__(self):
		self.positions = list(range(1,101))
		self.ladder = {6:16, 8:41, 26:29, 50:93, 55:80, 59:84}
		self.snakes = {32:13, 60:38, 63:3, 70:25, 73:47, 82:43, 89:53, 97:12}

class Dice(list):
	def __init__(self):
		self.nos = list(range(1,7))
	def throw(self):
		return random.choice(self.nos)

class Player():
	def __init__(self, name):
		self.name = name
		self.ticket = False
		self.pos = 0
		self.ladder_climed = 0
		self.snake_bites = 0

	def throw(self, other):
		return other.throw()

	def __str__(self):
		return f'{self.name} is at {self.pos} having ticket {self.ticket}'

class Game():
	def __init__(self, list_of_players):
		self.list_of_players = list_of_players
		self.board = Board()
		self.dice = Dice()
		self.winners = {}

	def start(self):
		# while len(self.winners) < len(self.list_of_players):
		for i in range(1, 1001):
			# print(f'------------round {i}-------------')
			for player in self.list_of_players:
				
				# checks whether player got the ticket to start
				if not player.ticket:
					if player.throw(self.dice) == 1:
						player.ticket = True

				# after getting the ticket

				if player.ticket:
					new_pos = player.throw(self.dice) + player.pos

					if new_pos <= 100:
						if new_pos in self.board.ladder.keys():
							player.pos = self.board.ladder[new_pos]
							player.ladder_climed += 1
						elif new_pos in self.board.snakes.keys():
							player.pos = self.board.snakes[new_pos]
							player.snake_bites += 1
						else:
							player.pos = new_pos
						if player.pos == 100:
							self.winners[player] = i
							self.list_of_players.remove(player)

				# print(player)
			# print(f'round - {i}')
			if len(self.list_of_players) == 0:
				break
			# if len(self.winners) == 1:
			# 	break
		for player in self.winners.keys():
			print(f'{player.name} wins after {self.winners[player]} rounds who climed ladder {player.ladder_climed} times and got bite {player.snake_bites} times')
			 


if __name__ == '__main__':
	player1 = Player("Tamim")
	player2 = Player("Fatima")
	player3 = Player("Maimuna")
	
	list_of_players = [player1, player2, player3]
	
	game = Game(list_of_players)

	game.start()
	print('-----------------the END--------------------')