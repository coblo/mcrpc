# mcrpc - Multichain RPC client

[![Version](https://img.shields.io/pypi/v/mcrpc.svg)](https://pypi.python.org/pypi/mcrpc/)
[![Downloads](https://pepy.tech/badge/mcrpc)](https://pepy.tech/project/mcrpc)


## Content Blockchain RPC Client

A Python 3 MultiChain RPC client build for the 
[Content Blockchain Project](https://content-blockchain.org/)

The versioning scheme follows [MultiChain](https://www.multichain.com/download-community/)
and includes code generated function annotations and api documentation to support code 
completion and get you up to speed fast.


## Code Completion

![mcrpc code completaion](https://raw.githubusercontent.com/coblo/mcrpc/master/images/mcrpc_cc.png)


## Code Documentation

![mcrpc documentation](https://raw.githubusercontent.com/coblo/mcrpc/master/images/mcrpc_doc.png)


## Installing

The RPC client is published with the package name [mcrpc](https://pypi.python.org/pypi/mcrpc) 
on Python Package Index. Install it with:

```console
$ pip3 install mcrpc
```

## Change Log

### 1.0.2 (2019-02-13)
- Fix signature of appendrawexchange and completerawexchange
- Build rpc client against Multichain 2 Beta 2
- Add pretty-print support for response objects
- Sort response class properties for cleaner diffs on updates