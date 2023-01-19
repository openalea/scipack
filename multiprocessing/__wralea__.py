from openalea.core import Factory as Fa
from openalea.core import IFunction, IInt, ISequence

__name__ = 'openalea.multiprocessing'

__editable__ = True
__description__ = 'Functional Node library.'
__license__ = 'CECILL-C'
__url__ = 'https://openalea.rtfd.io'
__alias__ = []
__version__ = '1.0.0'
__authors__ = 'OpenAlea Consortium'
__institutes__ = 'INRIA/CIRAD'
__icon__ = ''

__all__ = ['pmap_pmap', 'ppymap']

pmap_pmap = Fa(uid="a08a1ef04e7611e6bff6d4bed973e64a",
               name='parallel map',
               description='',
               category='Unclassified',
               nodemodule='openalea.multiprocessing.parallel_map',
               nodeclass='parallel_map',
               inputs=[{'interface': IFunction,
                        'name': 'function', 'value': None,
                        'desc': ''},
                       {'interface': ISequence,
                        'name': 'seq', 'value': None,
                        'desc': ''}],
               outputs=[
                   {'interface': None, 'name': 'result',
                    'desc': ''}],
               widgetmodule=None,
               widgetclass=None,
               )

ppymap = Fa(uid="a08a1ef14e7611e6bff6d4bed973e64a",
            name='pmap',
            description='Apply a function on a sequence',
            category='Functional',
            nodemodule='openalea.multiprocessing.parallel',
            nodeclass='pymap',
            inputs=({'interface': IFunction, 'name': 'func'},
                    {'interface': ISequence, 'name': 'seq'},
                    {'interface': IInt(min=1, max=16777216,
                                       step=1), 'name': 'N'}),
            outputs=(dict(name="out", interface=ISequence),),
            widgetmodule=None,
            widgetclass=None,
            )
