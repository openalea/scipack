###############################################################################
# -*- python -*-
#
#       Copyright or (C) or Copr. 2010 INRIA - CIRAD - INRA
#
#       File author(s): Thomas Cokelaer <Thomas.Cokelaer@sophia.inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################

__doc__="""pylab plotting nodes"""

__revision__ = " $Revision$ "
__author__ = "$Author$"
__date__ = "$Date$"

#//////////////////////////////////////////////////////////////////////////////


from openalea.core import Node
from openalea.core import Factory, IFileStr, IInt, IBool, IFloat, \
    ISequence, IEnumStr, IStr, IDirStr, ITuple3, IDict

from openalea.core.external import add_docstring

from openalea.pylab import tools


#sides = { 'default':'default',  'onesided':'onesided',  'twosided':'twosided' }



class Plotting(Node):
    """This class provides common connector related to decorate a figure or axes.

    It is a base class to all Plotting nodes so that they inherits from the Node class, 
    and get common connectors:

        * label
        * colorbar


    It also guarantee to have at least 1 output defined within each Plotting nodes.

    :author: Thomas Cokelaer
    """
    ERROR_NOXDATA = 'No data connected to the x connector. Connect a line2D, an array or a list of line2Ds or arrays'
    ERROR_FAILURE = 'Failed to generate the image. check your entries.'

    def __init__(self,  inputs={}):
        Node.__init__(self)
        self._title = None
        self._ylabel = None
        self._xlabel = None
        self.axe = None
        self.fig = None

        self.add_input(name="axes")
        for input in inputs:
            self.add_input(**input)

        self.add_input(name="figure", interface=IInt(1,100,1), value=1)

        self.add_output(name='axes')

    def figure(self):
        """call figure()"""
        from pylab import figure
        assert type(self.get_input('figure')) == int
        if self.fig == None:
            fig = figure(self.get_input('figure'))
            #print 'new figure created ', self.get_input('figure')
            self.fig = fig
        else:
            fig = figure(self.get_input('figure'))
            if fig == self.fig:
                #print 'figure exist already, nothing to do'
                pass
            else:
                print 'figure not found. Maybe it was closed !!! consider reloading this node.'
                
                self.fig = fig
                del self.axe
                self.axe = None
                #raise ValueError('figure not found. Maybe it was closed !!! consider reloading this node.')

        return self.fig

    #def legend(self):
    #    args = self.get_input('legend')
    #    if type(args)==bool:
    #        if args:
    #            self.axe.legend()
    #    else:
    #        self.axe.legend(**args)
    def axes(self):



        #sometimes, we want to add data to existing axe provided as an input argument. In such case, we do not want to clean
        # the axe and create a new one.
        if self.get_input('axes') != None:
            print 'Input axes found. Using it (%s)'  % self.get_input('axes')
            axes = self.get_input('axes')
            import matplotlib
            assert axes.__module__ in [matplotlib.axes.__name__,matplotlib.projections.polar.__name__], 'input must be a valid axes from matplotlib.axes %s given for %s' % (type(axes), axes)
            self.axe = axes
            self.axe.hold(True)
            return
        #if an axe already exist, no need to create a new one: we simply clean it
        if self.axe:
            from pylab import sca, cla
            print 'No input axe, but axes already set. Clear it. %s' % self.axe, self.axe.__str__
            #set the current axe to be axe of the node currently run
            #sca(self.axe)
            self.axe.clear()
            self.axe.get_figure().canvas.draw()
            sca(self.axe)
        #else, we need to create a new axe. Note, the use of label. Indeed, if same position is used, and same default label then
        # no new axes is created. See add_axes help. Our label is the number of axes.
        else:
            print 'No input axe and not axes set. Creating a new one.'
            label='axe' + str(len(self.fig.get_axes()))
            self.axe = self.fig.add_axes([.1,.1,.8,.8], label=label)


    def properties(self):
        """This is an alias method that calls legend, title, xlabel, ylabel, 
        grid, colorbar and show"""
        #self.legend()
        self.fig.canvas.draw()
        self.fig.show()




class PlotxyInterface():
    """A base class common to some plotting functions

    The plotting functions that uses this base class are:

        * plot
        * loglog
        * semilogx, semilogy
        * csd, psd, specgram
        * stem
        * step
        * fill

    They are plotting x data or x verus y data.

    This is used to manage the different possible x and y inputs.

    See :class:`PyLabPlot` for more explanation.

    It inherits from :class:`Colors`, :class:`LineStyles` and :class:`Markers` so that if there are 
    several inputs a basic combination of different colors and line styles are used.

    For more tunable colors and line styles, use the :class:`Line2D` convertor before passing 
    the data to a node.

    """
    ERROR_NOXDATA = 'No data connected to the x connector. Connect a line2D, an array or a list of line2Ds or arrays'
    ERROR_FAILURE = 'Failed to generate the image. check your entries.'

    def __init__(self):
        pass


    def call(self, plottype, kwds):
        """Function used to call the plot specified by`plottype`

        :param plottype: must be one of plot, loglog, semilogx, semilogy, csd, psd, specgram, step, stem, fill

        if several x are provided, different colors will be used for the markers cycling over the available :class:`Colors`
        """
        from pylab import hold, Line2D
        if plottype=='plot':
            from pylab import plot as plot
        elif plottype=='loglog':
            from pylab import loglog as plot
        elif plottype=='semilogx':
            from pylab import semilogx as plot
        elif plottype=='semilogy':
            from pylab import semilogy as plot
        elif plottype=='csd':
            from pylab import csd as plot
        elif plottype=='psd':
            from pylab import psd as plot
        elif plottype=='specgram':
            from pylab import specgram as plot
        elif plottype=='stem':
            from pylab import stem as plot
        elif plottype=='step':
            from pylab import step as plot
        elif plottype=='fill':
            from pylab import fill as plot
        elif plottype=='hist':
            from pylab import hist as plot

        xinputs = self.get_input("x")
        yinputs = self.get_input("y")

        # convert x and y inputs into lists
        if xinputs == None:
            raise ValueError(self.ERROR_NOXDATA)
        if type(xinputs)!=list:
            xinputs = [xinputs]
        if type(yinputs)!=list:
            yinputs = [yinputs]

        # case of an x input without y input. line2D are all manage in this if statement
        if yinputs[0]==None:
            #plot(line2D) and plot([line2D, line2D])
            if type(xinputs[0])==Line2D:
                for x in xinputs:
                    print kwds
                    line2dkwds = tools.get_kwds_from_line2d(line2d=x, input_kwds=kwds, type=plottype)
                    print line2dkwds
                    #returns the processed data ?
                    if plottype in ['specgram', 'psd']:
                        plot(x.get_ydata(orig=False), **line2dkwds)
                    else:
                        try:
                            plot(x.get_xdata(orig=False), x.get_ydata(orig=False), **line2dkwds)
                        except:
                            print kwds
                            print line2dkwds
                    hold(True)
            #plot([x1,None,x2,None, ...) and plot(x1)
            else:
                c = enumerate(tools.colors)
                for x in xinputs:
                    try:
                        color = c.next()
                        kwds['color']=color[1]
                    except:
                        print 'no more colors'
                    try:
                        plot(x, **kwds)
                    except:
                        raise ValueError("plot failed")
                    self.axe.hold(True)

        else:
            if len(xinputs)==1 and len(yinputs)!=1:
                # plot(x,y) and plot(x, [y1,y2])
                c = enumerate(tools.colors)
                for y in yinputs:
                    try:
                        color = c.next()
                        kwds['color']=color[1]
                    except:
                        print 'no more colors'
                    try:
                        plot(xinputs[0], y, **kwds)
                    except:
                        raise ValueError("plot failed")
                    self.axe.hold(True)
            else:
                if len(xinputs)!=len(yinputs):
                    print 'warning more x inputs than y inputs. correct the connectors'
                # plot([x1,x2], [y1,y2])
                # plot([x1], [y1])
                for x,y in zip(xinputs, yinputs):
                    try:
                        plot(x, y, **kwds)
                    except:
                        raise ValueError("plot failed")
        pass


