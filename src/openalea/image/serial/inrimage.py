# -*- python -*-
#
#       image.serial: read/write spatial nd images
#
#       Copyright 2006 - 2011 INRIA - CIRAD - INRA
#
#       File author(s): Jerome Chopard <jerome.chopard@sophia.inria.fr>
#                       Eric Moscardi <eric.moscardi@sophia.inria.fr>
#                       Daniel Barbeau <daniel.barbeau@sophia.inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
################################################################################
"""
This module defines inrimage format
"""

__license__= "Cecill-C"
__revision__=" $Id$ "

import os
from os import path
import numpy as np
from struct import calcsize,pack,unpack
import gzip
from io import BytesIO
from openalea.image.spatial_image import SpatialImage

__all__ = ["read_inriheader","read_inrimage","write_inrimage"]

specific_header_keys = ("XDIM","YDIM","ZDIM",
                        "VDIM","TYPE","PIXSIZE",
                        "SCALE","CPU",
                        "VX","VY","VZ",
                        "TX","TY","TZ",
                        "#GEOMETRY")

def open_inrifile (filename) :
    """Open an inrimage file
    :param filename: str
    :returns: f (_io.BytesIO)

    Manage the gz attribute
    """
    if path.splitext(filename)[1] in (".gz",".zip") :
        fzip = gzip.open(filename,'rb')
        f = BytesIO(fzip.read()) # must be bytes see below
        fzip.close()
    else :
        f = open(filename,'rb') # this is bytes in py3 ok => above bytes too

    return f

def _read_header (f) :
    """Extract header from a stream and return it
    as a python dict
    :param f : _io.BytesIO
    :returns: prop (dict of str)
    """

    #read header string
    header = ""
    while header[-4:] != "##}\n" :
        header += f.read(256).decode('utf-8') # f is _io.BytesIO we whant str

    #read infos in header
    prop = {}
    hstart = header.find("{\n") + 1
    hend = header.find("##}")
    infos = [gr for gr in header[hstart:hend].split("\n") \
                    if len(gr) > 0]

    #format infos
    for prop_def in infos :
        if not prop_def.strip().startswith('#'):
            key,val = prop_def.split("=")
            prop[key] = val

    #return
    return prop

def read_inriheader (filename) :
    """Read only the header of an inrimage

    :param filename: str - name of the file to read
    :returns:  prop (dict of str)
    """
    f = open_inrifile(filename)
    prop = _read_header(f)
    f.close()
    return prop

def read_inrimage (filename) :
    """Read an inrimage, either zipped or not according to extension

    :param filename: str - name of the file to read
    :returns:  img (SpatialImage)
    """
    f = open_inrifile(filename)

    #read header
    prop = _read_header(f)
    prop["Filename"] = filename # Jonathan : 14.05.2012

    #extract usefull infos to read image
    zdim = int(prop.pop("ZDIM") )
    ydim = int(prop.pop("YDIM") )
    xdim = int(prop.pop("XDIM") )
    vdim = int(prop.pop("VDIM") )

    #if vdim != 1 :
        #   msg = "don't know how to handle vectorial pixel values"
    #   raise NotImplementedError(msg)

    #find data type
    pixsize = int(prop.pop("PIXSIZE","0").split(" ")[0])
    dtype = prop.pop("TYPE")

    if dtype == "unsigned fixed" :
        if pixsize == 0 :
            ntyp = np.dtype(np.int)
        else :
            try :
                ntyp = eval("np.dtype(np.uint%d)" % pixsize)
            except AttributeError :
                raise UserWarning("undefined pix size: %d" % pixsize)
    elif dtype == "signed fixed" :
        if pixsize == 0 :
            ntyp = np.dtype(np.int)
        else :
            try :
                ntyp = eval("np.dtype(np.int%d)" % pixsize)
            except AttributeError :
                raise UserWarning("undefined pix size: %d" % pixsize)
    elif dtype == "float" :
        if pixsize == 0 :
            ntyp = np.dtype(np.float)
        else :
            try :
                ntyp = eval("np.dtype(np.float%d)" % pixsize)
            except AttributeError :
                raise UserWarning("undefined pix size: %d" % pixsize)
    else :
        msg = "unable to read that type of datas : %s" % dtype
        raise UserWarning(msg)

    #read datas
    size = ntyp.itemsize * xdim * ydim * zdim * vdim
    mat = np.frombuffer(f.read(size),ntyp)
    if vdim != 1 :
        mat = mat.reshape( (vdim,xdim,ydim,zdim), order="F" )
        mat = mat.transpose(1,2,3,0)
    else:
        mat = mat.reshape( (xdim,ydim,zdim), order="F" )
        #mat = mat.transpose(2,1,0)

    #create SpatialImage
    res = tuple(float(prop.pop(k) ) for k in ("VX","VY","VZ") )
    for k in ("TX","TY","TZ") :
        prop.pop(k,None)

    img = SpatialImage(mat,res,vdim,prop)

    #return
    f.close()
    return img


