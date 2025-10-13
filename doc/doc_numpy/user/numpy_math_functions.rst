Mathematical functions
#####################

The reference documentation is generated from numpy files, see also `API reference` on
`Numpy <https://numpy.org/>`_

.. currentmodule:: numpy

Trigonometric functions
-----------------------
All trigonometric functions use radians when an angle is called for.
The ratio of degrees to radians is :math:`180^{\circ}/\pi.`

.. autosummary::
   :toctree: generated/

   sin
   cos
   tan
   arcsin
   arccos
   arctan
   degrees
   radians
   deg2rad
   rad2deg

.. todo:: arctan2, hypot, unwrap

Hyperbolic functions
--------------------
.. autosummary::
   :toctree: generated/

   sinh
   cosh
   tanh
   arcsinh
   arccosh
   arctanh

Rounding
--------
.. autosummary::
   :toctree: generated/

   rint
   floor
   ceil
   trunc

.. todo:: around, fix

Sums, products, differences
---------------------------
.. autosummary::
   :toctree: generated/

   sum
   cumprod
   cumsum
   diff
   cross

.. todo:: prod, nansum, ediff1d, gradient, trapz

Exponents and logarithms
------------------------
.. autosummary::
   :toctree: generated/

   exp
   expm1
   exp2
   log
   log10

.. todo:: log2, log1p, logaddexp, logaddexp2

Arithmetic operations
---------------------
.. autosummary::
    :toctree: generated/

    add
    multiply

.. todo:: reciprocal, negative, divide, power, subtract, true_divide, floor_divide, fmod, mod, modf, remainder

Miscellaneous
-------------
.. autosummary::
    :toctree: generated/

    convolve
    clip
    sqrt
    square
    absolute
    fabs
    sign
    maximum
    minimum
    dtype
    dtype.itemsize

.. tip::

    The Python function ``max()`` will find the maximum over a one-dimensional
    array, but it will do so using a slower sequence interface. The reduce
    method of the maximum ufunc is much faster. Also, the ``max()`` method
    will not give answers you might expect for arrays with greater than
    one dimension. The reduce method of minimum also allows you to compute
    a total minimum over an array.

.. warning::

    the behavior of ``maximum(a, b)`` is different than that of ``max(a, b)``.
    As a ufunc, ``maximum(a, b)`` performs an element-by-element comparison
    of `a` and `b` and chooses each element of the result according to which
    element in the two arrays is larger. In contrast, ``max(a, b)`` treats
    the objects `a` and `b` as a whole, looks at the (total) truth value of
    ``a > b`` and uses it to return either `a` or `b` (as a whole). A similar
    difference exists between ``minimum(a, b)`` and ``min(a, b)``.

.. todo:: nan_to_num, real_if_close, interp

Array operations
----------------
.. autosummary::
    :toctree: generated/

    linalg.inv
    std
    dot
    outer
    mean
    putmask
    shape
    ndim
    size

Random functions
----------------
.. autosummary::
    :toctree: generated/

    random.rand
    random.randn
    random.random
    random.standard_normal
    random.uniform

Sorting, searching
------------------
.. autosummary::
    :toctree: generated/

    searchsorted
    where