class PyLabPlot(Plotting, PlotxyInterface):
    """VisuAlea version of pylab.plot

    The x connector must be connected. It must be in one of the following format:

        * a 1-D array.
            * If nothing is connected to `y`, then `x` is used as `y` (similarly to pylab.plot behaviour)
            * A 1-D array of same length may be connected to `y`.
            * Several 1-D arrays of same length as `x` may be connected to `y`. Therefore, 
              these arrays have the same `x` data
        * a Line2D object (see :ref:`Line2D`). `y` must  be empty in such case.
        * a list of Line2D objects. `y` must be empty in such case

    In order to customize the input data at will, it is necesserary to convert the xy data into a 
    :class:`PyLabLine2D` object and to pass it to the `x` connector. In such case, the y connector
    becomes useless.

    :param x: either an array or a PyLabLine2D object or a list of PyLabLine2D objects.
    :param y: either an array or list of arrays
    :param marker: circle marker by default
    :param markersize: marker size  (float, default=10)
    :param linestyle: solid line by default (default=solid)
    :param color: (default=blue)

    :return: the axes in which the data are plotted.

    :authors: Thomas Cokelaer
    """
    def __init__(self):
        PlotxyInterface.__init__(self)
        inputs = [
                    {'name':'x',          'interface':None,                           'value':None},
                    {'name':'y',          'interface':None,                           'value':None},
                    {'name':'marker',     'interface':IEnumStr(tools.markers.keys()),  'value':'circle'},
                    {'name':'markersize', 'interface':IFloat,                         'value':10},
                    {'name':'linestyle',  'interface':IEnumStr(tools.linestyles.keys()),    'value':'solid'},
                    {'name':'color',      'interface':IEnumStr(tools.colors.keys()),   'value':'blue'},
                    {'name':'scalex',     'interface':IBool, 'value':True},
                    {'name':'scaley',     'interface':IBool, 'value':True},
        ]
        Plotting.__init__(self, inputs)
        self.add_input(name='kwargs', interface=IDict, value={'label':None})

    def __call__(self, inputs):
        print 'Calling PyLabPlot'

        #todo label must be cast into string
        kwds = {}
        for key,value in self.get_input('kwargs').iteritems():
            kwds[key] = value
        kwds['markersize']=self.get_input("markersize")
        kwds['marker']=tools.markers[self.get_input("marker")]
        kwds['linestyle']=tools.linestyles[self.get_input("linestyle")]
        kwds['color']=tools.get_valid_color(self.get_input("color"))
        kwds['scaley']=self.get_input("scaley")
        kwds['scalex']=self.get_input("scalex")
        print kwds
        self.figure()
        self.axes()
        self.call('plot', kwds)
        self.properties()

        return self.axe



class PyLabLogLog(Plotting, PlotxyInterface):
    """VisuAlea version of pylab.loglog

    see :class:`PyLabPlot` documentation

    :Author: Thomas Cokelaer
    """

    def __init__(self):
        self.__doc__ = PyLabPlot.__doc__
        PlotxyInterface.__init__(self)
        inputs = [
                    {'name':'x',            'interface':None,                           'value':None},
                    {'name':'y',            'interface':None,                           'value':None},
                    {'name':'marker',       'interface':IEnumStr(tools.markers.keys()),       'value':'circle'},
                    {'name':'markersize',   'interface':IFloat,                         'value':10},
                    {'name':'linestyle',    'interface':IEnumStr(tools.linestyles.keys()),    'value':'solid'},
                    {'name':'color',        'interface':IEnumStr(tools.colors.keys()),        'value':'blue'},
        ]
        Plotting.__init__(self, inputs)

    def __call__(self, inputs):
        from pylab import cla

        self.figure()
        self.axes(
        #todo label must be cast into strinca
)
        cla()
        kwds = {}
        kwds['markersize']=self.get_input("markersize")
        kwds['marker']=tools.markers[self.get_input("marker")]
        kwds['linestyle']=tools.linestyles[self.get_input("linestyle")]
        kwds['color']=tools.colors[self.get_input("color")]

        self.call('loglog', kwds)
        self.properties()
        return self.axes_shown

class PyLabSemiLogy(Plotting, PlotxyInterface):
    """VisuAlea version of pylab.semilogy

    see :class:`PyLabPlot` documentation

    :Author: Thomas Cokelaer
    """
    def __init__(self):
        self.__doc__ = PyLabPlot.__doc__
        PlotxyInterface.__init__(self)
        inputs = [
                    {'name':'x',            'interface':None,                           'value':None},
                    {'name':'y',            'interface':None,                           'value':None},
                    {'name':'marker',       'interface':IEnumStr(tools.markers.keys()),       'value':'circle'},
                    {'name':'markersize',   'interface':IFloat,                         'value':10},
                    {'name':'linestyle',    'interface':IEnumStr(tools.linestyles.keys()),    'value':'solid'},
                    {'name':'color',        'interface':IEnumStr(tools.colors.keys()),        'value':'blue'},
        ]
        Plotting.__init__(self, inputs)

    def __call__(self, inputs):
        from pylab import cla

        self.figure()
        self.axes()
        cla()
        kwds = {}
        kwds['markersize']=self.get_input("markersize")
        kwds['marker']=tools.markers[self.get_input("marker")]
        kwds['linestyle']=tools.linestyles[self.get_input("linestyle")]
        kwds['color']=tools.colors[self.get_input("color")]

        self.call('semilogy', kwds)
        self.properties()
        return self.axes_shown

class PyLabSemiLogx(Plotting, PlotxyInterface):
    """VisuAlea version of pylab.semilogx

    see :class:`PyLabPlot` documentation

    :Author: Thomas Cokelaer
    """
    def __init__(self):
        self.__doc__ = PyLabPlot.__doc__
        PlotxyInterface.__init__(self)
        inputs = [
                    {'name':'x',            'interface':None,                           'value':None},
                    {'name':'y',            'interface':None,                           'value':None},
                    {'name':'marker',       'interface':IEnumStr(tools.markers.keys()),       'value':'circle'},
                    {'name':'markersize',   'interface':IFloat,                         'value':10},
                    {'name':'linestyle',    'interface':IEnumStr(tools.linestyles.keys()),    'value':'solid'},
                    {'name':'color',        'interface':IEnumStr(tools.colors.keys()),        'value':'blue'},
        ]
        Plotting.__init__(self, inputs)

    def __call__(self, inputs):
        from pylab import cla

        self.figure()
        self.axes()
        cla()
        kwds = {}
        kwds['markersize']=self.get_input("markersize")
        kwds['marker']=tools.markers[self.get_input("marker")]
        kwds['linestyle']=tools.linestyles[self.get_input("linestyle")]
        kwds['color']=tools.colors[self.get_input("color")]

        self.call('semilogy', kwds)
        self.properties()
        return self.axes_shown


