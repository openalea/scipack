from openalea.core import Factory as Fa
from openalea.core import IDirStr, IFileStr, ISequence, IStr

__name__ = 'openalea.file'

__editable__ = True
__description__ = 'File manimulation library.'
__license__ = 'CECILL-C'
__url__ = 'http://openalea.gforge.inria.fr'
__alias__ = ['catalog.file']
__version__ = '0.0.1'
__authors__ = 'OpenAlea Consortium'
__institutes__ = 'INRIA/CIRAD'
__icon__ = ''

__all__ = []

files_DirName = Fa(uid="cad746e64e7211e6bff6d4bed973e64a",
                   name='dirname',
                   description='Directory name',
                   category='File,IO',
                   nodemodule='openalea.file.files',
                   nodeclass='DirName',
                   inputs=(
                       {'interface': IDirStr, 'name': 'DirStr', 'value': ''},),
                   outputs=({'interface': IDirStr, 'name': 'DirStr'},),
                   widgetmodule=None,
                   widgetclass=None,
                   )
__all__.append('files_DirName')

files_joinpath = Fa(uid="d14e39624e7211e6bff6d4bed973e64a",
                    name='joinpath',
                    description='Join several strings to form a path',
                    category='File,IO',
                    nodemodule='openalea.file.files',
                    nodeclass='joinpath',
                    inputs=(
                        {'interface': ISequence, 'name': 'a', 'value': []},),
                    outputs=({'interface': IStr, 'name': 'path'},),
                    widgetmodule=None,
                    widgetclass=None,
                    )
__all__.append('files_joinpath')

expand_user = Fa(uid="d5b5d78a4e7211e6bff6d4bed973e64a",
                 name='expand_user_dir',
                 description='Replaces tilde by user home dir',
                 category='File,IO',
                 nodemodule='openalea.file.files',
                 nodeclass='expanduser',
                 inputs=({'interface': IStr, 'name': 'path', 'value': ''},),
                 outputs=({'interface': IStr, 'name': 'path'},),
                 widgetmodule=None,
                 widgetclass=None,
                 )
__all__.append('expand_user')

files_FileReadlines = Fa(uid="dad9c2264e7211e6bff6d4bed973e64a",
                         name='readlines',
                         description='read a file as a sequence of lines',
                         category='File,IO',
                         nodemodule='openalea.file.files',
                         nodeclass='FileReadlines',
                         inputs=({'interface': IFileStr, 'name': 'filename'},),
                         outputs=({'interface': ISequence, 'name': 'string'},),
                         widgetmodule=None,
                         widgetclass=None,
                         )
__all__.append('files_FileReadlines')

parentdir_parentdir = Fa(uid="dfbfc4f24e7211e6bff6d4bed973e64a",
                         name='parentdir',
                         description='os.path.dirname method',
                         category='data i/o',
                         nodemodule='openalea.file.files',
                         nodeclass='parentdir',
                         inputs=[{'interface': IFileStr, 'name': 'path',
                                  'value': '.', 'desc': 'file or path name'}],
                         outputs=[{'interface': IDirStr, 'name': 'dirname',
                                   'desc': ''}],
                         widgetmodule=None,
                         widgetclass=None,
                         )
__all__.append('parentdir_parentdir')

files_py_write = Fa(uid="e992b5ac4e7211e6bff6d4bed973e64a",
                    name='write',
                    description='write to a file',
                    category='File,IO',
                    nodemodule='openalea.file.files',
                    nodeclass='py_write',
                    inputs=({'interface': IStr, 'name': 'x'},
                            {'interface': IFileStr, 'name': 'filename'},
                            {'interface': IStr, 'name': 'mode', 'value': 'w'}),
                    outputs=({'interface': IFileStr, 'name': 'filename'},),
                    widgetmodule=None,
                    widgetclass=None,
                    )
__all__.append('files_py_write')

files_glob = Fa(uid="eecf95bc4e7211e6bff6d4bed973e64a",
                name='glob',
                description='Return a list of path that math the pattern',
                category='File,IO',
                nodemodule='openalea.file.files',
                nodeclass='glob',
                inputs=({'interface': IDirStr, 'name': 'directory'},
                        {'interface': IStr, 'name': 'pattern', 'value': '*'},),
                outputs=({'interface': ISequence, 'name': 'path_list'},),
                # widgetmodule='widget',
                # widgetclass="ListSelectorWidget",
                )
__all__.append('files_glob')

files_copy = Fa(uid="f407ae704e7211e6bff6d4bed973e64a",
                name='copy',
                description='Copy data and mode bits ("cp src dst")',
                category='File,IO',
                nodemodule='shutil',
                nodeclass='copy',
                inputs=({'interface': IFileStr, 'name': 'src'},
                        {'interface': IFileStr, 'name': 'dest'},),
                outputs=({'name': 'status'},),
                widgetmodule=None,
                widgetclass=None,
                )
__all__.append('files_copy')

