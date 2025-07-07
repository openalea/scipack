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


__doc__ = """catalog.math """

__license__ = "Cecill-C"
__revision__ = " $Id$ "

from openalea.core import Factory as Fa
from openalea.core import IBool, IFloat, IInt, ISequence
import math

__name__ = "openalea.math"
__alias__ = ["catalog.math"]

__version__ = '0.0.1'
__license__ = 'CECILL-C'
__authors__ = 'OpenAlea Consortium'
__institutes__ = 'INRIA/CIRAD'
__description__ = 'Mathematical Node library.'
__url__ = 'http://openalea.gforge.inria.fr'

__all__ = []

equal = Fa(uid="4ae10e204e7411e6bff6d4bed973e64a",
           name="==",
           description="Equality test",
           category="Math",
           inputs=(dict(name="a", interface=IInt, value=0),
                   dict(name="b", interface=IInt, value=0),),
           outputs=(dict(name="out", interface=IBool),),
           nodemodule="operator",
           nodeclass="eq",
           )

__all__.append('equal')

diff = Fa(uid="509416d24e7411e6bff6d4bed973e64a",
          name="!=",
          description="Equality test",
          category="Math",
          inputs=(dict(name="a", interface=IInt, value=0),
                  dict(name="b", interface=IInt, value=0),),
          outputs=(dict(name="out", interface=IBool),),
          nodemodule="operator",
          nodeclass="ne",
          )
__all__.append('diff')

sup = Fa(uid="58621c924e7411e6bff6d4bed973e64a",
         name=">",
         description="Greater than test",
         category="Math",
         inputs=(dict(name="a", interface=IInt, value=0),
                 dict(name="b", interface=IInt, value=0),),
         outputs=(dict(name="out", interface=IBool),),
         nodemodule="operator",
         nodeclass="gt",
         )

__all__.append('sup')

supeq = Fa(uid="60750c324e7411e6bff6d4bed973e64a",
           name=">=",
           description="greater or Equal test",
           category="Math",
           inputs=(dict(name="a", interface=IInt, value=0),
                   dict(name="b", interface=IInt, value=0),),
           outputs=(dict(name="out", interface=IBool),),
           nodemodule="operator",
           nodeclass="ge",
           )

__all__.append('supeq')

inf = Fa(uid="6484fb2a4e7411e6bff6d4bed973e64a",
         name="<",
         description="Lesser than test",
         category="Math",
         inputs=(dict(name="a", interface=IInt, value=0),
                 dict(name="b", interface=IInt, value=0),),
         outputs=(dict(name="out", interface=IBool),),
         nodemodule="operator",
         nodeclass="lt",
         )

__all__.append('inf')

infeq = Fa(uid="6b4bfc564e7411e6bff6d4bed973e64a",
           name="<=",
           description="Less or Equal test",
           category="Math",
           inputs=(dict(name="a", interface=IInt, value=0),
                   dict(name="b", interface=IInt, value=0),),
           outputs=(dict(name="out", interface=IBool),),
           nodemodule="operator",
           nodeclass="le",
           )

__all__.append('infeq')

and_ = Fa(uid="6faa124c4e7411e6bff6d4bed973e64a",
          name="and",
          description="Boolean And",
          category="Math",
          inputs=(dict(name="a", interface=IBool, value=True),
                  dict(name="b", interface=IBool, value=True),),
          outputs=(dict(name="out", interface=IBool),),
          nodemodule="operator",
          nodeclass="and_",
          )

__all__.append('and_')

or_ = Fa(uid="73f252884e7411e6bff6d4bed973e64a",
         name="or",
         description="Boolean Or",
         category="Math",
         inputs=(dict(name="a", interface=IBool, value=True),
                 dict(name="b", interface=IBool, value=True),),
         outputs=(dict(name="out", interface=IBool),),
         nodemodule="operator",
         nodeclass="or_",
         )

__all__.append('or_')

