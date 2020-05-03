# -*- coding: utf-8 -*-
# WARNING: Autogenerated code. Do not edit manually.


class Getblockchaininfo:
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self.bestblockhash = kwargs["bestblockhash"]
        self.blocks = kwargs["blocks"]
        self.chain = kwargs["chain"]
        self.chainname = kwargs["chainname"]
        self.chainrewards = kwargs["chainrewards"]
        self.chainwork = kwargs["chainwork"]
        self.description = kwargs["description"]
        self.difficulty = kwargs["difficulty"]
        self.headers = kwargs["headers"]
        self.protocol = kwargs["protocol"]
        self.reindex = kwargs["reindex"]
        self.setupblocks = kwargs["setupblocks"]
        self.verificationprogress = kwargs["verificationprogress"]

    def as_dict(self):
        return self._kwargs

    def __repr__(self):
        return repr(self._kwargs)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._kwargs == other._kwargs
        else:
            return False


class Getmempoolinfo:
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self.bytes = kwargs["bytes"]
        self.size = kwargs["size"]

    def as_dict(self):
        return self._kwargs

    def __repr__(self):
        return repr(self._kwargs)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._kwargs == other._kwargs
        else:
            return False


class Gettxoutsetinfo:
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self.bestblock = kwargs["bestblock"]
        self.bytes_serialized = kwargs["bytes_serialized"]
        self.hash_serialized = kwargs["hash_serialized"]
        self.height = kwargs["height"]
        self.total_amount = kwargs["total_amount"]
        self.transactions = kwargs["transactions"]
        self.txouts = kwargs["txouts"]

    def as_dict(self):
        return self._kwargs

    def __repr__(self):
        return repr(self._kwargs)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._kwargs == other._kwargs
        else:
            return False


class Getinfo:
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self.balance = kwargs["balance"]
        self.blocks = kwargs["blocks"]
        self.burnaddress = kwargs["burnaddress"]
        self.chainname = kwargs["chainname"]
        self.connections = kwargs["connections"]
        self.description = kwargs["description"]
        self.difficulty = kwargs["difficulty"]
        self.edition = kwargs["edition"]
        self.errors = kwargs["errors"]
        self.incomingpaused = kwargs["incomingpaused"]
        self.keypoololdest = kwargs["keypoololdest"]
        self.keypoolsize = kwargs["keypoolsize"]
        self.miningpaused = kwargs["miningpaused"]
        self.nodeaddress = kwargs["nodeaddress"]
        self.nodeversion = kwargs["nodeversion"]
        self.offchainpaused = kwargs["offchainpaused"]
        self.paytxfee = kwargs["paytxfee"]
        self.port = kwargs["port"]
        self.protocol = kwargs["protocol"]
        self.protocolversion = kwargs["protocolversion"]
        self.proxy = kwargs["proxy"]
        self.reindex = kwargs["reindex"]
        self.relayfee = kwargs["relayfee"]
        self.setupblocks = kwargs["setupblocks"]
        self.testnet = kwargs["testnet"]
        self.timeoffset = kwargs["timeoffset"]
        self.version = kwargs["version"]
        self.walletdbversion = kwargs["walletdbversion"]
        self.walletversion = kwargs["walletversion"]

    def as_dict(self):
        return self._kwargs

    def __repr__(self):
        return repr(self._kwargs)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._kwargs == other._kwargs
        else:
            return False


class Getinitstatus:
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self.initialized = kwargs["initialized"]
        self.nodeversion = kwargs["nodeversion"]
        self.version = kwargs["version"]

    def as_dict(self):
        return self._kwargs

    def __repr__(self):
        return repr(self._kwargs)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._kwargs == other._kwargs
        else:
            return False