class PyLabHist(Plotting):
    """pylab.hist interface

    :param x: the input data (1D array)
    :param bins: binning number (default is 10)
    :param facecolor: blue by default
    :param normed: normalised histogram (False by default)
    :param cumulative: cumulated histogram (False by default)
    :param histtype: (bar, step, stepfilled, etc) 
    :param alignment: (bar, step, stepfilled, etc) 
    :param orientation: horizontal or vertical (default is vertical)
    :param log: logarithmic scale (default is False)
    :param label: a text label

    :returns: axes object

    .. todo::

        range=None
        bottom=None,
        rwidth=None,

    :authors: Thomas Cokelaer
    """

    def __init__(self):

       
        inputs = [
            {'name':'x'},
            {'name':'bins',         'interface':IInt, 'value':10},
            {'name':'facecolor',    'interface':IEnumStr(tools.colors.keys()), 'value':'blue'},
            {'name':'normed',       'interface':IBool, 'value':False},
            {'name':'cumulative',   'interface':IBool, 'value':False},
            {'name':'histtype',     'interface':IEnumStr(tools.histtype.keys()), 'value':'bar'},
            {'name':'align',        'interface':IEnumStr(tools.align.keys()), 'value':'mid'},
            {'name':'orientation',  'interface':IEnumStr(tools.orientations.keys()), 'value':'vertical'},
            {'name':'log',          'interface':IBool,  'value':False},
            {'name':'label',          'interface':IStr,  'value':''}
        ]
        Plotting.__init__(self, inputs)

        #self.add_input(name="range", interface = ITuple3, value = None)
        #rectangle
        self.add_input(name="kwargs", interface = IDict, value={'alpha':1., 'animated':False})

        self.add_output(name="axes")
        
        self.add_output(name="position")
        self.add_output(name="counts")
        """
          antialiased or aa: [True | False]  or None for default         
          axes: an :class:`~matplotlib.axes.Axes` instance         
          clip_box: a :class:`matplotlib.transforms.Bbox` instance         
          clip_on: [True | False]         
          clip_path: [ (:class:`~matplotlib.path.Path`,         :class:`~matplotlib.transforms.Transform`) |         :class:`~matplotlib.patches.Patch` | None ]         
          contains: a callable function         
          edgecolor or ec: mpl color spec, or None for default, or 'none' for no color         
          fill: [True | False]         
          gid: an id string         
          hatch: [ '/' | '\\' | '|' | '-' | '+' | 'x' | 'o' | 'O' | '.' | '*' ]         
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
        from pylab import cla, hold, hist, Line2D
        self.figure()
        self.axes()
        #cla()
        kwds={}
        kwds['bins']=self.get_input("bins")
        kwds['normed']=self.get_input("normed")
        kwds['facecolor']=tools.get_valid_color(self.get_input("facecolor"))
        kwds['label']=self.get_input("label")
        kwds['log']=self.get_input("log")
        kwds['orientation']=tools.orientations[self.get_input("orientation")]
        kwds['figure']=self.get_input("figure")
        kwds['histtype']=tools.histtype[self.get_input("histtype")]
        kwds['align']=tools.align[self.get_input("align")]
        kwds['cumulative']=self.get_input("cumulative")
        #!! facecolor is alrady in the Hist node, so override it if available in kwargs dict
        for key,value in self.get_input('kwargs').iteritems():
            kwds[key] = value

        xinputs = self.get_input('x')
        if type(xinputs)!=list:
            xinputs = [xinputs]
        try:
            for x in xinputs:
                if type(x)==Line2D:
                    line2dkwds = tools.get_kwds_from_line2d(x, kwds, type='hist')
                    res = self.axe.hist(x.get_ydata(orig=False),**line2dkwds)
                else:
                    res = self.axe.hist(x,**kwds)
            hold(True)
        except ValueError, e:
            res = (None, None)
            print e
            raise ValueError('tttt')

        hold(False)
        self.properties()
        return (self.axe,res, res[1],res[0])


class PyLabAcorr(Plotting):
    """pylab.acorr interface

     Plot the autocorrelation of x. If normed = True, normalize
     the data by the autocorrelation at 0-th lag. x is detrended
     by the detrend callable (default no normalization).

    :param x: the input data
    :param normed: True
    :param detrend:
    :param usevlines:
    :param maxlags:
    :param xlabel: none by default
    :param ylabel: none by default
    :param title: none by default

    .. todo:: finalise doc and function
    :authors: Thomas Cokelaer
    """

    def __init__(self):
        inputs = [
                    {'name':'x', 'interface':None, 'value':None},
                    {'name':"maxlags",   'interface':IInt,  'value':10},
                    {'name':"normed",    'interface':IBool, 'value':False},
                    {'name':"usevlines", 'interface':IBool, 'value':True},
                    {'name':'detrend', 'interface':IEnumStr(tools.detrends.keys()), 'value':'none'},
                    {'name':"kwargs",    'interface':IDict, 'value':{}}
                ]
        Plotting.__init__(self, inputs)

    def __call__(self, inputs):
        from pylab import clf, hold, acorr, Line2D, cla
        import pylab
        self.figure()
        self.axes()
        cla()
        x = self.get_input("x")

        kwds = {}
        kwds['maxlags'] = self.get_input("maxlags")
        kwds['normed'] = self.get_input("normed")
        kwds['usevlines'] = self.get_input("usevlines")
        kwds['detrend'] = getattr(pylab, 'detrend_'+self.get_input('detrend'))

        res = None
        xinputs=self.get_input('x')
        if type(xinputs)!=list:
            xinputs = [xinputs]

        #line2dkwds = get_kwds_from_line2d(x, self.get_input('kwargs'), type='linecollection')
        #returns the processed data ?
        for x in xinputs:
            res =  acorr(x, **kwds)
            hold(True)
        self.properties()
        return self.axes_shown

        return res



#//////////////////////////////////////////////////////////////////////////////






class PyLabScatter(Plotting):
    """VisuAlea version of pylab.scatter

    create a scatter plot of the x-y input data


    :param x: a x-data array
    :param y: a y-data array
    :param label: None by default
    :param marker: circle marker by default
    :param linestyle: solid line by default
    :param color: blue by default
    :param xlabel: none by default
    :param ylabel: none by default
    :param title: none by default

    :return: the axes object

    .. todo:: deal with several multiple x-y data sets (e.g., line 2D?)
    
    .. todo:: add vmin/vmax, cmap

    :author: Thomas Cokelaer
    """
    def __init__(self):
        inputs = [
            {'name':'x',        'value':None},
            {'name':'y',        'value':None},
            {'name':'sizes',    'value':20},
            {'name':"color",    'interface':IEnumStr(tools.colors.keys()),  'value':'blue'},
            {'name':"marker",   'interface':IEnumStr(tools.markers.keys()), 'value' : 'circle'},
            {'name':"label",    'interface':IStr,       'value':None},
            {'name':"alpha",    'interface':IFloat,     'value' : 0.5},
        ]

        Plotting.__init__(self, inputs)


    def __call__(self, inputs):
        from pylab import scatter, cla
        x = self.get_input("x")
        y = self.get_input("y")
        sizes = self.get_input("sizes")
        color = tools.get_valid_color(self.get_input("color"))
        self.figure()
        self.axes()
        cla()
        res = scatter(x,y, s=sizes,c=color,
                marker=tools.markers[self.get_input("marker")],
                alpha=self.get_input("alpha"),
                label=self.get_input("label"))
        self.properties()
        return self.axes_shown




class PyLabBoxPlot(Plotting):
    """pylab.boxplot interface

    :param x: data
    :parma notch: (default 0)
    :param sym: '+'
    :param  vert: 1
    :param  whis: 1.5,
    :param  positions: None
    :param widths:None

    :authors: Thomas Cokelaer

    """
    def __init__(self):
        inputs = [
            {'name':"x"},
            {'name':"notch",    'interface':IInt, 'value':0},
            {'name':"sym",      'interface':IEnumStr(tools.markers.keys()), 'value':'circle'},
            {'name':"vert",     'interface':IInt,  'value':1},
        ]
        Plotting.__init__(self, inputs)
        #self.__doc__+=plot.__doc__

    def __call__(self, inputs):
        x = self.get_input("x")
        from pylab import boxplot, cla, hold
        self.figure()
        self.axes()
        cla()
        res = boxplot(x, 
                sym=tools.markers[self.get_input("sym")],
                vert=self.get_input("vert"),
                notch=self.get_input("notch"))
        self.properties()
        return self.axes_shown
        return res



class PyLabLine2D(Node):
    """todo"""
    def __init__(self):
        Node.__init__(self)

        self.add_input(name="xdata", value=[])
        self.add_input(name="ydata", value=[])
        self.add_input(name="linestyle", interface=IEnumStr(tools.linestyles.keys()), value='solid')
        self.add_input(name="color", interface=IEnumStr(tools.colors.keys()),value='blue')
        self.add_input(name="marker", interface=IEnumStr(tools.markers.keys()),value='circle')
        self.add_input(name="markersize", interface=IInt, value=10)
        self.add_input(name="markeredgewidth", interface=IFloat(0.,10,0.1) , value=None)
        self.add_input(name="markeredgecolor", interface=IEnumStr(tools.colors.keys()), value='None')
        self.add_input(name="linewidth", interface=IFloat, value=1.)
        self.add_input(name="fillstyle", interface=IEnumStr(tools.fillstyles), value='full')
        self.add_input(name="label", interface=IStr, value=None)
        self.add_input(name="alpha", interface=IFloat(0.,1., step=0.1), value=1.0)
        self.add_input(name="kwargs", interface=IDict, value={})

        self.add_output(name="line2d")

    def __call__(self, inputs):
        from pylab import Line2D

        kwds = {}
        for key, value in self.get_input('kwargs').iteritems():
            kwds[key] = value

        xdata=self.get_input('xdata')
        ydata=self.get_input('ydata')
        #why?
        if ydata == None or len(ydata)==0:
            ydata = xdata
            xdata = range(0, len(ydata))
        output = Line2D(
            xdata=xdata,
            ydata=ydata,
            linestyle=tools.linestyles[self.get_input('linestyle')],
            color=tools.colors[self.get_input('color')],
            marker=tools.markers[self.get_input('marker')],
            label=self.get_input('label'),
            markersize=self.get_input('markersize'),
            markeredgecolor=tools.colors[self.get_input('markeredgecolor')],
            markeredgewidth=self.get_input('markeredgewidth'),
            linewidth=self.get_input('linewidth'),
            fillstyle=self.get_input('fillstyle'),
            alpha=self.get_input('alpha'),**kwds
        )
        return (output, )

"""
antialiased=None, 
dash_capstyle=None,
solid_capstyle=None, 
dash_joinstyle=None,
solid_joinstyle=None,
pickradius=5,
drawstyle=None,
 markevery=None,
