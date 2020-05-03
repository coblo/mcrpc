# -*- coding: utf-8 -*-
from os import listdir
from os.path import exists, join
from typing import List, Optional
import appdirs
from configobj import ConfigObj


DATADIR = appdirs.user_data_dir("multichain", appauthor="", roaming=True)


def read_chains() -> List[str]:
    """Returns a list of chains installed on the system."""
    chains = []
    for maybe_chain_dir in listdir(DATADIR):
        if exists(join(DATADIR, maybe_chain_dir, "multichain.conf")):
            chains.append(maybe_chain_dir)
    return chains


def read_node_config(chain: str) -> ConfigObj:
    """Read node configuration from multichain.conf"""
    conf_path = join(DATADIR, chain, "multichain.conf")
    return ConfigObj(conf_path)


def read_chain_params(chain: str) -> ConfigObj:
    """Read chain params from params.dat file"""
    conf_path = join(DATADIR, chain, "params.dat")
    return ConfigObj(conf_path)


def autoconnect(chain: Optional[str] = None) -> Optional["RpcClient"]:
    """Return RPC client for chain from on-disk information.

    If no chain-name is passed it will return the first one found.
    """
    import mcrpc

    if chain is None:
        try:
            chain = read_chains()[0]
        except IndexError:
            return None
    params = read_chain_params(chain)
    config = read_node_config(chain)
    host = config.get("rpcbind") or "127.0.0.1"
    port = config.get("rpcport") or params["default-rpc-port"]
    user = config["rpcuser"]
    pwd = config["rpcpassword"]
    client = mcrpc.RpcClient(host, port, user, pwd)
    # Test client connection before returning
    try:
        client.getinfo()
    except Exception:
        return None
    return client
