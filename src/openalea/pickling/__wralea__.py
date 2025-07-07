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

__doc__ = """ catalog.pickle """
__revision__ = " $Id$ "

from openalea.core import Factory as Fa
from openalea.core import IBool, IFileStr

__name__ = "openalea.file.pickle"
__alias__ = ["catalog.pickle", "openalea.pickle"]

__version__ = '0.0.1'
__license__ = 'CECILL-C'
__authors__ = 'OpenAlea Consortium'
__institutes__ = 'INRIA/CIRAD'
__description__ = 'Python Node library'
__url__ = 'http://openalea.gforge.inria.fr'

__all__ = ['load', 'dump']

load = Fa(uid="e7aade0a4e7611e6bff6d4bed973e64a",
          name="pickle load",
          description="load pickled data",
          category="Python",
          nodemodule="openalea.pickling.pickling",
          nodeclass="py_load",
          inputs=(dict(name="file_path", interface=IFileStr),),
          outputs=(dict(name="data", interface=None, ),),
          lazy=False,
          )

dump = Fa(uid="e7aade0b4e7611e6bff6d4bed973e64a",
          name="pickle dump",
          description="pickled data writer",
          category="Python",
          nodemodule="openalea.pickling.pickling",
          nodeclass="py_dump",
          inputs=(dict(name="data", interface=None, ),
                  dict(name="file_path", interface=IFileStr),
                  dict(name="append", interface=IBool, value=False, ),),
          outputs=(),
          lazy=False,
          )