xor_ = Fa(uid="791e322c4e7411e6bff6d4bed973e64a",
          name="xor",
          description="Boolean XOR",
          category="Math",
          inputs=(dict(name="a", interface=IBool, value=True),
                  dict(name="b", interface=IBool, value=True),),
          outputs=(dict(name="out", interface=IBool),),
          nodemodule="operator",
          nodeclass="xor",
          )

__all__.append('xor_')

not_ = Fa(uid="7f19d96a4e7411e6bff6d4bed973e64a",
          name="not",
          description="Boolean Not",
          category="Math",
          inputs=(dict(name="a", interface=IBool, value=True),),
          outputs=(dict(name="out", interface=IBool),),
          nodemodule="operator",
          nodeclass="not_",
          )

__all__.append('not_')

plus = Fa(uid="8410ea8a4e7411e6bff6d4bed973e64a",
          name="+",
          description="Addition",
          category="Math",
          inputs=(dict(name="a", interface=IInt, value=0),
                  dict(name="b", interface=IInt, value=0),),
          outputs=(dict(name="out", interface=IInt),),
          nodemodule="operator",
          nodeclass="add",
          )

__all__.append('plus')

minus = Fa(uid="8925e0ac4e7411e6bff6d4bed973e64a",
           name="-",
           description="Soustraction",
           category="Math",
           inputs=(dict(name="a", interface=IInt, value=0),
                   dict(name="b", interface=IInt, value=0),),
           outputs=(dict(name="out", interface=IInt),),
           nodemodule="operator",
           nodeclass="sub",
           )

__all__.append('minus')

neg = Fa(uid="8ea948de4e7411e6bff6d4bed973e64a",
         name="neg",
         description="Negative",
         category="Math",
         inputs=(dict(name="a", interface=IInt, value=0),),
         outputs=(dict(name="out", interface=IInt),),
         nodemodule="operator",
         nodeclass="neg",
         )

__all__.append('neg')

times = Fa(uid="93dd0dcc4e7411e6bff6d4bed973e64a",
           name="*",
           description="Multiplication",
           category="Math",
           inputs=(dict(name="a", interface=IInt, value=0),
                   dict(name="b", interface=IInt, value=0),),
           outputs=(dict(name="out", interface=IInt),),
           nodemodule="operator",
           nodeclass="mul",
           )

__all__.append('times')

div = Fa(uid="9852b8e84e7411e6bff6d4bed973e64a",
         name="/",
         description="Division",
         category="Math",
         inputs=(dict(name="a", interface=IInt, value=0),
                 dict(name="b", interface=IInt, value=1),),
         outputs=(dict(name="out", interface=IInt),),
         nodemodule="operator",
         nodeclass="truediv",
         )

__all__.append('div')

mod = Fa(uid="9d5adb864e7411e6bff6d4bed973e64a",
         name="%",
         description="Modulo",
         category="Math",
         inputs=(dict(name="a", interface=IInt, value=0),
                 dict(name="b", interface=IInt, value=0),),
         outputs=(dict(name="out", interface=IInt),),
         nodemodule="operator",
         nodeclass="mod",
         )

__all__.append('mod')

abs_ = Fa(uid="a1915bee4e7411e6bff6d4bed973e64a",
          name="abs",
          description="Absolute value",
          category="Math",
          inputs=(dict(name="a", interface=IInt, value=0),),
          outputs=(dict(name="out", interface=IInt),),
          nodemodule="operator",
          nodeclass="abs",
          )

__all__.append('abs_')

cmp_ = Fa(uid="a5bf86504e7411e6bff6d4bed973e64a",
          name="cmp",
          description="Compare 2 objects",
          category="Math",
          inputs=(dict(name="a", interface=IInt, value=0),
                  dict(name="b", interface=IInt, value=0),),
          outputs=(dict(name="out", interface=IInt),),
          nodemodule="openalea.math.maths",
          nodeclass="py_cmp",
          )

__all__.append('cmp_')

