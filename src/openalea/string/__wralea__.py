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

__doc__ = """ catalog.string """
__revision__ = " $Id$ "

from openalea.core import Factory as Fa
from openalea.core import ISequence, IStr, ITextStr

__name__ = "openalea.data structure.string"
__alias__ = []

__version__ = '0.0.1'
__license__ = 'CECILL-C'
__authors__ = 'OpenAlea Consortium'
__institutes__ = 'INRIA/CIRAD'
__description__ = 'String library'
__url__ = 'http://openalea.gforge.inria.fr'

__all__ = ['split', 'join', 'strip']

split = Fa(uid="335b1dc24e7911e6bff6d4bed973e64a",
           name="split",
           description="split a string",
           category="String,Python",
           nodemodule="openalea.string.strings",
           nodeclass="str_split",

           inputs=(dict(name="String", interface=IStr, value=''),
                   dict(name="Split Char", interface=IStr, value='\n'),
                   ),
           outputs=(dict(name="List", interface=ISequence),),
           )

strip = Fa(uid="335b1dc34e7911e6bff6d4bed973e64a",
           name="strip",
           description=("Return a copy of the string s with leading and "
                        "trailing whitespace removed."),
           category="String,Python",
           nodemodule="openalea.string.strings",
           nodeclass="str_strip",

           inputs=(dict(name="string", interface=IStr, value=''),
                   dict(name="chars", interface=IStr, value=' '),
                   ),
           outputs=(dict(name="ostring", interface=IStr),),
           )

join = Fa(uid="335b1dc44e7911e6bff6d4bed973e64a",
          name="join",
          description="Join a list of string",
          category="String,Python",
          nodemodule="openalea.string.strings",
          nodeclass="str_join",

          inputs=(dict(name="String List", interface=ISequence, value=[]),
                  dict(name="Join Char", interface=IStr, value='\n'),
                  ),
          outputs=(dict(name="List", interface=IStr),),
          )

str_ = Fa(uid="335b1dc54e7911e6bff6d4bed973e64a",
          name="string",
          description="String,Python",
          category="datatype",
          nodemodule="openalea.string.strings",
          nodeclass="String",

          inputs=(dict(name="String", interface=IStr, value=''),),
          outputs=(dict(name="String", interface=IStr),),
          )

__all__.append('str_')

text = Fa(uid="335b1dc64e7911e6bff6d4bed973e64a",
          name="text",
          description="Text",
          category="Python",
          nodemodule="openalea.string.strings",
          nodeclass="text",

          inputs=(dict(name="Text", interface=ITextStr, value=''),),
          outputs=(dict(name="Text", interface=ITextStr),),
          )

__all__.append('text')
