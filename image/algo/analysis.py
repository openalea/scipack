# -*- python -*-
#
#       Copyright 2015 INRIA - CIRAD - INRA - ENS
#
#       File author(s): Jonathan Legrand <jonathan.legrand@ens-lyon.fr>
#
################################################################################
"""This file is provided in 'openalea-component' to ensure import compatibility as used in older version of vplants.container (SVN)"""

DeprecationWarning("This is an outdated file to use SpatialImageAnalysis objects")
DeprecationWarning("Please use 'vplants.tissue_analysis.spatial_image_analysis' from 'marsalt' git repository instead!")
from vplants.tissue_analysis.spatial_image_analysis import *