pow_ = Fa(uid="aa0b16344e7411e6bff6d4bed973e64a",
          name="**",
          description="Power",
          category="Math",
          inputs=(dict(name="a", interface=IInt, value=1),
                  dict(name="b", interface=IInt, value=1),),
          outputs=(dict(name="out", interface=IInt),),
          nodemodule="operator",
          nodeclass="pow",
          )
__all__.append('pow_')

# Trigonometry
cos = Fa(uid="aedb1fa64e7411e6bff6d4bed973e64a",
         name="cos",
         description="Cosinus",
         category="Math",
         inputs=(dict(name="a", interface=IFloat, value=0.),),
         outputs=(dict(name="out", interface=IFloat),),
         nodemodule="math",
         nodeclass="cos",
         )

__all__.append('cos')

sin = Fa(uid="b43079604e7411e6bff6d4bed973e64a",
         name="sin",
         description="Sinus",
         category="Math",
         inputs=(dict(name="a", interface=IFloat, value=0.),),
         outputs=(dict(name="out", interface=IFloat),),
         nodemodule="math",
         nodeclass="sin",
         )

__all__.append('sin')

tan = Fa(uid="b85fa27c4e7411e6bff6d4bed973e64a",
         name="tan",
         description="Tangent",
         category="Math",
         inputs=(dict(name="a", interface=IFloat, value=0.),),
         outputs=(dict(name="out", interface=IFloat),),
         nodemodule="math",
         nodeclass="tan",
         )

__all__.append('tan')

acos = Fa(uid="bcf9a2ce4e7411e6bff6d4bed973e64a",
          name="acos",
          description="Arccosinus",
          category="Math",
          inputs=(dict(name="a", interface=IFloat, value=0.),),
          outputs=(dict(name="out", interface=IFloat),),
          nodemodule="math",
          nodeclass="acos",
          )

__all__.append('acos')

asin = Fa(uid="c1903f964e7411e6bff6d4bed973e64a",
          name="asin",
          description="Arcsinus",
          category="Math",
          inputs=(dict(name="a", interface=IFloat, value=0.),),
          outputs=(dict(name="out", interface=IFloat),),
          nodemodule="math",
          nodeclass="asin",
          )

__all__.append('asin')

atan = Fa(uid="c810fa184e7411e6bff6d4bed973e64a",
          name="atan",
          description="Arctangent",
          category="Math",
          inputs=(dict(name="a", interface=IFloat, value=0.),),
          outputs=(dict(name="out", interface=IFloat),),
          nodemodule="math",
          nodeclass="atan",
          )

__all__.append('atan')

radians = Fa(uid="ce7158d04e7411e6bff6d4bed973e64a",
             name="radians",
             description="Degrees to radians converter",
             category="Math",
             inputs=(dict(name="a", interface=IFloat, value=0.),),
             outputs=(dict(name="out", interface=IFloat),),
             nodemodule="math",
             nodeclass="radians",
             )

__all__.append('radians')

degrees = Fa(uid="d3098c464e7411e6bff6d4bed973e64a",
             name="degrees",
             description="Radians to degrees converter",
             category="Math",
             inputs=(dict(name="a", interface=IFloat, value=0.),),
             outputs=(dict(name="out", interface=IFloat),),
             nodemodule="math",
             nodeclass="degrees",
             )

__all__.append('degrees')

round_ = Fa(uid="d75b6d3c4e7411e6bff6d4bed973e64a",
            name="round",
            description="Round value",
            category="Math",
            inputs=(dict(name="a", interface=IFloat, value=0.),),
            outputs=(dict(name="out", interface=IFloat),),
            nodemodule="openalea.math.maths",
            nodeclass="py_round",
            )

__all__.append('round_')

floor = Fa(uid="dba4ccda4e7411e6bff6d4bed973e64a",
           name="floor",
           description="floor of x",
           category="Math",
           inputs=(dict(name="x", interface=IFloat, value=0.),),
           outputs=(dict(name="y", interface=IFloat),),
           nodemodule="math",
           nodeclass="floor",
           )

__all__.append('floor')

