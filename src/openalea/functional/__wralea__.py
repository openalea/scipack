# -*- python -*-
#
#       OpenAlea.StdLib
#
#       Copyright 2006-2009 INRIA - CIRAD - INRA  
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
################################################################################

__doc__ = """ openalea.function operator """
__revision__ = " $Id$ "

from openalea.core import Factory as Fa
from openalea.core import IBool, IFunction, ISequence, IStr

__name__ = "openalea.function operator"

__alias__ = ["catalog.functional", "openalea.functional"]

__version__ = '0.0.2'
__license__ = 'CECILL-C'
__authors__ = 'OpenAlea Consortium'
__institutes__ = 'INRIA/CIRAD'
__description__ = 'Functional Node library.'
__url__ = 'http://openalea.gforge.inria.fr'

__all__ = ['map_', 'filter_', 'reduce_', 'apply_', 'func', 'ifelse_']

map_ = Fa(uid="d68a1fc64e7311e6bff6d4bed973e64a",
          name="map",
          description="Apply a function on a sequence",
          category="Functional",
          inputs=(dict(name='func', interface=IFunction),
                  dict(name='seq', interface=ISequence),),
          outputs=(dict(name="out", interface=ISequence),),
          nodemodule="openalea.functional.functional",
          nodeclass="pymap",
          )

filter_ = Fa(uid="dbaf9b984e7311e6bff6d4bed973e64a",
             name="filter",
             description=("Apply a function on a sequence and return only"
                          " true values"),
             category="Functional",
             inputs=(dict(name='func', interface=IFunction),
                     dict(name='seq', interface=ISequence)),
             outputs=(dict(name="out", interface=ISequence),),
             nodemodule="openalea.functional.functional",
             nodeclass="pyfilter",
             )

reduce_ = Fa(uid="e0a91ff24e7311e6bff6d4bed973e64a",
             name="reduce",
             description=("Apply a function of two arguments cumulatively"
                          " to the items of a sequence"),
             category="Functional",
             inputs=(dict(name='func', interface=IFunction),
                     dict(name='seq', interface=ISequence)),
             outputs=(dict(name="out", interface=None),),
             nodemodule="openalea.functional.functional",
             nodeclass="pyreduce",
             )

apply_ = Fa(uid="e4f61f384e7311e6bff6d4bed973e64a",
            name="apply",
            description="Apply a function with arguments",
            category="Functional",
            inputs=(dict(name='func', interface=IFunction),
                    dict(name='seq', interface=ISequence),
                    dict(name='one argument', interface=IBool,
                         value=False),),
            outputs=(dict(name="out", interface=None),),
            nodemodule="openalea.functional.functional",
            nodeclass="pyapply",
            )

func = Fa(uid="ea7332fc4e7311e6bff6d4bed973e64a",
          name="function",
          description="Creates a function from a python string",
          category="Functional",
          inputs=(dict(name="code", interface=IStr),),
          outputs=(dict(name="out", interface=IFunction),),
          nodemodule="openalea.functional.functional",
          nodeclass="pyfunction",
          )
ifelse_ = Fa(uid="eeb2d4e44e7311e6bff6d4bed973e64a",
             name="ifelse",
             description=("Execute two dataflow functions depending"
                          " on a condition"),
             category="Functional",
             inputs=(dict(name='value', ),
                     dict(name='condition', interface=IBool),
                     dict(name='function1', interface=IFunction),
                     dict(name='function2', interface=IFunction),
                     ),
             outputs=(dict(name="out", interface=None),),
             nodemodule="openalea.functional.functional",
             nodeclass="pyifelse",
             )