**kwargs)

      animated: [True | False]         
      antialiased or aa: [True | False]         
      axes: an :class:`~matplotlib.axes.Axes` instance         
      clip_box: a :class:`matplotlib.transforms.Bbox` instance         
      clip_on: [True | False]         
      clip_path: [ (:class:`~matplotlib.path.Path`,         :class:`~matplotlib.transforms.Transform`) |         :class:`~matplotlib.patches.Patch` | None ]         
      contains: a callable function         
      dash_capstyle: ['butt' | 'round' | 'projecting']         
      dash_joinstyle: ['miter' | 'round' | 'bevel']         
      dashes: sequence of on/off ink in points         
      data: 2D array         
      drawstyle: [ 'default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post' ]         
      figure: a :class:`matplotlib.figure.Figure` instance         
      gid: an id string         
      lod: [True | False]         
      markerfacecolor or mfc: any matplotlib color         
      markevery: None | integer | (startind, stride)
      picker: float distance in points or callable pick function         ``fn(artist, event)``         
      pickradius: float distance in points 
      rasterized: [True | False | None]         
      snap: unknown
      solid_capstyle: ['butt' | 'round' |  'projecting']         
      solid_joinstyle: ['miter' | 'round' | 'bevel']         
      transform: a :class:`matplotlib.transforms.Transform` instance         
      url: a url string         
      visible: [True | False]         
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



class PyLabPie(Plotting):

    def __init__(self):
        inputs = [
            { 'name':'x'},
            {'name':'colors',       'interface':IStr,   'value':None},
            {'name':'labels',       'interface':ISequence, 'value':None},
            {'name':'explode',      'interface':ISequence, 'value':None},
            {'name':'pctdistance',  'interface':IFloat, 'value':0.6},
            {'name':'labeldistance','interface':IFloat, 'value':1.1},
            {'name':'shadow',       'interface':IBool,  'value':False},
            {'name':'hold',         'interface':IBool,  'value':False},
            {'name':'autopct',      'interface':IStr,   'value':None}
        ]

        Plotting.__init__(self, inputs)

    def __call__(self, inputs):
        from pylab import pie, cla
        self.figure()
        self.axes()
        cla()
        kwds = {}
        kwds['explode'] = self.get_input('explode')
        kwds['colors'] = self.get_input('colors')
        kwds['labels'] = self.get_input('labels')
        kwds['pctdistance'] = self.get_input('pctdistance')
        kwds['labeldistance'] = self.get_input('labeldistance')
        kwds['shadow'] = self.get_input('shadow')
        kwds['hold'] = self.get_input('hold')
        kwds['autopct'] = self.get_input('autopct')

        res = pie(self.get_input('x'), **kwds)

        self.properties()
        return self.axes_shown
        return res


class PyLabBar(Plotting):
    """.. todo:: to be completed"""
    def __init__(self):
        inputs = [
            {'name':'left', 'interface':ISequence, 'value':[]},
            {'name':'height', 'interface':ISequence, 'value':[]}
        ]
        Plotting.__init__(self, inputs)


    def __call__(self, inputs):
        from pylab import bar, hold, cla

        self.figure()
        self.axes()
        cla()
        left = self.get_input('left')
        height = self.get_input('height')

        if type(left)!=list:
            left = [left]


        res = None
        if type(left[0])==float:
            width = left[1] - left[0]
            print width
            print left
            print height
            res = bar(left[1:], height, width=width)
        else:
            c = enumerate(tools.colors)
            for x,y in zip(left, height):
                color = c.next()
                #width = x[1]-x[0]
                width=0.1
                res = bar(x[1:],y, width=width, color=color[1], alpha=0.5)
                hold(True)
        self.properties()
        return self.axes_shown

        return res

class PyLabCohere(Plotting):
    """ A function or a vector of length *NFFT*. To create window
          vectors see :func:`window_hanning`, :func:`window_none`,
          :func:`numpy.blackman`, :func:`numpy.hamming`,
          :func:`numpy.bartlett`, :func:`scipy.signal`,
          :func:`scipy.signal.get_window`, etc. The default is
          :func:`window_hanning`.  If a function is passed as the
          argument, it must take a data segment as an argument and
          return the windowed version of the segment.

    .. todo:: to be completed
    """
    def __init__(self):
        #     window = mlab.window_hanning, noverlap=0, pad_to=None,
        #     sides='default', scale_by_freq=None, **kwargs)
        inputs = [
            {'name':'x',            'interface':None,   'value':None},
            {'name':'y',            'interface':None,   'value':None},
            {'name':'NFFT',         'interface':IInt,   'value':256},
            {'name':'Fs',           'interface':IFloat, 'value':2.},
            {'name':'detrend',      'interface':IEnumStr(tools.detrends.keys()), 'value':'none'},
            #{'name':'window',       'interface':None, 'value':'tobedone'},
            {'name':'noverlap',     'interface':IInt,   'value':0},
            {'name':'pad_to',       'interface':IInt,   'value':None},
            {'name':'sides',        'interface':IEnumStr(tools.sides.keys()), 'value':'default'},
            #{'name':'scale_by_freq','interface':IBool,  'value':True},
            {'name':'Fc',           'interface':IFloat, 'value':0},
            ]

        Plotting.__init__(self, inputs)


    def __call__(self, inputs):
        from pylab import cohere, cla, detrend_none, detrend_linear, detrend_mean, hold, Line2D
        import pylab
        cla()
        self.figure()
        self.axes()
        cla()
        kwds = {}
        kwds['NFFT'] = self.get_input('NFFT')
        kwds['Fs'] = self.get_input('Fs')
        kwds['detrend'] = getattr(pylab, 'detrend_'+self.get_input('detrend'))
        #kwds['window'] = self.get_input('window')
        kwds['noverlap'] = self.get_input('noverlap')
        kwds['pad_to'] = self.get_input('pad_to')
        kwds['sides'] = self.get_input('sides')
        #kwds['scale_by_freq'] = self.get_input('scale_by_freq')
        kwds['Fc'] = self.get_input('Fc')

        cxy = None
        freq = None
        try:
            cxy, freq = cohere(self.get_input('x'), self.get_input('y'), **kwds)
        except:
            xinputs=self.get_input('x')
            if type(xinputs)!=list:
                xinputs = [xinputs]
            if type(xinputs[0])==Line2D:
                for x in xinputs:
                    line2dkwds = tools.get_kwds_from_line2d(x, kwds)
                    #returns the processed data ?
                    cxy, freq = cohere(x.get_xdata(orig=False), x.get_ydata(orig=False),**line2dkwds)
                    hold(True)

        self.properties()
        return self.axes_shown
        return (cxy, freq)



