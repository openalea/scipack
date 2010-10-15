###############################################################################
# -*- python -*-
#
#       amlPy function implementation
#
#       Copyright or (C) or Copr. 2006 INRIA - CIRAD - INRA
#
#       File author(s): Christophe Pradal <christophe.prada@cirad.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################

__doc__="""
amlPy functions
"""

__license__= "Cecill-C"
__revision__=" $Id: py_stat.py 7897 2010-02-09 09:06:21Z cokelaer $ "

#//////////////////////////////////////////////////////////////////////////////


from openalea.core import Node
from openalea.core import Factory, IFileStr, IInt, IBool, IFloat, \
    ISequence, IEnumStr, IStr, IDirStr, ITuple3, IDict

from pylab import *

#matplotlib.pyplot.rcParams
scale = {'linear':'linear',
    'log':'log',
    'symlog':'symlog'}
axis = {
    'off':'off',
    'manual':'manual',
    'equal':'equal',
    'tight':'tight',
    'scaled':'scaled',
    'image':'image',
    'auto':'auto',
    'normal':'normal'
    }

sides = { 'default':'default',  'onesided':'onesided',  'twosided':'twosided' }

detrends = {
    'none':'detrend_none',
    'linear':'detrend_linear',
    'mean':'detrend_mean'
    }

streches = {
    'ultra-condensed':'ultra-condensed',
    'extra-condensed':'extra-condensed',
    'condensed':'condensed',
    'semi-condensed':'semi-condensed',
    'normal':'normal',
    'semi-expanded':'semi-expanded',
    'expanded':'expanded',
    'extra-expanded':'extra-expanded' ,
    'ultra-expanded':'ultra-expanded'
    }

weights = {
    'ultralight':'ultralight',
    'light':'light',
    'normal':'normal',
    'regular':'regular',
    'book':'book',
    'medium':'medium',
    'roman':'roman',
    'semibold':'semibold',
    'demibold':'demibold',
    'demi':'demi',
    'bold':'bold',
    'heavy':'heavy',
    'extra bold':'extra bold',
    'black':'black'
    }


sizes = {
    'xx-small':'xx-small',
    'x-small':'x-small',
    'small':'small',
    'medium':'medium',
    'large':'large',
    'x-large':'x-large',
    'xx-large':'xx-large'
    }

styles = {
    'italic':'italic',
    'normal':'normal',
    'oblique':'oblique'}

variants = {
    'normal':'normal',
    'small-caps':'small-caps'}

families = {
    'serif':'serif',
    'sans-serif':'sans-serif',
    'cursive':'cursive',
    'fantasy':'fantisy',
    'monospace':'monospace'}

horizontalalignment = {
    'center':'center',
    'right':'right' ,
    'left':'left' }

verticalalignment = {
    'center':'center' ,
    'top':'top' ,
    'bottom':'bottom' ,
    'baseline':'baseline'}

ticks= {'auto':'auto', 'None':'None'}

colors = {
    'blue':'b',
    'green':'g',
    'red':'r',
    'cyan':'c',
    'magenta':'m',
    'yellow':'y',
    'black':'k',
    'white':'w',
    'None':'None'}

origins = {'lower':'lower',
    'upper':'upper',
    'none':'None',
    }

from pylab import Line2D

drawstyles = {}
for key,value in Line2D.drawStyles.iteritems():
    drawstyles[value.replace('_draw_','')]=key

# line style --, -., .....
linestyles = {}
for key,value in Line2D.lineStyles.iteritems():
    linestyles[value.replace('_draw_','')]=key

# markers : o, square, ...
markers = {}
for key,value in Line2D.markers.iteritems():
    markers[value.replace('_draw_','')]=key

#pylab.Line2D.filled_markers

fillstyles={'top':'top',
    'full':'full',
    'bottom':'bottom',
    'left':'left',
    'right':'right',
    }

from pylab import cm, get_cmap
maps=[m for m in cm.datad if not m.endswith("_r")]
cmaps = {}
for c in maps:
    cmaps[c] = get_cmap(c)


class Locations():
    """location class used by :class:`PyLabLegend`

    """
    def __init__(self):

        self.locations = {
            'best' : 0,
            'upper right'  : 1,
            'upper left'   : 2,
            'lower left'   : 3,
            'lower right'  : 4,
            'right'        : 5,
            'center left'  : 6,
            'center right' : 7,
            'lower center' : 8,
            'upper center' : 9,
            'center'       : 10,}


orientation_fig = {
    'portrait':'portrait',
    'landscape':'landscape'}


papertypes = {
    'letter':'letter',
    'legal':'legal',
    'executive':'executive',
    'ledger':'ledger',
    'a0':'a0',
    'a1':'a1',
    'a2':'a2',
    'a3':'a3',
    'a4':'a4',
    'a5':'a5',
    'a6':'a6',
    'a7':'a7',
    'a8':'a8',
    'a9':'a9',
    'a10':'a10',
    'b0':'b0',
    'b1':'b1',
    'b2':'b2',
    'b3':'b3',
    'b4':'b4',
    'b5':'b5',
    'b6':'b6',
    'b7':'b7',
    'b8':'b8',
    'b9':'b9',
    'b10':'b10'
    }


def get_kwds_from_line2d(line2d, kwds={}, type=None):
    """create a dict from line2d properties
    """
    kwds['color']=line2d.get_color()
    kwds['linestyle']=line2d.get_linestyle()
    kwds['linewidth']=line2d.get_linewidth()
    if type!='linecollection':
        kwds['marker']=line2d.get_marker()
        kwds['markersize']=line2d.get_markersize()
        kwds['markeredgewidth']=line2d.get_markeredgewidth()
        kwds['markersize']=line2d.get_markersize()
        kwds['fillstyle']=line2d.get_fillstyle()
        kwds['markeredgecolor']=line2d.get_markeredgecolor()
    kwds['label']=line2d.get_label()
    kwds['alpha']=line2d.get_alpha()
    return kwds


def line2d2kwds(line2d, kwds={}):
    try:
        for key, value in line2d.properties().properties():
            kwds[key] = value
    except:
        print 'warning: line2d may not be a valid Line2D object'
        pass
    return kwds


def text2kwds(text, kwds={}):
    try:
        for key, value in text.properties().properties():
            kwds[key] = value
    except:
        print 'warning: text may not be a valid Text object'
        pass
    return kwds

def font2kwds(font, kwds={}):
    pass