# viewfile = CNF(uid="", name='viewfile',
#                description='View the content of a file.',
#                category='File,IO,composite',
#                doc='',
#                inputs=[{'interface': IFileStr, 'name': 'filename(read)',
#                         'value': ''}],
#                outputs=[{'interface': ITextStr, 'name': 'Text(text)'}],
#                elt_factory={2: ('catalog.file', 'read'),
#                             3: ('catalog.data', 'text')},
#                elt_connections={135946380: (2, 0, 3, 0),
#                                 135946392: (3, 0, '__out__', 0),
#                                 135946404: ('__in__', 0, 2, 0)},
#                elt_data={2: {'caption': 'read',
#                              'hide': True,
#                              'lazy': False,
#                              'minimal': False,
#                              'port_hide_changed': set(),
#                              'posx': 246.25,
#                              'posy': 111.25,
#                              'priority': 0},
#                          3: {'caption': 'text',
#                              'hide': False,
#                              'lazy': True,
#                              'minimal': False,
#                              'port_hide_changed': set(),
#                              'posx': 246.25,
#                              'posy': 166.25,
#                              'priority': 0},
#                          '__in__': {'caption': 'In',
#                                     'hide': True,
#                                     'lazy': True,
#                                     'minimal': False,
#                                     'port_hide_changed': set(),
#                                     'posx': 20.0,
#                                     'posy': 5.0,
#                                     'priority': 0},
#                          '__out__': {'caption': 'Out',
#                                      'hide': True,
#                                      'lazy': True,
#                                      'minimal': False,
#                                      'port_hide_changed': set(),
#                                      'posx': 20.0,
#                                      'posy': 250.0,
#                                      'priority': 0}},
#                elt_value={2: [], 3: [], '__in__': [], '__out__': []},
#                elt_ad_hoc={},
#                lazy=True,
#                )
# __all__.append('viewfile')


files_FileName = Fa(uid="00e3915e4e7311e6bff6d4bed973e64a",
                    name='filename',
                    description='Browser to select a file pathname',
                    category='File,IO',
                    nodemodule='files',
                    nodeclass='FileName',
                    inputs=(
                        {'interface': IFileStr, 'name': 'FileStr',
                         'value': ''},),
                    outputs=({'interface': IFileStr, 'name': 'FileStr'},),
                    widgetmodule=None,
                    widgetclass=None,
                    )
__all__.append('files_FileName')

files_FileRead = Fa(uid="068efeea4e7311e6bff6d4bed973e64a",
                    name='read',
                    description='read a file',
                    category='File,IO',
                    nodemodule='openalea.file.files',
                    nodeclass='FileRead',
                    inputs=({'interface': IFileStr, 'name': 'filename'},),
                    outputs=({'interface': IStr, 'name': 'string'},),
                    widgetmodule=None,
                    widgetclass=None,
                    )
__all__.append('files_FileRead')

files_py_tmpnam = Fa(uid="0a5af1824e7311e6bff6d4bed973e64a",
                     name='tmpnam',
                     description='return a unique name for a temporary file.',
                     category='File,IO',
                     nodemodule='openalea.file.files',
                     nodeclass='py_tmpnam',
                     inputs=(),
                     outputs=({'interface': IStr, 'name': 'filename'},),
                     widgetmodule=None,
                     widgetclass=None,
                     )
__all__.append('files_py_tmpnam')

files_PackageDir = Fa(uid="0f7030f64e7311e6bff6d4bed973e64a",
                      name='packagedir',
                      description='Package Directory',
                      category='File,IO',
                      nodemodule='openalea.file.files',
                      nodeclass='PackageDir',
                      inputs=(
                          {'interface': IStr, 'name': 'PackageStr',
                           'value': ''},),
                      outputs=({'interface': IDirStr, 'name': 'DirStr'},),
                      widgetmodule=None,
                      widgetclass=None,
                      )
__all__.append('files_PackageDir')

files_listdir = Fa(uid="13b33a284e7311e6bff6d4bed973e64a",
                   name='listdir',
                   description='ls',
                   category='File,IO',
                   nodemodule='openalea.file.files',
                   nodeclass='listdir',
                   inputs=(
                       {'interface': IDirStr, 'name': 'directory',
                        'value': '.'},
                       {'interface': IStr, 'name': 'pattern', 'value': '*'}),
                   outputs=({'interface': IDirStr, 'name': 'DirStr'},),
                   )
__all__.append('files_listdir')

start = Fa(uid="18619aa64e7311e6bff6d4bed973e64a",
           name='start',
           description='Open a file with the default application',
           category='File,IO',
           nodemodule='openalea.file.files',
           nodeclass='start',
           inputs=({'interface': IFileStr, 'name': 'path', 'value': '.'},),
           )
__all__.append('start')

httpfile = Fa(uid="1e5c24264e7311e6bff6d4bed973e64a",
              name='http file',
              description=('Copy a network object denoted by a URL to a local'
                           ' file, if necessary. If the URL points to a local'
                           ' file, or a valid cached copy of the object exists,'
                           ' the object is not copied.'),
              category='File,IO, http',
              nodemodule='urllib',
              nodeclass='urlretrieve',
              inputs=({'interface': IStr, 'name': 'url'},),
              outputs=(dict(name='filename', interface=IFileStr),
                       dict(name='headers', interface=None)),
              )
__all__.append('httpfile')
