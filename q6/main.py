# all imports below

"""
Any extra lines of code (if required)
as helper for this function.
"""
def findDist(v, theta):
	g = 9.807 
	h = 8848
	t = math.sqrt((2*g*h) + v*v*math.sin(theta)*math.sin(theta))
	return t*v*math.cos(theta)/g


def findstrike(velocity, alt, az):
	'''
	Parameters
	----------
	velocity : A `float`
    alt: A `float`
    az: A `float`

	Returns
	-------
	A `tuple` of two floats
	'''

	v = velocity
	lat1 = 27.9881
	lon1 = 86.9250
	earth_radius = 6.3781e6
	distance = findDist(v, math.radians(alt))
	b = distance/earth_radius
	a = math.acos(math.cos(b)*math.cos(90-lat1) + math.sin(90-lat1)*math.sin(b)*math.cos(az))
	B = math.asin(math.sin(b)*math.sin(az)/math.sin(a))
	lat2 = 90 - a
	lon2 = B + lon1
	return [lat2, lon2]
