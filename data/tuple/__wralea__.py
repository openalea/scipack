# -*- python -*-
#
#       OpenAlea.StdLib
#
#       Copyright 2006 - 2008 INRIA - CIRAD - INRA  
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
################################################################################


__doc__ = """ OpenAlea dictionary data structure"""
__license__ = "Cecill-C"
__revision__ = " $Id$ "

from openalea.core import Factory as Fa
from openalea.core import ISequence, ITuple

__name__ = "openalea.data structure.tuple"
__alias__ = []

__version__ = '0.0.1'
__license__ = "Cecill-C"
__authors__ = 'OpenAlea Consortium'
__institutes__ = 'INRIA/CIRAD'
__description__ = 'Nodes for standard data structure creation, edition and visualisation.'
__url__ = 'http://openalea.gforge.inria.fr'

__all__ = []

pair = Fa(uid="c2c0d3164e7011e6bff6d4bed973e64a",
          name="pair",
          description="Python 2-uples",
          category="datatype",
          nodemodule="openalea.data.tuple.tuples",
          nodeclass="Pair",
          inputs=(dict(name="IN0", interface=None, ),
                  dict(name="IN1", interface=None, ),),
          outputs=(dict(name="OUT", interface=ISequence),),
          )

__all__.append('pair')

tuple3 = Fa(uid="be557a344e7011e6bff6d4bed973e64a",
            name="tuple3",
            description="Python 3-uples",
            category="datatype",
            nodemodule="openalea.data.tuple.tuples",
            nodeclass="Tuple3",
            inputs=(dict(name="IN0", interface=None, ),
                    dict(name="IN1", interface=None, ),
                    dict(name="IN2", interface=None, ),
                    ),
            outputs=(dict(name="OUT", interface=ISequence),),
            )

__all__.append('tuple3')

tuple_ = Fa(uid="b9665eb24e7011e6bff6d4bed973e64a",
            name="tuple",
            description="Python tuple",
            category="datatype",
            nodemodule="openalea.data.tuple.tuples",
            nodeclass="Tuple",
            inputs=(dict(name="tuple", interface=ITuple),),
            outputs=(dict(name="tuple", interface=ITuple),),
            )

__all__.append('tuple_')
