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

startobs = datetime(2000, 1, 1, 0, 0, 0) #replace it by the time when Saturn will be just visible
endobs = datetime(2020, 1, 1) #replace it by the time when Saturn is no longer visible from SAC terrace



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

def stentime():
	gravity = EarthLocation(lat=31.78135*u.deg, lon=76.99313*u.deg, height=1000*u.m)
	time = Time(datetime(2020, 6, 8, 20, 18, 37, 274634))
	delta = np.linspace(0, 12, 1440)*u.hour
	utcoffset = 5.5*u.hour
	time = time - utcoffset
	saturn = get_body('Saturn', time=time, location=gravity)
	frame = AltAz(obstime=time+delta,location=gravity)
	range = saturn.transform_to(frame)
	alts = range.alt.value
	rise = 0
	set = 0
	for i in range(1440):
		if(alst[i] > 20):

	# plt.plot(delta, range.alt.value)
	# plt.xlim(0, 12)
	# plt.xlabel('Hours from 8 PM IST')
	# plt.ylabel('Alt')
	# plt.show()
