import pytest

from openalea.core.alea import *

pm = PackageManager()
pm.init(verbose=False)

test_names = ['numpy.tri', 'numpy.eye']

demo_names = [
    'creation of two dimensional array',
    'simple creation of array'
    ]


#datasets = ['PyLabBivariateNormal']



def check(wralea, name):
    res = run(('openalea.numpy.%s' % wralea, name),{},pm=pm)

#class TestReplaceYield:
#@pytest.mark.parametrize('dataset', datasets)
#def test_dataset(dataset):
#    check('datasets', dataset)

@pytest.mark.parametrize('test', test_names)
def test_workflow(test):
    check('test.creation', test)

@pytest.mark.parametrize('demo', demo_names)
def test_demo(demo):
    check('demo', demo)