ceil = Fa(uid="e25c28e84e7411e6bff6d4bed973e64a",
          name="ceil",
          description="Ceil of x",
          category="Math",
          inputs=(dict(name="x", interface=IFloat, value=0.),),
          outputs=(dict(name="y", interface=IInt),),
          nodemodule="math",
          nodeclass="ceil",
          )

__all__.append('ceil')

sqrt = Fa(uid="e7ef6fea4e7411e6bff6d4bed973e64a",
          name="sqrt",
          description="Square root",
          category="Math",
          inputs=(dict(name="x", interface=IFloat, value=0.),),
          outputs=(dict(name="y", interface=IFloat),),
          nodemodule="math",
          nodeclass="sqrt",
          )

__all__.append('sqrt')

log10 = Fa(uid="ec7243ee4e7411e6bff6d4bed973e64a",
           name="log10",
           description="Base 10 logarithm",
           category="Math",
           inputs=(dict(name="x", interface=IFloat, value=0.),),
           outputs=(dict(name="y", interface=IFloat),),
           nodemodule="math",
           nodeclass="log10",
           )

__all__.append('log10')

log = Fa(uid="f0f94bc44e7411e6bff6d4bed973e64a",
         name="log",
         description="Logarithm",
         category="Math",
         inputs=(dict(name="a", interface=IFloat, value=0.),
                 dict(name="base", interface=IFloat, value=math.e),),
         outputs=(dict(name="y", interface=IFloat),),
         nodemodule="math",
         nodeclass="log",
         )

__all__.append('log')

exp = Fa(uid="f57bc9384e7411e6bff6d4bed973e64a",
         name="exp",
         description="Exponential",
         category="Math",
         inputs=(dict(name="x", interface=IFloat, value=0.),),
         outputs=(dict(name="y", interface=IFloat),),
         nodemodule="math",
         nodeclass="exp",
         )

__all__.append('exp')

min_ = Fa(uid="fa34939c4e7411e6bff6d4bed973e64a",
          name="min",
          description="Minimum of a sequence",
          category="Math",
          inputs=(dict(name="x", interface=ISequence, value=0.),),
          outputs=(dict(name="out", interface=IFloat),),
          nodemodule="openalea.math.maths",
          nodeclass="py_min",
          )

__all__.append('min_')

max_ = Fa(uid="fe3795ca4e7411e6bff6d4bed973e64a",
          name="max",
          description="Maximum of a sequence",
          category="Math",
          inputs=(dict(name="x", interface=ISequence, value=0.),),
          outputs=(dict(name="out", interface=IFloat),),
          nodemodule="openalea.math.maths",
          nodeclass="py_max",
          )

__all__.append('max_')

# Random function
randint = Fa(uid="028f2a484e7511e6bff6d4bed973e64a",
             name="randint",
             description="Random integer in range[a,b]",
             category="Math",
             nodemodule="random",
             nodeclass="randint",
             inputs=(dict(name='a', interface=IInt, value=0),
                     dict(name='b', interface=IInt, value=100),
                     ),
             outputs=(dict(name="out", interface=IInt),),
             lazy=False,
             )

__all__.append('randint')

random = Fa(uid="0704e07c4e7511e6bff6d4bed973e64a",
            name="random",
            description="Random float [0,1)",
            category="Math",
            nodemodule="random",
            nodeclass="random",
            outputs=(dict(name="out", interface=IFloat),),
            lazy=False,
            )

__all__.append('random')

randlist = Fa(uid="0bb48aa04e7511e6bff6d4bed973e64a",
              name="randlist",
              description="List of Random integer",
              category="Math",
              nodemodule="openalea.math.maths",
              nodeclass="py_randlist",
              inputs=(dict(name='a', interface=IInt, value=0),
                      dict(name='b', interface=IInt, value=100),
                      dict(name='size', interface=IInt, value=10),
                      ),
              outputs=(dict(name="out", interface=ISequence),),
              lazy=False,
              )

__all__.append('randlist')
