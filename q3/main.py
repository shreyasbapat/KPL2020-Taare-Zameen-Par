# all imports below
from astropy import constants
from astropy import units as u
"""
Any extra lines of code (if required)
as helper for this function.
"""

def findDelay(dist):
	'''
	Parameters
	----------
	dist : A `float`

	Returns
	-------
	A `float`
	'''
	dist = dist * u.m
	Me = 5.94 * 10**24 * u.kg
	c = constants.c
	G = constants.G
	Re = 6357000 * u.m
	velocity = ((G * Me) / dist)**0.5
	beta = velocity**2 / c**2
	gamma = 1/ ((1 - beta)**0.5)
	T = 1 * gamma
	return T.value
