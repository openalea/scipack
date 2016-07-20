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
from openalea.core import IDict, IFloat, ISequence, IStr

__name__ = "openalea.stat.test"
__alias__ = ["stat.test"]

__version__ = '0.0.1'
__license__ = 'CECILL-C'
__authors__ = 'OpenAlea consortium'
__institutes__ = 'INRIA/CIRAD/UM2'
__description__ = 'Test functions  from Rpy and Scipy.'
__url__ = 'http://rpy.sourceforge.net and http://www.scipy.org/'

__editable__ = 'False'

__all__ = ['chisquare', 'studenttest', 'kstest', ]

chisquare = Fa(uid="0fff229c4e7911e6bff6d4bed973e64a",
               name="chi square test (rpy)",
               description="Compute the Chisquare Test",
               category="test",
               nodemodule="openalea.stat.stattest",
               nodeclass="chisqtest",
               inputs=(dict(name="X", interface=ISequence, showwidget=True),
                       dict(name="Y", interface=ISequence, showwidget=True),
                       dict(name="Proportion", interface=ISequence,
                            showwidget=True),
                       ),
               outputs=(dict(name="chisqtest", interface=IDict),
                        ),
               )

studenttest = Fa(uid="0fff229d4e7911e6bff6d4bed973e64a",
                 name="student test (scipy)",
                 description="compute the Student Test",
                 category="test",
                 nodemodule="openalea.stat.stattest",
                 nodeclass="ttest",
                 inputs=(dict(name="X", interface=ISequence, showwidget=True),
                         dict(name="Y", interface=ISequence, showwidget=True),
                         dict(name="mu", interface=IFloat, value=0.),
                         ),
                 outputs=(dict(name="ttest", interface=IDict),
                          ),
                 )

kstest = Fa(uid="0fff229e4e7911e6bff6d4bed973e64a",
            name="kolmogorov smirnov test (scipy)",
            description="compute the Kolmogorov-Smirnov Test",
            category="test",
            nodemodule="openalea.stat.stattest",
            nodeclass="kstest",
            inputs=(dict(name="X", interface=ISequence, showwidget=True),
                    dict(name="Y", interface=ISequence, showwidget=True),
                    dict(name="Cdf", interface=IStr, showwidget=True),
                    dict(name="Args", interface=ISequence, showwidget=True),
                    ),
            outputs=(dict(name="kstest", interface=IDict),
                     ),
            )
