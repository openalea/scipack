from importlib import metadata

version = metadata.metadata('openalea.scipack')['version']
authors = metadata.metadata('openalea.scipack')['Author']

from . import tools