def PyLabExp(t):
    from pylab import exp
    return (exp(t))


class PyLabData1(Node):
    def __init__(self):
        Node.__init__(self)
        self.add_input(name='X', interface=ISequence, value=[])
        self.add_input(name='Y', interface=ISequence, value=[])
    def __call__(self, inputs):
        from matplotlib.mlab import bivariate_normal
        #delta = 0.025  
        #x = np.arange(-3.0, 3.0, delta)
        #y = np.arange(-2.0, 2.0, delta)
        X = self.get_input('X')
        Y = self.get_input('Y')
        Z1 = bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
        Z2 = bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
        # difference of Gaussians
        Z = 10.0 * (Z2 - Z1)

        return Z

class CustomizeAxes(object):
    def __init__(self):
        pass
    def get_axes(self):
        axes = self.get_input('axes')
        if type(axes)!=list:
            axes = [axes]
        for axe in axes:
            import matplotlib
            assert axe.__module__ in [matplotlib.axes.__name__,matplotlib.projections.polar.__name__], 'input must be a valid axes from matplotlib.axes %s given for %s' % (type(axes), axes)
        return axes

class PyLabLegend(Node, CustomizeAxes):
    """VisuAlea version of pylab.legend

    :param *shadow*: draw a shadow behind legend. 
    :param *location*: legend location. See :class:`Locations` 
    :param *numpoints*: the number of points in the legend for line
    :param *markercolor*:
    :param *fancybox*: draw a frame with a round fancybox
    :param *ncol*: number of columns. default is 1
    :param *mode*: if mode is "expand", the legend will be horizontally expanded
    :param *title*: the legend title
    :param *prop*: connect an optional :class`PyLabFontProperties` object to customise further
    
    .. todo::   *scatterpoints*: integer, *scatteroffsets*: , markerscale*: expand
      *bbox_to_anchor* ,  *bbox_transform*
        borderpad, labelspacing, handlelength,andletextpad,  borderaxespad,  columnspacing

    :author: Thomas Cokelaer
    """
    def __init__(self):
        Node.__init__(self)
        CustomizeAxes.__init__(self)
        self.locations = Locations().locations
        self.add_input(name='axes')
        self.add_input(name="shadow", interface=IBool, value=False)
        self.add_input(name="location", interface=IEnumStr(self.locations.keys()), value=0)
        self.add_input(name="numpoints", interface=IInt, value=2)
        self.add_input(name="markerscale", interface=IFloat(0.1,10,0.1), value=1)
        self.add_input(name="fancybox", interface=IBool, value=True)
        self.add_input(name="ncol", interface=IInt(1,10), value=1)
        self.add_input(name="mode", interface=IEnumStr({'None':'None','Expanded':'exapanded'}), value=None)
        self.add_input(name="title", interface=IStr, value=None)
        #rodo scatterpoints
        #borderpad          the fractional whitespace inside the legend border
        #    labelspacing       the vertical space between the legend entries
        #    handlelength       the length of the legend handles
        #    handletextpad      the pad between the legend handle and text
        #    borderaxespad      the pad between the axes and legend border
        #    columnspacing      the spacing between columns
        #borderaxespad
        self.add_input(name="prop", interface=IDict, value={})
        #p = pylab.matplotlib.font_manager.FontProperties(size=26)

        self.add_output(name="kwds", interface=IDict, value={})

    def __call__(self, inputs):
        from pylab import legend
        kwds = {}
        # pylab options
        kwds['loc'] = self.get_input('location')
        kwds['numpoints'] = self.get_input('numpoints')
        kwds['loc'] = self.get_input('location')
        kwds['fancybox'] = self.get_input('fancybox')
        kwds['markerscale'] = self.get_input('markerscale')
        kwds['shadow'] = self.get_input('shadow')
        kwds['ncol'] = self.get_input('ncol')
        kwds['mode'] = self.get_input('mode')
        kwds['title'] = self.get_input('title')
        kwds['prop'] = self.get_input('prop')

        axes = self.get_axes()
        for axe in axes:
            axe.legend(**kwds)
            axe.get_figure().canvas.draw()
        return self.get_input('axes')

class PyLabFigure2(Node):
    """pylab.figure interface

    Create figure

    :authors: Thomas Cokelaer
    """
    def __init__(self):
        Node.__init__(self)
        self.add_input(name="axes", interface=ISequence, value=[])
        self.add_input(name="num", interface=IInt, value=1)
        self.add_input(name="figsize", interface=ISequence, value=(8, 6))
        self.add_input(name="dpi", interface=IFloat, value=80.)
        self.add_input(name="facecolor", interface=IEnumStr(colors.keys()), value='white')
        self.add_input(name="edgecolor", interface=IEnumStr(colors.keys()), value='black')
        self.add_input(name="frameon", interface=IBool, value=True)
        self.add_input(name="subplotpars", interface=ISequence, value=None)
        self.add_input(name="kwds", interface=IDict, value={})

        self.add_output(name="kwds", interface=IDict, value={})

    def __call__(self, inputs):
        from pylab import figure
        from copy import deepcopy
        try:
            kwds = self.get_input('kwds')
        except:
            kwds = {}
        kwds['num'] = self.get_input('num')
        kwds['edgecolor']=self.get_input('edgecolor')
        kwds['frameon']=self.get_input('frameon')
        kwds['subplotpars']=self.get_input('subplotpars')

        c = self.get_input('axes')
        if type(c) != list:
            c = [c]
        if len(c) == 0:
            return None


        fignum = c[0].figure.number
        self.fig = figure(fignum)
        self.fig.set_facecolor(self.get_input('facecolor'))
        self.fig.set_edgecolor(self.get_input('edgecolor'))
        self.fig.set_frameon(self.get_input('frameon'))
        self.fig.set_dpi(self.get_input('dpi'))
        self.fig.canvas.draw()
        return self.fig

