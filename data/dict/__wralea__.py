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
from openalea.core import IDict

__name__ = "openalea.data structure.dict"

__version__ = '0.0.1'
__license__ = "Cecill-C"
__authors__ = 'OpenAlea Consortium'
__institutes__ = 'INRIA/CIRAD'
__description__ = 'Nodes for standard data structure creation, edition and visualisation.'
__url__ = 'http://openalea.gforge.inria.fr'

__all__ = []

dict_ = Fa(uid="35c30fca4e6f11e6bff6d4bed973e64a",
           name="dict",
           description="Python dictionary",
           category="datatype",
           nodemodule="openalea.data.dict.dicts",
           nodeclass="Dict",

           inputs=(dict(name="Dict", interface=IDict),),
           outputs=(dict(name="Dict", interface=IDict),),
           )
__all__.append('dict_')

edict_ = Fa(uid="3cb6ccd64e6f11e6bff6d4bed973e64a",
            name="edit dict",
            description="Python dictionary",
            category="datatype",
            nodemodule="openalea.data.dict.dicts",
            nodeclass="EditDict",

            inputs=(dict(name="Dict"), dict(name="dict", interface=IDict),),
            outputs=(dict(name="Dict", interface=IDict),),
            )

__all__.append('edict_')
