import analyses as an
import time


def main():

	#an.analyse_nbtweets('tweets.csv')
	#an.analyse_client('tweets.csv')

t0 = time.clock()

if __name__ == '__main__':
	main()

t1 = time.clock()

print('Temps d\'execution: ', t1-t0, 's')