class PyLabFigure(Node):
    """pylab.figure interface

    Create figure

    :authors: Thomas Cokelaer
    """
    def __init__(self):
        Node.__init__(self)
        self.add_input(name="axes", interface=ISequence, value=[])
        self.add_input(name="num", interface=IInt, value=1)
        self.add_input(name="figsize", interface=ISequence, value=(8, 6))
        self.add_input(name="dpi", interface=IFloat, value=80.)
        self.add_input(name="facecolor", interface=IEnumStr(colors.keys()), value='white')
        self.add_input(name="edgecolor", interface=IEnumStr(colors.keys()), value='black')
        self.add_input(name="kwds", interface=IDict, value={})

        self.add_output(name="kwds", interface=IDict, value={})

    def __call__(self, inputs):
        from pylab import figure
        try:
            kwds = self.get_input('kwds')
        except:
            kwds = {}
        kwds['num'] = self.get_input('num')
        kwds['facecolor']=self.get_input('facecolor')
        kwds['edgecolor']=self.get_input('edgecolor')
        kwds['dpi']=self.get_input('dpi')
        fig = figure(**kwds)
        fig.clf()
        c = self.get_input('axes')
        if type(c) != list:
            c = [c]
        for axe in c:
            fig.add_axes(axe)
        fig.show()
        return fig



class PyLabAxes(Node):
    def __init__(self):
        Node.__init__(self)
        #[left, bottom, width,      height]
        self.add_input(name='left',     interface=IFloat(0, 1, 0.01), value=0.12)
        self.add_input(name='bottom',   interface=IFloat(0, 1, 0.01), value=0.12)
        self.add_input(name='width',    interface=IFloat(0, 1, 0.01), value=0.78)
        self.add_input(name='height',   interface=IFloat(0, 1, 0.01), value=0.78)
        self.add_input(name='axisbg',   interface=IEnumStr(colors.keys()), value='white')
        self.add_input(name='frameon',  interface=IBool, value=True)
        self.add_input(name='polar',    interface=IBool, value=False)
        self.add_input(name='xticks',    interface=IEnumStr(ticks.keys()), value='auto')
        self.add_input(name='yticks',    interface=IEnumStr(ticks.keys()), value='auto')
        self.add_output(name='kwds', interface=IDict, value={})

    def __call__(self, inputs):
        from pylab import axes
        kwds = {}
        kwds['position'] = [self.get_input('left'),  self.get_input('bottom'),
                            self.get_input('width'), self.get_input('height')]
        kwds['axisbg'] = self.get_input('axisbg')
        kwds['frameon'] = self.get_input('frameon')
        kwds['polar'] = self.get_input('polar')
        if self.get_input('xticks')=='None':
            kwds['xticks'] = []
        if self.get_input('yticks')=='None':
            kwds['yticks'] = []
        #    aa = axes(**kwds)
        return kwds

class PyLabAxis(Node):

    def __init__(self):
        Node.__init__(self)
        self.add_input(name='type', interface=IEnumStr(axis.keys()), value='normal')
        self.add_input(name='xmin', interface=IFloat(step=0.1), value=0.)
        self.add_input(name='xmax', interface=IFloat(step=0.1), value=1.)
        self.add_input(name='ymin', interface=IFloat(step=0.1), value=0.)
        self.add_input(name='ymax', interface=IFloat(step=0.1), value=1.)
        self.add_output(name='kwds', interface=IDict, value={})

    def __call__(self, inputs):
        from pylab import axis
        kwds = {}
        kwds['type'] = self.get_input('type')
        kwds['xmin'] = self.get_input('xmin')
        kwds['xmax'] = self.get_input('xmax')
        kwds['ymin'] = self.get_input('ymin')
        kwds['ymax'] = self.get_input('ymax')
        #aa = axes(**kwds)
        return kwds





class PyLabTextOptions(Node):

    def __init__(self):

        Node.__init__(self)
        #self.add_input(name="text", interface=IStr)
        #self.add_input(name="fontdict", interface=IDict, value=None)
        self.add_input(name="fontsize", interface=IFloat, value=12.)
        self.add_input(name="alpha", interface=IFloat(0., 1., step=0.1), value=0.5)
        self.add_input(name="color", interface=IEnumStr(colors.keys()), value='blue')
        self.add_input(name='backgroundcolor', interface=IEnumStr(colors.keys()), value='white')
        self.add_input(name='rotation', interface=IFloat, value='horizontal')
        #self.add_input(name="withdash", interface=IBool, value=False)
        self.add_input(name="kwargs", interface=IDict, value={})
        self.add_input(name="fontproperties", interface=IDict, value={})

        self.add_output(name="kwargs", interface=IDict, value=None)


    def __call__(self, inputs):
        from pylab import text
        from matplotlib.font_manager import FontProperties as FP
        kwds = {}
        #kwds['text'] = self.get_input('text')
        kwds['fontsize'] = self.get_input('fontsize')
        kwds['alpha'] = self.get_input('alpha')
        kwds['color'] = self.get_input('color')
        kwds['backgroundcolor'] = self.get_input('backgroundcolor')
        kwds['rotation'] = self.get_input('rotation')
        kwds['fontproperties'] = FP(**self.get_input('fontproperties'))
        for key, value in self.get_input('kwargs').iteritems():
            try:
                kwds[key] = value
            except:
                print 'key already defined. skip it'
                pass

        #res = text(0,0, self.get_input('text'), **kwds)

        return ( kwds,)

""" 
      animated: [True | False]         
      axes: an :class:`~matplotlib.axes.Axes` instance         
      bbox: rectangle prop dict         
      clip_box: a :class:`matplotlib.transforms.Bbox` instance         
      clip_on: [True | False]    i
 clip_on: [True | False]         
      clip_box: a :class:`matplotlib.transforms.Bbox` instance         
      clip_on: [True | False]         
      clip_path: [ (:class:`~matplotlib.path.Path`,         :class:`~matplotlib.transforms.Transform`) |         :class:`~matplotlib.patches.Patch` | None ]         
      color: any matplotlib color         
      contains: a callable function         
      family or fontfamily or fontname or name: [ FONTNAME | 'serif' | 'sans-serif' | 'cursive' | 'fantasy' | 'monospace' ]         
      figure: a :class:`matplotlib.figure.Figure` instance         
      gid: an id string         
      horizontalalignment or ha: [ 'center' | 'right' | 'left' ]         
      label: any string         
      linespacing: float (multiple of font size)         
      lod: [True | False]         
      multialignment: ['left' | 'right' | 'center' ]         
      picker: [None|float|boolean|callable]         
      rasterized: [True | False | None]         
      rotation_mode: unknown
      size or fontsize: [ size in points | 'xx-small' | 'x-small' | 'small' | 'medium' | 'large' | 'x-large' | 'xx-large' ]         
      snap: unknown
      stretch or fontstretch: [ a numeric value in range 0-1000 | 'ultra-condensed' | 'extra-condensed' | 'condensed' | 'semi-condensed' | 'normal' | 'semi-expanded' | 'expanded' | 'extra-expanded' | 'ultra-expanded' ]         
      style or fontstyle: [ 'normal' | 'italic' | 'oblique']         
      text: string or anything printable with '%s' conversion.         
      transform: :class:`~matplotlib.transforms.Transform` instance         
      url: a url string         
      variant or fontvariant: [ 'normal' | 'small-caps' ]         
      verticalalignment or va or ma: [ 'center' | 'top' | 'bottom' | 'baseline' ]         
      visible: [True | False]         
      weight or fontweight: [ a numeric value in range 0-1000 | 'ultralight' | 'light' | 'normal' | 'regular' | 'book' | 'medium' | 'roman' | 'semibold' | 'demibold' | 'demi' | 'bold' | 'heavy' | 'extra bold' | 'black' ]         
      zorder: any number         
"""


