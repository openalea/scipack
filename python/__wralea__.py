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
#       OpenAlea WebSite : https://openalea.rtfd.io
#
################################################################################

__doc__ = """ openalea.python method"""
__revision__ = " $Id$ "

from openalea.core import Factory as Fa
from openalea.core import (ICodeStr, IDict, IFileStr, IInt,
                           ISequence, IStr, ITextStr)

__name__ = "openalea.python method"
__alias__ = ["catalog.python", "openalea.python"]

__version__ = '1.0.0'
__license__ = 'CECILL-C'
__authors__ = 'OpenAlea Consortium'
__institutes__ = 'INRIA/CIRAD'
__description__ = 'Python Node library.'
__url__ = 'https://openalea.rtfd.io'

__all__ = []

# Factories
ifelse = Fa(uid="3b5edf424e7711e6bff6d4bed973e64a",
            name="ifelse",
            description="Condition",
            category="Python",
            nodemodule="python",
            nodeclass="py_ifelse",
            )

__all__.append('ifelse')

getitem = Fa(uid="3b5edf434e7711e6bff6d4bed973e64a",
             name="getitem",
             description="Python __getitem__",
             category="Python",

             inputs=[dict(name="obj", interface=None),
                     dict(name="key", interface='IInt', value=0), ],
             outputs=[dict(name='obj', interface=None)],
             nodemodule="openalea.python.python",
             nodeclass="PyGetItem",
             widgetmodule="list_selector",
             widgetclass="ListSelectorWidget",
             )

__all__.append('getitem')

setitem = Fa(uid="3b5edf444e7711e6bff6d4bed973e64a",
             name="setitem",
             description="Python __setitem__",
             category="Python",
             inputs=[dict(name="obj", interface=None),
                     dict(name="key", interface=None),
                     dict(name="value", interface=None)],
             outputs=(dict(name="out", interface=None),),
             nodemodule="openalea.python.python",
             nodeclass="py_setitem",
             )

__all__.append('setitem')

delitem = Fa(uid="3b5edf454e7711e6bff6d4bed973e64a",
             name="delitem",
             description="Python __delitem__",
             category="Python",
             nodemodule="openalea.python.python",
             nodeclass="py_delitem",
             )

__all__.append('delitem')

keys = Fa(uid="3b5edf464e7711e6bff6d4bed973e64a",
          name="keys",
          description="Python keys()",
          category="Python",
          nodemodule="openalea.python.python",
          nodeclass="keys",
          )

__all__.append('keys')

values = Fa(uid="3b5edf474e7711e6bff6d4bed973e64a",
            name="values",
            description="Python values()",
            category="Python",
            nodemodule="openalea.python.python",
            nodeclass="values",
            )

__all__.append('values')

items = Fa(uid="3b5edf484e7711e6bff6d4bed973e64a",
           name="items",
           description="Python items()",
           category="Python",
           nodemodule="openalea.python.python",
           nodeclass="items",
           )

__all__.append('items')

range_ = Fa(uid="3b5edf494e7711e6bff6d4bed973e64a",
            name="range",
            description="Returns an arithmetic progression of integers",
            category="Python",
            nodemodule="openalea.python.python",
            nodeclass="pyrange",
            inputs=[dict(name="start", interface=IInt),
                    dict(name="stop", interface=IInt),
                    dict(name="step", interface=IInt)],
            outputs=(dict(name="out", interface=IInt),),
            )

__all__.append('range_')

enum_ = Fa(uid="3b5edf4a4e7711e6bff6d4bed973e64a",
           name="enumerate",
           description="Returns a python enumerate object.",
           category="Python",
           nodemodule="openalea.python.python",
           nodeclass="pyenumerate",
           )

__all__.append('enum_')

len_ = Fa(uid="3b5edf4b4e7711e6bff6d4bed973e64a",
          name="len",
          description="Returns the number of items of a sequence or mapping.",
          category="Python",
          nodemodule="openalea.python.python",
          nodeclass="pylen",
          )

__all__.append('len_')

print_ = Fa(uid="3b5edf4c4e7711e6bff6d4bed973e64a",
            name="print",
            description="Console output",
            category="Python",
            nodemodule="openalea.python.python",
            nodeclass="py_print",
            # outputs=(),
            lazy=False,
            )

__all__.append('print_')

sorted_ = Fa(uid="3b5edf4d4e7711e6bff6d4bed973e64a",
             name="sorted",
             description="Console output",
             category="Python",
             nodemodule="__builtin__",
             nodeclass="sorted",
             # outputs=(),
             lazy=False,
             )

__all__.append('sorted_')

method_ = Fa(uid="3b5edf4e4e7711e6bff6d4bed973e64a",
             name="method",
             description="Calls object method",
             category="Python",
             nodemodule="openalea.python.python",
             nodeclass="py_method",
             inputs=(dict(name="obj", interface=None),
                     dict(name="member_name", interface=IStr),
                     dict(name="args", interface=IDict)),
             outputs=(dict(name="member"),),
             )

__all__.append('method_')

getattr_ = Fa(uid="3b5edf4f4e7711e6bff6d4bed973e64a",
              name="getattr",
              description="Gets class attribute",
              category="Python",
              nodemodule="openalea.python.python",
              nodeclass="py_getattr",

              inputs=(dict(name="obj", interface=None),
                      dict(name="member_name", interface=IStr)),
              outputs=(dict(name="member"),),
              )

__all__.append('getattr_')

