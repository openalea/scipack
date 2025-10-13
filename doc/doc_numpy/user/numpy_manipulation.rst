Array manipulation routines
***************************

This is the list of nodes available within VisuAlea in the **numpy.manipulation**
package.
The reference documentation is generated from numpy files, see also `API reference` on
`Numpy <https://numpy.org/>`_

.. currentmodule:: numpy

Changing array shape
====================
.. autosummary::
   :toctree: generated/


   reshape
   ravel
   ndarray.flatten

.. todo:: ndarray.flat

Transpose-like operations
=========================
.. autosummary::
   :toctree: generated/

   transpose

.. todo:: rollaxis, swapaxes, ndarray.T

Changing number of dimensions
=============================
.. autosummary::
   :toctree: generated/

.. todo:: atleast_1d, atleast_2d, atleast_3d, broadcast, broadcast_arrays, expand_dims, squeeze

Changing kind of array
======================
.. autosummary::
   :toctree: generated/

.. todo:: asarray, asanyarray, asmatrix, asfarray, asfortranarray, asscalar, require

Joining arrays
==============
.. autosummary::
   :toctree: generated/

   hstack
   vstack

.. todo:: column_stack, concatenate, dstack

Splitting arrays
================
.. autosummary::
   :toctree: generated/

.. todo:: array_split, dsplit, hsplit, split, vsplit

Tiling arrays
=============
.. autosummary::
   :toctree: generated/

.. todo:: tile, repeat

Adding and removing elements
============================
.. autosummary::
   :toctree: generated/

   unique

.. todo:: delete, insert, append, resize, trim_zeros

Rearranging elements
====================
.. autosummary::
   :toctree: generated/

.. todo:: fliplr, flipud, roll, rot90

Window functions
================

`window` is a wrapper of the flowwing numpy's window functions.

.. autosummary::
    :toctree: generated/

    bartlett
    blackman
	hamming
	hanning
    kaiser

Utilities
=========

`axis_rotation_matrix`: Create a 4x4 matrix that represents a rotation around one axis


Comparison functions
--------------------
.. warning::

    Do not use the Python keywords ``and`` and ``or`` to combine
    logical array expressions. These keywords will test the truth
    value of the entire array (not element-by-element as you might
    expect). Use the bitwise operators & and \| instead.

.. warning::

    The bit-wise operators & and \| are the proper way to perform
    element-by-element array comparisons. Be sure you understand the
    operator precedence: ``(a > 2) & (a < 5)`` is the proper syntax because
    ``a > 2 & a < 5`` will result in an error due to the fact that ``2 & a``
    is evaluated first.

