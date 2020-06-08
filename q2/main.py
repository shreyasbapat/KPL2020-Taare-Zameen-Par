# all imports below
import astropy.units as u

"""
Any extra lines of code (if required)
as helper for this function.
"""

def findDistance(vrec):
	'''
	Parameters
	----------
	vrec : a `float`

	Returns
	-------
	a `float`
	'''
	vrec = vrec * u.km / u.s
	mpar = 1000000 * u.parsec
	H = 71 * u.km / u.s / mpar
	D = vrec / H
	D = D.to(lyr)
	return D.value
