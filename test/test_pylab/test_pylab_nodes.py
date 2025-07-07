import pytest

from openalea.core.alea import *

pm = PackageManager()
pm.init(verbose=False)

test_names = ['acorr', 'annotation', 'axhspan_axvspan', 'boxplot', 
    'cohere', 'circle', 'cohere', 'colorbar', 'contour', 'csd', 'ellipse', 'errorbar', 
    'figure', 'fill', 'fill_between', 'grid', 'hexbin', 'hist', 'imshow', 'legend', 
    'loglog', 'mcontour3d', 'mcontourf3d', 'mplot3d', 'patches', 'pcolor', 'pie',  
    'plot', 'polygon', 'polar', 'psd', 'quiver', 'rectangle', 'scatter', 
    'semilogx', 'semilogy', 'specgram', 'stem', 'step', 'tickparams', 'title', 
    'tutorial_plot', 'tutorial_plot_line2d', 'wedge', 'xcorr', 
    'xylabels', 'xylim', 'xyticks']

# TODO: test failed :  'axhline_axvline'

demo_names = [
    'polar_scatter', 'polar_demo','labels_demo','cross_spectral_density_windowing',
    'hexbin_and_colorbar','SeveralAxesOnSameFigure','pie_demo','scatter_and_histograms',
    'scatter_demo','Line2D_and_multiplots','test_image.npy','fill_between','patches','plot_demos'
    ]


datasets = ['PyLabBivariateNormal']



def check(wralea, name):
    res = run(('openalea.pylab.%s' % wralea, name),{},pm=pm)
    from pylab import close
    close('all')

#class TestReplaceYield:
@pytest.mark.parametrize('dataset', datasets)
def test_dataset(dataset):
    check('datasets', dataset)

@pytest.mark.parametrize('test', test_names)
def test_workflow(test):
    check('test', test)

@pytest.mark.parametrize('demo', demo_names)
def test_demo(demo):
    check('demo', demo)