def write_inrimage_to_stream(stream, img):
    """
    Write img to a _io.BytesIO stream with the proper header
    :param stream: _io.BytesIO
    :param img: |SpatialImage| - image to write

    """
    assert img.ndim in (3,4)

    #metadata
    info = dict(getattr(img,"info",{}) )

    #image dimensions
    if img.ndim < 4 :
        info["XDIM"],info["YDIM"],info["ZDIM"] = ("%d" % val for val in img.shape)
        info["VDIM"] = "1"
    else:
        info["XDIM"],info["YDIM"],info["ZDIM"],info["VDIM"] = ("%d" % val for val in img.shape)

    #image resolution
    res = getattr(img,"resolution",(1,1,1) )
    info["VX"],info["VY"],info["VZ"] = ("%f" % val for val in res)

    #data type
    if img.dtype == np.uint8 :
        info["TYPE"] = "unsigned fixed"
        info["PIXSIZE"] = "8 bits"
    elif img.dtype == np.uint16 :
        info["TYPE"] = "unsigned fixed"
        info["PIXSIZE"] = "16 bits"
    elif img.dtype == np.uint32 :
        info["TYPE"] = "unsigned fixed"
        info["PIXSIZE"] = "32 bits"
    elif img.dtype == np.uint64 :
        info["TYPE"] = "unsigned fixed"
        info["PIXSIZE"] = "64 bits"
    elif img.dtype == np.float32 :
        info["TYPE"] = "float"
        info["PIXSIZE"] = "32 bits"
    elif img.dtype == np.float64 :
        info["TYPE"] = "float"
        info["PIXSIZE"] = "64 bits"
    #elif img.dtype == np.float128 :
    #   info["TYPE"] = "float"
    #   info["PIXSIZE"] = "128 bits"
    else :
        msg = "unable to write that type of datas : %s" % str(img.dtype)
        raise UserWarning(msg)

    #mandatory else an error occurs when reading image
    info['#GEOMETRY']='CARTESIAN'
    info['CPU']='decm'

    #write header
    header = "#INRIMAGE-4#{\n"
    for k in specific_header_keys :#HACK pas bo to ensure order of specific headers
        try:
            header += "%s=%s\n" % (k,info[k])
        except KeyError:
            pass

    for k in set(info) - set(specific_header_keys) :
        header += "%s=%s\n" % (k,info[k])

    #fill header to be a multiple of 256
    header_size = len(header) + 4
    if (header_size % 256) > 0 :
        header += "\n" * ( 256 - header_size % 256 )

    header += "##}\n"

    stream.write(header.encode('utf-8')) # needs to be bite because opened in "wb" see in write_inrimage f = open(filename,'wb')
    if img.ndim == 3:
        stream.write(img.tobytes("F"))
    elif img.ndim == 4 :
        mat = img.transpose(3,0,1,2)
        stream.write(mat.tobytes("F") )
    else:
        raise Exception("Unhandled image dimension %d."%img.ndim)


def write_inrimage (filename, img) :
    """Write an inrimage zipped or not according to the extension

    .. warning:: if img is not a |SpatialImage|, default values will be used
                 for the resolution of the image

    :param img: |SpatialImage| - image to write
    :param filename: str - name of the file to read
    """
    #open stream
    zipped = ( path.splitext(filename)[1] in (".gz",".zip") )

    # we got here an _io.BytesIO
    if zipped :
        f = gzip.GzipFile(filename, "wb")
    else :
        f = open(filename,'wb')

    try:
        write_inrimage_to_stream(f, img)
    except:
        # -- remove probably corrupt file--
        f.close()
        if path.exists(filename) and path.isfile(filename):
            os.remove(filename)
        raise
    else:
        f.close()
