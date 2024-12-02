#import sys
#sys.exit()

def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]


def calculate(expenses):
	for x in expenses:
		for y in expenses:
			if(x + y < 2020):
				for z in expenses:
					if(x + y + z == 2020):
						print(x)
						print(y)
						print(z)
						print(x * y * z)
						return


expenses = read_integers("Day1IN.txt")
calculate(expenses)
