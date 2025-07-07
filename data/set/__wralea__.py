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
from openalea.core import ISequence

__name__ = "openalea.data structure.set"

__version__ = '0.0.1'
__license__ = "Cecill-C"
__authors__ = 'OpenAlea Consortium'
__institutes__ = 'INRIA/CIRAD'
__description__ = 'Nodes for standard data structure creation, edition and visualisation.'
__url__ = 'http://openalea.gforge.inria.fr'

__all__ = []

set_ = Fa(uid="47489b7e4e7011e6bff6d4bed973e64a",
          name="set",
          description="Python set",
          category="datatype",
          nodemodule="openalea.data.set.sets",
          nodeclass="py_set",
          inputs=(dict(name="sequence", interface=ISequence, ),),
          outputs=(dict(name="set", interface=ISequence),),
          )

__all__.append('set_')

clear_ = Fa(uid="4d3434624e7011e6bff6d4bed973e64a",
            name="clear",
            description="Remove all elements from a set.",
            category="datatype",
            nodemodule="openalea.data.set.sets",
            nodeclass="py_clear",
            inputs=(dict(name="set", interface=ISequence, ),),
            outputs=(dict(name="set", interface=ISequence),),
            )

__all__.append('clear_')

add_ = Fa(uid="555a10f84e7011e6bff6d4bed973e64a",
          name="add",
          description="Add an element to a set.",
          category="datatype",
          nodemodule="openalea.data.set.sets",
          nodeclass="py_add",
          inputs=(dict(name="set", interface=ISequence),
                  dict(name="obj", interface=None)),
          outputs=(dict(name="set", interface=ISequence),),
          )

__all__.append('add_')

diff_ = Fa(uid="5afd88324e7011e6bff6d4bed973e64a",
           name="difference",
           description=" Return the difference of two sets as a new sets.",
           category=" datatype",
           nodemodule="openalea.data.set.sets",
           nodeclass="py_difference",
           inputs=(dict(name="set1", interface=ISequence),
                   dict(name="set2", interface=ISequence)),
           outputs=(dict(name="set", interface=ISequence),),
           )

__all__.append('diff_')

intersect_ = Fa(uid="60f66aa64e7011e6bff6d4bed973e64a",
                name="intersection",
                description=" Return the intersection of two sets as a new sets.",
                category="datatype",
                nodemodule="openalea.data.set.sets",
                nodeclass="py_intersection",
                inputs=(dict(name="set1", interface=ISequence),
                        dict(name="set2", interface=ISequence)),
                outputs=(dict(name="set", interface=ISequence),),
                )

__all__.append('intersect_')

issubset_ = Fa(uid="6521474a4e7011e6bff6d4bed973e64a",
               name="issubset",
               description=" Report whether another set contains this set. ",
               category="datatype",
               nodemodule="openalea.data.set.sets",
               nodeclass="py_issubset",
               inputs=(dict(name="set1", interface=ISequence),
                       dict(name="set2", interface=ISequence)),
               outputs=(dict(name="set", interface=ISequence),),
               )

__all__.append('issubset_')

issuperset_ = Fa(uid="6ba263b04e7011e6bff6d4bed973e64a",
                 name="issuperset",
                 description=" Report whether a set contains another set. ",
                 category="datatype",
                 nodemodule="openalea.data.set.sets",
                 nodeclass="py_issuperset",
                 inputs=(dict(name="set1", interface=ISequence),
                         dict(name="set2", interface=ISequence)),
                 outputs=(dict(name="set", interface=ISequence),),
                 )

__all__.append('issuperset_')

sym_ = Fa(uid="7300615c4e7011e6bff6d4bed973e64a",
          name="symmetric_difference",
          description="Return the symmetric difference of two sets as a new set. ",
          category="datatype",
          nodemodule="openalea.data.set.sets",
          nodeclass="py_symmetric_difference",
          inputs=(dict(name="set1", interface=ISequence),
                  dict(name="set2", interface=ISequence)),
          outputs=(dict(name="set", interface=ISequence),),
          )

__all__.append('sym_')

union_ = Fa(uid="793f7d324e7011e6bff6d4bed973e64a",
            name="union",
            description="Return the union of two sets as a new set.",
            category="datatype",
            nodemodule="openalea.data.set.sets",
            nodeclass="py_union",
            inputs=(dict(name="set1", interface=ISequence),
                    dict(name="set2", interface=ISequence)),
            outputs=(dict(name="set", interface=ISequence),),
            )

__all__.append('union_')

update_ = Fa(uid="8082057e4e7011e6bff6d4bed973e64a",
             name="update",
             description="Update a set with the union of set1 and set2..",
             category="datatype",
             nodemodule="openalea.data.set.sets",
             nodeclass="py_update",
             inputs=(dict(name="set1", interface=ISequence),
                     dict(name="set2", interface=ISequence)),
             outputs=(dict(name="set", interface=ISequence),),
             )

__all__.append('update_')
