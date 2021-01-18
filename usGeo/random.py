import random

from .usZips import *
from .usCounties import *
from .usStates import *

def rndZipcode(
	N: 			"Number of unrepeated zip codes" = 1,
	excStates: 	"List of States that will not be sampled" = [],
	incStates:	"List of States that will be sampled, overwrites `excStates" = []
	) -> "Return a randomly selected zip code":

	if (len(excStates) == 0 and len(incStates) == 0):
		zipList = list(validZips.keys())
	elif (len(incStates) > 0):
		zipList = [z for z, s in validZips.items() if s['state'] in incStates]
	else:
		zipList = [z for z, s in validZips.items() if s['state'] not in excStates]
	zipcodes = random.sample(zipList, N)
	return zipcodes