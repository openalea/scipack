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


__doc__ = """ OpenAlea.Data Structure."""
__license__ = "Cecill-C"
__revision__ = " $Id$ "

from openalea.core import Factory as Fa
from openalea.core import (Alias,
                           IBool, IDateTime, IDict, IDirStr, IFileStr,
                           IFloat, IInt, IRGBColor, ISequence, IStr, ITextStr)
from openalea.core.pkgdict import protected

__name__ = "openalea.data structure"
__alias__ = ['catalog.data', 'openalea.data']

__version__ = '0.0.2'
__license__ = "Cecill-C"
__authors__ = 'OpenAlea Consortium'
__institutes__ = 'INRIA/CIRAD'
__description__ = 'Nodes for standard data structure creation, edition and visualisation.'
__url__ = 'http://openalea.gforge.inria.fr'

__all__ = []

var_ = Fa(uid="29278da24e7111e6bff6d4bed973e64a",
          name="variable",
          description="Variable",
          category="datatype",
          nodemodule="openalea.data.data",
          nodeclass="Variable",

          inputs=(dict(name='Caption', interface=IStr, value='Variable'),
                  dict(name='Object', interface=None, value=None),
                  ),
          outputs=(dict(name='Object', interface=None),)
          )

__all__.append('var_')

str_ = Fa(uid="2ec3b2a44e7111e6bff6d4bed973e64a",
          name=protected("string"),
          description="String",
          category="datatype",
          nodemodule="openalea.data.data",
          nodeclass="String",

          inputs=(dict(name="String", interface=IStr, value=''),),
          outputs=(dict(name="String", interface=IStr),),
          )

__all__.append('str_')

text = Fa(uid="33ab90204e7111e6bff6d4bed973e64a",
          name=protected("text"),
          description="Text",
          category="datatype",
          nodemodule="openalea.data.data",
          nodeclass="Text",

          inputs=(dict(name="Text", interface=ITextStr, value=''),),
          outputs=(dict(name="Text", interface=ITextStr),),
          )

__all__.append('text')

datetime_ = Fa(uid="389e52e84e7111e6bff6d4bed973e64a",
               name="datetime",
               description="DateTime",
               category="datatype",
               nodemodule="openalea.data.data",
               nodeclass="DateTime",

               inputs=(dict(name="DateTime", interface=IDateTime),),
               outputs=(dict(name="DateTime", interface=IDateTime),),
               )

__all__.append('datetime_')

bool_ = Fa(uid="3ddafad64e7111e6bff6d4bed973e64a",
           name="bool",
           description="boolean",
           category="datatype",
           nodemodule="openalea.data.data",
           nodeclass="Bool",

           inputs=(dict(name="Bool", interface=IBool, value=False),),
           outputs=(dict(name="Bool", interface=IBool),),
           )

__all__.append('bool_')

float_ = Fa(uid="427a6d884e7111e6bff6d4bed973e64a",
            name="float",
            description="Float Value",
            category="datatype",
            nodemodule="openalea.data.data",
            nodeclass="Float",

            inputs=(dict(name="Float", interface=IFloat, value=0.0),),
            outputs=(dict(name="Float", interface=IFloat),),
            )

__all__.append('float_')

floatscy = Fa(uid="484f63d04e7111e6bff6d4bed973e64a",
              name="float scy",
              description="Float Value",
              category="datatype",
              nodemodule="openalea.data.data",
              nodeclass="FloatScy",

              inputs=(dict(name="str", interface=IStr, value="0.0"),),
              outputs=(dict(name="Float", interface=IFloat),),
              )

__all__.append('floatscy')

int_ = Fa(uid="4d7cbd3a4e7111e6bff6d4bed973e64a",
          name="int",
          description="Int Value",
          category="datatype",
          nodemodule="openalea.data.data",
          nodeclass="Int",

          inputs=(dict(name="in", interface=IInt, value=0),),
          outputs=(dict(name="out", interface=IInt),),
          )

__all__.append('int_')