class PyLabHexBin(Plotting):
    """ .. todo:: tohis documentation"""

    def __init__(self):
        inputs = [
            {'name':"x"},
            {'name':"y"},
            {'name':"bins", 'interface':ISequence, 'value':[]},
            #bins could be 'log', None, integer or sequence
            {'name':"gridsize", 'interface':IInt, 'value':100},
            {'name':"xscale", 'interface':IEnumStr(tools.keys()), 'value':'linear'},
            {'name':"yscale", 'interface':IEnumStr(tools.keys()), 'value':'linear'},
            {'name':"mincnt", 'interface':IInt, 'value':None},
            {'name':"alpha", 'interface':IFloat(0,1,0.1), 'value':1.0},
            {'name':"marginals", 'interface':IBool, 'value':False},
            #{'name':"norm", 'interface':matplotlib.colors.Normalize, 'value':[vmin,vmax]},
            # inorm sets vmin and vmax. So choose either norm method or vmin/vmax method.
            {'name':"vmin", 'interface':IFloat, 'value':None},
            {'name':"vmax", 'interface':IFloat, 'value':None},
            {'name':"extent", 'value':None},
            {'name':"linewidths", 'interface':IFloat(0,10,1), 'value':None},
            {'name':"edgecolors", 'interface':IEnumStr(tools.colors.keys()), 'value':None},
            {'name':"cmap", 'interface':IStr, 'value':None},
        ]

        """         reduce_C_function = np.mean, """
        Plotting.__init__(self, inputs)


    def __call__(self, inputs):
        from pylab import hexbin, cla
        kwds={}
        if len(self.get_input('bins'))>=1:
            kwds['bins'] = self.get_input('bins')
        else:
            kwds['bins'] = None
        kwds['xscale'] = self.get_input('xscale')
        kwds['yscale'] = self.get_input('yscale')
        kwds['gridsize'] = self.get_input('gridsize')
        #None by default
        if self.get_input('mincnt'):
            kwds['mincnt'] = self.get_input('mincnt')
        if self.get_input('cmap'):
            kwds['cmap'] = self.get_input('cmap')

        kwds['marginals'] = self.get_input('marginals')
        kwds['alpha'] = self.get_input('alpha')
        kwds['vmin'] = self.get_input('vmin')
        kwds['vmax'] = self.get_input('vmax')
        kwds['linewidths'] = self.get_input('linewidths')
        if self.get_input('edgecolors'):
            kwds['edgecolors'] = self.colors[self.get_input('edgecolors')]


        self.figure()
        self.axes()
        cla()
        hexbin(self.get_input('x'), self.get_input('y'), **kwds)
        self.properties()
        return self.axes_shown


class PyLabCLabel(Node):
    """ .. todo:: tohis documentation"""

    def __init__(self):
        Node.__init__(self)
        self.add_input(name='fontsize', interface=IInt, value=10)
        self.add_input(name='inline', interface=IBool, value=True)
        self.add_input(name='rightside_up', interface=IBool, value=True)
        self.add_input(name='inline_spacing', interface=IInt, value=5)
        self.add_input(name='fmt', interface=IStr, value='%1.3f')
        self.add_input(name='colors', interface=IEnumStr(tools.colors.keys()), value=None)
        # colors may be a list such as ('r', 'green', 'blue', (1,1,0), '#afeeee', '0.5')
        self.add_output(name='kwds')

    def __call__(self, inputs):
        from pylab import clabel
        kwds = {}
        kwds['fontsize'] = self.get_input('fontsize')
        kwds['inline'] = self.get_input('inline')
        kwds['rightside_up'] = self.get_input('rightside_up')
        kwds['inline_spacing'] = self.get_input('inline_spacing')
        kwds['fmt'] = self.get_input('fmt')
        try:
            kwds['colors'] = tools.colors[self.get_input('colors')]
        except:
            kwds['colors'] = self.get_input('colors')

        return kwds




class PcolorInterface():
    """ .. todo:: tohis documentation"""
    def __init__(self):
        self.inputs = []
        self.inputs.append({'name': 'X', 'value':None})
        self.inputs.append({'name': 'Y', 'value':None})
        self.inputs.append({'name': 'Z', 'value':None})
        self.inputs.append({'name':"cmap", 'interface':IStr, 'value':None})
        """todo:: norm, vmin/vmax, shading, edgecolor, alpha"""
    def get_kwds(self):

        self.kwds = {}
        if self.get_input('cmap'):
            self.kwds['cmap'] = self.get_input('cmap')

    def __call__(self, inputs):
        raise NotImplementedError


#class PyLabPcolormesh(Plotting, PcolorInterface): is exactly the same as pcolor but the color optio does not exist.
class PyLabPcolor(Plotting, PcolorInterface):
    """ .. todo:: tohis documentation


    .. note:: pcolormesh is equivalent to pcolor. """
    def __init__(self):
        PcolorInterface.__init__(self)
        Plotting.__init__(self, self.inputs)

    def __call__(self, inputs):
        from pylab import pcolor, cla
        self.figure()
        self.axes()
        cla()
        X = self.get_input('X')
        Y = self.get_input('Y')
        Z = self.get_input('Z')
        self.get_kwds()
        if X is not None and Y is not None:
            pcolor(X, Y, Z, **self.kwds)
        elif Z is not None:
            pcolor(Z, **self.kwds)
        else:
            raise ValueError('Z is compulsary. If X provided, Y must be provided as well.')

        self.properties() 
        return self.axes_shown




class PyLabContour(Plotting):
    """ .. todo:: tohis documentation"""

    def __init__(self):

        inputs = [
            {'name':"X"},
            {'name':"Y"},
            {'name':"Z"},
            {'name':"n", 'interface':IInt, 'value':None},
            {'name':"filled", 'interface':IBool, 'value':False},
            {'name':"linewidths", 'interface':IInt, 'value':1.},
            {'name':"linestyles", 'interface':IEnumStr(tools.linestyles.keys()), 'value':'solid'},
            {'name':"alpha", 'interface':IFloat(0,1,0.1), 'value':1.0},
            {'name':"cmap", 'interface':IStr, 'value':None},
            #{'name':"origin", 'interface':IStr, 'value':None},could be lower, upper, image
            #extent, colorsm,extent,locator,extend
            #contourf:  m antialiased, nchunk
            {'name':"clabel", 'interface':IDict, 'value':{'inline':True, 'fontsize':10, 'rightside_up':True, 'inline_spacing':5, 'fmt':'%1.3f'}}
        ]
        Plotting.__init__(self, inputs)


    def __call__(self, inputs):
        from pylab import clabel, cla, contour, contourf

        kwds={}
        X = self.get_input('X')
        Y = self.get_input('Y')
        Z = self.get_input('Z')
        n = self.get_input('n')
        if type(n)==int and n<=0:
            n= None

        kwds['linewidths']=self.get_input('linewidths')
        kwds['alpha']=self.get_input('alpha')
        if self.get_input('linestyles') in [None, 'None']:
            kwds['linestyles']='solid'
        else:
            kwds['linestyles']=tools.linestyles[self.get_input('linestyles')]
        if self.get_input('cmap'):
            kwds['cmap']=self.get_input('cmap')

        self.figure()
        self.axes()
        cla()
        if n is None:
            if self.get_input('filled')==True:
                contourf(X,Y,Z, **kwds)
                if self.get_input('colorbar') is True:
                    from pylab import colorbar
                    colorbar()
                    self.set_input('colorbar', False)
                #superimpose the contour in black and reset cmap because either colors or cmap must be none
                kwds['colors'] = 'k'
                kwds['cmap'] = None
                CS = contour(X,Y,Z, **kwds)
            else:
                CS = contour(X,Y,Z, **kwds)
        else:
            if self.get_input('filled')==True:
                contourf(X,Y,Z,n, **kwds)
                if self.get_input('colorbar') is True:
                    from pylab import colorbar
                    colorbar()
                    self.set_input('colorbar', False)
                #superimpose the contour in black and reset cmap because either colors or cmap must be none
                kwds['colors'] = 'k'
                kwds['cmap'] = None
                CS = contour(X,Y,Z,n, **kwds)
            else:
                CS = contour(X,Y,Z,n, **kwds)
        if type(self.get_input('clabel'))==clabel:
            pass
        else:
            kwds2 = {}
            kwds2 = self.get_input('clabel')
            clabel(CS, **kwds2)
        self.properties()
        #todo: return self.axes_shown
        return CS


