import matplotlib.pyplot as plt
import random

from .usZips import *
from .usCounties import *
from .usStates import *
from .usStatesPoly import *

def randomColor():
	color = "#%06x" % random.randint(0, 0xFFFFFF)
	return color

def plotStatesPoly(
	fig:		"Based matplotlib figure object" = None,
	ax:			"Based matplotlib ax object" = None,
	size:		"Size of figure" = 1,
	states: 	"States that going to be plotted" = [],
	color:		"Color of state boundary \
				 1) String 'Random', or \
				 2) String of color" = 'Random',
	saveFigPath:"1) None, if not exporting image, or \
				 2) String, the path for exporting image" = None
	) -> "fig, ax":

	# State list in full name =================================================
	stateList = []
	for state in states:
		if (state not in validStates and state not in statesAbbrDict):
			print("ERROR: '%s' is not a valid State name" % state)
		elif (state in statesAbbrDict):
			stateList.append(statesAbbrDict[state])
		else:
			stateList.append(state)

	# If no based matplotlib figure, define boundary ==========================
	if (fig == None or ax == None):
		fig, ax = plt.subplots()
		allLats = []
		allLons = []
		for state in stateList:
			poly = polyStates[state]
			for pt in poly:
				allLats.append(pt[0])
				allLons.append(pt[1])
		xMin = min(allLons) - 0.25
		xMax = max(allLons) + 0.25
		yMin = min(allLats) - 0.25
		yMax = max(allLats) + 0.25
		xSpan = None
		ySpan = None
		if (xMax - xMin > yMax - yMin):
			xSpan = 20
			ySpan = 20 * ((yMax - yMin) / (xMax - xMin))
		else:
			xSpan = 20 * ((xMax - xMin) / (yMax - yMin))
			ySpan = 20
		fig.set_figheight(ySpan * size)
		fig.set_figwidth(xSpan * size)
		ax.set_xlim(xMin, xMax)
		ax.set_ylim(yMin, yMax)

	# Plot polygon state by state =============================================
	for state in stateList:
		lx = []
		ly = []
		poly = polyStates[state]
		for pt in poly:
			lx.append(pt[1])
			ly.append(pt[0])
		lx.append(poly[0][1])
		ly.append(poly[0][0])
		if (color == 'Random'):
			rndColor = randomColor()
			ax.plot(lx, ly, color=rndColor)
		else:
			ax.plot(lx, ly, color=color)
	# Save figure =============================================================
	if (saveFigPath != None):
		fig.savefig(saveFigPath)

	return fig, ax