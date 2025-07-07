# -*- python -*-
#
#       OpenAlea.image
#
#       Copyright 2012 INRIA - CIRAD - INRA
#
#       File author(s):  Jonathan Legrand <jonathan.legrand@ens-lyon.fr>
#                        Frederic Boudon <frederic.boudon@cirad.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite: http://openalea.gforge.inria.fr
#
################################################################################
"""Test creation of PropertyGraph from SpatialImages"""
import numpy as np

from openalea.image.serial.basics import imread
#from vplants.tissue_analysis.spatial_image_analysis import SpatialImageAnalysis
from openalea.image.algo.graph_from_image import graph_from_image
#from openalea.plantgl.gui import Viewer

def test_graph_from_image(visual = False):
    im =  imread("segmentation.inr.gz")
    graph = graph_from_image(im)


if __name__ == '__main__':
    #test_graph_from_simple_image()
    test_graph_from_image()
