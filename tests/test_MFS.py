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
from imfractal import *

import time

def do_test():
    path = '/almacen/members.imaglabs.org/felix.thomsen/Rodrigo/BioAsset/mats/'
    filename = path + 'BA01_120_1Slices.mat'
    file_mask = path + 'BA01_120_1Mask.mat'
    i = MFS_3D()
    i.setDef(1, 20, 3, filename, file_mask)
    print "Calculating 3D MFS Multifractal Spectrum (Holder)..."
    t = time.clock()
    fds3 = i.getFDs()
    t = time.clock() - t
    print "Time 3D MFS: ", t
    print fds3


    filename = 'images/baguette2.tif'#fractal20Bread.png'
    i = MFS()
    i.setDef(1,20,3,True)
    print "Calculating MFS Multifractal Spectrum..."
    t =  time.clock()
    fds3 = i.getFDs(filename)
    t =  time.clock()-t
    print "Time MFS: ", t
    print fds3

    i = Singularity(20)

    print "Calculating Singularity Multifractal Spectrum..."
    t =  time.clock()
    fds = i.getFDs(filename)
    t =  time.clock()-t
    print "Time Singularity: ", t
    print fds

    i = Sandbox(14)
    i.setDef(40,1.15)

    print "Calculating Sandbox Multifractal Spectrum..."
    t =  time.clock()
    fds2 = i.getFDs(filename)
    t =  time.clock()-t
    print "Time Sandbox: ", t
    print fds2

    i = MFS()
    i.setDef(1,20,3,True)

    print "Calculating MFS Multifractal Spectrum..."
    t =  time.clock()
    fds3 = i.getFDs(filename)
    t =  time.clock()-t
    print "Time MFS: ", t
    print fds3
