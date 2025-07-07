# -*- python -*-
#
#       OpenAlea.StdLib
#
#       Copyright 2006-2023 INRIA - CIRAD - INRA  
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
################################################################################
""" Standard python functions for functional programming. """

__license__ =  "Cecill-C"
__revision__ = " $Id: parallel.py 2245 2010-02-08 17:11:34Z cokelaer $ "

from openalea.core import Node, ITextStr

import ipyparallel as ipp

def pmap(func, seq):
    """ map(func, seq) """
    
    if func and seq:
        cluster = ipp.Cluster(n=4)
        cluster.start_cluster_sync()
        rc = cluster.connect_client_sync()
        dview = rc[:]
        return ( dview.map_sync(func, seq), )
    else:
        return ( [], )


