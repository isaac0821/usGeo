import math

from .usClosestZips import *
from .usZips import *

def getTauFromZipcodeList(zipcodeList):
	tau = {}
	for i in zipcodeList:
		for j in zipcodeList:
			if (i < j):
				tau[i, j] = getZipcodeDist(i, j)
				tau[j, i] = getZipcodeDist(j, i)
			else:
				tau[i, j] = 0.0001
	return tau

def getZipcodeDistNet(zipcode1, zipcode2):
	if (zipcode1 == None or zipcode2 == None or zipcode1 == zipcode2):
		return 0.0001
	elif (zipcode1 not in closestZips):
		print("Zip code " + str(zipcode1) + " not found.")
		return None
	elif (zipcode2 not in closestZips):
		print("Zip code " + str(zipcode2) + " not found.")
	else:
		return shortestDistNet(zipcode1, zipcode2)

def shortestDistNet(nodeID1, nodeID2):
	dist = None

	return dist


def getZipcodeDist(zipcode1, zipcode2):
	if (zipcode1 == None or zipcode2 == None or zipcode1 == zipcode2):
		return 0.0001
	elif (zipcode1 not in validZips):
		print("Zip code " + str(zipcode1) + " not found.")
		return None
	elif (zipcode2 not in validZips):
		print("Zip code " + str(zipcode2) + " not found.")
	else:
		return sphereEuclidean2D(validZips[zipcode1]['loc'], validZips[zipcode2]['loc']) * 1.3

def sphereEuclidean2D(coord1, coord2):
	R = 3958.8  # Earth radius in miles
	lat1, lon1 = coord1
	lat2, lon2 = coord2
	phi1, phi2 = math.radians(lat1), math.radians(lat2) 
	dphi       = math.radians(lat2 - lat1)
	dlambda    = math.radians(lon2 - lon1)
	a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
	return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))