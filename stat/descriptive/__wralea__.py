# -*- python -*-
#
#       OpenAlea.StdLib
#
#       Copyright 2006 - 2008 INRIA - CIRAD - INRA  
#
#       File author(s): CHAUBERT Florence <florence.chaubert@cirad.fr>
#                       Da SILVA David <david.da_silva@cirad.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#


from openalea.core import Factory as Fa
from openalea.core import IDict, IFloat, ISequence

__name__ = "openalea.stat.descriptive"
__alias__ = ["stat.descriptive"]

__version__ = '0.0.1'
__license__ = 'CECILL-C'
__authors__ = 'OpenAlea consortium'
__institutes__ = 'INRIA/CIRAD/UM2'
__description__ = 'Descriptive statistics from Rpy and Scipy.'
__url__ = 'http://rpy.sourceforge.net and http://www.scipy.org/'

__editable__ = 'False'

__all__ = ['log', 'statsummary', 'correlation', 'mean', 'median', 'mode',
           'variance', 'standarddeviation', 'frequencies', 'density', ]

log = Fa(uid="0c3edb084e7811e6bff6d4bed973e64a",
         name="log",
         description="Compute the log of each item of the input list",
         category="Math,stat",
         nodemodule="openalea.stat.descriptive.descriptive",
         nodeclass="list_log",
         inputs=(dict(name="x", interface=ISequence, showwidget=True),
                 ),
         outputs=(dict(name="log", interface=ISequence),
                  ),
         )

statsummay = Fa(uid="0c3edb094e7811e6bff6d4bed973e64a",
                name="stat summary",
                description=("Compute the statistical summary "
                             "(min, max, median, mean, sd) "),
                category="descriptive",
                nodemodule="openalea.stat.descriptive.descriptive",
                nodeclass="StatSummary",
                inputs=(dict(name="x", interface=ISequence, showwidget=True),
                        ),
                outputs=(dict(name="statsummary", interface=ISequence),
                         ),
                )

correlation = Fa(uid="0c3edb0a4e7811e6bff6d4bed973e64a",
                 name="correlation",
                 description="Compute the correlations",
                 category="descriptive",
                 nodemodule="openalea.stat.descriptive.descriptive",
                 nodeclass="Corr",
                 inputs=(dict(name="X", interface=ISequence, showwidget=True),
                         dict(name="Y", interface=ISequence, showwidget=True),
                         ),
                 outputs=(dict(name="Corr", interface=IDict),
                          ),
                 )

mean = Fa(uid="0c3edb0b4e7811e6bff6d4bed973e64a",
          name="mean",
          description="Compute the mean",
          category="descriptive",
          nodemodule="openalea.stat.descriptive.descriptive",
          nodeclass="Mean",
          inputs=(dict(name="X", interface=ISequence, showwidget=True),
                  ),
          outputs=(dict(name="Mean", interface=IFloat),
                   ),
          )

median = Fa(uid="0c3edb0c4e7811e6bff6d4bed973e64a",
            name="median",
            description="Compute the median",
            category="descriptive",
            nodemodule="openalea.stat.descriptive.descriptive",
            nodeclass="Median",
            inputs=(dict(name="X", interface=ISequence, showwidget=True),
                    ),
            outputs=(dict(name="Median", interface=IFloat),
                     ),
            )

mode = Fa(uid="0c3edb0d4e7811e6bff6d4bed973e64a",
          name="mode",
          description="Compute the mode",
          category="descriptive",
          nodemodule="openalea.stat.descriptive.descriptive",
          nodeclass="Mode",
          inputs=(dict(name="X", interface=ISequence, showwidget=True),
                  ),
          outputs=(dict(name="Mode", interface=IDict),
                   ),
          )

variance = Fa(uid="0c3edb0e4e7811e6bff6d4bed973e64a",
              name="variance",
              description="Compute the variance",
              category="descriptive",
              nodemodule="openalea.stat.descriptive.descriptive",
              nodeclass="Var",
              inputs=(dict(name="X", interface=ISequence, showwidget=True),
                      ),
              outputs=(dict(name="Variance", interface=IFloat),
                       ),
              )

standarddeviation = Fa(uid="0c3edb0f4e7811e6bff6d4bed973e64a",
                       name="standard deviation",
                       description="Compute the standard deviation",
                       category="descriptive",
                       nodemodule="openalea.stat.descriptive.descriptive",
                       nodeclass="Std",
                       inputs=(
                           dict(name="X", interface=ISequence, showwidget=True),
                       ),
                       outputs=(dict(name="Std", interface=IFloat),
                                ),
                       )

frequencies = Fa(uid="0c3edb104e7811e6bff6d4bed973e64a",
                 name="frequencies",
                 description="Compute the frequencies",
                 category="descriptive",
                 nodemodule="openalea.stat.descriptive.descriptive",
                 nodeclass="Freq",
                 inputs=(dict(name="X", interface=ISequence, showwidget=True),
                         ),
                 outputs=(dict(name="Freq", interface=IDict),
                          ),
                 )

density = Fa(uid="0c3edb114e7811e6bff6d4bed973e64a",
             name="density",
             description="Compute the Kernel density estimation",
             category="descriptive",
             nodemodule="openalea.stat.descriptive.descriptive",
             nodeclass="Density",
             inputs=(dict(name="X", interface=ISequence, showwidget=True),
                     ),
             outputs=(dict(name="density", interface=IDict),
                      ),
             )
