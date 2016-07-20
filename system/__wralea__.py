# -*- python -*-
#
#       OpenAlea.Core
#
#       Copyright 2006-2009 INRIA - CIRAD - INRA  
#
#       File author(s): Samuel Dufour-Kowalski <samuel.dufour@sophia.inria.fr>
#                       Christophe Pradal <christophe.prada@cirad.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################

__doc__ = """
Wralea for System nodes
"""

__revision__ = " $Id$ "

from openalea.core import Factory as Fa
from openalea.core import IBool, IDirStr, ISequence, IStr, ITextStr

__name__ = "openalea.system"

__version__ = '0.0.2'
__license__ = "Cecill-C"
__authors__ = 'OpenAlea Consortium'
__institutes__ = 'INRIA/CIRAD'
__description__ = 'System Node library.'
__url__ = 'http://openalea.gforge.inria.fr'

__all__ = []

cmd = Fa(uid="55edfaee4e7911e6bff6d4bed973e64a",
         name="command",
         description="Call a system command",
         category="misc,Python",
         nodemodule="openalea.system.systemnodes",
         nodeclass="system_cmd",
         inputs=(dict(name="commands", interface=ISequence, value=[],
                      desc='List of command strings'),
                 ),
         outputs=(dict(name="stdout", interface=None, desc='result'),
                  dict(name="stderr", interface=None, desc='result'),),
         )

__all__.append('cmd')

shcmd = Fa(uid="55edfaef4e7911e6bff6d4bed973e64a",
           name="shell command",
           description="Call a shell command in a specific directory",
           category="misc,Python",
           nodemodule="openalea.system.systemnodes",
           nodeclass="shell_command",
           inputs=(dict(name="command", interface=IStr,
                        desc='The command line to execute in a shell'),
                   dict(name='cwd', interface=IDirStr,
                        desc=('The working directory where the command will'
                              ' be executed.'))
                   ),
           outputs=(dict(name="status", desc='status'),
                    dict(name="output", interface=ITextStr,
                         desc='output stream of the command'),),
           )

__all__.append('shcmd')

vprint = Fa(uid="55edfaf04e7911e6bff6d4bed973e64a",
            name="vprint",
            description="Visual Print",
            category="IO",
            nodemodule="openalea.system.vprint",
            nodeclass="VPrint",
            inputs=(
                dict(name="obj", interface=None, desc='The object to display'),
                dict(name="caption", interface=IStr,
                     desc='The caption of the display', value='Value is'),
                # ,hide=True
                dict(name="blocking", interface=IBool,
                     desc='The caption of the display', value=False),
                # ,hide=True
                dict(name="strfunc", interface=None,
                     desc='The function to convert the object to a string',
                     value=str),
                # ,hide=True
            ),
            outputs=(
                dict(name="returned_obj", interface=None, desc='The object'),),
            )

__all__.append('vprint')
