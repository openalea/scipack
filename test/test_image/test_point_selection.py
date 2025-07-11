#
#       image: image GUI
#
#       Copyright 2006 INRIA - CIRAD - INRA
#
#       File author(s): Eric Moscardi <eric.moscardi@sophia.inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
"""
Test point selection
"""

__license__= "Cecill-C"
__revision__ = " $Id: $ "

from qtpy import QtWidgets
from openalea.image.all import point_selection, SpatialImage
from scipy.ndimage import rotate
import numpy as np

def square(shape=(100,100), voxels=(1,1), dimensions=(10,10), center=(49,49)):
    """
    Generating a 2-D square
    :Parameters:
    - `shape` (tuple) - image shape (xdim,ydim)
    - `voxels` (tuple) - voxels size (vx,vy)
    - `dimensions` (tuple) - dimensions of square (w,h)
    - `center` (tuple) - coordinates of center (cx,cy)
    :Returns: 2-D square into a inrimage
    """

    xdim, ydim = shape
    zdim = 1.
    vx,vy = voxels
    w,h = dimensions
    cx,cy = center

    data = np.zeros([xdim, ydim, zdim],np.uint8)

    for i in range(xdim):
        for j in range(ydim):
            if abs(i * vx - cx) < w and abs(j * vy - cy) < h :
                data[i,j] = 255 * i*j

    out = SpatialImage(data,(vx,vy,1))
    return out

qapp = QtWidgets.QApplication.instance()
if qapp:
    im1 = square()
    im2 = rotate(im1, 30)
    im2 = SpatialImage(im2,im1.resolution)

    w1 = point_selection (im1)
    w2 = point_selection (im2)
