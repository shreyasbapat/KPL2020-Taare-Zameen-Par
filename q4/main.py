# all imports below
from datetime import datetime
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import EarthLocation, AltAz, get_body
import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style, quantity_support
plt.style.use(astropy_mpl_style)
quantity_support()
"""
Any extra lines of code (if required)
as helper for this function.
"""

startobs = datetime(2020, 6, 9, 0, 9, 46, 906323)
 #replace it by the time when Saturn will be just visible
endobs = datetime(2020, 6, 9, 6, 41, 3, 209311) #replace it by the time when Saturn is no longer visible from SAC terrace



def findSaturn(obstime):
	'''
	Parameters
	----------
	obstime : A `~datetime.datetime` instance.

	Returns
	-------
	A `tuple` of two floats.
	'''
	time = Time(obstime)
	utcoffset = 5.5*u.hour
	time = time - utcoffset
	gravity = EarthLocation(lat=31.78135*u.deg, lon=76.99313*u.deg, height=1000*u.m)
	saturn = get_body('Saturn', time=time, location=gravity)
	saturnaltaz = saturn.transform_to(AltAz(obstime=time,location=gravity))
	return saturnaltaz.alt.value, saturnaltaz.az.value

def stentime(plot=False):
	gravity = EarthLocation(lat=31.78135*u.deg, lon=76.99313*u.deg, height=1000*u.m)
	time = Time(datetime(2020, 6, 8, 20, 18, 37, 274634))
	deluni = np.linspace(0, 12, 1440)
	delta = deluni*u.hour
	utcoffset = 5.5*u.hour
	time = time - utcoffset
	saturn = get_body('Saturn', time=time, location=gravity)
	frame = AltAz(obstime=time+delta,location=gravity)
	range1 = saturn.transform_to(frame)
	alts = range1.alt.value
	list20=[]
	for i in range(1440):
		if(alts[i]>=20):
			list20.append(i)
	first20delta=deluni[list20[0]]
	last20delta=deluni[list20[len(list20)-1]]
	st = first20delta * u.hour
	ls = last20delta * u.hour
	if plot:
		plt.plot(delta, range1.alt.value)
		plt.xlim(0, 12)
		plt.xlabel('Hours from 8 PM IST')
		plt.ylabel('Saturn Alt at Gravity')
		plt.show()
	rise = time + st + utcoffset
	set = time + ls + utcoffset
	rised = rise.to_datetime()
	setd = set.to_datetime()
	print(rise.to_datetime())
	print(set.to_datetime())
	return rised, setd