rgb_ = Fa(uid="5276d67c4e7111e6bff6d4bed973e64a",
          name=protected("rgb"),
          description="RGB tuple",
          category="Color,datatype",
          nodemodule="openalea.data.data",
          nodeclass="RGB",

          inputs=(dict(name="RGB", interface=IRGBColor, value=(0, 0, 0),
                       desc='3 uples RGB color'),),
          outputs=(
              dict(name="RGB", interface=ISequence, desc='3 uples RGB color'),),
          )

__all__.append('rgb_')
Alias(rgb_, 'rgb')

list_ = Fa(uid="5782a8264e7111e6bff6d4bed973e64a",
           name=protected("list"),
           description="Python list",
           category="datatype",
           nodemodule="openalea.data.data",
           nodeclass="List",

           inputs=(dict(name="List", interface=ISequence),),
           outputs=(dict(name="List", interface=ISequence),),
           )

__all__.append('list_')

dict_ = Fa(uid="5c38fd164e7111e6bff6d4bed973e64a",
           name=protected("dict"),
           description="Python dictionary",
           category="datatype",
           nodemodule="openalea.data.data",
           nodeclass="Dict",

           inputs=(dict(name="Dict", interface=IDict),),
           outputs=(dict(name="Dict", interface=IDict),),
           )

__all__.append('dict_')

pair = Fa(uid="60a0e9544e7111e6bff6d4bed973e64a",
          name=protected("pair"),
          description="Python 2-uples",
          category="datatype",
          nodemodule="openalea.data.data",
          nodeclass="Pair",
          inputs=(dict(name="IN0", interface=None, ),
                  dict(name="IN1", interface=None, ),),
          outputs=(dict(name="OUT", interface=ISequence),),
          )

__all__.append('pair')

tuple3 = Fa(uid="65bb65c24e7111e6bff6d4bed973e64a",
            name=protected("tuple3"),
            description="Python 3-uples",
            category="datatype",
            nodemodule="openalea.data.data",
            nodeclass="Tuple3",
            inputs=(dict(name="IN0", interface=None, ),
                    dict(name="IN1", interface=None, ),
                    dict(name="IN2", interface=None, ),
                    ),
            outputs=(dict(name="OUT", interface=ISequence),),
            )

__all__.append('tuple3')

# DEPRECATED
fname = Fa(uid="6ba94f764e7111e6bff6d4bed973e64a",
           name=protected("filename"),
           description="File name",
           category="datatype",
           nodemodule="openalea.data.data",
           nodeclass="FileName",

           inputs=(dict(name='FileStr', interface=IFileStr, value=''),
                   dict(name='cwd', interface=IDirStr, value='', hide=True),),
           outputs=(dict(name='FileStr', interface=IFileStr),)
           )

__all__.append('fname')

dname = Fa(uid="715c11104e7111e6bff6d4bed973e64a",
           name=protected("dirname"),
           description="Directory name",
           category="datatype",
           nodemodule="openalea.data.data",
           nodeclass="DirName",

           inputs=(dict(name='DirStr', interface=IDirStr, value=''),
                   dict(name='cwd', interface=IDirStr, value='', hide=True)),
           outputs=(dict(name='DirStr', interface=IDirStr),)
           )

__all__.append('dname')

pdir = Fa(uid="76aa0e064e7111e6bff6d4bed973e64a",
          name=protected("packagedir"),
          description="Package Directory",
          category="datatype",
          nodemodule="openalea.data.data",
          nodeclass="PackageDir",

          inputs=(dict(name='PackageStr', interface=IStr, value=''),),
          outputs=(dict(name='DirStr', interface=IDirStr),)
          )

__all__.append('pdir')

none_ = Fa(uid="7b3bc4fa4e7111e6bff6d4bed973e64a",
           name="None",
           description="None object",
           category="datatype",
           nodemodule="openalea.data.data",
           nodeclass="none",

           outputs=(dict(name="None"),),
           )

__all__.append('none_')