class PyLabPolar(Node):

    def __init__(self):
        Node.__init__(self)
        self.add_input(name="r")
        self.add_input(name="theta")
        self.add_input(name="kwargs", interface = IDict, value = {})
        self.add_output(name="figure")

    def __call__(self, inputs):
        from pylab import polar, show
        kwargs = self.get_input('kwargs')
        fig = polar(self.get_input('r'), self.get_input('theta'), **kwargs)
        show()
        return (fig,)


class PyLabXLabel(Node):
    """VisuAlea version of pylab.xlabel

    :param text:
    :param fontsize:
    :param verticalalignement:
    :param horizontalalignment:
    :param text properties: output of a :class:`TextProperties` Node
    """
    def __init__(self):
        Node.__init__(self)
        self.add_input(name="text", interface=IStr, value=None)
        self.add_input(name="fontsize", interface=IFloat, value=12.)
        self.add_input(name="verticalalignment", interface=IEnumStr(verticalalignment.keys()), value='top')
        self.add_input(name="horizontalalignment", interface=IEnumStr(horizontalalignment.keys()), value='center')
        self.add_input(name="text properties", interface=IDict, value={})

        self.add_output(name='kwargs', interface=IDict, value={})

    def __call__(self, inputs):
        from pylab import xlabel, hold

        kwargs = {}
        kwargs['fontsize'] = self.get_input('fontsize')
        kwargs['verticalalignment'] = self.get_input('verticalalignment')
        kwargs['horizontalalignment'] = self.get_input('horizontalalignment')
        for key, value in self.get_input('text properties').iteritems():
            kwargs[key]=value

        #xlabel(self.get_input('text'), **kwargs)
        kwargs['text'] = self.get_input('text')

        return kwargs

class PyLabYLabel(Node):
    """VisuAlea version of pylab.ylabel

    :param text:
    :param fontsize:
    :param verticalalignement:
    :param horizontalalignment:
    :param text properties: output of a :class:`TextProperties` Node

    """
    def __init__(self):
        Node.__init__(self)
        self.add_input(name="text", interface=IStr, value=None)
        self.add_input(name="fontsize", interface=IFloat, value=12.)
        self.add_input(name="verticalalignment", interface=IEnumStr(verticalalignment.keys()), value='top')
        self.add_input(name="horizontalalignment", interface=IEnumStr(horizontalalignment.keys()), value='center')
        self.add_input(name="text properties", interface=IDict, value={})

        self.add_output(name='kwargs', interface=IDict, value={})

    def __call__(self, inputs):
        from pylab import ylabel, hold

        kwargs = {}
        kwargs['fontsize'] = self.get_input('fontsize')
        kwargs['verticalalignment'] = self.get_input('verticalalignment')
        kwargs['horizontalalignment'] = self.get_input('horizontalalignment')
        for key, value in self.get_input('text properties').iteritems():
            kwargs[key]=value

        #ylabel(self.get_input('text'), **kwargs)
        kwargs['text'] = self.get_input('text')
        return kwargs


class PyLabTitle(Node):

    def __init__(self):
        from matplotlib import font_manager
        Node.__init__(self)
        self.add_input(name="text", interface=IStr, value=None)
        self.add_input(name="fontsize", interface=IFloat, value=12)
        self.add_input(name="color", interface=IEnumStr(colors.keys()), value='black')
        #self.add_input(name="fontproperties", interface=IDict, value=font_manager.FontProperties())
        self.add_input(name='kwargs', interface=IDict, value={})

        self.add_output(name='output', interface=IDict, value={})

    def __call__(self, inputs):
        from pylab import title

        kwargs = {}
        kwargs['fontsize'] = self.get_input('fontsize')
        #kwargs['fontproperties'] = self.get_input('fontproperties')
        kwargs['color'] = self.get_input('color')
        if 'text' in kwargs.keys():
            self.set_input('text', kwargs['text'], notify=True)
        for key, value in self.get_input('kwargs').iteritems():
            kwargs[key]=value

        #print self.get_input('text')
        #print kwargs
        #title(self.get_input('text'), **kwargs)
        kwargs['text'] = self.get_input('text')
        return kwargs







class PyLabFontProperties(Node):

    def __init__(self):
        Node.__init__(self)
        self.add_input(name='family', interface=IEnumStr(families.keys()), value='serif')
        self.add_input(name='style', interface=IEnumStr(styles.keys()), value='normal')
        self.add_input(name='variant', interface=IEnumStr(variants.keys()), value='normal')
        self.add_input(name='weight', interface=IEnumStr(weights.keys()), value='normal')
        self.add_input(name='stretch', interface=IEnumStr(streches.keys()), value='normal')
        self.add_input(name='size', interface=IEnumStr(sizes.keys()), value='medium')
        #todo size could be number, similarly for stretch and weight
        #self.add_input(name='fname', fname=None)
        #self.add_input(name='_init', _init=None)
        #todo style, variant and strethc do not seem to work
        self.add_output(name='kwds', interface=IDict, value={})

    def __call__(self,inputs):
        kwds = {}
        kwds['family'] = self.get_input('family')
        kwds['style'] = self.get_input('style')
        kwds['size'] = self.get_input('size')
        kwds['variant'] = self.get_input('variant')
        kwds['weight'] = self.get_input('weight')
        kwds['stretch'] = self.get_input('stretch')

        return kwds


