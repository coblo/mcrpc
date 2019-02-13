=====
mcrpc
=====

|status| |license|

.. |status| image:: https://img.shields.io/pypi/v/mcrpc.svg
   :target: https://pypi.python.org/pypi/mcrpc/
   :alt: PyPI Status
.. |license| image:: https://img.shields.io/pypi/l/mcrpc.svg
   :target: https://pypi.python.org/pypi/mcrpc/
   :alt: PyPI License


Content Blockchain RPC Client
=============================

A Python 3 MultiChain RPC client build for the `Content Blockchain Project <https://content-blockchain.org/>`_

This client is build against the API of the v2.0 beta 2 build (February 11, 2019) of `MultiChain <https://www.multichain.com/download-install/>`_ and includes code generated function annotations and api documentation to support code completion and get you up to speed fast.


Code Completion
---------------

.. figure:: https://raw.githubusercontent.com/coblo/mcrpc/master/images/mcrpc_cc.png
   :align: center
   :alt: mcrpc code completaion


Code Documentation
------------------

.. figure:: https://raw.githubusercontent.com/coblo/mcrpc/master/images/mcrpc_doc.png
   :align: center
   :alt: mcrpc documentation


Installing
==========

The RPC client is published with the package name `mcrpc <https://pypi.python.org/pypi/mcrpc>`_ on Python Package Index. Install it with:

.. code-block:: bash

    pip install mcrpc


Release History
===============

1.0.2 (2019-02-13)
------------------

* Fix signature of appendrawexchange and completerawexchange
* Build rpc client against Multichain 2 Beta 2
* Add pretty-print support for response objects
* Sort response class properties for cleaner diffs on updates