setattr_ = Fa(uid="3b5edf504e7711e6bff6d4bed973e64a",
              name="setattr",
              description="Sets class attribute",
              category="Python",
              nodemodule="openalea.python.python",
              nodeclass="py_setattr",
              lazy=False,
              inputs=(dict(name="obj", interface=None),
                      dict(name="member_name", interface=IStr),
                      dict(name="value", interface=IStr)),
              outputs=(dict(name="obj"),),
              )

__all__.append('getattr_')

eval_ = Fa(uid="3b5edf514e7711e6bff6d4bed973e64a",
           name="eval",
           description="Eval str as python expression",
           category="Python",
           nodemodule="openalea.python.python",
           nodeclass="py_eval",

           inputs=(dict(name="expression", interface=ITextStr),),
           outputs=(dict(name="result"),),
           )

__all__.append('eval_')

exec_ = Fa(uid="3b5edf524e7711e6bff6d4bed973e64a",
           name="exec",
           description="Exec str as python code",
           category="Python",
           nodemodule="openalea.python.python",
           nodeclass="py_exec",

           inputs=(dict(name="code", interface=ITextStr),),
           outputs=(dict(name="locals", interface=IDict),),
           )

__all__.append('exec_')

source_code = Fa(uid="3b5edf534e7711e6bff6d4bed973e64a",
                 name="source code",
                 description="Execute python code",
                 category="Python",
                 nodemodule="openalea.python.python",
                 nodeclass="py_exec",
                 inputs=(dict(name="code", interface=ICodeStr),),
                 outputs=(dict(name="locals", interface=IDict),),
                 )

__all__.append('source_code')

zip_ = Fa(uid="3b5edf544e7711e6bff6d4bed973e64a",
          name="zip",
          description="Zip 2 sequences",
          category="Python",
          nodemodule="openalea.python.python",
          nodeclass="py_zip",
          inputs=[dict(name='in1'), dict(name='in2')],
          outputs=[dict(name='res')]
          )

__all__.append('zip_')

zip2_ = Fa(uid="3b5edf554e7711e6bff6d4bed973e64a",
           name="zip2",
           description="Zip N sequences",
           category="Python",
           nodemodule="openalea.python.python",
           nodeclass="py_zip2",
           inputs=[dict(name="lists", interface="ISequence")],
           outputs=[dict(name="zipped", interface="ISequence")]
           )

__all__.append('zip2_')

flatten_ = Fa(uid="3b5edf564e7711e6bff6d4bed973e64a",
              name="flatten",
              description="flatten list",
              category="Python",
              nodemodule="openalea.python.python",
              nodeclass="py_flatten",
              )

__all__.append('flatten_')

extract_ = Fa(uid="3b5edf574e7711e6bff6d4bed973e64a",
              name="extract",
              description="Extract element from a list or a dict",
              category="Python",
              nodemodule="openalea.python.python",
              nodeclass="extract",
              inputs=[dict(name='indexable', interface=ISequence, value=[]),
                      dict(name='keys', interface=ISequence, value=[])
                      ],
              outputs=[dict(name='list', interface=ISequence)],
              )

__all__.append('extract_')

pysum = Fa(uid="3b5edf584e7711e6bff6d4bed973e64a",
           name="sum",
           description=sum.__doc__,
           category="Python",
           nodemodule="openalea.python.python",
           nodeclass="pysum",
           inputs=[dict(name='sequence', interface=ISequence, value=[]), ],
           outputs=[dict(name='value')],
           )
__all__.append('pysum')
pymean = Fa(uid="3b5edf594e7711e6bff6d4bed973e64a",
            name="mean",
            description="Compute the mean of a sequence",
            category="Python",
            nodemodule="openalea.python.python",
            nodeclass="pymean",
            inputs=[dict(name='sequence', interface=ISequence, value=[]), ],
            outputs=[dict(name='value')],
            )
__all__.append('pymean')

# DEPRECATED
fwrite = Fa(uid="3b5edf5a4e7711e6bff6d4bed973e64a",
            name="fwrite",
            description="File output",
            category="Python",
            nodemodule="openalea.python.python",
            nodeclass="py_fwrite",
            inputs=(dict(name="x", interface=IStr),
                    dict(name="filename", interface=IFileStr),
                    dict(name="mode", interface=IStr, value="w"),
                    ),
            outputs=(),
            lazy=False,
            )

__all__.append('fwrite_')

fread = Fa(uid="3b5edf5b4e7711e6bff6d4bed973e64a",
           name="fread",
           description="File input",
           category="Python",
           nodemodule="openalea.python.python",
           nodeclass="FileRead",
           inputs=(dict(name="filename", interface=IFileStr),
                   ),
           outputs=(dict(name="string", interface=IStr),),
           lazy=False,
           )

__all__.append('fread')

select_callable = Fa(uid="3b5edf5c4e7711e6bff6d4bed973e64a",
                     name='select callable',
                     authors='Daniel BARBEAU (INRIA)',
                     description=('Given an object, it allows to select a'
                                  ' member of the object. The node morphs'
                                  ' into the given method.'),
                     category='Experimental HardCore',  # this is true!
                     nodemodule='wrap_method',
                     nodeclass='SelectCallable',
                     inputs=[{'interface': None,
                              'name': 'object',
                              'value': None,
                              'desc': 'the object to inspect'}],
                     outputs=[],
                     widgetmodule='wrap_method_gui',
                     widgetclass='SelectCallable',
                     )

__all__.append('select_callable')
