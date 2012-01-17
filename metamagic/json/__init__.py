##
# Copyright (c) 2012 Sprymix Inc.
# All rights reserved.
#
# See LICENSE for details.
##


try:
    from ._encoder import Encoder
except ImportError:
    from .encoder import Encoder


def dumps(obj, encoder=Encoder):
    '''Returns a JSON representation of ``obj`` in a Python string.

       Uses the given Encoder class which is supposed to have a ``dumps`` method.

       By default tries to use the C version of the Encoder class from the
       ``_encoder`` module. If there is no C version uses the Python version
       from the ``encoder`` module.

       See documentation for the given Encoder class for details.

       **Examples**:

       .. code-block:: pycon

           >>> dumps(True)
           'true'

           >>> dumps('foo')
           '"foo"'

       Using custom __sx_serialize__:

       .. code-block:: pycon

           >>> class Foo:
           ... def __sx_serialize__(self):
           ...     return 'foo'

           >>> dumps(Foo())
           '"foo"'
    '''
    return Encoder().dumps(obj)

def dumpb(obj, encoder=Encoder):
    '''Returns a JSON representation of ``obj`` in a bytes() array.

       Uses the given Encoder class which is supposed to have a ``dumpb`` method.

       By default tries to use the C version of the Encoder class from the
       ``_encoder`` module. If there is no C version uses the Python version
       from the ``encoder`` module.

       See documentation for the given Encoder class for details.

       **Examples**:

       .. code-block:: pycon

           >>> dumpb(True)
           b'true'
    '''
    return Encoder().dumpb(obj)
