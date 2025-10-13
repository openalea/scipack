List of Numpy functionalities available as VisuAlea nodes
#########################################################

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

Other special functions
-----------------------
.. autosummary::
   :toctree: generated/

.. todo:: i0, sinc

Floating point routines
-----------------------
.. autosummary::
   :toctree: generated/

.. todo:: signbit, copysign, frexp, ldexp

Arithmetic operations
---------------------
.. autosummary::
    :toctree: generated/

    add
    multiply

.. todo:: reciprocal, negative, divide, power, subtract, true_divide, floor_divide, fmod, mod, modf, remainder

Handling complex numbers
------------------------
.. autosummary::
   :toctree: generated/

.. todo:: angle, real, imag, conj

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
