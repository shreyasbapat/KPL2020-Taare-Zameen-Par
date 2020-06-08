# all imports below

import requests
from bs4 import BeautifulSoup
import numpy as np
from datetime import datetime
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
        q = 'XRT_' + self.tof
        for i in soup.findAll('a'):
            name = i.get('href')
            if q in name:
                d = name.split('_')
                sta = d[3]
                end = d[4]
                time = datetime(int(sta[:4]),int(sta[4:6]) ,int(sta[6:8]) , int(end[:2]), int(end[2:4]), int(end[4:6]), 0)
                if time >= self.st and time <= self.et:
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

# start = datetime(2013,7 , 9, 0, 1, 39, 642080)
# end = datetime(2016,7 , 9, 0, 1, 39, 642080)
# example = ScraperXRT("Al_mesh" , start , end)
# urls = example.query()
# print(urls)
# downloads = example.get()
# example.view(downloads[0])
# print(downloads)