class PsdInterface():
    """base class for the :class:`PyLabSpecgram`, :class:`PyLabCsd`, :class:`PyLabPsd` classes.

    :param type: either 'xy' or 'x' to specify number of inputs.
    :param noverlap: default is 0 (Specgram requires value >0).
    :param nfft: default is 256
    :param cmap: the colormap


    This class defines the following VisuAlea connectors:

    :param NFFT: The number of data points used in each block for 
        the FFT. The default is 256.
    :param Fs:  The sampling frequency. The default is 2.
    :param Fc:   The center frequency of *x*. Default is 0.
    :param noverlap: The number of points of overlap between blocks.  
        The default value is 0.
    :param sides: Specifies which sides of the PSD to return. Default is 'default'.
    :param pad_to:  The number of points to which the data segment is padded when
          performing the FFT. The default is None.
    :param detrend:  The function applied to each segment before fft-ing,
          designed to remove the mean or linear trend (default is 'none')
    :param scale_by_freq:   (default is True)
    :param window: function or a vector of length *NFFT*. default is hanning window
        To create other window, use the :class:`~openalea.pylab_text_wralea.py_pylab.PyLabWindow` node.
    
    :author: Thomas Cokelaer <Thomas.Cokelaer@sophia.inria.fr>

    """
    def __init__(self, type='x', noverlap=0, nfft=256, cmap=False):
       
        self.kwds = {}
        if type=='xy':
            self.inputs = [
            {'name':"x"},
            {'name':"y"}]
        else:
            self.inputs = [
            {'name':"x"},]

        self.inputs.extend([
            {'name':"NFFT",     'interface':IInt, 'value':nfft},
            {'name':"Fs",       'interface':IInt, 'value':2},
            {'name':"Fc",       'interface':IInt, 'value':0},
            {'name':"noverlap", 'interface':IInt, 'value':noverlap},
            {'name':"sides", 'interface':IEnumStr(tools.sides), 'value':'default'},
            {'name':"pad_to", 'interface':IInt, 'value':None},
            {'name':'detrend', 'interface':IEnumStr(tools.detrends.keys()), 'value':'none'},
            {'name':'scale_by_freq', 'interface':IBool, 'value':True},
            {'name':"window", 'interface':IEnumStr(tools.windows.keys()), 'value':'hanning'},])

        if cmap:
            self.inputs.extend([{'name':"cmap", 'interface':IStr, 'value':None}])

        """TODO : csd( 
        scale_by_freq=None)"""

    def _get_kwds(self):
        """returns a dictionary with the parameters"""
        self.kwds['NFFT'] = self.get_input('NFFT')
        self.kwds['Fs'] = self.get_input('Fs')
        self.kwds['Fc'] = self.get_input('Fc')
        self.kwds['noverlap'] = self.get_input('noverlap')
        self.kwds['sides'] = self.get_input('sides')
        self.kwds['pad_to'] = self.get_input('pad_to')
        self.kwds['scale_by_freq'] = self.get_input('scale_by_freq')
        if self.get_input('detrend')!='none':
            from pylab import detrend_none, detrend_linear, detrend_mean
            import pylab
            self.kwds['detrend'] = getattr(pylab, 'detrend_'+self.get_input('detrend'))

    def _set_window(self):
        """Get the correct windowing function. """
        if self.get_input('window') in ['hanning', 'none']:
            self.kwds['window']=tools.windows[self.get_input('window')]
        else:
            self.kwds['window'] = self.get_input('window')
            assert len(self.kwds['window'])==self.kwds['NFFT'], '!! NFFT and window''s length must be equal'
    def __call__(self, inputs):
        raise NotImplementedError


class PyLabPsd(PsdInterface, Plotting,PlotxyInterface):
    """VisuAlea version of pylab.psd

    :param x: the signal to analyse (a 1D- array)
    :param NFFT: The number of data points used in each block for 
        the FFT. The default is 256.
    :param Fs:  The sampling frequency. The default is 2.
    :param Fc:   The center frequency of *x*. Default is 0.
    :param noverlap: The number of points of overlap between blocks.  
        The default value is 0.
    :param sides: Specifies which sides of the PSD to return. Default is 'default'.
    :param pad_to:  The number of points to which the data segment is padded when
          performing the FFT. The default is None.
    :param detrend:  The function applied to each segment before fft-ing,
          designed to remove the mean or linear trend (default is 'none')
    :param scale_by_freq:   (default is True)
    :param window: function or a vector of length *NFFT*. default is hanning window
        To create other window, use the :class:`~openalea.pylab_text_wralea.py_pylab.PyLabWindow` node.


    :author: Thomas Cokelaer <Thomas.Cokelaer@sophia.inria.fr>
    """
    def __init__(self):
        PsdInterface.__init__(self, type='x')
        Plotting.__init__(self, self.inputs)
        PlotxyInterface.__init__(self)

    def __call__(self, inputs):
        from pylab import cla

        kwds=self._get_kwds()
        self._set_window()
        self.figure()
        self.axes()
        cla()

        #psd has no y, yet, self.call requires an x and a y input. So let us cheat:
        try:
            self.get_input('y')
        except:
            self.add_input(name='y', value=None)

        c = self.call('psd',self.kwds)
        self.properties()
        #todo return self.axes_shown
        return c


class PyLabCsd(Plotting,PlotxyInterface, PsdInterface):
    """VisuAlea version of pylab.csd

    :param x: the signal to analyse (a 1D- array)
    :param y: the signal to analyse (a 1D- array)
    :param NFFT: The number of data points used in each block for
        the FFT. The default is 256.
    :param Fs:  The sampling frequency. The default is 2.
    :param Fc:   The center frequency of *x*. Default is 0.
    :param noverlap: The number of points of overlap between blocks.
        The default value is 0.
    :param sides: Specifies which sides of the PSD to return. Default is 'default'.
    :param pad_to:  The number of points to which the data segment is padded when
          performing the FFT. The default is None.
    :param detrend:  The function applied to each segment before fft-ing,
          designed to remove the mean or linear trend (default is 'none')
    :param scale_by_freq:   (default is True)
    :param window: function or a vector of length *NFFT*. default is hanning window
        To create other window, use the :class:`~openalea.pylab_text_wralea.py_pylab.PyLabWindow` node.


    :author: Thomas Cokelaer <Thomas.Cokelaer@sophia.inria.fr>
    """

    def __init__(self):
        PsdInterface.__init__(self, type='xy')
        Plotting.__init__(self, self.inputs)
        PlotxyInterface.__init__(self)

    def __call__(self, inputs):
        from pylab import cla

        self._get_kwds()
        self._set_window()
        self.figure()
        self.axes()
        cla()
        c = self.call('csd',self.kwds)
        self.properties()
        return self.axes_shown

