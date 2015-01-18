############################################################
# Author: Druddigon
# Date Created: 18/1/2015
# Purpose: Program to make decisions between two options
#          for you. Will flip a coin repeatedly until X 
#          number of heads or X number of tails occur 
#          in a row. 
#
############################################################

from random import randint

def what_to_do(in_a_row, heads_wins, tails_wins):
	heads = 0
	tails = 0
	flips = 0
	while (heads != in_a_row and tails != in_a_row):
		a = randint(1,2)
		flips += 1
		if (a == 1):
			heads += 1
			tails = 0
		else:
			tails += 1
			heads = 0

	if heads == in_a_row:
		print("{} heads in a row! Decision made: {}".format(in_a_row, heads_wins))
	else:
		print("{} tails in a row! Decision made: {}".format(in_a_row, tails_wins))

	print("Flips: {}".format(flips))

if __name__ == '__main__':
	print("How many flips in a row for a decision?")
	num_flips = int(input())
	print("What are you going to do if heads wins?")
	heads_wins = input()
	print("What are you going to do if tails wins?")
	tails_wins = input()
	print("Determining decision, please wait.")
	what_to_do(num_flips, heads_wins, tails_wins)


