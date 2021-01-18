import math

from .usZips import *

def getZipcodeDist(zipCode1, zipCode2):
	if (zipCode1 == None or zipCode2 == None or zipCode1 == zipCode2):
		return 0.0001
	elif (zipCode1 not in validZips):
		print("Zip code " + str(zipCode1) + " not found.")
		return None
	elif (zipCode2 not in validZips):
		print("Zip code " + str(zipCode2) + " not found.")
	else:
		return sphereEuclidean2D(validZips[zipCode1]['loc'], validZips[zipCode2]['loc'])

def sphereEuclidean2D(coord1, coord2):
	R = 3958.8  # Earth radius in miles
	lat1, lon1 = coord1
	lat2, lon2 = coord2
	phi1, phi2 = math.radians(lat1), math.radians(lat2) 
	dphi       = math.radians(lat2 - lat1)
	dlambda    = math.radians(lon2 - lon1)
	a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
	return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))