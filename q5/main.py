# all imports below

import requests
from bs4 import BeautifulSoup
import numpy as np
import datetime
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename

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

        self.urls = []
        self.downloads = []
        self.tof = typeof_file
        self.st = startime
        self.et = endtime

    def query(self):

        '''
        Returns
        -------
        A `list` of strings of URLs.
        '''

        r = requests.get('http://solar.physics.montana.edu/HINODE/XRT/QL/syn_comp_fits/')
        soup = BeautifulSoup(r.content , 'html5lib')
        q = 'XRT_' + self.tof + '_' + self.st + '_' + self.et
        for i in soup.findAll('a'):
            name = i.get('href')
            if q in name:
                self.urls.append('http://solar.physics.montana.edu/HINODE/XRT/QL/syn_comp_fits/' + name)
        return self.urls

    def get(self):

        '''
        Returns
        -------
        A `list` of strings for files.
        '''

        for i in self.urls:
            r1 = requests.get(i)
            filename = i[61:]
            with open(filename , 'wb') as f:
                f.write(r1.content)
                self.downloads.append(filename)
        return self.downloads

    def view(self, filepath):

        '''
        Parameters
        ----------
        filepath: A `string` representing absolute path of file in system.

        Returns
        -------
        An instance of `matplotlib.image.AxesImage`, returned using `plt.imshow(data)`.
        '''

        image_file = get_pkg_data_filename(filepath)
        image_data = fits.getdata(image_file)
        plt.imshow(image_data, cmap='gray')
        plt.colorbar()
        plt.show()

example = ScraperXRT("Ti_poly" , "20150426" , "214354")
urls = example.query()
downloads = example.get()
example.view(downloads[0])
