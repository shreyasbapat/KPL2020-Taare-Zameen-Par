# all imports below
from astropy.coordinates import SkyCoord  # High-level coordinates
from astropy.coordinates import ICRS, GCRS, CartesianDifferential, CartesianRepresentation
from astropy.coordinates import Angle, Latitude, Longitude  # Angles
import astropy.units as u

from poliastro.plotting import OrbitPlotter2D, OrbitPlotter3D
from poliastro.bodies import Earth

from poliastro.twobody.orbit import Orbit
"""
Any extra lines of code (if required)
as helper for this function.
"""

def CartesianToSpherical(x, y, z):
	r = math.sqrt(x*x + y*y + z*z)
	alt = math.atan(y/x)
	az = math.acos(z/r)
	return [r, alt, az]

def sphericalToCartesian(v, alt, az):
	x = v*math.cos(alt)*math.sin(az)
	y = v*math.cos(alt)*math.cos(az)
	z = v*math.sin(alt)
	return [x, y, z]

def timeOfFlight(e):
	f = 1-e
	alpha = Earth.R.to(u.km).value / (Earth.R.to(u.km).value + 8.848)
	minutes = 13.5*math.acos((1-alpha*(2-f))/math.sqrt(pow((3-alpha*(2-f)),2) - 4*alpha/f))
	return minutes*u.min

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
	p = sphericalToCartesian(velocity, alt, az)
	vx = p[0]
	vy = p[1]
	vz = p[2]
	g = GCRS(x=0*u.km, y=0*u.km, z=(Earth.R.to(u.km).value + 8.848)*u.km, v_x=vx*u.km/u.s, v_y=vy*u.km/u.s, v_z=vz*u.km/u.s,
	representation_type=CartesianRepresentation, differential_type=CartesianDifferential)
	orb = Orbit.from_coords(Earth, g)
	tof = timeOfFlight(orb.ecc.value)
	orb2 = orb.propagate(tof)
	position = orb.r.value
	m = CartesianToSpherical(position[0], position[1], position[2])
	alt = m[1] * u.rad
	az = m[2] * u.rad
	altd = alt.to(u.deg)
	azd = az.to(u.deg)
	return altd, azd
