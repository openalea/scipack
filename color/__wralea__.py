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
"""Node declaration for colors
"""

__license__ = "Cecill-C"
__revision__ = " $Id$ "

from openalea.core import Factory as Fa
from openalea.core import Alias, Factory, IFloat, IInt, IRGBColor
from .color_interface import IColor

__name__ = "openalea.color"
__alias__ = ["catalog.color"]

__all__ = ['colormap', 'rgbcolormap']

color = Fa(uid="10f07e684e5511e6bff6d4bed973e64a",
           name="color",
           description="edit color",
           category="datatype,image",
           nodemodule="openalea.color.py_color",
           nodeclass="ColorNode",
           inputs=(dict(name="RGB",
                        interface=IColor,
                        value=(0, 0, 0)),),
           outputs=(dict(name="RGB", interface=IColor),),
           )

Alias(color, 'rgb')
__all__.append("color")

black = Fa(uid="48f7e27e4e5511e6bff6d4bed973e64a",
           name="black",
           description="black color",
           category="datatype,image",
           nodemodule="openalea.color.py_color",
           nodeclass="BlackNode",
           inputs=(),
           outputs=(dict(name="RGB", interface=IColor),),
           )

__all__.append("black")

white = Fa(uid="4da61a2a4e5511e6bff6d4bed973e64a",
           name="white",
           description="white color",
           category="datatype,image",
           nodemodule="openalea.color.py_color",
           nodeclass="WhiteNode",
           inputs=(),
           outputs=(dict(name="RGB", interface=IColor),),
           )

__all__.append("white")

red = Fa(uid="5252eae44e5511e6bff6d4bed973e64a",
         name="red",
         description="red color",
         category="datatype,image",
         nodemodule="openalea.color.py_color",
         nodeclass="RedNode",
         inputs=(),
         outputs=(dict(name="RGB", interface=IColor),),
         )

__all__.append("red")

green = Fa(uid="56dc75264e5511e6bff6d4bed973e64a",
           name="green",
           description="green color",
           category="datatype,image",
           nodemodule="openalea.color.py_color",
           nodeclass="GreenNode",
           inputs=(),
           outputs=(dict(name="RGB", interface=IColor),),
           )

__all__.append("green")

blue = Fa(uid="5a61e83e4e5511e6bff6d4bed973e64a",
          name="blue",
          description="blue color",
          category="datatype,image",
          nodemodule="openalea.color.py_color",
          nodeclass="BlueNode",
          inputs=(),
          outputs=(dict(name="RGB", interface=IColor),),
          )

__all__.append("blue")

col_item = Fa(uid="68819be44e5511e6bff6d4bed973e64a",
              name="col_item",
              description="color from color list",
              category="datatype,image",
              nodemodule="openalea.color.py_color",
              nodeclass="col_item",
              inputs=(dict(name="ind", interface=IInt, value=0),),
              outputs=(dict(name="RGB", interface=IColor),),
              )

__all__.append("col_item")

random = Fa(uid="6de9db504e5511e6bff6d4bed973e64a",
            name="random",
            description="random color",
            category="datatype,image",
            nodemodule="openalea.color.py_color",
            nodeclass="random",
            inputs=(dict(name="alpha", interface=IInt, value=255),),
            outputs=(dict(name="RGB", interface=IColor),),
            )

__all__.append("random")

hsv2rgb = Fa(uid="7241f7784e5511e6bff6d4bed973e64a",
             name="hsv2rgb",
             description="RGB tuple",
             category="datatype,image",
             nodemodule="py_color",
             nodeclass="rgb",
             inputs=(dict(name="H", interface=IInt, value=0),
                     dict(name="S", interface=IInt, value=0),
                     dict(name="V", interface=IInt, value=0),
                     dict(name="alpha", interface=IInt, value=None),),
             outputs=(dict(name="RGB", interface=IColor),),
             )

__all__.append("hsv2rgb")

rgb2hsv = Fa(uid="81071d1a4e5511e6bff6d4bed973e64a",
             name="rgb2hsv",
             description="HSV tuple",
             category="datatype,image",
             nodemodule="py_color",
             nodeclass="hsv",
             inputs=(dict(name="RGB", interface=IColor, value=(0, 0, 0)),),
             outputs=(dict(name="H", interface=IInt),
                      dict(name="S", interface=IInt),
                      dict(name="V", interface=IInt),
                      dict(name="alpha", interface=IInt),),
             )

__all__.append("rgb2hsv")
Alias(rgb2hsv, "hsv")

colormap = Fa(uid="86cf1d064e5511e6bff6d4bed973e64a",
              name='colormap',
              description='defines a color map from a range of values [I,J] to RGB',
              category='Visualization,image',
              nodemodule='openalea.color.py_color',
              nodeclass='color_map',
              inputs=({'interface': IFloat, 'name': 'val'},
                      {'interface': IFloat, 'name': 'minval', 'value': 0},
                      {'interface': IFloat, 'name': 'maxval', 'value': 1},
                      {'interface': IFloat, 'name': 'color1HSV',
                       'value': 20},
                      {'interface': IFloat, 'name': 'color2HSV',
                       'value': 80}),
              outputs=({'interface': IRGBColor, 'name': 'color'},
                       ),
              widgetmodule=None,
              widgetclass=None,
              )

rgbcolormap = Fa(uid="8c78ce284e5511e6bff6d4bed973e64a",
                 name='rgbcolormap',
                 description='defines a RGB color map from 2 colors given in HSV',
                 category='Visualization,image',
                 nodemodule='openalea.color.py_color',
                 nodeclass='rgb_color_map',
                 inputs=({'interface': IFloat, 'name': 'val'},
                         {'interface': IFloat, 'name': 'minval',
                          'value': 0},
                         {'interface': IFloat, 'name': 'maxval',
                          'value': 1},
                         {'interface': IInt(0, 400), 'name': 'Hue1',
                          'value': 0},
                         {'interface': IInt(0, 400), 'name': 'Hue2',
                          'value': 100},
                         {'interface': IInt(0,
                                            255),
                          'name': 'Sat',
                          'value': 220,
                          'showwidget': False,
                          'hide': True},
                         {'interface': IInt(0,
                                            255),
                          'name': 'Val',
                          'value': 220,
                          'showwidget': False,
                          'hide': True},
                         ),
                 outputs=(dict(name="Color", interface=IRGBColor, ),
                          ),
                 widgetmodule=None,
                 widgetclass=None,
                 )