class Getruntimeparams:
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self.acceptfiltertimeout = kwargs["acceptfiltertimeout"]
        self.autocombinedelay = kwargs["autocombinedelay"]
        self.autocombinemaxinputs = kwargs["autocombinemaxinputs"]
        self.autocombineminconf = kwargs["autocombineminconf"]
        self.autocombinemininputs = kwargs["autocombinemininputs"]
        self.autocombinesuspend = kwargs["autocombinesuspend"]
        self.autosubscribe = kwargs["autosubscribe"]
        self.bantx = kwargs["bantx"]
        self.gen = kwargs["gen"]
        self.genproclimit = kwargs["genproclimit"]
        self.handshakelocal = kwargs["handshakelocal"]
        self.hideknownopdrops = kwargs["hideknownopdrops"]
        self.lockadminminerounds = kwargs["lockadminminerounds"]
        self.lockblock = kwargs["lockblock"]
        self.lockinlinemetadata = kwargs["lockinlinemetadata"]
        self.maxqueryscanitems = kwargs["maxqueryscanitems"]
        self.maxshowndata = kwargs["maxshowndata"]
        self.mineemptyrounds = kwargs["mineemptyrounds"]
        self.miningrequirespeers = kwargs["miningrequirespeers"]
        self.miningturnover = kwargs["miningturnover"]
        self.port = kwargs["port"]
        self.reindex = kwargs["reindex"]
        self.rescan = kwargs["rescan"]
        self.sendfiltertimeout = kwargs["sendfiltertimeout"]
        self.txindex = kwargs["txindex"]
        self.v1apicompatible = kwargs["v1apicompatible"]

    def as_dict(self):
        return self._kwargs

    def __repr__(self):
        return repr(self._kwargs)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._kwargs == other._kwargs
        else:
            return False


class Getmininginfo:
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self.blocks = kwargs["blocks"]
        self.chain = kwargs["chain"]
        self.currentblocksize = kwargs["currentblocksize"]
        self.currentblocktx = kwargs["currentblocktx"]
        self.difficulty = kwargs["difficulty"]
        self.errors = kwargs["errors"]
        self.generate = kwargs["generate"]
        self.genproclimit = kwargs["genproclimit"]
        self.hashespersec = kwargs["hashespersec"]
        self.networkhashps = kwargs["networkhashps"]
        self.pooledtx = kwargs["pooledtx"]
        self.testnet = kwargs["testnet"]

    def as_dict(self):
        return self._kwargs

    def __repr__(self):
        return repr(self._kwargs)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._kwargs == other._kwargs
        else:
            return False


class Getchunkqueueinfo:
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self.bytes = kwargs["bytes"]
        self.chunks = kwargs["chunks"]

    def as_dict(self):
        return self._kwargs

    def __repr__(self):
        return repr(self._kwargs)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._kwargs == other._kwargs
        else:
            return False


class Getchunkqueuetotals:
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self.bytes = kwargs["bytes"]
        self.chunks = kwargs["chunks"]

    def as_dict(self):
        return self._kwargs

    def __repr__(self):
        return repr(self._kwargs)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._kwargs == other._kwargs
        else:
            return False


class Getnettotals:
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self.timemillis = kwargs["timemillis"]
        self.totalbytesrecv = kwargs["totalbytesrecv"]
        self.totalbytessent = kwargs["totalbytessent"]

    def as_dict(self):
        return self._kwargs

    def __repr__(self):
        return repr(self._kwargs)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._kwargs == other._kwargs
        else:
            return False


class Getnetworkinfo:
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self.connections = kwargs["connections"]
        self.localaddresses = kwargs["localaddresses"]
        self.localservices = kwargs["localservices"]
        self.networks = kwargs["networks"]
        self.protocolversion = kwargs["protocolversion"]
        self.relayfee = kwargs["relayfee"]
        self.subversion = kwargs["subversion"]
        self.timeoffset = kwargs["timeoffset"]
        self.version = kwargs["version"]

    def as_dict(self):
        return self._kwargs

    def __repr__(self):
        return repr(self._kwargs)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._kwargs == other._kwargs
        else:
            return False


class Getwalletinfo:
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self.balance = kwargs["balance"]
        self.keypoololdest = kwargs["keypoololdest"]
        self.keypoolsize = kwargs["keypoolsize"]
        self.txcount = kwargs["txcount"]
        self.utxocount = kwargs["utxocount"]
        self.walletdbversion = kwargs["walletdbversion"]
        self.walletversion = kwargs["walletversion"]

    def as_dict(self):
        return self._kwargs

    def __repr__(self):
        return repr(self._kwargs)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._kwargs == other._kwargs
        else:
            return False