class PyLabSpecgram(Plotting,PlotxyInterface, PsdInterface):
    """VisuAlea version of pylab.psd

    :param x: the signal to analyse (a 1D- array)
    :param NFFT: The number of data points used in each block for 
        the FFT. The default is 128.
    :param Fs:  The sampling frequency. The default is 2.
    :param Fc:   The center frequency of *x*. Default is 0.
    :param noverlap: The number of points of overlap between blocks.
        The default value is 128.
    :param sides: Specifies which sides of the PSD to return. Default is 'default'.
    :param pad_to:  The number of points to which the data segment is padded when
          performing the FFT. The default is None.
    :param detrend:  The function applied to each segment before fft-ing,
          designed to remove the mean or linear trend (default is 'none')
    :param scale_by_freq:   (default is True)
    :param window: function or a vector of length *NFFT*. default is hanning window
        To create other window, use the :class:`~openalea.pylab_text_wralea.py_pylab.PyLabWindow` node.


    :author: Thomas Cokelaer <Thomas.Cokelaer@sophia.inria.fr>
    """

    def __init__(self):
        PsdInterface.__init__(self, type='x', noverlap=128, cmap=True)
        Plotting.__init__(self, self.inputs)
        PlotxyInterface.__init__(self)
        #         xextent=None, 

    def __call__(self, inputs):
        from pylab import cla

        self._get_kwds()
        self._set_window()
        self.figure()
        self.axes()
        print self.kwds
        cla()
        if self.get_input('cmap'):
            self.kwds['cmap'] = self.get_input('cmap')
        try:
            self.get_input('y')
        except:
            self.add_input(name='y', value=None)
        c = self.call('specgram',self.kwds)
        self.properties()
        return self.axes_shown


class PyLabStem(Plotting, PlotxyInterface):
    """VisuAlea version of pylab.stem

    :param x: 1D array
    :param y: 1D array
    :param marker_color: color of the marker (see :ref:`colors`)
    :param line_color: color of the line (see :ref:`colors`)
    :param base_color: color of the base line (see ref:`colors`)
    :param marker_style:
    :param line_style:
    :param base_style:

    :return: a axes object

    :author: Thomas Cokelaer <Thomas.Cokelaer@sophia.inria.fr>
    """

    def __init__(self):
        PlotxyInterface.__init__(self)
        inputs = [
            {'name': 'x'},
            {'name': 'y'},
            {'name':'marker_color', 'interface':IEnumStr(tools.colors.keys()), 'value':'blue'},
            {'name':'line_color', 'interface':IEnumStr(tools.colors.keys()), 'value':'blue'},
            {'name':'base_color', 'interface':IEnumStr(tools.colors.keys()), 'value':'red'},
            {'name':'marker_style', 'interface':IEnumStr(tools.markers.keys()), 'value':'circle'},
            {'name':'line_style', 'interface':IEnumStr(tools.linestyles.keys()), 'value':'solid'},
            {'name':'base_style', 'interface':IEnumStr(tools.linestyles.keys()), 'value':'solid'},
        ]
        Plotting.__init__(self, inputs)

    def __call__(self, inputs):
        from pylab import cla

        self.figure()
        self.axes()
        cla()
        kwds = {}
        kwds['markerfmt'] = tools.colors[self.get_input('marker_color')]+ tools.markers[self.get_input('marker_style')]
        kwds['basefmt'] = tools.colors[self.get_input('base_color')]+ tools.linestyles[self.get_input('base_style')]
        kwds['linefmt'] = tools.colors[self.get_input('line_color')]+ tools.linestyles[self.get_input('line_style')]
        c = self.call('stem', kwds)
        self.properties()
        return self.axes_shown


class PyLabStep(Plotting, PlotxyInterface):
    """VisuAlea version of pylab.step

    :param x: 1D array
    :param y: 1D array
    :param marker: marker (see :ref:`markers`)
    :param markersize:  (default is 10)
    :param color: (see ref:`colors`)

    :return: a axes object

    .. todo:: where parameter

    :author: Thomas Cokelaer <Thomas.Cokelaer@sophia.inria.fr>
    """
    def __init__(self):
        PlotxyInterface.__init__(self)
        inputs = [
                    {'name':'x', 'interface':None, 'value':None},
                    {'name':'y', 'interface':None, 'value':None},
                    {'name':'marker', 'interface':IEnumStr(tools.markers.keys()), 'value':'circle'},
                    {'name':'markersize', 'interface':IFloat, 'value':10},
                    {'name':'color', 'interface':IEnumStr(tools.colors.keys()), 'value':'blue'},
        ]
        Plotting.__init__(self, inputs)

    def __call__(self, inputs):
        from pylab import cla

        self.figure()
        self.axes()
        cla()

        kwds = {}
        kwds['markersize']=self.get_input("markersize")
        kwds['marker']=tools.markers[self.get_input("marker")]
        kwds['color']=tools.colors[self.get_input("color")]
        c = self.call('step', kwds)
        self.properties()
        return self.axes_shown




class PyLabQuiver(Plotting):
    """ .. todo:: tohis documentation"""

    def __init__(self):
        
        inputs = [
                    {'name':'X',            'interface':None,                           'value':None},
                    {'name':'Y',            'interface':None,                           'value':None},
                    {'name':'U',            'interface':None,                           'value':None},
                    {'name':'V',            'interface':None,                           'value':None},
                    {'name':'C',            'interface':None,                           'value':None},
                    {'name':'units',        'interface':IEnumStr(tools.units),           'value':'width'},
                    {'name':'angles',       'interface':IEnumStr(tools.angles),          'value':'uv'},
                    {'name':'scale',        'interface':IFloat,                         'value':None},
                    {'name':'width',        'interface':IFloat(0.005, 1, 0.005),      'value':None},
                    {'name':'headwidth',    'interface':IFloat,                         'value':3},
                    {'name':'headlength',   'interface':IFloat,                         'value':5},
                    {'name':'headaxislength','interface':IFloat,                        'value':4.5},
                    {'name':'minshaft',     'interface':IFloat,                         'value':1},
                    {'name':'minlength',    'interface':IFloat,                         'value':1},
                    {'name':'pivot',        'interface':IEnumStr(tools.pivots),               'value':'tail'},
                    {'name':'color',        'interface':IEnumStr(tools.colors.keys()),        'value':'None'},
                    {'name':'polycollection', 'interface':IDict,        'value':{}},
        ]
        Plotting.__init__(self, inputs)

    def __call__(self, inputs):
        from pylab import quiver, cla

        self.figure()
        self.axes()
        cla()

        X = self.get_input('X')
        Y = self.get_input('Y')
        U = self.get_input('U')
        V = self.get_input('V')
        C = self.get_input('C')
        kwds = {}

        for key in ['units', 'angles', 'scale', 'width', 'headwidth', 'headlength', 'headaxislength', 'minshaft', 'minlength']:
            kwds[key]=self.get_input(key)
        if self.get_input('color')!='None':
            kwds['color']=tools.colors[self.get_input('color')]
        for key, value in self.get_input('polycollection').iteritems():
            kwds[key]=value

        if X is None and Y is None and C is None and U is not None and V is not None:
            c = quiver(U, V, **kwds)
        elif X is None and Y is None and C is not None and U is not None and V is not None:
            c = quiver(U, V, C, **kwds)
        elif X is not None and Y is not None and C is None and U is not None and V is not None:
            c = quiver(X, Y, U, V, **kwds)
        elif X is not None and Y is not None and C is not None and U is not None and V is not None:
            c = quiver(X, Y, U, V, C, **kwds)
        else:
            raise SyntaxError('Wrong usage. See documentation. ')

        print X
        print Y
        print U
        #self.properties()
        from pylab import show
        show()
        return self.axes_shown