class PyLabShow(Node):
    """VisuAlea version of pylab.show
    
    Since all plotting nodes call the pylab.show() command, 
    this node is in principle useless. 
    However, it may be used as a common node to connect several 
    plotting nodes.

    :param input: connect whatever you want to be executed
    :param legend: obsolet
    :return:nothing
 
    :author: Thomas Cokelaer
    """
    def __init__(self):
        Node.__init__(self)
        self.add_input(name='input')
        self.add_input(name='legend', interface=IDict, value=None)

    def __call__(self, inputs):
        from pylab import show, legend
        if self.get_input('legend')!=None:
            legend(**self.get_input('legend'))
        show()

class PyLabBox(Node):
    def __init__(self):
        Node.__init__(self)
        self.add_input(name='input')
        self.add_output(name='output')

    def __call__(self, inputs):
        from pylab import box
        box()


class PyLabXLim(Node):
    def __init__(self):
        Node.__init__(self)
        self.add_input(name='xmin', interface=IFloat, value=None )
        self.add_input(name='xmax', interface=IFloat, value=None )
        self.add_output(name='output')

    def __call__(self, inputs):
        from pylab import xlim
        xlim(self.get_input('xmin'), self.get_input('xmax'))

class PyLabYLim(Node):
    def __init__(self):
        Node.__init__(self)
        self.add_input(name='ymin', interface=IFloat, value=None )
        self.add_input(name='ymax', interface=IFloat, value=None )
        self.add_output(name='output')

    def __call__(self, inputs):
        from pylab import ylim
        ylim(self.get_input('ymin'), self.get_input('ymax'))


class PyLabSaveFig(Node):
    """ should include hanning, ...."""
    def __init__(self):
        from matplotlib.pyplot import rcParams
        Node.__init__(self)

        self.add_input(name='fname',        interface=IStr, value=None)
        self.add_input(name='transparent',  interface=IBool, value=False)
        self.add_input(name='dpi',          interface=IInt(40,200,1), value=rcParams['figure.dpi'])
        self.add_input(name='facecolor',    interface=IEnumStr(colors.keys()), value='white')
        self.add_input(name='edgecolor',    interface=IEnumStr(colors.keys()), value='w')
        self.add_input(name='orientation',  interface=IEnumStr(orientation_fig.keys()), value='portrait')
        self.add_input(name='papertype',    interface=IEnumStr(papertypes.keys()), value=None)
        self.add_input(name='format',       interface=IStr, value='png')

    def __call__(self, inputs):
        from pylab import savefig
        kwds = {}
        kwds['dpi'] = self.get_input('dpi')
        kwds['facecolor']=self.get_input('facecolor')
        kwds['edgecolor']= self.get_input('edgecolor')
        kwds['orientation']=self.get_input('orientation')
        kwds['papertype']=self.get_input('papertype')
        kwds['format']=self.get_input('format')
        kwds['transparent']=self.get_input('transparent')
        savefig(self.get_input('fname'), **kwds)



class PyLabColorMap(Node):

    def __init__(self):
        Node.__init__(self)
        self.add_input(name='colormap', interface=IEnumStr(cmaps.keys()), value='jet')
        self.add_input(name='show', interface=IBool, value=False)
        self.add_input(name='showall', interface=IBool, value=False)
        self.add_output(name='output')

    def __call__(self, inputs):
        from numpy import outer, arange, ones
        from pylab import figure, axis, imshow, title, show, subplot, text, clf, subplots_adjust
        maps = self.get_input('colormap')
        a=outer(arange(0,1,0.01),ones(10))

        if self.get_input('showall') is True:
            figure(figsize=(10,5))
            clf()
            l = len(cmaps)
            subplots_adjust(top=0.9,bottom=0.05,left=0.01,right=0.99)
            for index, m in enumerate(cmaps):
                print index
                subplot(int(l/2)+l%2+1, 2, index+1)
                print int(l/2)+l%2, 2, (index+1)/2+(index+1)%2+1
                axis("off")
                imshow(a.transpose(),aspect='auto',cmap=get_cmap(m),origin="lower")
                #title(m,rotation=0,fontsize=10)
                text(0.5,0.5, m)
            show()
        elif self.get_input('show') is True:
            figure(figsize=(10,5))
            clf()
            axis("off")
            imshow(a.transpose(),aspect='auto',cmap=get_cmap(maps),origin="lower")
            title(maps,rotation=0,fontsize=10)
            show()
        res = get_cmap(maps)
        return res


class Windowing(Node):
    """ should include hanning, ...."""
    def __init__(self):
        pass

    def __call__(self, inputs):
        pass

class PyLabColorBar(Node):

    """ should include colornap and colorbar options"""
    def __init__(self):

        Node.__init__(self)
        orientations = {'vertical':'vertical','horizontal':'horizontal'}
        self.add_input(name='orientation', interface=IEnumStr(orientations.keys()), value='vertical')
        self.add_input(name='fraction', interface=IFloat(0.,1,0.01), value=0.15)
        self.add_input(name='pad', interface=IFloat(0.,1,0.01), value=0.05)
        self.add_input(name='shrink', interface=IFloat(0.,1,0.01), value=1)
        self.add_input(name='aspect', interface=IFloat(1,100,0.01), value=20)
        self.add_input(name='drawedges', interface=IBool, value=False)
        self.add_input(name='ticks', interface=ISequence, value=[])
        self.add_input(name='format', interface=IStr, value=None)
        self.add_input(name='label', interface=IStr, value=None)
        self.add_input(name='cmap', interface=IEnumStr, value=None)
        self.add_input(name='show', interface=IBool, value=False)
        self.add_output(name='kwargs', interface=IDict, value={})

    def __call__(self, inputs):
        from pylab import colorbar
        kwds = {}
        kwds['fraction'] = self.get_input('fraction')
        kwds['orientation'] = self.get_input('orientation') #no need for dictionary conversion since key==value
        kwds['pad'] = self.get_input('pad')
        kwds['shrink'] = self.get_input('shrink')
        kwds['aspect'] = self.get_input('aspect')
        kwds['drawedges'] = self.get_input('drawedges')
        if len(self.get_input('ticks'))>0:
            kwds['ticks'] = self.get_input('ticks')
        kwds['format'] = self.get_input('format')

        if self.get_input('show'):
            c = colorbar(**kwds)

        if self.get_input('label') is not None:
            c.set_label(self.get_input('label'))

        return kwds

