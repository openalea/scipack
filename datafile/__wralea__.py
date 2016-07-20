from openalea.core import Factory as Fa
from openalea.core import IStr

__name__ = 'openalea.data file'
__alias__ = []

__version__ = '0.0.1'
__license__ = "Cecill-C"
__authors__ = 'OpenAlea Consortium'
__institutes__ = 'INRIA/CIRAD'
__description__ = ''
__url__ = 'http://openalea.gforge.inria.fr'

__all__ = ['qd']

qd = Fa(uid="c20b6c144e7111e6bff6d4bed973e64a",
        name='get_data',
        authors='OpenAlea Consortium',
        description=('This node permits to find a shared data file located'
                     ' in a given Python package. The data file is searched'
                     ' among the data nodes of the PackageManager.'),
        category='data i/o',
        nodemodule='openalea.datafile.datafile',
        nodeclass='GetData',
        inputs=[
            {'interface': IStr, 'name': 'package', 'value': None},
            {'interface': IStr, 'name': 'glob', 'value': '*'},
            {'interface': IStr, 'name': 'filename', 'value': None}],
        outputs=[{'interface': IStr, 'name': 'filepath'}],
        widgetmodule='datafile_widget',
        widgetclass='GetDataBrowser',
        )
