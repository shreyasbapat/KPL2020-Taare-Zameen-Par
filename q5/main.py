# all imports below

"""
Any extra lines of code (if required)
as helper for this function.
"""

class ScraperXRT:
    '''
    Description
    -----------
    A class to scrap XRT files from the telescope archive.
    '''

    def __init__(self, typeof_file, startime, endtime):
    '''
    Parameters
	----------
	typeof_file: A `string`
    startime: A `~datetime.datetime` instance
    endtime: A `~datetime.datetime` instance
	'''

    def query(self):
	'''
	Returns
	-------
	A `list` of strings of URLs.
	'''
	return NotImplementedError

    def get(self):
	'''
	Returns
	-------
	A `list` of strings for files.
	'''
	return NotImplementedError

    def view(self, filepath):
	'''
    Parameters
	----------
    filepath: A `string` representing absolute path of file in system.

	Returns
	-------
	An instance of `matplotlib.image.AxesImage`, returned using `plt.imshow(data)`.
	'''
	return NotImplementedError