class PyLabFancyArrowPatch(Node):

    def __init__(self):
        arrowstyles={}
        for x in ['-','->','-[','-|>','<-', '<->','<|-', '<|-|>', 'fancy', 'simple', 'wedge']:
            arrowstyles[x] = x
        ecs = {'none':'none','':''}
        connectionstyles = {}
        for x in ['angle', 'angle3','arc','arc3', 'bar']:
            connectionstyles[x]=x
        Node.__init__(self)
        self.add_input(name='arrowstyle', interface=IEnumStr(arrowstyles.keys()), value='simple')
        self.add_input(name='edgecolor', interface=IEnumStr(colors.keys()), value='none')
        self.add_input(name='connectionstyle', interface=IEnumStr(connectionstyles.keys()), value='arc3')
        self.add_input(name='mutation_scale', interface=IFloat, value=1)
        #todo for connection style, connectionstyle="angle,angleA=0,angleB=-90,rad=10"
        #todo for arrowstyle:head_length=0.4,head_width=0.2 tail_width=0.3,shrink_factor=0.5 
        self.add_output(name='output', interface=IDict)

    def __call__(self, inputs):

        kwds = {}
        kwds['arrowstyle'] = self.get_input('arrowstyle')
        kwds['edgecolor'] = self.get_input('edgecolor')
        kwds['connectionstyle'] = self.get_input('connectionstyle')
        kwds['mutation_scale'] = self.get_input('mutation_scale')

        return kwds

class PyLabYAArow(Node):
    # do not call the class but use its args and kwrags for others like BBox
    def __init__(self):
        Node.__init__(self)
        self.add_input(name='width', interface=IFloat(0,100,0.1), value=4)
        #figure, xytip and xybase are not needed
        self.add_input(name='headwidth', interface=IFloat(0,100,0.1), value=12)
        self.add_input(name='frac', interface=IFloat(0,1,0.05), value=0.1)
        self.add_input(name='alpha', interface=IFloat(0,1,0.05), value=1)
        self.add_input(name='color', interface=IEnumStr(colors.keys()), value='blue')
    
        self.add_output(name='output', interface=IDict, value = {})
    """
      animated: [True | False]         
      antialiased or aa: [True | False]  or None for default         
      clip_path: [ (:class:`~matplotlib.path.Path`,         :class:`~matplotlib.transforms.Transform`) |         :class:`~matplotlib.patches.Patch` | None ]         
      contains: a callable function         
      edgecolor or ec: mpl color spec, or None for default, or 'none' for no color         
      facecolor or fc: mpl color spec, or None for default, or 'none' for no color         
      figure: a :class:`matplotlib.figure.Figure` instance         
      fill: [True | False]         
      gid: an id string         
      hatch: [ '/' | '\\' | '|' | '-' | '+' | 'x' | 'o' | 'O' | '.' | '*' ]         
      label: any string         
      linestyle or ls: ['solid' | 'dashed' | 'dashdot' | 'dotted']         
      linewidth or lw: float or None for default         
      lod: [True | False]         
      picker: [None|float|boolean|callable]         
      rasterized: [True | False | None]         
      snap: unknown
      transform: :class:`~matplotlib.transforms.Transform` instance         
      url: a url string         
      visible: [True | False]         
      zorder: any number         
    """

    def __call__(self, inputs):
        kwds = {}
        kwds['width']= self.get_input('width')
        kwds['headwidth']= self.get_input('headwidth')
        kwds['frac']= self.get_input('frac')
        kwds['alpha']= self.get_input('alpha')
        kwds['color']= self.get_input('color')
        return kwds

class PyLabBBox(Node):

    def __init__(self):
        Node.__init__(self)
        boxstyles = {}
        for x in ['round', 'round4', 'larrow','rarrow','roundtooth', 'sawtooth', 'square']:
            boxstyles[x] = x

        self.add_input(name='boxstyle',interface=IEnumStr(boxstyles.keys()), value='round')
        self.add_input(name='fc',interface=IFloat(0,1,0.1), value=0.8)
        self.add_input(name='pad',interface=IFloat(0,1,0.1), value=0.3)
        self.add_output(name='output', interface=IDict)
        #todo: ec
    def __call__(self, inputs):
        #from pylab import bbox
        kwds = {}
        kwds['boxstyle'] = self.get_input('boxstyle') + ',pad='+str(self.get_input('pad'))
        kwds['fc'] = str(self.get_input('fc'))
        return kwds 

class PyLabAnnotate(Node):


    """ should include colornap and colorbar options"""
    def __init__(self):
        xycoords = {}
        for x in ['figure points', 'figure pixels', 'figure fraction', 'axes points', 'axes pixels', 'axes fraction', 'data', 'offset points', 'polar']:
            xycoords[x]=x
        Node.__init__(self)
        self.add_input(name='text', interface=IStr, value=None)
        self.add_input(name='x target position', interface=IFloat, value=0)
        self.add_input(name='y target position', interface=IFloat, value=0)
        self.add_input(name='x text position', interface=IFloat, value=0)
        self.add_input(name='y text position', interface=IFloat, value=0)
        self.add_input(name='target coords', interface=IEnumStr(xycoords.keys()), value='data')
        self.add_input(name='text coords', interface=IEnumStr(xycoords.keys()), value='data')
        self.add_input(name='arrowprops', interface=IDict, value={'arrowstyle':'->', 'connectionstyle':'arc3', 'rad':.2})
        self.add_input(name='bbox', interface=IDict, value=None)
        self.add_output(name='output')

    """
alpha: float (0.0 transparent through 1.0 opaque)         
      animated: [True | False]         
      axes: an :class:`~matplotlib.axes.Axes` instance         
      backgroundcolor: any matplotlib color         
      clip_box: a :class:`matplotlib.transforms.Bbox` instance         
      clip_on: [True | False]         
      clip_path: [ (:class:`~matplotlib.path.Path`,         :class:`~matplotlib.transforms.Transform`) |         :class:`~matplotlib.patches.Patch` | None ]         
      color: any matplotlib color         
      contains: a callable function         
      family or fontfamily or fontname or name: [ FONTNAME | 'serif' | 'sans-serif' | 'cursive' | 'fantasy' | 'monospace' ]         
      figure: a :class:`matplotlib.figure.Figure` instance         
      fontproperties or font_properties: a :class:`matplotlib.font_manager.FontProperties` instance         
      gid: an id string         
      horizontalalignment or ha: [ 'center' | 'right' | 'left' ]         
      label: any string         
      linespacing: float (multiple of font size)         
      lod: [True | False]         
      multialignment: ['left' | 'right' | 'center' ]         
      picker: [None|float|boolean|callable]         
      position: (x,y)         
      rasterized: [True | False | None]         
      rotation: [ angle in degrees | 'vertical' | 'horizontal' ]         
      rotation_mode: unknown
      size or fontsize: [ size in points | 'xx-small' | 'x-small' | 'small' | 'medium' | 'large' | 'x-large' | 'xx-large' ]         
      snap: unknown
 snap: unknown
      stretch or fontstretch: [ a numeric value in range 0-1000 | 'ultra-condensed' | 'extra-condensed' | 'condensed' | 'semi-condensed' | 'normal' | 'semi-expanded' | 'expanded' | 'extra-expanded' | 'ultra-expanded' ]         
      style or fontstyle: [ 'normal' | 'italic' | 'oblique']         
      text: string or anything printable with '%s' conversion.         
      transform: :class:`~matplotlib.transforms.Transform` instance         
      url: a url string         
      variant or fontvariant: [ 'normal' | 'small-caps' ]         
      verticalalignment or va or ma: [ 'center' | 'top' | 'bottom' | 'baseline' ]         
      visible: [True | False]         
      weight or fontweight: [ a numeric value in range 0-1000 | 'ultralight' | 'light' | 'normal' | 'regular' | 'book' | 'medium' | 'roman' | 'semibold' | 'demibold' | 'demi' | 'bold' | 'heavy' | 'extra bold' | 'black' ]         
      zorder: any number         
    """


    def __call__(self, inputs):
        from pylab import annotate, show
        kwds = {}
        
        s = self.get_input('text')
        xy = [self.get_input('x target position'), self.get_input('y target position')]
        xytext = [self.get_input('x text position'), self.get_input('y text position')]
        xycoords = self.get_input('target coords')
        textcoords = self.get_input('text coords')

        annotate(s, xy, xytext, xycoords=xycoords, textcoords=textcoords, bbox=self.get_input('bbox'), arrowprops=self.get_input('arrowprops'))
        show()
        return None






