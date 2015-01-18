from random import randint

def what_to_do(in_a_row=25):
	heads = 0
	tails = 0
	while (heads != in_a_row and tails != in_a_row):
		a = randint(1,2)
		if (a == 1):
			heads += 1
			tails = 0
		else:
			tails += 1
			heads = 0

		print("Heads count: {}. Tails count: {}".format(heads, tails))


	if heads == in_a_row:
		print("Heads successful")
	else:
		print("Tails successful")

if __name__ == '__main__':
	what_to_do()


