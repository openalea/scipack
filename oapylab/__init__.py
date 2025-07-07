from importlib import metadata

version = metadata.metadata('openalea.pylab')['version']
authors = metadata.metadata('openalea.pylab')['Author']

from . import tools
