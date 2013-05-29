"""
Copyright (c) 2013 Rodrigo Baravalle
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
3. The name of the author may not be used to endorse or promote products
derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


from Algorithm import *
from random import randrange,randint
from math import log
from scipy import ndimage
#from pylab import plot, title, show , legend
#import matplotlib
#from matplotlib import pyplot as plt
import Image
import numpy as np
import sys
import os

class Boxdimension (Algorithm):
     """
    :Box dimension
    :version: 1.0
    :author: Rodrigo Baravalle
    """

    def __init__(self):
        pass

    # returns the sum of (summed area) image pixels in the box between
    # (x1,y1) and (x2,y2)
    def mww(self,x1,y1,x2,y2,intImg):
        sum = intImg[x2][y2]
        if (x1>= 1 and y1 >= 1):
            sum = sum + intImg[x1-1][y1-1]
        if (x1 >= 1):
            sum = sum - intImg[x1-1][y2];
        if (y1 >= 1):
            sum = sum - intImg[x2][y1-1]
        return sum/((x2-x1+1)*(y2-y1+1));

    # constructs summed area table
    # img: original image
    # Nx: img size(x)
    # Ny: img size(y)
    # which: type of img: 
    #   'img': Image
    #   else:  array
    def sat(self,img,Nx,Ny,which):
        # summed area table, useful for speed up the computation by adding image pixels 
        intImg = [ [ 0 for i in range(Nx) ] for j in range(Ny) ]
        if(which == 'img'):
            intImg[0][0] = img.getpixel((0,0))
            
            arrNx = range(1,Nx)
            arrNy = range(1,Ny)
            for h in arrNx:
                intImg[h][0] = intImg[h-1][0] + img.getpixel((h,0))
            
            for w in arrNy:
                intImg[0][w] = intImg[0][w-1] + img.getpixel((0,w))
            
            for f in arrNx:
                for g in arrNy:
                   intImg[f][g] = img.getpixel((f,g))+intImg[f-1][g]+intImg[f][g-1]-intImg[f-1][g-1]
        else:
            intImg[0][0] = img[0][0]
            
            arrNx = range(1,Nx)
            arrNy = range(1,Ny)
            for h in arrNx:
                intImg[h][0] = intImg[h-1][0] + img[h][0]
            
            for w in arrNy:
                intImg[0][w] = intImg[0][w-1] + img[0][w]
            
            for f in arrNx:
                for g in arrNy:
                   intImg[f][g] = img[f][g]+intImg[f-1][g]+intImg[f][g-1]-intImg[f-1][g-1]

        return intImg

    # white's algorithm
    # local threshold schema
    def white(self,img,Nx,Ny):
               
        im = np.zeros((Nx,Ny))
        
        intImg = self.sat(img,Nx,Ny,'img')
            
        arrNx = range(Nx)
        arrNy = range(Ny)

        vent = int(self.v)
        for i in arrNx:
            for j in arrNy:
                if(self.mww(max(0,i-vent),max(0,j-vent),min(Nx-1,i+vent),min(Ny-1,j+vent),intImg) >= img.getpixel((i,j))*self.b ): 
                    im[j,i] = img.getpixel((i,j))

        # do an opening operation to remove small elements
        return ndimage.binary_opening(im, structure=np.ones((2,2))).astype(np.int)


    def getFDs(self,filename):
        #tP = (self.P)   # tP : two raised to P
        #x = tP+1
        #y = tP+1
        #cantSelected = 0

        a = Image.open(filename)
        Nx, Ny = a.size
        L = Nx*Ny

        points = []     # number of elements in the structure
        gray = a.convert('L') # rgb 2 gray

        gray = self.white(gray,Nx,Ny) # local thresholding algorithm

        return []