class PyLabFill(Plotting, PlotxyInterface):
    """VisuAlea version of pylab.fill

    :param x: 1D array
    :param y: 1D array
    :param linewidth:
    :param facecolor:
    :param patch: connect a :class:`~openalea.pylab_patches.wralea.py_pylab.Patch`.

    :return: a axes object

    :author: Thomas Cokelaer <Thomas.Cokelaer@sophia.inria.fr>
    """

    def __init__(self):
        PlotxyInterface.__init__(self)
        inputs = [
                    {'name':'x'},
                    {'name':'y'},
                    {'name':'linewidth', 'interface':IFloat, 'value':1},
                    {'name':'facecolor', 'interface':IEnumStr(tools.colors.keys()), 'value':'blue'},
                    {'name':'kwargs (Patch)','interface':IDict, 'value':{}},
        ]
        Plotting.__init__(self, inputs)
        #todo : as many patch as x/y

    def __call__(self, inputs):
        from pylab import fill, cla

        self.figure()
        self.axes()
        kwds = self.get_input('kwargs (Patch)')
        kwds['facecolor'] = tools.colors[self.get_input('facecolor')]
        kwds['linewidth'] = self.get_input('linewidth')

        c = self.call('fill', kwds)

        self.properties()
        return self.axes_shown

class PyLabFillBetween(Plotting, PlotxyInterface):
    """VisuAlea version of pylab.fill_between

    :param x: 1D array
    :param y1: 1D array
    :param y2: 1D array
    :param where:
    :param patch: connect a :class:`~openalea.pylab_patches.wralea.py_pylab.Patch`.

    :return: a axes object

    :author: Thomas Cokelaer <Thomas.Cokelaer@sophia.inria.fr>
    """
    def __init__(self):
        PlotxyInterface.__init__(self)
        inputs = [
                    {'name':'x'},
                    {'name':'y1'},
                    {'name':'y2'},
                    {'name':'where', 'interface':IStr, 'value':'None'},
                    {'name':'kwargs (Patch)','interface':IDict, 'value':{}},
        ]
        Plotting.__init__(self, inputs)
        #todo : as many patch as x/y

    def __call__(self, inputs):
        from pylab import fill_between, cla

        self.figure()
        self.axes()
        try:
            kwds = self.get_input('kwargs (Patch)')
            del kwds['fill']
        except:
            kwds = {}
        x = self.get_input('x')
        y1 = self.get_input('y1')
        y2 = self.get_input('y2')
        where = eval(str(self.get_input('where')))
        c = fill_between(x, y1, y2, where=where, **kwds)
        self.properties()
        return self.axes_shown







class PyLabErrorBar(Plotting, PlotxyInterface):
    """VisuAlea version of pylab.errorbar

    :param x: 1D array
    :param y: 1D array
    :param xerr: 1D array
    :param yerr: 1D array (optional)
    :param ecolor: color of the error bars
    :param elinewidth: width of the errorbars
    :param Patch: a node to provide :class:`Patch` arguments

    .. todo:: fmt='-', capsize=3, barsabove=False, lolims=False, uplims=False, xlolims=False, xuplims=False)

    :param patch: connect a :class:`~openalea.pylab_patches.wralea.py_pylab.Patch`.

    :return: a axes object

    :author: Thomas Cokelaer <Thomas.Cokelaer@sophia.inria.fr>
    """

    def __init__(self):
        PlotxyInterface.__init__(self)
        inputs = [
                    {'name':'x'},
                    {'name':'y'},
                    {'name':'xerr', 'value':None},
                    {'name':'yerr', 'value':None},
                    {'name':'ecolor', 'value':None},
                    {'name':'elinewidth', 'value':None},
                    {'name':'kwargs (Patch)','interface':IDict, 'value':{}},
        ]
        Plotting.__init__(self, inputs)
        #todo : as many patch as x/y

    def __call__(self, inputs):
        from pylab import errorbar, cla

        self.figure()
        self.axes()
        try:
            kwds = self.get_input('kwargs (Patch)')
            del kwds['fill']
        except:
            kwds = {}

        x = self.get_input('x')
        y = self.get_input('y')
        xerr = self.get_input('xerr')
        yerr = self.get_input('yerr')
        c = errorbar(x, y, xerr, yerr, **kwds)
        self.properties()
        return self.axes_shown


class PyLabImshow(Plotting):
    #@add_docstring(pylab.imshow)
    def __init__(self):
        inputs = [
                    {'name':'image', 'interface':None},
                    {'name':"cmap", 'interface':IEnumStr(tools.cmaps.keys()), 'value':'None'},
                    {'name':"interpolation", 'interface':IEnumStr(tools.interpolation), 'value':'None'},
                    {'name':"aspect", 'interface':IEnumStr(tools.aspect), 'value':'None'},
                    {'name':"alpha", 'interface':IFloat(0., 1., 0.01), 'value':1},
                    {'name':"vmin", 'interface':IFloat, 'value':None},
                    {'name':"vmax", 'interface':IFloat, 'value':None},
                    {'name':'kwargs','interface':IDict, 'value':{}},
        ]
        #norm is not implemented: use vmin/vmax instead
        Plotting.__init__(self, inputs)

    def __call__(self, inputs):
        from pylab import imshow, hold, cla, subplot, show

        self.figure()
        self.axes()

        kwds = self.get_input('kwargs')

        X = self.get_input('image')
        if type(X)!=list:
            X = [X]
        if self.get_input('cmap'):
            kwds['cmap']=get_cmap(self.get_input('cmap'))
        kwds['alpha'] = self.get_input('alpha')
        kwds['vmin'] = self.get_input('vmin')
        kwds['vmax'] = self.get_input('vmax')
        if self.get_input('interpolation')!='None':
            kwds['interpolation'] = self.get_input('interpolation')
        if self.get_input('aspect')!='None':
            kwds['aspect'] = self.get_input('aspect')

        try:
            row = self.get_input('subplot')[0]
            column = self.get_input('subplot')[1]
        except:
            from pylab import ceil, floor, sqrt
            row, column  = int(ceil(sqrt(len(X)))), int(floor(sqrt(len(X))))
            if row*column < len(X):
                row, column  = int(ceil(sqrt(len(X)))), int(ceil(sqrt(len(X))))
            
        count = 0
        #assert len(X) == row * column, 'len(X)=%s and row*colum=%s' % (len(X), row*column)
        hold(True)
        for r in range(1, row+1):
            for c in range(1, column+1):
                count+=1
                subplot(row,column,count)
                try:
                    imshow(X[count-1], **kwds)
                    hold(True)
                except:
                    pass
        #show()
                self.properties()
        hold(False)
        return self.axes_shown

    """
      *extent*: [ None | scalars (left, right, bottom, top) ]
        Data limits for the axes.  The default assigns zero-based row,
        column indices to the *x*, *y* centers of the pixels.
      *shape*: [ None | scalars (columns, rows) ]
        For raw buffer images
      *filternorm*:
        A parameter for the antigrain image resize filter.  From the
        antigrain documentation, if *filternorm* = 1, the filter normalizes
        integer values and corrects the rounding errors. It doesn't do
        anything with the source floating point values, it corrects only
        integers according to the rule of 1.0 which means that any sum of
        pixel weights must be equal to 1.0.  So, the filter function must
        produce a graph of the proper shape.
      *filterrad*:
        The filter radius for filters that have a radius
        parameter, i.e. when interpolation is one of: 'sinc',
        'lanczos' or 'blackman'
    Additional kwargs are :class:`~matplotlib.artist.Artist` properties:

      alpha: float (0.0 transparent through 1.0 opaque)         
      animated: [True | False]         
      axes: an :class:`~matplotlib.axes.Axes` instance         
      clip_box: a :class:`matplotlib.transforms.Bbox` instance         
      clip_on: [True | False]         
      clip_path: [ (:class:`~matplotlib.path.Path`,         :class:`~matplotlib.transforms.Transform`) |         :class:`~matplotlib.patches.Patch` | None ]         
      contains: a callable function         
      figure: a :class:`matplotlib.figure.Figure` instance         
      gid: an id string         
      label: any string         
      lod: [True | False]         
      picker: [None|float|boolean|callable]         
      rasterized: [True | False | None]         
      snap: unknown
      transform: :class:`~matplotlib.transforms.Transform` instance         
      url: a url string         
      visible: [True | False]         
      zorder: any number         
    """



