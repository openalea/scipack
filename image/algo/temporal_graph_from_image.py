# -*- python -*-
#
#       Copyright 2015 INRIA - CIRAD - INRA - ENS
#
#       File author(s): Jonathan Legrand <jonathan.legrand@ens-lyon.fr>
#
################################################################################
"""This file is provided in 'openalea-component' to ensure import compatibility as used in older version of vplants.container (SVN)"""

DeprecationWarning("This is an outdated file to create TemporalPropertyGraph objects from segmented images and lineages.")
DeprecationWarning("Please use 'vplants.tissue_analysis.temporal_graph_from_image' from 'marsalt' git repository instead!")
from vplants.tissue_analysis.temporal_graph_from_image import *