class PyLabAxhline(Node):
    """VisuAlea version of pylab.axhline

    :param *y*: the y position
    :param *xmin*: starting x position
    :param *xmax*: ending x position
    :param *hold*: True by default
    :param *kwargs Line2D*: connect a Line2D object (optional)

    :returns: pylab.axhline output
    :author: Thomas Cokelaer
    .. todo:: should include colormap and colorbar options

    """
    def __init__(self):
        Node.__init__(self)
        self.add_input(name='y', interface=IFloat, value=0.5)
        self.add_input(name='xmin', interface=IFloat, value=0.5)
        self.add_input(name='xmax', interface=IFloat, value=1)
        self.add_input(name='hold', interface=IBool, value=True)
        self.add_input(name='kwargs (Line2D)', interface=IDict, value={})
        self.add_output(name='output')

    def __call__(self, inputs):
        from pylab import axhline, Line2D
        kwds = {}
        kwds = get_kwds_from_line2d(self.get_input('kwargs (Line2D)'), kwds) 
        res = axhline(self.get_input('y'), xmin=self.get_input('xmin'),
                xmax=self.get_input('xmax'), hold=self.get_input('hold'),
                **kwds)
        return res

class PyLabAxvline(Node):
    """VisuAlea version of pylab.axvline

    :param *x*: the y position
    :param *ymin*: starting x position
    :param *ymax*: ending x position
    :param *hold*: True by default
    :param *kwargs Line2D*: connect a Line2D object (optional)

    :returns: pylab.axhline output
    :author: Thomas Cokelaer

    .. todo:: should include colormap and colorbar options
    """
    def __init__(self):
        Node.__init__(self)
        self.add_input(name='x', interface=IFloat, value=0.5)
        self.add_input(name='ymin', interface=IFloat, value=0)
        self.add_input(name='ymax', interface=IFloat, value=0.5)
        self.add_input(name='hold', interface=IBool, value=True)
        self.add_input(name='kwargs (Line2D)', interface=IDict, value={})
        self.add_output(name='output')

    def __call__(self, inputs):
        from pylab import axvline
        kwds = {}
        kwds = get_kwds_from_line2d(self.get_input('kwargs (Line2D)'), kwds) 
        res = axvline(self.get_input('x'), ymin=self.get_input('ymin'),
                ymax=self.get_input('ymax'), hold=self.get_input('hold'),
                **kwds)
        return res

class PyLabAxhspan(Node):
    """VisuAlea version of pylab.axvspan

    :param *ymin*: starting y position
    :param *ymax*: ending y position
    :param *xmin*: starting x position
    :param *xmax*: ending x position
    :param *hol*: True by default
    :param *kwargs Patch*: connect a Patch object (optional)

    :returns: pylab.axhspan output
    :author: Thomas Cokelaer

    .. todo:: should include colormap and colorbar options
    """
    def __init__(self):
        Node.__init__(self)
        self.add_input(name='ymin', interface=IFloat, value=0)
        self.add_input(name='ymax', interface=IFloat, value=0.5)
        self.add_input(name='xmin', interface=IFloat, value=0)
        self.add_input(name='xmax', interface=IFloat, value=1)
        self.add_input(name='hold', interface=IBool, value=True)
        self.add_input(name='kwargs (Patch)', interface=IDict, value={})
        self.add_output(name='output')

    def __call__(self, inputs):
        from pylab import axhspan
        print self.get_input('kwargs (Patch)')
        res = axhspan(self.get_input('ymin'), self.get_input('ymax'), xmin=self.get_input('xmin'),
                xmax=self.get_input('xmax'), **self.get_input('kwargs (Patch)'))
        return res

class PyLabAxvspan(Node):
    """VisuAlea version of pylab.axvspan

    :param *xmin*: starting x position
    :param *xmax*: ending x position
    :param *ymin*: starting y position
    :param *ymax*: ending y position
    :param *hol*: True by default
    :param *kwargs Patch*: connect a Patch object (optional)

    :returns: pylab.axvspan output

    :author: Thomas Cokelaer
    .. todo:: should include colormap and colorbar options
    """
    def __init__(self):
        Node.__init__(self)
        self.add_input(name='xmin', interface=IFloat, value=0)
        self.add_input(name='xmax', interface=IFloat, value=0.5)
        self.add_input(name='ymin', interface=IFloat, value=0)
        self.add_input(name='ymax', interface=IFloat, value=1)
        self.add_input(name='hold', interface=IBool, value=True)
        self.add_input(name='kwargs (Patch)', interface=IDict, value={})
        self.add_output(name='output')

    def __call__(self, inputs):
        from pylab import axvspan
        print self.get_input('kwargs (Patch)')
        res = axvspan(self.get_input('xmin'), self.get_input('xmax'), ymin=self.get_input('ymin'),
                ymax=self.get_input('ymax'), **self.get_input('kwargs (Patch)'))
        return res



