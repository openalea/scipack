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
from openalea.core import IEnumStr, IFloat, IInt, ISequence

__name__ = "openalea.stat.distribution"
__alias__ = ["stat.distribution"]

__version__ = '0.0.1'
__license__ = 'CECILL-C'
__authors__ = 'OpenAlea consortium'
__institutes__ = 'INRIA/CIRAD/UM2'
__description__ = 'Probability distributions from Rpy and Scipy.'
__url__ = 'http://rpy.sourceforge.net and http://www.scipy.org/'

__editable__ = 'False'

__all__ = ['randomcontinuous', 'densitynormal', 'cumulativenormal',
           'randomnormal', 'densitypoisson', 'cumulatepoisson', 'randompoisson',
           'randomdiscrete']

randomcontinuous = Fa(uid="3b3979904e7811e6bff6d4bed973e64a",
                      name="random continuous (rpy)",
                      description=("Generate random values from continuous "
                                   "distribution"),
                      category="statistics",
                      nodemodule="openalea.stat.distribution.distribution",
                      nodeclass="random_continuous_law",
                      inputs=(dict(name="law",
                                   interface=IEnumStr(['exp', 'norm', 'unif']),
                                   showwidget=True),
                              dict(name="n", interface=IInt, showwidget=True),
                              dict(name="args", interface=ISequence,
                                   showwidget=True),
                              ),
                      outputs=(dict(name="res", interface=ISequence),
                               ),
                      )

densitynormal = Fa(uid="3b3979914e7811e6bff6d4bed973e64a",
                   name="density normal",
                   description="Compute the density of normal distribution",
                   category="statistics.normal distribution",
                   nodemodule="openalea.stat.distribution.distribution",
                   nodeclass="dnorm",
                   inputs=(dict(name="X", interface=ISequence, showwidget=True),
                           dict(name="Mean", interface=IFloat, value=0.),
                           dict(name="Sd", interface=IFloat, value=1.),
                           ),
                   outputs=(dict(name="density", interface=ISequence),
                            ),
                   )

cumulativenormal = Fa(uid="3b3979924e7811e6bff6d4bed973e64a",
                      name="cumulative normal",
                      description=("Compute the cumulative probability of "
                                   "normal distribution"),
                      category="statistics.normal distribution",
                      nodemodule="openalea.stat.distribution.distribution",
                      nodeclass="pnorm",
                      inputs=(
                          dict(name="X", interface=ISequence, showwidget=True),
                          dict(name="Mean", interface=IFloat, value=0.),
                          dict(name="Sd", interface=IFloat, value=1.),
                      ),
                      outputs=(dict(name="cumulate", interface=ISequence),
                               ),
                      )

randomnormal = Fa(uid="3b3979934e7811e6bff6d4bed973e64a",
                  name="random normal",
                  description="Generate random values from normal distribution",
                  category="statistics.normal distribution",
                  nodemodule="openalea.stat.distribution.distribution",
                  nodeclass="rnorm",
                  inputs=(
                      dict(name="n", interface=IInt, value=1, showwidget=True),
                      dict(name="Mean", interface=IFloat, value=0.),
                      dict(name="Sd", interface=IFloat, value=1.),
                  ),
                  outputs=(dict(name="random", interface=ISequence),
                           ),
                  )

densitypoisson = Fa(uid="3b3979944e7811e6bff6d4bed973e64a",
                    name="density poisson",
                    description="Compute the density of poisson distribution",
                    category="statistics.poisson distribution",
                    nodemodule="openalea.stat.distribution.distribution",
                    nodeclass="dpois",
                    inputs=(
                        dict(name="X", interface=ISequence, showwidget=True),
                        dict(name="Lambda", interface=IFloat, value=1.),
                    ),
                    outputs=(dict(name="density", interface=ISequence),
                             ),
                    )

cumulatepoisson = Fa(uid="3b3979954e7811e6bff6d4bed973e64a",
                     name="cumulate poisson",
                     description=("Compute the cumulative probability of "
                                  "poisson distribution"),
                     category="statistics.poisson distribution",
                     nodemodule="openalea.stat.distribution.distribution",
                     nodeclass="ppois",
                     inputs=(
                         dict(name="X", interface=ISequence, showwidget=True),
                         dict(name="Lambda", interface=IFloat, value=1.),
                     ),
                     outputs=(dict(name="cumulate", interface=ISequence),
                              ),
                     )

randompoisson = Fa(uid="3b3979964e7811e6bff6d4bed973e64a",
                   name="random poisson",
                   description=("Generate random values from poisson"
                                " distribution"),
                   category="statistics.poisson distribution",
                   nodemodule="openalea.stat.distribution.distribution",
                   nodeclass="rpois",
                   inputs=(
                       dict(name="n", interface=IInt, value=1, showwidget=True),
                       dict(name="Lambda", interface=IFloat, value=1.),
                   ),
                   outputs=(dict(name="random", interface=ISequence),
                            ),
                   )

randomdiscrete = Fa(uid="3b3979974e7811e6bff6d4bed973e64a",
                    name="random discrete (rpy)",
                    description=("Generate random values from discrete"
                                 " distribution"),
                    category="statistics",
                    nodemodule="openalea.stat.distribution.distribution",
                    nodeclass="random_discrete_law",
                    inputs=(dict(name="law",
                                 interface=IEnumStr(['binom', 'geom', 'pois']),
                                 showwidget=True),
                            dict(name="n", interface=IInt, showwidget=True),
                            dict(name="args", interface=ISequence,
                                 showwidget=True),
                            ),
                    outputs=(dict(name="res", interface=ISequence),
                             ),
                    )