class PyLabXTicks(Node):
    """VisuAlea version of pylab.xticks


    :author: Thomas Cokelaer
    """
    def __init__(self):
        Node.__init__(self)
        self.add_input(name='locs', interface=ISequence, value=None)
        self.add_input(name='labels', interface=ISequence, value=None)
        self.add_input(name='text properties', interface=IDict, value={})
        self.add_output(name='output')

    def __call__(self, inputs):
        from pylab import xticks
        kwds = {}
        for key, value in self.get_input('text properties').iteritems():
            kwds[key] = value
        del kwds['fontsize']
        print kwds
        if self.get_input('locs') and self.get_input('labels'):
            res = xticks(self.get_input('locs'), self.get_input('labels'), **kwds)
        elif self.get_input('locs'):
            res = xticks(self.get_input('locs'),  **kwds)
        else:
            res = xticks(**kwds)
        return res

class PyLabYTicks(Node):

    """Does not work yet"""
    def __init__(self):
        Node.__init__(self)
        self.add_input(name='locs', interface=ISequence, value=None)
        self.add_input(name='labels', interface=ISequence, value=None)
        self.add_input(name='text properties', interface=IDict, value={})
        self.add_output(name='output')

    def __call__(self, inputs):
        from pylab import yticks
        kwds = {}
        for key, value in self.get_input('text properties').iteritems():
            kwds[key] = value
        del kwds['fontsize']
        print kwds
        if self.get_input('locs') and self.get_input('labels'):
            res = yticks(self.get_input('locs'), self.get_input('labels'), **kwds)
        elif self.get_input('locs'):
            res = yticks(self.get_input('locs'),  **kwds)
        else:
            res = yticks(**kwds)
        return res


class PyLabGrid(Node, CustomizeAxes):
    which = {'major':'major','minor':'minor', 'both':'both'}
    def __init__(self):
        Node.__init__(self)
        CustomizeAxes.__init__(self)

        self.add_input(name='axes')
        self.add_input(name='b', interface=IBool, value=True)
        self.add_input(name='which', interface=IEnumStr(PyLabGrid.which.keys()), value='major')
        self.add_input(name='linestyle', interface=IEnumStr(linestyles.keys()),   value='dotted')
        self.add_input(name='color', interface=IEnumStr(colors.keys()),   value='black')
        self.add_input(name='linewidth', interface=IFloat, value=1.0)
        self.add_input(name='kwargs', interface=IDict, value={})

        self.add_output(name='axes')

    def __call__(self, inputs):
        kwds = {}
        for key, value in self.get_input('kwargs').iteritems():
            kwds[key] = value
        kwds['linestyle']=linestyles[self.get_input("linestyle")]
        kwds['color']=colors[self.get_input("color")]
        kwds['linewidth']=self.get_input("linewidth")
        kwds['b']=self.get_input("b")
        kwds['which']=self.get_input("which")

        axes = self.get_axes()
        for axe in axes:
            axe.grid(**kwds)
            axe.get_figure().canvas.draw()
        return self.get_input('axes')


class PyLabOrigin(Node):

    def __init__(self):
        Node.__init__(self)
        self.add_input(name='origin', interface=IEnumStr(origins), value=None)
        self.add_output(name='output', interface=IDict, value={})

    def __call__(self, inputs):
        kwds = {}
        kwds['origin'] = self.get_input('origin') 
        return (kwds ,)


class PyLabAxes2(Node):
    def __init__(self):
        Node.__init__(self)
        #[left, bottom, width,      height]
        self.add_input(name='input')
        self.add_input(name='clear', interface=IBool, value=True)
        self.add_input(name='left',     interface=IFloat(0, 1, 0.01), value=0.12)
        self.add_input(name='bottom',   interface=IFloat(0, 1, 0.01), value=0.12)
        self.add_input(name='width',    interface=IFloat(0, 1, 0.01), value=0.78)
        self.add_input(name='height',   interface=IFloat(0, 1, 0.01), value=0.78)
        self.add_input(name='axisbg',   interface=IEnumStr(colors.keys()), value='white')
        self.add_input(name='frameon',  interface=IBool, value=True)
        self.add_input(name='polar',    interface=IBool, value=False)
        self.add_input(name='xscale',    interface=IEnumStr(scale.keys()), value='linear')
        self.add_input(name='yscale',    interface=IEnumStr(scale.keys()), value='linear')
        self.add_input(name='xticks',    interface=IEnumStr(ticks.keys()), value='auto')
        self.add_input(name='yticks',    interface=IEnumStr(ticks.keys()), value='auto')
        self.add_input(name='kwargs',    interface=IDict, value={})
        self.add_output(name='axes', interface=IDict, value={})

        self.axe = None

    def __call__(self, inputs):
        from pylab import axes, gcf
        kwds = {}
        position = [self.get_input('left'),  self.get_input('bottom'),
                            self.get_input('width'), self.get_input('height')]
        if self.get_input('xticks')=='None':
            kwds['xticks'] = []
        if self.get_input('yticks')=='None':
            kwds['yticks'] = []

        input_axes = self.get_input('input')

        # case of an empty input, we need to create the axes if it does not exist, or clean the existing one.
        if input_axes == None:
            print 'Axes2: input axes is none'
            #this command return the current axe if it exist otherwise it creates a new one
            input_axes = axes(position, polar=self.get_input('polar'))
            if self.get_input('clear')==True:
                input_axes.clear()
            input_axes.set_axis_bgcolor(self.get_input('axisbg'))
            input_axes.set_frame_on(self.get_input('frameon'))
            input_axes.set_xscale(self.get_input('xscale'))
            input_axes.set_yscale(self.get_input('yscale'))
            f = input_axes.get_figure()
            f.canvas.draw()
            return input_axes

        #else
        print 'Axes2: input axes is not none'
        if type(input_axes)!=list: input_axes = [input_axes]

        for axe in input_axes:
            axe.set_position(position)
            axe.set_axis_bgcolor(self.get_input('axisbg'))
            axe.set_frame_on(self.get_input('frameon'))
            axe.set_xscale(self.get_input('xscale'))
            axe.set_yscale(self.get_input('yscale'))
        f = gcf()
        f.canvas.draw()

        return input_axes
