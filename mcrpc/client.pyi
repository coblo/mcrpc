# -*- coding: utf-8 -*-
import typing as t


class RpcClient:

    def __init__(self, host: str, port: str, user: str, pwd: str, use_ssl: bool=False):
        self.host: str
        self.port: str
        self.user: str
        self.pwd: str
        self.use_ssl: bool

    def _url(self) -> str: ...

    def _call(self, method: str, *args) -> t.Dict: ...

    def _get_methods(self) -> t.List[str]: ...

    def addmultisigaddress(self, nrequired: int, keys: t.List[str]) -> str:
        """
        addmultisigaddress nrequired keys ( "account" )

        Add a nrequired-to-sign multisignature address to the wallet.
        Each key is a address or hex-encoded public key.
        If 'account' is specified, assign address to that account.

        Arguments:
        1. nrequired                        (numeric, required) The number of required signatures out of the n keys or addresses.
        2. keys                             (array, required) A json array of addresses or hex-encoded public keys
             [
               "address"                    (string) address or hex-encoded public key
               ...,
             ]
        3. "account"                        (string, optional) An account to assign the addresses to.

        Result:
        "address"                           (string) A address associated with the keys.

        Examples:

        Add a multisig address from 2 addresses
        > multichain-cli testchain addmultisigaddress 2 "[\"16sSauSf5pF2UkUwvKGq4qjNRzBZYqgEL5\",\"171sgjn4YtPu27adkKGrdDwzRTxnRkBfKV\"]"

        As json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "addmultisigaddress", "params": [2, "[\"16sSauSf5pF2UkUwvKGq4qjNRzBZYqgEL5\",\"171sgjn4YtPu27adkKGrdDwzRTxnRkBfKV\"]"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def addnode(self, node: str, command:str) -> None:
        """
        addnode "node" "add"|"remove"|"onetry"

        Attempts add or remove a node from the addnode list.
        Or try a connection to a node once.

        Arguments:
        1. "node"                           (string, required) The node (see getpeerinfo for nodes)
        2. "command"                        (string, required) 'add' to add a node to the list, 'remove' to remove a node from the list,
                                                               'onetry' to try a connection to the node once

        Examples:
        > multichain-cli testchain addnode "192.168.0.6:8333" "onetry"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "addnode", "params": ["192.168.0.6:8333", "onetry"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def appendrawchange(self, tx_hex: str, address: str, native_fee=None) -> str:
        """
        appendrawchange "tx-hex" "address" ( native-fee )

        Appends change output to raw transaction, containing any remaining assets / 
        native currency in the inputs that are not already sent to other outputs.

        Arguments:
        1. "tx-hex"                         (string, required) The hex string of the raw transaction)
        2. "address"                        (string, required) The address to send the change to.
        3. native-fee                       (numeric, optional) Native currency value deducted from that amount so it becomes a transaction fee.
                                                                Default - calculated automatically

        Result:
        "transaction"                       (string) hex string of the transaction

        Examples:
        > multichain-cli testchain appendrawchange "hex""1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 
        > multichain-cli testchain appendrawchange "hex""1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.01
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "appendrawchange", "params": ["hex" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def appendrawdata(self, *args) -> t.Dict:
        """
        appendrawdata tx-hex data 

        Appends new OP_RETURN output to existing raw transaction
        Returns hex-encoded raw transaction.

        Arguments:
        1. "tx-hex"                           (string, required) The transaction hex string
        2. data                               (string or object, required) Data, see help data-all for details.

        Result:
        "transaction"                         (string) hex string of the transaction

        Examples:
        > multichain-cli testchain appendrawdata "tx-hexstring" 48656C6C6F20576F726C64210A
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "appendrawdata", "params": ["tx-hexstring","48656C6C6F20576F726C64210A"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def appendrawexchange(self, *args) -> t.Dict:
        """
        appendrawexchange "hex" "txid" vout ask-assets 

        Adds to the raw atomic exchange transaction in tx-hex given by a previous call to createrawexchange or appendrawexchange. 

        Arguments:
        1. "hex"                            (string, required) The transaction hex string
        2. "txid"                           (string, required) Transaction ID of the output prepared by preparelockunspent.
        3. vout                             (numeric, required) Output index
        4. ask-assets                       (object, required) A json object of assets to ask
            {
              "asset-identifier" : asset-quantity
              ,...
            }

        Result:
        {
          "hex": "value",                   (string) The raw transaction with signature(s) (hex-encoded string)
          "complete": true|false            (boolean) if exchange is completed and can be sent 
        }

        Examples:
        > multichain-cli testchain appendrawexchange "hexstring" f4c3dd510dd55761015c9d96bff7793b0d501dd6f01a959fd7dd02478fb47dfb 1 "{\"1234-5678-1234\":200}"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "appendrawexchange", "params": ["hexstring","f4c3dd510dd55761015c9d96bff7793b0d501dd6f01a959fd7dd02478fb47dfb",1,"{\"1234-5678-1234\":200}\"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def appendrawtransaction(self, *args) -> t.Dict:
        """
        appendrawtransaction "tx-hex" [{"txid":"id","vout":n},...] ( {"address":amount,...} [data] "action" ) 

        Append inputs and outputs to raw transaction

        Arguments:
        1. "tx-hex"                               (string, required) Source transaction hex string
        2. transactions                           (array, required) A json array of json objects
             [
               {
                 "txid":"id",                     (string, required) The transaction id
                 "vout":n                         (numeric, required) The output number
                 "scriptPubKey": "hex",           (string, optional) script key, used if cache=true or action=sign
                 "redeemScript": "hex"            (string, optional) redeem script, used if action=sign
                 "cache":true|false               (boolean, optional) If true - add cached script to tx, if omitted - add automatically if needed
               }
               ,...
             ]
        3. addresses                              (object, required) Object with addresses as keys, see help addresses-all for details.
        4. data                                   (array, optional) Array of hexadecimal strings or data objects, see help data-all for details.
        5."action"                                (string, optional, default "") Additional actions: "lock", "sign", "lock,sign", "sign,lock", "send". 

        Result:
        "transaction"                             (string) hex string of the transaction (if action= "" or "lock")
          or 
        {                                         (object) A json object (if action= "sign" or "lock,sign" or "sign,lock")
          "hex": "value",                         (string) The raw transaction with signature(s) (hex-encoded string)
          "complete": true|false                  (boolean) if transaction has a complete set of signature (0 if not)
        }
          or 
        "hex"                                     (string) The transaction hash in hex (if action= "send")

        Examples
        > multichain-cli testchain appendrawtransaction "hexstring" "[{\"txid\":\"myid\",\"vout\":0}]" "{\"address\":0.01}"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "appendrawtransaction", "params": ["hexstring", "[{\"txid\":\"myid\",\"vout\":0}]", "{\"address\":0.01}"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def approvefrom(self, *args) -> t.Dict:
        """
        approvefrom "from-address" "upgrade-identifier" ( approve )

        Approve upgrade using specific address.

        Arguments:
        1. "from-address"                   (string, required) Address used for approval.
        2. "upgrade-identifier"             (string, required) Upgrade identifier - one of the following: upgrade txid, upgrade name.
        3. approve                          (boolean, required)  Approve or disapprove

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain approvefrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "upgrade1"
        > multichain-cli testchain approvefrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "upgrade1" false
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "approvefrom", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "upgrade1", true] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def backupwallet(self, *args) -> t.Dict:
        """
        backupwallet "destination"

        Safely copies wallet.dat to destination, which can be a directory or a path with filename.

        Arguments:
        1. "destination"                  (string) The destination directory or file

        Examples:
        > multichain-cli testchain backupwallet "backup.dat"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "backupwallet", "params": ["backup.dat"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def clearmempool(self) -> t.Dict:
        """
        clearmempool 

        Removes all transactions from the TX memory pool.
        Local mining and the processing of incoming transactions and blocks should be paused.

        Examples:
        > multichain-cli testchain clearmempool 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "clearmempool", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def combineunspent(self, *args) -> t.Dict:
        """
        combineunspent ( "address(es)" minconf maxcombines mininputs maxinputs maxtime )

        Optimizes wallet performance by combining unspent txouts.

        Arguments:
        1. "address(es)"                    (string, optional) Addresses to optimize (comma delimited). Default - "*", all.
        2. minconf                          (numeric, optional) The minimum confirmations to filter. Default - 1
        3. maxcombines                      (numeric, optional) Maximal number of transactions to send. Default - 100
        4. mininputs                        (numeric, optional) Minimal number of txouts to combine in one transaction. Default - 2
        5. maxinputs                        (numeric, optional) Maximal number of txouts to combine in one transaction. Default - 100
        6. maxtime                          (numeric, optional) Maximal time for creating combining transactions, at least one transaction will be sent. Default - 15s

        Result:
        "transactionids"                    (array) Array of transaction ids.

        Examples:
        > multichain-cli testchain combineunspent "*" 1 100 5 20 120
        > multichain-cli testchain combineunspent "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "combineunspent", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd",1,100, 5, 20, 120] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def completerawexchange(self, *args) -> t.Dict:
        """
        completerawexchange hex txid vout ask-assets ( data|publish-new-stream-item ) 

        Completes existing exchange transaction, adds fee if needed
        Returns hex-encoded raw transaction.

        Arguments:
        1. "hex"                            (string, required) The transaction hex string
        2. "txid"                           (string, required) Transaction ID of the output prepared by preparelockunspent.
        3. "vout"                           (numeric, required) Output index
        4. "ask-assets"                     (object, required) A json object of assets to ask
            {
              "asset-identifier" : asset-quantity
              ,...
            }
        5. data|publish-new-stream-item     (string or object, optional) Data, see help data-with for details. 

        Result:
        "transaction"                       (string) hex string of the transaction

        Examples:
        > multichain-cli testchain completerawexchange "hexstring" f4c3dd510dd55761015c9d96bff7793b0d501dd6f01a959fd7dd02478fb47dfb 1 "{\"1234-5678-1234\":200}"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "completerawexchange", "params": ["hexstring","f4c3dd510dd55761015c9d96bff7793b0d501dd6f01a959fd7dd02478fb47dfb",1,"{\"1234-5678-1234\":200}\"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def create(self, entity_type: str, entity_name: str, open: bool, custom_fields: t.Optional[dict]=None) -> str:
        """
        create "entity-type" "entity-name" open ( custom-fields )

        Creates stream or upgrade

        Arguments:
        1. "entity-type"                    (string, required) stream
        2. "stream-name"                    (string, required) Stream name, if not "" should be unique.
        3. open                             (boolean, required ) Allow anyone to publish in this stream
        4  custom-fields                    (object, optional)  a json object with custom fields
            {
              "param-name": "param-value"   (strings, required) The key is the parameter name, the value is parameter value
              ,...
            }
          or 
        1. "entity-type"                    (string, required) upgrade
        2. "upgrade-name"                   (string, required) Upgrade name, if not "" should be unique.
        3. open                             (boolean, required ) Should be false
        4  custom-fields                    (object, required)  a json object with custom fields
            {
              "protocol-version": version   (numeric, optional) Protocol version to upgrade to
              "parameter-name": value       (numeric, optional) New value for upgradable parameter, one of the following: 
                                                                target-block-time,
                                                                maximum-block-size,
                                                                max-std-tx-size,
                                                                max-std-op-returns-count,
                                                                max-std-op-return-size,
                                                                max-std-op-drops-count,
                                                                max-std-element-size
              "startblock": block           (numeric, optional, default 0) Block to apply from 
              ,...
            }

        Result:
        "transactionid"  (string) The transaction id.

        Examples:
        > multichain-cli testchain create stream test false 
        > multichain-cli testchain create stream test false '{"Description":"Test stream"}'
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "create", "params": ["stream", "test", false] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def createfrom(self, *args) -> t.Dict:
        """
        createfrom "from-address" "entity-type" "entity-name" open ( custom-fields )

        Creates stream using specific address

        Arguments:
        1. "from-address"                   (string, required) Address used for creating.
        2. entity-type                      (string, required) stream
        3. "stream-name"                    (string, required) Stream name, if not "" should be unique.
        4. open                             (boolean, required) Allow anyone to publish in this stream
        5  custom-fields                    (object, optional)  a json object with custom fields
            {
              "param-name": "param-value"   (strings, required) The key is the parameter name, the value is parameter value
              ,...
            }
          or 
        1. "from-address"                   (string, required) Address used for creating.
        2. entity-type                      (string, required) upgrade
        3. "upgrade-name"                   (string, required) Upgrade name, if not "" should be unique.
        4. open                             (boolean, required ) Should be false
        5  custom-fields                    (object, required)  a json object with custom fields
            {
              "protocol-version": version   (numeric, optional) Protocol version to upgrade to 
              "parameter-name": value       (numeric, optional) New value for upgradable parameter, one of the following: 
                                                                target-block-time,
                                                                maximum-block-size,
                                                                max-std-tx-size,
                                                                max-std-op-returns-count,
                                                                max-std-op-return-size,
                                                                max-std-op-drops-count,
                                                                max-std-element-size
              "start-block": block          (numeric, optional, default 0) Block to apply from 
              ,...
            }

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain createfrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" stream test false 
        > multichain-cli testchain createfrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" stream test false '{"Description":"Test stream"}'
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "createfrom", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "stream", "test", false] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def createkeypairs(self, *args) -> t.Dict:
        """
        createkeypairs ( count )

        Creates public/private key pairs. These key pairs are not stored in the wallet.

        Arguments: 
        1. count                            (number, optional, default=1) Number of pairs to create.

        Result:
        [                                   (json array of )
           {
              "address" : "address",        (string) Pay-to-pubkeyhash address
              "pubkey"  : "pubkey",         (string) Public key (hexadecimal)
              "privkey" : "privatekey",     (string) Private key, base58-encoded as required for signrawtransaction
          }
        ]

        Examples:
        > multichain-cli testchain createkeypairs 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "createkeypairs", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def createmultisig(self, *args) -> t.Dict:
        """
        createmultisig nrequired keys

        Creates a multi-signature address with n signature of m keys required.
        It returns a json object with the address and redeemScript.

        Arguments:
        1. nrequired                        (numeric, required) The number of required signatures out of the n keys or addresses.
        2. keys                             (array, required) A json array of keys which are addresses or hex-encoded public keys
             [
               "key"                        (string) address or hex-encoded public key
               ,...
             ]

        Result:
        {
          "address":"multisigaddress",      (string) The value of the new multisig address.
          "redeemScript":"script"           (string) The string value of the hex-encoded redemption script.
        }

        Examples:

        Create a multisig address from 2 addresses
        > multichain-cli testchain createmultisig 2 "[\"16sSauSf5pF2UkUwvKGq4qjNRzBZYqgEL5\",\"171sgjn4YtPu27adkKGrdDwzRTxnRkBfKV\"]"

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "createmultisig", "params": [2, "[\"16sSauSf5pF2UkUwvKGq4qjNRzBZYqgEL5\",\"171sgjn4YtPu27adkKGrdDwzRTxnRkBfKV\"]"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def createrawexchange(self, *args) -> t.Dict:
        """
        createrawexchange "txid" vout ask-assets

        Creates new exchange transaction
        Note that the transaction should be completed by appendrawexchange

        Arguments:
        1. "txid"                           (string, required) Transaction ID of the output prepared by preparelockunspent.
        2. vout                             (numeric, required) Output index
        3. ask-assets                       (object, required) A json object of assets to ask
            {
              "asset-identifier" : asset-quantity
              ,...
            }

        Result:
        "transaction"                       (string) hex string of the transaction

        Examples:
        > multichain-cli testchain createrawexchange f4c3dd510dd55761015c9d96bff7793b0d501dd6f01a959fd7dd02478fb47dfb 1 "{\"1234-5678-1234\":200}"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "createrawexchange", "params": ["f4c3dd510dd55761015c9d96bff7793b0d501dd6f01a959fd7dd02478fb47dfb",1,"{\"1234-5678-1234\":200}\"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def createrawsendfrom(self, *args) -> t.Dict:
        """
        createrawsendfrom "from-address" {"address":amount,...} ( [data] "action" ) 

        Create a transaction using the given sending address.

        Arguments:
        1. "from-address"                           (string, required) Address to send from.
        2. addresses                                (object, required) Object with addresses as keys, see help addresses-all for details.
        3. data                                     (array, optional) Array of hexadecimal strings or data objects, see help data-all for details.
        4. "action"                                 (string, optional, default "") Additional actions: "lock", "sign", "lock,sign", "sign,lock", "send". 

        Result:
        "transaction"                               (string) hex string of the transaction (if action= "" or "lock")
          or 
        {                                           (object) A json object (if action= "sign" or "lock,sign" or "sign,lock")
          "hex": "value",                           (string) The raw transaction with signature(s) (hex-encoded string)
          "complete": true|false                    (boolean) if transaction has a complete set of signature (0 if not)
        }
          or 
        "hex"                                       (string) The transaction hash in hex (if action= "send")

        Examples
        > multichain-cli testchain createrawsendfrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "{\"address\":0.01}"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "createrawsendfrom", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "{\"address\":0.01}"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def createrawtransaction(self, *args) -> t.Dict:
        """
        createrawtransaction [{"txid":"id","vout":n},...] {"address":amount,...} ( [data] "action" ) 

        Create a transaction spending the given inputs.

        Arguments:
        1. transactions                           (array, required) A json array of json objects
             [
               {
                 "txid":"id",                     (string, required) The transaction id
                 "vout":n                         (numeric, required) The output number
                 "scriptPubKey": "hex",           (string, optional) script key, used if cache=true or action=sign
                 "redeemScript": "hex"            (string, optional) redeem script, used if action=sign
                 "cache":true|false               (boolean, optional) If true - add cached script to tx, if omitted - add automatically if needed
               }
               ,...
             ]
        2. addresses                              (object, required) Object with addresses as keys, see help addresses-all for details.
        3. data                                   (array, optional) Array of hexadecimal strings or data objects, see help data-all for details.
        4. "action"                               (string, optional, default "") Additional actions: "lock", "sign", "lock,sign", "sign,lock", "send". 

        Result:
        "transaction"                             (string) hex string of the transaction (if action= "" or "lock")
          or 
        {                                         (object) A json object (if action= "sign" or "lock,sign" or "sign,lock")
          "hex": "value",                         (string) The raw transaction with signature(s) (hex-encoded string)
          "complete": true|false                  (boolean) if transaction has a complete set of signature (0 if not)
        }
          or 
        "hex"                                     (string) The transaction hash in hex (if action= "send")

        Examples
        > multichain-cli testchain createrawtransaction "[{\"txid\":\"myid\",\"vout\":0}]" "{\"address\":0.01}"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "createrawtransaction", "params": ["[{\"txid\":\"myid\",\"vout\":0}]", "{\"address\":0.01}"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def decoderawexchange(self, *args) -> t.Dict:
        """
        decoderawexchange "tx-hex" ( verbose )

        Return a JSON object representing the serialized, hex-encoded exchange transaction.

        Arguments:
        1. "tx-hex"                         (string, required) The exchange transaction hex string
        2. verbose                          (boolean, optional, default=false) If true, returns array of all exchanges
                                                                               created by createrawexchange or appendrawexchange

        Results is an object with exchange details

        Examples:
        > multichain-cli testchain decoderawexchange "hexstring"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "decoderawexchange", "params": ["hexstring"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def decoderawtransaction(self, *args) -> t.Dict:
        """
        decoderawtransaction "tx-hex"

        Return a JSON object representing the serialized, hex-encoded transaction.

        Arguments:
        1. "tx-hex"                                     (string, required) The transaction hex string

        Result:
        {
          "txid" : "id",                                (string) The transaction id
          "version" : n,                                (numeric) The version
          "locktime" : ttt,                             (numeric) The lock time
          "vin" : [                                     (array of json objects)
             {
               "txid": "id",                            (string) The transaction id
               "vout": n,                               (numeric) The output number
               "scriptSig": {                           (json object) The script
                 "asm": "asm",                          (string) asm
                 "hex": "hex"                           (string) hex
               },
               "sequence": n                            (numeric) The script sequence number
             }
             ,...
          ],
          "vout" : [                                    (array of json objects)
             {
               "value" : x.xxx,                         (numeric) The value in btc
               "n" : n,                                 (numeric) index
               "scriptPubKey" : {                       (json object)
                 "asm" : "asm",                         (string) the asm
                 "hex" : "hex",                         (string) the hex
                 "reqSigs" : n,                         (numeric) The required sigs
                 "type" : "pubkeyhash",                 (string) The type, eg 'pubkeyhash'
                 "addresses" : [                        (json array of string)
                   "12tvKAXCxZjSmdNbao16dKXC8tRWfcF5oc" (string) address
                   ,...
                 ]
               }
             }
             ,...
          ],
        }

        Examples:
        > multichain-cli testchain decoderawtransaction "hexstring"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "decoderawtransaction", "params": ["hexstring"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def decodescript(self, *args) -> t.Dict:
        """
        decodescript script-hex

        Decode a hex-encoded script.

        Arguments:
        1. script-hex                       (string) the hex encoded script

        Result:
        {
          "asm":"asm",                      (string) Script public key
          "hex":"hex",                      (string) hex encoded public key
          "type":"type",                    (string) The output type
          "reqSigs": n,                     (numeric) The required signatures
          "addresses": [                    (json array of string)
             "address"                      (string) address
             ,...
          ],
          "p2sh","address"                  (string) script address
        }

        Examples:
        > multichain-cli testchain decodescript "hexstring"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "decodescript", "params": ["hexstring"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def disablerawtransaction(self, *args) -> t.Dict:
        """
        disablerawtransaction "tx-hex"

        Disable raw transaction by spending one of its inputs and sending it back to the wallet.

        Arguments:
        1. "tx-hex"                         (string, required) The transaction hex string

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain disablerawtransaction "hexstring"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "disablerawtransaction", "params": ["hexstring"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def dumpprivkey(self, *args) -> t.Dict:
        """
        dumpprivkey "address"

        Reveals the private key corresponding to 'address'.
        Then the importprivkey can be used with this output

        Arguments:
        1. "address"                        (string, required) The MultiChain address for the private key

        Result:
        "key"                               (string) The private key

        Examples:
        > multichain-cli testchain dumpprivkey "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ"
        > multichain-cli testchain importprivkey "mykey"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "dumpprivkey", "params": ["1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def dumpwallet(self, *args) -> t.Dict:
        """
        dumpwallet "filename"

        Dumps all wallet keys in a human-readable format.

        Arguments:
        1. "filename"                       (string, required) The filename

        Examples:
        > multichain-cli testchain dumpwallet "test"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "dumpwallet", "params": ["test"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def encryptwallet(self, *args) -> t.Dict:
        """
        encryptwallet "passphrase"

        Encrypts the wallet with 'passphrase'. This is for first time encryption.
        After this, any calls that interact with private keys such as sending or signing 
        will require the passphrase to be set prior the making these calls.
        Use the walletpassphrase call for this, and then walletlock call.
        If the wallet is already encrypted, use the walletpassphrasechange call.
        Note that this will shutdown the server.

        Arguments:
        1. "passphrase"                     (string) The pass phrase to encrypt the wallet with.                                              It must be at least 1 character, but should be long.

        Examples:

        Encrypt you wallet
        > multichain-cli testchain encryptwallet "my pass phrase"

        Now set the passphrase to use the wallet, such as for signing or sending assets
        > multichain-cli testchain walletpassphrase "my pass phrase"

        Now we can so something like sign
        > multichain-cli testchain signmessage "address" "test message"

        Now lock the wallet again by removing the passphrase
        > multichain-cli testchain walletlock 

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "encryptwallet", "params": ["my pass phrase"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def estimatefee(self, *args) -> t.Dict:
        """
        estimatefee nblocks

        Estimates the approximate fee per kilobyte
        needed for a transaction to begin confirmation
        within nblocks blocks.

        Arguments:
        1. nblocks                          (numeric)

        Result:
        n :                                 (numeric) estimated fee-per-kilobyte

        -1.0 is returned if not enough transactions and
        blocks have been observed to make an estimate.

        Example:
        > multichain-cli testchain estimatefee 6

        """

    def estimatepriority(self, *args) -> t.Dict:
        """
        estimatepriority nblocks

        Estimates the approximate priority
        a zero-fee transaction needs to begin confirmation
        within nblocks blocks.

        Arguments:
        1. nblocks                          (numeric)

        Result:
        n :                                 (numeric) estimated priority

        -1.0 is returned if not enough transactions and
        blocks have been observed to make an estimate.

        Example:
        > multichain-cli testchain estimatepriority 6

        """

    def getaccount(self, *args) -> t.Dict:
        """
        getaccount "address"

        Returns the account associated with the given address.

        Arguments:
        1. "address"                        (string, required) The address for account lookup.

        Result:
        "accountname"                       (string) the account address

        Examples:
        > multichain-cli testchain getaccount "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaccount", "params": ["1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getaccountaddress(self, *args) -> t.Dict:
        """
        getaccountaddress "account"

        Returns the current address for receiving payments to this account.

        Arguments:
        1. "account"                        (string, required) The account name for the address.
                                                               It can also be set to the empty string "" to represent the default account.
                                                               The account does not need to exist, it will be created and a new address created
                                                               if there is no account by the given name.

        Result:
        "address"                           (string) The account address

        Examples:
        > multichain-cli testchain getaccountaddress 
        > multichain-cli testchain getaccountaddress ""
        > multichain-cli testchain getaccountaddress "myaccount"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaccountaddress", "params": ["myaccount"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getaddednodeinfo(self, *args) -> t.Dict:
        """
        getaddednodeinfo dns ( "node" )

        Returns information about the given added node, or all added nodes
        (note that onetry addnodes are not listed here)
        If dns is false, only a list of added nodes will be provided,
        otherwise connected information will also be available.

        Arguments:
        1. dns                                      (boolean, required) If false, only a list of added nodes will be provided,
                                                                        otherwise connected information will also be available.
        2. "node"                                   (string, optional)  If provided, return information about this specific node,
                                                                         otherwise all nodes are returned.

        Result:
        [
          {
            "addednode" : "192.168.0.201",          (string) The node ip address
            "connected" : true|false,               (boolean) If connected
            "addresses" : [
               {
                 "address" : "192.168.0.201:8333",  (string) The MultiChain server host and port
                 "connected" : "outbound"           (string) connection, inbound or outbound
               }
               ,...
             ]
          }
          ,...
        ]

        Examples:
        > multichain-cli testchain getaddednodeinfo true
        > multichain-cli testchain getaddednodeinfo true "192.168.0.201"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddednodeinfo", "params": [true, "192.168.0.201"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getaddressbalances(self, *args) -> t.Dict:
        """
        getaddressbalances "address" ( minconf includeLocked ) 

        Returns asset balances for specified address

        Arguments:
        1. "address"                        (string, required) Address to return balance for.
        2. minconf                          (numeric, optional, default=1) Only include transactions confirmed at least this many times.
        3. includeLocked                    (bool, optional, default=false) Also take locked outputs into account

        Result:
        An array of Objects with totals and details for each asset.

        Examples:

        The total amount in the server across all accounts
        > multichain-cli testchain getaddressbalances "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd"
        > multichain-cli testchain getaddressbalances "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0 true
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddressbalances", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getaddresses(self, *args) -> t.Dict:
        """
        getaddresses ( verbose )

        Returns the list of all addresses in the wallet.

        Arguments: 
        1. verbose                          (boolean, optional, default=false) The account name.

        Result:
        [                                   (json array of )
          "address"                         (string) an address 
          or 
          address-datails                   (object) address details if verbose=true
          ,...
        ]

        Examples:
        > multichain-cli testchain getaddresses 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddresses", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getaddressesbyaccount(self, *args) -> t.Dict:
        """
        getaddressesbyaccount "account"

        Returns the list of addresses for the given account.

        Arguments:
        1. "account"                        (string, required) The account name.

        Result:
        [                                   (json array of string)
          "address"                         (string) an address associated with the given account
          ,...
        ]

        Examples:
        > multichain-cli testchain getaddressesbyaccount "tabby"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddressesbyaccount", "params": ["tabby"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getaddresstransaction(self, *args) -> t.Dict:
        """
        getaddresstransaction "address" "txid" ( verbose )

        Provides information about transaction txid related to address in this nodeâ  s wallet

        Arguments:
        1. "address"                        (string, required) Address used for balance calculation.
        2. "txid"                           (string, required) The transaction id
        3. verbose                          (bool, optional, default=false) If true, returns detailed array of inputs and outputs and raw hex of transactions

        Result:
        [
          {
            "balance": {...},               (object)  Changes in address balance. 
            {
              "amount": x.xxx,              (numeric) The amount in native currency. Negative value means amount was send by the wallet, positive - received
              "assets": {...},              (object)  Changes in asset amounts. 
            }
            "myaddresses": [...],           (array)   Address passed as parameter
            "addresses": [...],             (array)   Array of counterparty addresses  involved in transaction  
            "permissions": [...],           (array)   Changes in permissions 
            "issue": {...},                 (object)  Issue details  
            "data" : "metadata",            (array)   Hexadecimal representation of metadata appended to the transaction
            "confirmations": n,             (numeric)  The number of confirmations for the transaction. Available for 'send' and 
                                                 'receive' category of transactions.
            "blockhash": "hashvalue",       (string) The block hash containing the transaction. Available for 'send' and 'receive'
                                                category of transactions.
            "blockindex": n,                (numeric) The block index containing the transaction. Available for 'send' and 'receive'
                                              category of transactions.
            "txid": "transactionid",        (string) The transaction id. Available for 'send' and 'receive' category of transactions.
            "time": xxx,                    (numeric) The transaction time in seconds since epoch (midnight Jan 1 1970 GMT).
            "timereceived": xxx,            (numeric) The time received in seconds since epoch (midnight Jan 1 1970 GMT). Available 
                                                  for 'send' and 'receive' category of transactions.
            "comment": "...",               (string) If a comment is associated with the transaction.
            "vin": [...],                   (array)  If verbose=true. Array of input details
            "vout": [...],                  (array)  If verbose=true. Array of output details
            "hex" : "data"                  (string) If verbose=true. Raw data for transaction
          }
        ]

        Examples:
        > multichain-cli testchain getaddresstransaction "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"
        > multichain-cli testchain getaddresstransaction "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d" true
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddresstransaction", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getassetbalances(self, *args) -> t.Dict:
        """
        getassetbalances ( "account" minconf includeWatchonly includeLocked )

        If account is not specified, returns the server's total available asset balances.
        If account is specified, returns the balances in the account.
        Note that the account "" is not the same as leaving the parameter out.
        The server total may be different to the balance in the default "" account.

        Arguments:
        1. "account"                        (string, optional) The selected account, or "*" for entire wallet. It may be the default account using "".
        2. minconf                          (numeric, optional, default=1) Only include transactions confirmed at least this many times.
        3. includeWatchonly                 (bool, optional, default=false) Also include balance in watchonly addresses (see 'importaddress')
        4. includeLocked                    (bool, optional, default=false) Also take locked outputs into account
        Results are an array of Objects with totals and details for each asset.

        Examples:

        The total amount in the server across all accounts
        > multichain-cli testchain getassetbalances 

        The total amount in the server across all accounts, with at least 5 confirmations
        > multichain-cli testchain getassetbalances "*" 6

        The total amount in the default account with at least 1 confirmation
        > multichain-cli testchain getassetbalances ""

        The total amount in the account named tabby with at least 6 confirmations
        > multichain-cli testchain getassetbalances "tabby" 6 true

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getassetbalances", "params": ["tabby", 6] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getassettransaction(self, *args) -> t.Dict:
        """
        getassettransaction "asset-identifier" "txid" ( verbose )

        Retrieves a specific transaction txid involving asset.

        Arguments:
        1. "asset-identifier"               (string, required) Asset identifier - one of the following: asset txid, asset reference, asset name.
        2. "txid"                           (string, required) The transaction id
        3. verbose                          (boolean, optional, default=false) If true, returns information about item transaction 

        Result:
        "transaction"                       (object) Information about an individual transaction from the perspective of a particular asset.

        Examples:
        > multichain-cli testchain getassettransaction "myasset" "mytxid"
        > multichain-cli testchain getassettransaction "myasset" "mytxid"  true
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getassettransaction", "params": ["myasset", "mytxid", false] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getbalance(self, *args) -> t.Dict:
        """
        getbalance ( "account" minconf includeWatchonly )

        If account is not specified, returns the server's total available balance.
        If account is specified, returns the balance in the account.
        Note that the account "" is not the same as leaving the parameter out.
        The server total may be different to the balance in the default "" account.

        Arguments:
        1. "account"                        (string, optional) The selected account, or "*" for entire wallet. It may be the default account using "".
        2. minconf                          (numeric, optional, default=1) Only include transactions confirmed at least this many times.
        3. includeWatchonly                 (bool, optional, default=false) Also include balance in watchonly addresses (see 'importaddress')

        Result:
        amount                              (numeric) The total amount in native currency received for this account.

        Examples:

        The total amount in the server across all accounts
        > multichain-cli testchain getbalance 

        The total amount in the server across all accounts, with at least 5 confirmations
        > multichain-cli testchain getbalance "*" 6

        The total amount in the default account with at least 1 confirmation
        > multichain-cli testchain getbalance ""

        The total amount in the account named tabby with at least 6 confirmations
        > multichain-cli testchain getbalance "tabby" 6

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getbalance", "params": ["tabby", 6] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getbestblockhash(self) -> t.Dict:
        """
        getbestblockhash

        Returns the hash of the best (tip) block in the longest block chain.

        Result
        "hex"                               (string) the block hash hex encoded

        Examples
        > multichain-cli testchain getbestblockhash 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getbestblockhash", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getblock(self, *args) -> t.Dict:
        """
        getblock "hash"|height ( verbose )

        Returns hex-encoded data or json object for block.

        Arguments:
        1. "hash"                           (string, required) The block hash
         or
        1. height                           (numeric, required) The block height in active chain
        2. verbose                          (numeric or boolean, optional, default=1) 0(or false) - encoded data, 1(or true) - json object,
                                                                                      2 - with tx encoded data, 4 - with tx json object

        Result (for verbose = 1, see help getrawtransaction for details about transactions - verbose = 4):
        {
          "hash" : "hash",                  (string) the block hash (same as provided)
          "miner" : "miner",                (string) the address of the miner
          "confirmations" : n,              (numeric) The number of confirmations, or -1 if the block is not on the main chain
          "size" : n,                       (numeric) The block size
          "height" : n,                     (numeric) The block height or index
          "version" : n,                    (numeric) The block version
          "merkleroot" : "xxxx",            (string) The merkle root
          "tx" : [                          (array of strings) The transaction ids
             "transactionid"                (string) The transaction id
             ,...
          ],
          "time" : ttt,                     (numeric) The block time in seconds since epoch (Jan 1 1970 GMT)
          "nonce" : n,                      (numeric) The nonce
          "bits" : "1d00ffff",              (string) The bits
          "difficulty" : x.xxx,             (numeric) The difficulty
          "previousblockhash" : "hash",     (string) The hash of the previous block
          "nextblockhash" : "hash"          (string) The hash of the next block
        }

        Result (for verbose=false):
        "data"                              (string) A string that is serialized, hex-encoded data for block 'hash'.

        Examples:
        > multichain-cli testchain getblock "00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblock", "params": ["00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getblockchaininfo(self) -> t.Dict:
        """
        getblockchaininfo
        Returns an object containing various state info regarding block chain processing.

        Result:
        {
          "chain": "xxxx",                  (string) current network name as defined in BIP70 (main, test, regtest)
          "chainname": "xxxx",              (string) multichain network name
          "description": "xxxx",            (string) network desctription
          "protocol": "xxxx",               (string) protocol - multichain or bitcoin
          "setupblocks": "xxxx",            (string) number of network setup blocks
          "blocks": xxxxxx,                 (numeric) the current number of blocks processed in the server
          "headers": xxxxxx,                (numeric) the current number of headers we have validated
          "bestblockhash": "...",           (string) the hash of the currently best block
          "difficulty": xxxxxx,             (numeric) the current difficulty
          "verificationprogress": xxxx,     (numeric) estimate of verification progress [0..1]
          "chainwork": "xxxx"               (string) total amount of work in active chain, in hexadecimal
        }

        Examples:
        > multichain-cli testchain getblockchaininfo 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockchaininfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getblockchainparams(self, *args) -> t.Dict:
        """
        getblockchainparams ( displaynames with-upgrades )

        Returns a list of values of this blockchainâ  s parameters

        Arguments:
        1. displaynames                     (boolean, optional, default=true) use display names instead of internal
        2. with-upgrades                    (boolean, optional, default=true) Take upgrades into account 

        Result:
        An object containing various blockchain parameters.

        Examples:
        > multichain-cli testchain getblockchainparams 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockchainparams", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getblockcount(self) -> t.Dict:
        """
        getblockcount

        Returns the number of blocks in the longest block chain.

        Result:
        n                                   (numeric) The current block count

        Examples:
        > multichain-cli testchain getblockcount 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockcount", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getblockhash(self, *args) -> t.Dict:
        """
        getblockhash index

        Returns hash of block in best-block-chain at index provided.

        Arguments:
        1. index                            (numeric, required) The block index

        Result:
        "hash"                              (string) The block hash

        Examples:
        > multichain-cli testchain getblockhash 1000
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockhash", "params": [1000] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getblocktemplate(self, *args) -> t.Dict:
        """
        getblocktemplate ( "jsonrequestobject" )

        If the request parameters include a 'mode' key, that is used to explicitly select between the default 'template' request or a 'proposal'.
        It returns data needed to construct a block to work on.
        See https://en.bitcoin.it/wiki/BIP_0022 for full specification.

        Arguments:
        1. "jsonrequestobject"              (string, optional) A json object in the following spec
             {
               "mode":"template"            (string, optional) This must be set to "template" or omitted
               "capabilities":[             (array, optional) A list of strings
                   "support"                (string) client side supported feature, 'longpoll', 'coinbasetxn', 'coinbasevalue', 'proposal', 'serverlist', 'workid'
                   ,...
                 ]
             }


        Result:
        {
          "version" : n,                    (numeric) The block version
          "previousblockhash" : "xxxx",     (string) The hash of current highest block
          "transactions" : [                (array) contents of non-coinbase transactions that should be included in the next block
              {
                 "data" : "xxxx",           (string) transaction data encoded in hexadecimal (byte-for-byte)
                 "hash" : "xxxx",           (string) hash/id encoded in little-endian hexadecimal
                 "depends" : [              (array) array of numbers 
                     n                      (numeric) transactions before this one (by 1-based index in 'transactions' list) that must be present in the final block if this one is
                     ,...
                 ],
                 "fee": n,                  (numeric) difference in value between transaction inputs and outputs (in Satoshis); for coinbase transactions, this is a negative Number of the total collected block fees (ie, not including the block subsidy); if key is not present, fee is unknown and clients MUST NOT assume there isn't one
                 "sigops" : n,              (numeric) total number of SigOps, as counted for purposes of block limits; if key is not present, sigop count is unknown and clients MUST NOT assume there aren't any
                 "required" : true|false    (boolean) if provided and true, this transaction must be in the final block
              }
              ,...
          ],
          "coinbaseaux" : {                 (json object) data that should be included in the coinbase's scriptSig content
              "flags" : "flags"             (string) 
          },
          "coinbasevalue" : n,              (numeric) maximum allowable input to coinbase transaction, including the generation award and transaction fees (in Satoshis)
          "coinbasetxn" : { ... },          (json object) information for coinbase transaction
          "target" : "xxxx",                (string) The hash target
          "mintime" : xxx,                  (numeric) The minimum timestamp appropriate for next block time in seconds since epoch (Jan 1 1970 GMT)
          "mutable" : [                     (array of string) list of ways the block template may be changed 
             "value"                        (string) A way the block template may be changed, e.g. 'time', 'transactions', 'prevblock'
             ,...
          ],
          "noncerange" : "00000000ffffffff",(string) A range of valid nonces
          "sigoplimit" : n,                 (numeric) limit of sigops in blocks
          "sizelimit" : n,                  (numeric) limit of block size
          "curtime" : ttt,                  (numeric) current timestamp in seconds since epoch (Jan 1 1970 GMT)
          "bits" : "xxx",                   (string) compressed target of next block
          "height" : n                      (numeric) The height of the next block
        }

        Examples:
        > multichain-cli testchain getblocktemplate 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblocktemplate", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getchaintips(self) -> t.Dict:
        """
        getchaintips
        Return information about all known tips in the block tree, including the main chain as well as orphaned branches.

        Result:
        [
          {
            "height": xxxx,                 (numeric) height of the chain tip
            "hash": "xxxx",                 (string) block hash of the tip
            "branchlen": 0                  (numeric) zero for main chain
            "status": "active"              (string) "active" for the main chain
          },
          {
            "height": xxxx,
            "hash": "xxxx",
            "branchlen": 1                  (numeric) length of branch connecting the tip to the main chain
            "status": "xxxx"                (string) status of the chain (active, valid-fork, valid-headers, headers-only, invalid)
          }
        ]
        Possible values for status:
        1.  "invalid"                       This branch contains at least one invalid block
        2.  "headers-only"                  Not all blocks for this branch are available, but the headers are valid
        3.  "valid-headers"                 All blocks are available for this branch, but they were never fully validated
        4.  "valid-fork"                    This branch is not part of the active chain, but is fully validated
        5.  "active"                        This is the tip of the active main chain, which is certainly valid

        Examples:
        > multichain-cli testchain getchaintips 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getchaintips", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getconnectioncount(self) -> t.Dict:
        """
        getconnectioncount

        Returns the number of connections to other nodes.

        bResult:
        n                                   (numeric) The connection count

        Examples:
        > multichain-cli testchain getconnectioncount 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getconnectioncount", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getdifficulty(self) -> t.Dict:
        """
        getdifficulty

        Returns the proof-of-work difficulty as a multiple of the minimum difficulty.

        Result:
        n.nnn                                 (numeric) the proof-of-work difficulty as a multiple of the minimum difficulty.

        Examples:
        > multichain-cli testchain getdifficulty 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getdifficulty", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getgenerate(self) -> t.Dict:
        """
        getgenerate

        Return if the server is set to generate coins or not. The default is false.
        It is set with the command line argument -gen (or bitcoin.conf setting gen)
        It can also be set with the setgenerate call.

        Result
        true|false                          (boolean) If the server is set to generate coins or not

        Examples:
        > multichain-cli testchain getgenerate 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getgenerate", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def gethashespersec(self) -> t.Dict:
        """
        gethashespersec

        Returns a recent hashes per second performance measurement while generating.
        See the getgenerate and setgenerate calls to turn generation on and off.

        Result:
        n                                   (numeric) The recent hashes per second when generation is on (will return 0 if generation is off)

        Examples:
        > multichain-cli testchain gethashespersec 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "gethashespersec", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getinfo(self) -> t.Dict:
        """
        getinfo

        Returns general information about this node and blockchain.

        Result:
        {
          "version": xxxxx,                 (numeric) the server version
          "protocolversion": xxxxx,         (numeric) the protocol version
          "chainname": "xxxx",              (string) multichain network name
          "description": "xxxx",            (string) network desctription
          "protocol": "xxxx",               (string) protocol - multichain or bitcoin
          "port": xxxx,                     (numeric) network port
          "setupblocks": "xxxx",            (string) number of network setup blocks
          "walletversion": xxxxx,           (numeric) the wallet version
          "balance": xxxxxxx,               (numeric) the total native currency balance of the wallet
          "walletdbversion": xxxxx,         (numeric) the wallet database version
          "blocks": xxxxxx,                 (numeric) the current number of blocks processed in the server
          "timeoffset": xxxxx,              (numeric) the time offset
          "connections": xxxxx,             (numeric) the number of connections
          "proxy": "host:port",             (string, optional) the proxy used by the server
          "difficulty": xxxxxx,             (numeric) the current difficulty
          "testnet": true|false,            (boolean) if the server is using testnet or not
          "keypoololdest": xxxxxx,          (numeric) the timestamp (seconds since GMT epoch) of the oldest pre-generated key in the key pool
          "keypoolsize": xxxx,              (numeric) how many new keys are pre-generated
          "unlocked_until": ttt,            (numeric) the timestamp in seconds since epoch (midnight Jan 1 1970 GMT) that the wallet is unlocked for transfers, or 0 if the wallet is locked
          "paytxfee": x.xxxx,               (numeric) the transaction fee set in btc/kb
          "relayfee": x.xxxx,               (numeric) minimum relay fee for non-free transactions in btc/kb
          "errors": "..."                   (string) any error messages
        }

        Examples:
        > multichain-cli testchain getinfo 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getmempoolinfo(self) -> t.Dict:
        """
        getmempoolinfo

        Returns details on the active state of the TX memory pool.

        Result:
        {
          "size": xxxxx                     (numeric) Current tx count
          "bytes": xxxxx                    (numeric) Sum of all tx sizes
        }

        Examples:
        > multichain-cli testchain getmempoolinfo 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getmempoolinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getmininginfo(self) -> t.Dict:
        """
        getmininginfo

        Returns a json object containing mining-related information.
        Result:
        {
          "blocks": nnn,                    (numeric) The current block
          "currentblocksize": nnn,          (numeric) The last block size
          "currentblocktx": nnn,            (numeric) The last block transaction
          "difficulty": xxx.xxxxx           (numeric) The current difficulty
          "errors": "..."                   (string) Current errors
          "generate": true|false            (boolean) If the generation is on or off (see getgenerate or setgenerate calls)
          "genproclimit": n                 (numeric) The processor limit for generation. -1 if no generation. (see getgenerate or setgenerate calls)
          "hashespersec": n                 (numeric) The hashes per second of the generation, or 0 if no generation.
          "pooledtx": n                     (numeric) The size of the mem pool
          "testnet": true|false             (boolean) If using testnet or not
          "chain": "xxxx",                  (string) current network name as defined in BIP70 (main, test, regtest)
        }

        Examples:
        > multichain-cli testchain getmininginfo 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getmininginfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getmultibalances(self, *args) -> t.Dict:
        """
        getmultibalances ( address(es) assets minconf includeLocked includeWatchonly ) 

        Returns asset balances for specified address

        Arguments:
        1. "address(es)"                    (string, optional) Address(es) to return balance for, comma delimited. Default - all
         or
        1. address(es)                      (array, optional) A json array of addresses to return balance for
        2. "asset"                          (string) Single asset identifier to return balance for, default "*"
         or
        2. assets                           (array, optional) Json array of asset identifiers to return balance for
        3. minconf                          (numeric, optional, default=1) Only include transactions confirmed at least this many times.
        4. includeWatchonly                 (bool, optional, default=false) Include transactions to watchonly addresses (see 'importaddress')
        5. includeLocked                    (bool, optional, default=false) Also take locked outputs into account

        Result:
        An object of balance arrays with totals and details for each address.

        Examples:
        > multichain-cli testchain getmultibalances 
        > multichain-cli testchain getmultibalances "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getmultibalances", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getnettotals(self) -> t.Dict:
        """
        getnettotals

        Returns information about network traffic, including bytes in, bytes out,
        and current time.

        Result:
        {
          "totalbytesrecv": n,              (numeric) Total bytes received
          "totalbytessent": n,              (numeric) Total bytes sent
          "timemillis": t                   (numeric) Total cpu time
        }

        Examples:
        > multichain-cli testchain getnettotals 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getnettotals", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getnetworkhashps(self, *args) -> t.Dict:
        """
        getnetworkhashps ( blocks height )

        Returns the estimated network hashes per second based on the last n blocks.
        Pass in [blocks] to override # of blocks, -1 specifies since last difficulty change.
        Pass in [height] to estimate the network speed at the time when a certain block was found.

        Arguments:
        1. blocks                           (numeric, optional, default=120) The number of blocks, or -1 for blocks since last difficulty change.
        2. height                           (numeric, optional, default=-1) To estimate at the time of the given height.

        Result:
        x                                   (numeric) Hashes per second estimated

        Examples:
        > multichain-cli testchain getnetworkhashps 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getnetworkhashps", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getnetworkinfo(self) -> t.Dict:
        """
        getnetworkinfo
        Returns an object containing various state info regarding P2P networking.

        Result:
        {
          "version": xxxxx,                      (numeric) the server version
          "subversion": "/Satoshi:x.x.x/",       (string) the server subversion string
          "protocolversion": xxxxx,              (numeric) the protocol version
          "localservices": "xxxxxxxxxxxxxxxx",   (string) the services we offer to the network
          "timeoffset": xxxxx,                   (numeric) the time offset
          "connections": xxxxx,                  (numeric) the number of connections
          "networks": [                          (array) information per network
          {
            "name": "xxx",                       (string) network (ipv4, ipv6 or onion)
            "limited": true|false,               (boolean) is the network limited using -onlynet?
            "reachable": true|false,             (boolean) is the network reachable?
            "proxy": "host:port"                 (string) the proxy that is used for this network, or empty if none
          }
          ,...
          ],
          "relayfee": x.xxxxxxxx,                (numeric) minimum relay fee for non-free transactions in btc/kb
          "localaddresses": [                    (array) list of local addresses
          {
            "address": "xxxx",                   (string) network address
            "port": xxx,                         (numeric) network port
            "score": xxx                         (numeric) relative score
          }
          ,...
          ]
        }

        Examples:
        > multichain-cli testchain getnetworkinfo 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getnetworkinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getnewaddress(self, *args) -> t.Dict:
        """
        getnewaddress ( "account" )

        Returns a new address for receiving payments.
        If 'account' is specified (deprecated), it is added to the address book 
        so payments received with the address will be credited to 'account'.

        Arguments:
        1. "account"                        (string, optional) The account name for the address to be linked to.
                                                                If not provided, the default account "" is used.
                                                                It can also be set to the empty string "" to represent the default account.
                                                                The account does not need to exist, it will be created if there is no account by the given name.

        Result:
        "address"                           (string) The new address

        Examples:
        > multichain-cli testchain getnewaddress 
        > multichain-cli testchain getnewaddress ""
        > multichain-cli testchain getnewaddress "myaccount"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getnewaddress", "params": ["myaccount"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getpeerinfo(self) -> t.Dict:
        """
        getpeerinfo

        Returns data about each connected network node as a json array of objects.

        Result:
        [
          {
            "id": n,                        (numeric) Peer index
            "addr":"host:port",             (string) The ip address and port of the peer
            "addrlocal":"ip:port",          (string) local address
            "services":"xxxxxxxxxxxxxxxx",  (string) The services offered
            "lastsend": ttt,                (numeric) The time in seconds since epoch (Jan 1 1970 GMT) of the last send
            "lastrecv": ttt,                (numeric) The time in seconds since epoch (Jan 1 1970 GMT) of the last receive
            "bytessent": n,                 (numeric) The total bytes sent
            "bytesrecv": n,                 (numeric) The total bytes received
            "conntime": ttt,                (numeric) The connection time in seconds since epoch (Jan 1 1970 GMT)
            "pingtime": n,                  (numeric) ping time
            "pingwait": n,                  (numeric) ping wait
            "version": v,                   (numeric) The peer version, such as 7001
            "subver": "/Satoshi:0.8.5/",    (string) The string version
            "handshakelocal": n,            (string) If protocol is Multichain. Address used by local node for handshake.
            "handshake": n,                 (string) If protocol is Multichain. Address used by remote node for handshake.
            "inbound": true|false,          (boolean) Inbound (true) or Outbound (false)
            "startingheight": n,            (numeric) The starting height (block) of the peer
            "banscore": n,                  (numeric) The ban score
            "synced_headers": n,            (numeric) The last header we have in common with this peer
            "synced_blocks": n,             (numeric) The last block we have in common with this peer
            "inflight": [
               n,                           (numeric) The heights of blocks we're currently asking from this peer
               ...
            ]
          }
          ,...
        ]

        Examples:
        > multichain-cli testchain getpeerinfo 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getpeerinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getrawchangeaddress(self) -> t.Dict:
        """
        getrawchangeaddress

        Returns a new  address, for receiving change.
        This is for use with raw transactions, NOT normal use.

        Result:
        "address"                           (string) The address

        Examples:
        > multichain-cli testchain getrawchangeaddress 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getrawchangeaddress", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getrawmempool(self, *args) -> t.Dict:
        """
        getrawmempool ( verbose )

        Returns all transaction ids in memory pool as a json array of string transaction ids.

        Arguments:
        1. verbose                          (boolean, optional, default=false) true for a json object, false for array of transaction ids

        Result: (for verbose = false):
        [                                   (json array of string)
          "transactionid"                   (string) The transaction id
          ,...
        ]

        Result: (for verbose = true):
        {                                   (json object)
          "transactionid" : {               (json object)
            "size" : n,                     (numeric) transaction size in bytes
            "fee" : n,                      (numeric) transaction fee in native currency units
            "time" : n,                     (numeric) local time transaction entered pool in seconds since 1 Jan 1970 GMT
            "height" : n,                   (numeric) block height when transaction entered pool
            "startingpriority" : n,         (numeric) priority when transaction entered pool
            "currentpriority" : n,          (numeric) transaction priority now
            "depends" : [                   (array) unconfirmed transactions used as inputs for this transaction
                "transactionid",            (string) parent transaction id
               ... ]
          }, ...
        ]

        Examples
        > multichain-cli testchain getrawmempool true
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getrawmempool", "params": [true] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getrawtransaction(self, *args) -> t.Dict:
        """
        getrawtransaction "txid" ( verbose )

        NOTE: By default this function only works sometimes. This is when the tx is in the mempool
        or there is an unspent output in the utxo for this transaction. To make it always work,
        you need to maintain a transaction index, using the -txindex command line option.

        Return the raw transaction data.

        If verbose=0, returns a string that is serialized, hex-encoded data for 'txid'.
        If verbose is non-zero, returns an Object with information about 'txid'.

        Arguments:
        1. "txid"                           (string, required) The transaction id
        2. verbose                          (numeric, optional, default=0) If 0, return a string, other return a json object

        Result (if verbose is not set or set to 0):
        "data"                              (string) The serialized, hex-encoded data for 'txid'

        Result (if verbose > 0):
        {
          "hex" : "data",                   (string) The serialized, hex-encoded data for 'txid'
          "txid" : "id",                    (string) The transaction id (same as provided)
          "version" : n,                    (numeric) The version
          "locktime" : ttt,                 (numeric) The lock time
          "vin" : [                         (array of json objects)
             {
               "txid": "id",                (string) The transaction id
               "vout": n,                   (numeric) 
               "scriptSig": {               (json object) The script
                 "asm": "asm",              (string) asm
                 "hex": "hex"               (string) hex
               },
               "sequence": n                (numeric) The script sequence number
             }
             ,...
          ],
          "vout" : [                        (array of json objects)
             {
               "value" : x.xxx,             (numeric) The value in btc
               "n" : n,                     (numeric) index
               "scriptPubKey" : {           (json object)
                 "asm" : "asm",             (string) the asm
                 "hex" : "hex",             (string) the hex
                 "reqSigs" : n,             (numeric) The required sigs
                 "type" : "pubkeyhash",     (string) The type, eg 'pubkeyhash'
                 "addresses" : [            (json array of string)
                   "address"                (string) address
                   ,...
                 ]
               }
             }
             ,...
          ],
          "blockhash" : "hash",             (string) the block hash
          "confirmations" : n,              (numeric) The confirmations
          "time" : ttt,                     (numeric) The transaction time in seconds since epoch (Jan 1 1970 GMT)
          "blocktime" : ttt                 (numeric) The block time in seconds since epoch (Jan 1 1970 GMT)
        }

        Examples:
        > multichain-cli testchain getrawtransaction "mytxid"
        > multichain-cli testchain getrawtransaction "mytxid" 1
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getrawtransaction", "params": ["mytxid", 1] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getreceivedbyaccount(self, *args) -> t.Dict:
        """
        getreceivedbyaccount "account" ( minconf )

        Returns the total amount received by addresses with <account> in transactions with at least [minconf] confirmations.

        Arguments:
        1. "account"                        (string, required) The selected account, may be the default account using "".
        2. minconf                          (numeric, optional, default=1) Only include transactions confirmed at least this many times.

        Result:
        amount                              (numeric) The total amount in native currency received for this account.

        Examples:

        Amount received by the default account with at least 1 confirmation
        > multichain-cli testchain getreceivedbyaccount ""

        Amount received at the tabby account including unconfirmed amounts with zero confirmations
        > multichain-cli testchain getreceivedbyaccount "tabby" 0

        The amount with at least 6 confirmation, very safe
        > multichain-cli testchain getreceivedbyaccount "tabby" 6

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getreceivedbyaccount", "params": ["tabby", 6] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getreceivedbyaddress(self, *args) -> t.Dict:
        """
        getreceivedbyaddress "address" ( minconf )

        Returns the total amount received by the given address in transactions with at least minconf confirmations.

        Arguments:
        1. "address"                        (string, required) The address for transactions.
        2. minconf                          (numeric, optional, default=1) Only include transactions confirmed at least this many times.

        Result:
        amount                              (numeric) The total amount in native currency received at this address.

        Examples:

        The amount from transactions with at least 1 confirmation
        > multichain-cli testchain getreceivedbyaddress "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ"

        The amount including unconfirmed transactions, zero confirmations
        > multichain-cli testchain getreceivedbyaddress "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ" 0

        The amount with at least 6 confirmation, very safe
        > multichain-cli testchain getreceivedbyaddress "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ" 6

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getreceivedbyaddress", "params": ["1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ", 6] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getruntimeparams(self) -> t.Dict:
        """
        getruntimeparams 

        Returns a selection of this nodeâ  s runtime parameters.

        Result:
        An object containing various runtime parameters

        Examples:
        > multichain-cli testchain getruntimeparams 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getruntimeparams", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getstreamitem(self, *args) -> t.Dict:
        """
        getstreamitem "stream-identifier" "txid" ( verbose )

        Returns stream item.

        Arguments:
        1. "stream-identifier"              (string, required) Stream identifier - one of the following: stream txid, stream reference, stream name.
        2. "txid"                           (string, required) The transaction id
        3. verbose                          (boolean, optional, default=false) If true, returns information about item transaction 

        Result:
        "stream-item"                       (object) Stream item.

        Examples:
        > multichain-cli testchain getstreamitem "mytxid"
        > multichain-cli testchain getstreamitem "mytxid"  true
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getstreamitem", "params": ["mytxid", false] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getstreamkeysummary(self, *args) -> t.Dict:
        """
        getstreamkeysummary "stream-identifier" "key" "mode"

        Returns stream json object items summary for specific key.

        Arguments:
        1. "stream-identifier"              (string, required) Stream identifier - one of the following: stream txid, stream reference, stream name.
        2. "key"                            (string, required) Stream key
        3. "mode"                           (string, required) Comma delimited list of the following:
                                                               jsonobjectmerge (required) - merge json objects
                                                               recursive - merge json sub-objects recursively
                                                               noupdate -  preserve first value for each key instead of taking the last
                                                               omitnull - omit keys with null values
                                                               ignore - ignore items that cannot be included in summary (otherwise returns an error)
                                                               firstpublishersany - only summarize items by a publisher of first item with this key
                                                               firstpublishersall - only summarize items by all publishers of first item with this key

        Result:
        summary-object                      (object) Summary object for specific key.

        Examples:
        > multichain-cli testchain getstreamkeysummary "test-stream" "key01" "jsonobjectmerge"
        > multichain-cli testchain getstreamkeysummary "test-stream" "key01" "jsonobjectmerge,ignore,recursive"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getstreamkeysummary", "params": ["test-stream", "key01", "jsonobjectmerge,ignore,recursive"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getstreampublishersummary(self, *args) -> t.Dict:
        """
        getstreampublishersummary "stream-identifier" "address" "mode"

        Returns stream json object items summary for specific publisher.

        Arguments:
        1. "stream-identifier"              (string, required) Stream identifier - one of the following: stream txid, stream reference, stream name.
        2. "address"                        (string, required) Publisher address
        3. "mode"                           (string, required) Comma delimited list of the following:
                                                               jsonobjectmerge (required) - merge json objects
                                                               recursive - merge json sub-objects recursively
                                                               noupdate -  preserve first value for each key instead of taking the last
                                                               omitnull - omit keys with null values
                                                               ignore - ignore items that cannot be included in summary (otherwise returns an error)

        Result:
        summary-object                      (object) Summary object for specific publisher.

        Examples:
        > multichain-cli testchain liststreampublisheritems "test-stream" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "jsonobjectmerge"
        > multichain-cli testchain liststreampublisheritems "test-stream" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "jsonobjectmerge,ignore,recursive"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "liststreampublisheritems", "params": ["test-stream", "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "jsonobjectmerge,ignore,recursive"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def gettotalbalances(self, *args) -> t.Dict:
        """
        gettotalbalances ( minconf includeWatchonly includeLocked )

        Returns a list of all the asset balances in this nodeâ  s wallet, with at least minconf confirmations.

        Arguments:
        1. minconf                          (numeric, optional, default=1) Only include transactions confirmed at least this many times.
        2. includeWatchonly                 (bool, optional, default=false) Also include balance in watchonly addresses (see 'importaddress')
        3. includeLocked                    (bool, optional, default=false) Also take locked outputs into account

        Result:
        An array of Objects with totals and details for each asset.

        Examples:

        The total amount in the server across all accounts
        > multichain-cli testchain gettotalbalances 

        The total amount in the server across all accounts, with at least 5 confirmations
        > multichain-cli testchain gettotalbalances 6

        The total amount in the default account with at least 1 confirmation
        > multichain-cli testchain gettotalbalances 

        The total amount in the account named tabby with at least 6 confirmations
        > multichain-cli testchain gettotalbalances 6 true

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "gettotalbalances", "params": ["tabby", 6] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def gettransaction(self, *args) -> t.Dict:
        """
        gettransaction "txid" ( includeWatchonly )

        Get detailed information about in-wallet transaction <txid>

        Arguments:
        1. "txid"                           (string, required) The transaction id
        2. includeWatchonly                 (bool, optional, default=false) Whether to include watchonly addresses in balance calculation and details[]

        Result:
        {
          "amount" : x.xxx,                 (numeric) The transaction amount in native currency
          "confirmations" : n,              (numeric) The number of confirmations
          "blockhash" : "hash",             (string) The block hash
          "blockindex" : xx,                (numeric) The block index
          "blocktime" : ttt,                (numeric) The time in seconds since epoch (1 Jan 1970 GMT)
          "txid" : "transactionid",         (string) The transaction id.
          "time" : ttt,                     (numeric) The transaction time in seconds since epoch (1 Jan 1970 GMT)
          "timereceived" : ttt,             (numeric) The time received in seconds since epoch (1 Jan 1970 GMT)
          "details" : [
            {
              "account" : "accountname",    (string) The account name involved in the transaction, can be "" for the default account.
              "address" : "address",        (string) The address involved in the transaction
              "category" : "send|receive",  (string) The category, either 'send' or 'receive'
              "amount" : x.xxx              (numeric) The amount in native currency
              "vout" : n,                   (numeric) the vout value
            }
            ,...
          ],
          "hex" : "data"                    (string) Raw data for transaction
        }

        Examples:
        > multichain-cli testchain gettransaction "1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"
        > multichain-cli testchain gettransaction "1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d" true
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "gettransaction", "params": ["1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def gettxout(self, *args) -> t.Dict:
        """
        gettxout "txid" n ( includemempool )

        Returns details about an unspent transaction output.

        Arguments:
        1. "txid"                           (string, required) The transaction id
        2. n                                (numeric, required) vout value
        3. includemempool                   (boolean, optional) Whether to included the mem pool

        Result:
        {
          "bestblock" : "hash",             (string) the block hash
          "confirmations" : n,              (numeric) The number of confirmations
          "value" : x.xxx,                  (numeric) The transaction value in btc
          "scriptPubKey" : {                (json object)
             "asm" : "code",                (string) 
             "hex" : "hex",                 (string) 
             "reqSigs" : n,                 (numeric) Number of required signatures
             "type" : "pubkeyhash",         (string) The type, eg pubkeyhash
             "addresses" : [                (array of string) array of addresses
                "address"                   (string) address
                ,...
             ]
          },
          "version" : n,                    (numeric) The version
          "coinbase" : true|false           (boolean) Coinbase or not
        }

        Examples:

        Get unspent transactions
        > multichain-cli testchain listunspent 

        View the details
        > multichain-cli testchain gettxout "txid" 1

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "gettxout", "params": ["txid", 1] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def gettxoutdata(self, *args) -> t.Dict:
        """
        gettxoutdata "txid" vout ( count-bytes start-byte )

        Returns metadata of transaction output.

        Arguments:
        1. "txid"                           (string, required) The transaction id
        2. vout                             (numeric, required) vout value
        3. count-bytes                      (numeric, optional, default=INT_MAX) Number of bytes to return
        4. start-byte                       (numeric, optional, default=0) start from specific byte 

        Result:
        "data-hex"                          (string) transaction output metadata in hexadecimal form.

        Examples:

        View the data
        > multichain-cli testchain gettxoutdata "txid" 1

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "gettxoutdata", "params": ["txid", 1] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def gettxoutsetinfo(self) -> t.Dict:
        """
        gettxoutsetinfo

        Returns statistics about the unspent transaction output set.
        Note this call may take some time.

        Result:
        {
          "height":n,                       (numeric) The current block height (index)
          "bestblock": "hex",               (string) the best block hash hex
          "transactions": n,                (numeric) The number of transactions
          "txouts": n,                      (numeric) The number of output transactions
          "bytes_serialized": n,            (numeric) The serialized size
          "hash_serialized": "hash",        (string) The serialized hash
          "total_amount": x.xxx             (numeric) The total amount
        }

        Examples:
        > multichain-cli testchain gettxoutsetinfo 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "gettxoutsetinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getunconfirmedbalance(self) -> t.Dict:
        """
        getunconfirmedbalance
        Returns the server's total unconfirmed balance

        """

    def getwalletinfo(self) -> t.Dict:
        """
        getwalletinfo
        Returns an object containing various wallet state info.

        Result:
        {
          "walletversion": xxxxx,           (numeric) the wallet version
          "balance": xxxxxxx,               (numeric) the total native currency balance of the wallet
          "txcount": xxxxxxx,               (numeric) the total number of transactions in the wallet
          "walletdbversion": xxxxx,         (numeric) the wallet database version
          "keypoololdest": xxxxxx,          (numeric) the timestamp (seconds since GMT epoch) of the oldest pre-generated key in the key pool
          "keypoolsize": xxxx,              (numeric) how many new keys are pre-generated
          "unlocked_until": ttt,            (numeric) the timestamp in seconds since epoch (midnight Jan 1 1970 GMT)
                                                      that the wallet is unlocked for transfers, or 0 if the wallet is locked
        }

        Examples:
        > multichain-cli testchain getwalletinfo 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getwalletinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def getwallettransaction(self, *args) -> t.Dict:
        """
        getwallettransaction "txid" ( includeWatchonly verbose )

        Get detailed information about in-wallet transaction <txid>

        Arguments:
        1. "txid"    (string, required) The transaction id
        2. includeWatchonly    (bool, optional, default=false) Whether to include watchonly addresses in balance calculation and details[]
        3. verbose (bool, optional, default=false) If true, returns detailed array of inputs and outputs and raw hex of transactions

        Result:
        [
          {
            "balance": {...},               (object)  Changes in wallet balance. 
            {
              "amount": x.xxx,              (numeric) The amount in native currency. Negative value means amount was send by the wallet, positive - received
              "assets": {...},              (object)  Changes in asset amounts. 
            }
            "myaddresses": [...],           (array)   Array of wallet addresses involved in transaction   
            "addresses": [...],             (array)   Array of counterparty addresses  involved in transaction  
            "permissions": [...],           (array)   Changes in permissions 
            "issue": {...},                 (object)  Issue details  
            "data" : "metadata",            (array)   Hexadecimal representation of metadata appended to the transaction
            "confirmations": n,             (numeric)  The number of confirmations for the transaction. Available for 'send' and 
                                                       'receive' category of transactions.
            "blockhash": "hashvalue",       (string) The block hash containing the transaction. Available for 'send' and 'receive'
                                                       category of transactions.
            "blockindex": n,                (numeric) The block index containing the transaction. Available for 'send' and 'receive'
                                                      category of transactions.
            "txid": "transactionid",        (string) The transaction id. Available for 'send' and 'receive' category of transactions.
            "time": xxx,                    (numeric) The transaction time in seconds since epoch (midnight Jan 1 1970 GMT).
            "timereceived": xxx,            (numeric) The time received in seconds since epoch (midnight Jan 1 1970 GMT). Available 
                                                      for 'send' and 'receive' category of transactions.
            "comment": "...",               (string) If a comment is associated with the transaction.
            "vin": [...],                   (array)  If verbose=true. Array of input details
            "vout": [...],                  (array)  If verbose=true. Array of output details
            "hex" : "data"                  (string) If verbose=true. Raw data for transaction
          }
        ]

        Examples:
        > multichain-cli testchain getwallettransaction "1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"
        > multichain-cli testchain getwallettransaction "1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d" true
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getwallettransaction", "params": ["1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def grant(self, *args) -> t.Dict:
        """
        grant "address(es)" "permission(s)" ( native-amount startblock endblock "comment" "comment-to" )

        Grant permission(s) to a given address. 

        Arguments:
        1. "address(es)"                    (string, required)  The multichain addresses to send to (comma delimited)
        2. "permission(s)"                  (string, required)  Permission strings, comma delimited. 
                                                                Global: connect,send,receive,issue,mine,admin,activate,create 
                                                                or per-asset: asset-identifier.issue,admin,activate,send,receive 
                                                                or per-stream: stream-identifier.write,activate,admin 
        3. native-amount                    (numeric, optional) Native currency amount to send. eg 0.1. Default - 0.0
        4. startblock                       (numeric, optional) Block to apply permissions from (inclusive). Default - 0
        5. endblock                         (numeric, optional) Block to apply permissions to (exclusive). Default - 4294967295
                                                                If -1 is specified default value is used.
        6. "comment"                        (string, optional)  A comment used to store what the transaction is for. 
                                                                This is not part of the transaction, just kept in your wallet.
        7. "comment-to"                     (string, optional)  A comment to store the name of the person or organization 
                                                                to which you're sending the transaction. This is not part of the 
                                                                transaction, just kept in your wallet.

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain grant "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 connect,send,receive
        > multichain-cli testchain grant "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 mystream.admin,write
        > multichain-cli testchain grant "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 mine "permission to mine" "Miners Ltd."
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "grant", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", 0.1, admin "temporary admin", "Admins Ltd." 20000 30000] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def grantfrom(self, *args) -> t.Dict:
        """
        grantfrom "from-address" "to-address(es)" "permission(s)" ( native-amount startblock endblock "comment" "comment-to" )

        Grant permission using specific address.

        Arguments:
        1. "from-address"                   (string, required) Address used for grant.
        2. "to-address(es)"                 (string, required) The multichain addresses to grant permissions to
        3. "permission(s)"                  (string, required)  Permission strings, comma delimited. 
                                                                Global: connect,send,receive,issue,mine,admin,activate,create 
                                                                or per-asset: asset-identifier.issue,admin,activate,send,receive 
                                                                or per-stream: stream-identifier.write,activate,admin 
        4. native-amount                    (numeric, optional) Native currency amount to send. eg 0.1. Default - 0.0
        5. startblock                       (numeric, optional) Block to apply permissions from (inclusive). Default - 0
        6. endblock                         (numeric, optional) Block to apply permissions to (exclusive). Default - 4294967295
                                                                If -1 is specified default value is used.
        7. "comment"                        (string, optional)  A comment used to store what the transaction is for. 
                                                                This is not part of the transaction, just kept in your wallet.
        8. "comment-to"                     (string, optional)  A comment to store the name of the person or organization 
                                                                to which you're sending the transaction. This is not part of the 
                                                                transaction, just kept in your wallet.

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain grantfrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 connect,send,receive
        > multichain-cli testchain grantfrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 mine "permission to mine" "Miners Ltd."
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "grantfrom", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", 0.1, admin "temporary admin", "Admins Ltd." 20000 30000] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def grantwithdata(self, *args) -> t.Dict:
        """
        grantwithdata "address(es)" "permission(s)" data|publish-new-stream-item ( native-amount startblock endblock )

        Grant permission(s) with metadata to a given address. 

        Arguments:
        1. "address(es)"                    (string, required) The multichain addresses to send to (comma delimited)
        2. "permission(s)"                  (string, required) Permission strings, comma delimited. 
                                                               Global: connect,send,receive,issue,mine,admin,activate,create 
                                                               or per-asset: asset-identifier.issue,admin,activate,send,receive 
                                                               or per-stream: stream-identifier.write,activate,admin 
        3. data|publish-new-stream-item     (string or object, required) Data, see help data-with for details. 
        4. native-amount                    (numeric, optional)  Native currency amount to send. eg 0.1. Default - 0.0
        5. startblock                       (numeric, optional)  Block to apply permissions from (inclusive). Default - 0
        6. endblock                         (numeric, optional)  Block to apply permissions to (exclusive). Default - 4294967295
                                                                 If -1 is specified default value is used.

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain grantwithdata "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" connect,send,receive 48656C6C6F20576F726C64210A
        > multichain-cli testchain grantwithdata "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" mine 48656C6C6F20576F726C64210A 0.1
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "grantwithdata", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", admin, 48656C6C6F20576F726C64210A] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def grantwithdatafrom(self, *args) -> t.Dict:
        """
        grantwithdatafrom "from-address" "to-address(es)" "permission(s)" data|publish-new-stream-item ( native-amount startblock endblock )

        Grant permission with metadata using specific address.

        Arguments:
        1. "from-address"                   (string, required) Address used for grant.
        2. "address(es)"                    (string, required) The multichain addresses to send to (comma delimited)
        3. "permission(s)"                  (string, required) Permission strings, comma delimited. 
                                                               Global: connect,send,receive,issue,mine,admin,activate,create 
                                                               or per-asset: asset-identifier.issue,admin,activate,send,receive 
                                                               or per-stream: stream-identifier.write,activate,admin 
        4. data|publish-new-stream-item     (string or object, required) Data, see help data-with for details. 
        5. native-amount                    (numeric, optional)  Native currency amount to send. eg 0.1. Default - 0.0
        6. startblock                       (numeric, optional)  Block to apply permissions from (inclusive). Default - 0
        7. endblock                         (numeric, optional)  Block to apply permissions to (exclusive). Default - 4294967295
                                                                 If -1 is specified default value is used.

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain grantwithdatafrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" connect,send,receive 48656C6C6F20576F726C64210A
        > multichain-cli testchain grantwithdatafrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" mine 48656C6C6F20576F726C64210A 0.1 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "grantwithdatafrom", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", admin, 48656C6C6F20576F726C64210A] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def help(self, *args) -> t.Dict:
        """
        help ( command )

        List all commands, or get help for a specified command.

        Arguments:
        1. "command"                        (string, optional) The command to get help on

        Result:
        "text"                              (string) The help text

        """

    def importaddress(self, *args) -> t.Dict:
        """
        importaddress address(es) ( "label" rescan )

        Adds an address or script (in hex) that can be watched as if it were in your wallet but cannot be used to spend.

        Arguments:
        1. "address(es)"                    (string, required) The addresses, comma delimited
         or
        1. address(es)                      (array, optional) A json array of addresses 
        2. "label"                          (string, optional, default="") An optional label
        3. rescan                           (boolean, optional, default=true) Rescan the wallet for transactions

        Note: This call can take minutes to complete if rescan is true.

        Result:

        Examples:

        Import an address with rescan
        > multichain-cli testchain importaddress "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd"

        Import using a label without rescan
        > multichain-cli testchain importaddress "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "testing" false

        As a JSON-RPC call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "importaddress", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "testing", false] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def importprivkey(self, *args) -> t.Dict:
        """
        importprivkey privkey(s) ( "label" rescan )

        Adds a private key (as returned by dumpprivkey) to your wallet.

        Arguments:
        1. "privkey(s)"                     (string, required) The private key (see dumpprivkey), comma delimited
         or
        1. privkey(s)                       (array, optional) A json array of private keys 
        2. "label"                          (string, optional, default="") An optional label
        3. rescan                           (boolean, optional, default=true) Rescan the wallet for transactions

        Note: This call can take minutes to complete if rescan is true.

        Result:

        Examples:

        Dump a private key
        > multichain-cli testchain dumpprivkey "myaddress"

        Import the private key with rescan
        > multichain-cli testchain importprivkey "mykey"

        Import using a label and without rescan
        > multichain-cli testchain importprivkey "mykey" "testing" false

        As a JSON-RPC call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "importprivkey", "params": ["mykey", "testing", false] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def importwallet(self, *args) -> t.Dict:
        """
        importwallet "filename"

        Imports keys from a wallet dump file (see dumpwallet).

        Arguments:
        1. "filename"                       (string, required) The wallet file

        Examples:

        Dump the wallet
        > multichain-cli testchain dumpwallet "test"

        Import the wallet
        > multichain-cli testchain importwallet "test"

        Import using the json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "importwallet", "params": ["test"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def issue(self, *args) -> t.Dict:
        """
        issue "address" "asset-name"|asset-params quantity ( smallest-unit native-amount custom-fields )

        Issue new asset

        Arguments:
        1. "address"                        (string, required) The address to send newly created asset to.
        2. "asset-name"                     (string, required) Asset name, if not "" should be unique.
         or
        2. asset-params                     (object, required) A json object of with asset params
            {
              "name" : "asset-name"         (string, optional) Asset name
              "open" : true|false           (boolean, optional, default false) True if follow-on issues are allowed
              "restrict" : "restrictions"   (string, optional) Permission strings, comma delimited. Possible values: send,receive
              ,...
            }
        3. quantity                         (numeric, required) The asset total amount in display units. eg. 1234.56
        4. smallest-unit                    (numeric, optional, default=1) Number of raw units in one displayed unit, eg 0.01 for cents
        5. native-amount                    (numeric, optional) native currency amount to send. eg 0.1, Default: minimum-per-output.
        6  custom-fields                    (object, optional)  a json object with custom fields
            {
              "param-name": "param-value"   (strings, required) The key is the parameter name, the value is parameter value
              ,...
            }

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain issue "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "Dollar" 1000000
        > multichain-cli testchain issue "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" Dollar 1000000 0.01 0.01 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "issue", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "Dollar", 1000000, 0.01, 0.01 "description=1 Million dollars"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def issuefrom(self, *args) -> t.Dict:
        """
        issuefrom "from-address" "to-address" "asset-name"|asset-params quantity ( smallest-unit native-amount custom-fields )

        Issue asset using specific address

        Arguments:
        1. "from-address"                   (string, required) Address used for issuing.
        2. "to-address"                     (string, required) The  address to send newly created asset to.
        3. "asset-name"                     (string, required) Asset name, if not "" should be unique.
         or
        3. asset-params                     (object, required) A json object of with asset params
            {
              "name" : "asset-name"         (string, optional) Asset name
              "open" : true|false           (boolean, optional, default false) True if follow-on issues are allowed
              "restrict" : "restrictions"   (string, optional) Permission strings, comma delimited. Possible values: send,receive
              ,...
            }
        4. quantity                         (numeric, required) The asset total amount in display units. eg. 1234.56
        5. smallest-unit                    (numeric, optional, default=1) Number of raw units in one displayed unit, eg 0.01 for cents
        6. native-amount                    (numeric, optional) native currency amount to send. eg 0.1, Default: minimum-per-output.
        7  custom-fields                    (object, optional)  a json object with custom fields
            {
              "param-name": "param-value"   (strings, required) The key is the parameter name, the value is parameter value
              ,...
            }

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain issuefrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "Dollar" 1000000
        > multichain-cli testchain issuefrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" Dollar 1000000 0.01 0.01 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "issuefrom", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "Dollar", 1000000, 0.01, 0.01 "description=1 Million dollars"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def issuemore(self, *args) -> t.Dict:
        """
        issuemore "address" "asset-identifier" quantity ( native-amount custom-fields )

        Create more units for asset

        Arguments:
        1. "address"                        (string, required) The address to send newly created asset to.
        2. "asset-identifier"               (string, required) Asset identifier - one of the following: issue txid, asset reference, asset name.
        3. quantity                         (numeric, required) The asset total amount in display units. eg. 1234.56
        4. native-amount                    (numeric, optional) native currency amount to send. eg 0.1, Default: minimum-per-output.
        5  custom-fields                    (object, optional)  a json object with custom fields
            {
              "param-name": "param-value"   (strings, required) The key is the parameter name, the value is parameter value
              ,...
            }

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain issuemore "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "Dollar" 1000000
        > multichain-cli testchain issuemore "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" Dollar 1000000 0.01 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "issuemore", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "Dollar", 1000000,  0.01 "description=1 Million dollars"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def issuemorefrom(self, *args) -> t.Dict:
        """
        issuemorefrom "from-address" "to-address" "asset-identifier" quantity ( native-amount custom-fields )

        Create more units for asset from specific address

        Arguments:
        1. "from-address"                   (string, required) Address used for issuing.
        2. "to-address"                     (string, required) The  address to send newly created asset to.
        3. "asset-identifier"               (string, required) Asset identifier - one of the following: issue txid, asset reference, asset name.
        4. quantity                         (numeric, required) The asset total amount in display units. eg. 1234.56
        5. native-amount                    (numeric, optional) native currency amount to send. eg 0.1, Default: minimum-per-output.
        6  custom-fields                    (object, optional)  a json object with custom fields
            {
              "param-name": "param-value"   (strings, required) The key is the parameter name, the value is parameter value
              ,...
            }

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain issuemorefrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "Dollar" 1000000
        > multichain-cli testchain issuemorefrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" Dollar 1000000 0.01 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "issuemorefrom", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "Dollar", 1000000, 0.01 "description=1 Million dollars"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def keypoolrefill(self, *args) -> t.Dict:
        """
        keypoolrefill ( newsize )

        Fills the keypool.
        Arguments
        1. newsize                          (numeric, optional, default=100) The new keypool size

        Examples:
        > multichain-cli testchain keypoolrefill 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "keypoolrefill", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def listaccounts(self, *args) -> t.Dict:
        """
        listaccounts ( minconf includeWatchonly)

        Returns Object that has account names as keys, account balances as values.

        Arguments:
        1. minconf                          (numeric, optional, default=1) Only include transactions with at least this many confirmations
        2. includeWatchonly                 (bool, optional, default=false) Include balances in watchonly addresses (see 'importaddress')

        Result:
        {                                   (json object where keys are account names, and values are numeric balances
          "account": x.xxx,                 (numeric) The property name is the account name, and the value is the total balance for the account.
          ...
        }

        Examples:

        List account balances where there at least 1 confirmation
        > multichain-cli testchain listaccounts 

        List account balances including zero confirmation transactions
        > multichain-cli testchain listaccounts 0

        List account balances for 6 or more confirmations
        > multichain-cli testchain listaccounts 6

        As json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listaccounts", "params": [6] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def listaddresses(self, *args) -> t.Dict:
        """
        listaddresses ( address(es) verbose count start ) 

        Returns asset balances for specified address

        Arguments:
        1. "address(es)"                    (string, optional, default *) Address(es) to return information for, comma delimited. Default - all
         or
        1. address(es)                      (array, optional) A json array of addresses to return information for
        2. verbose                          (boolean, optional, default=false) If true return more information about address.
        3. count                            (number, optional, default=INT_MAX - all) The number of addresses to display
        4. start                            (number, optional, default=-count - last) Start from specific address, 0 based, if negative - from the end

        Result:
        An array of address Objects.

        Examples:
        > multichain-cli testchain listaddresses 
        > multichain-cli testchain listaddresses "*" true
        > multichain-cli testchain listaddresses "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" true
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listaddresses", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def listaddressgroupings(self) -> t.Dict:
        """
        listaddressgroupings

        Lists groups of addresses which have had their common ownership
        made public by common use as inputs or as the resulting change
        in past transactions

        Result:
        [
          [
            [
              "address",                    (string) The address
              amount,                       (numeric) The amount in native currency
              "account"                     (string, optional) The account
            ]
            ,...
          ]
          ,...
        ]

        Examples:
        > multichain-cli testchain listaddressgroupings 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listaddressgroupings", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def listaddresstransactions(self, *args) -> t.Dict:
        """
        listaddresstransactions "address" ( count skip verbose )

        Lists information about the <count> most recent transactions related to address in this nodeâ  s wallet.

        Arguments:
        1. "address"                        (string, required)  Address to list transactions for.
        2. count                            (numeric, optional, default=10) The number of transactions to return
        3. skip                             (numeric, optional, default=0) The number of transactions to skip
        4. verbose                          (boolean, optional, default=false) If true, returns detailed array of inputs and outputs and raw hex of transactions

        Result:
        [
          {
            "balance": {...},               (object)  Changes in address balance. 
            {
              "amount": x.xxx,              (numeric) The amount in native currency. Negative value means amount was send by the wallet, positive - received
              "assets": {...},              (object)  Changes in asset amounts. 
            }
            "myaddresses": [...],           (array)   Address passed as parameter.   
            "addresses": [...],             (array)   Array of counterparty addresses  involved in transaction  
            "permissions": [...],           (array)   Changes in permissions 
            "issue": {...},                 (object)  Issue details  
            "data" : "metadata",            (array)   Hexadecimal representation of metadata appended to the transaction
            "confirmations": n,             (numeric)  The number of confirmations for the transaction. Available for 'send' and 
                                                 'receive' category of transactions.
            "blockhash": "hashvalue",       (string) The block hash containing the transaction. Available for 'send' and 'receive'
                                                  category of transactions.
            "blockindex": n,                (numeric) The block index containing the transaction. Available for 'send' and 'receive'
                                                  category of transactions.
            "txid": "transactionid",        (string) The transaction id. Available for 'send' and 'receive' category of transactions.
            "time": xxx,                    (numeric) The transaction time in seconds since epoch (midnight Jan 1 1970 GMT).
            "timereceived": xxx,            (numeric) The time received in seconds since epoch (midnight Jan 1 1970 GMT). Available 
                                                  for 'send' and 'receive' category of transactions.
            "comment": "...",               (string) If a comment is associated with the transaction.
            "vin": [...],                   (array)  If verbose=true. Array of input details
            "vout": [...],                  (array)  If verbose=true. Array of output details
            "hex" : "data"                  (string) If verbose=true. Raw data for transaction
          }
        ]

        Examples:

        List the most recent 10 transactions in the systems
        > multichain-cli testchain listaddresstransactions "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd"

        List transactions 100 to 120 
        > multichain-cli testchain listaddresstransactions "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 20 100

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listaddresstransactions", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", 20, 100] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def listassets(self, *args) -> t.Dict:
        """
        listassets ( asset-identifier(s) verbose count start )

        Returns list of defined assets

        Arguments:
        1. "asset-identifier"               (string, optional) Asset identifier - one of the following: issue txid, asset reference, asset name.
         or
        1. asset-identifier(s)              (array, optional) A json array of asset identifiers 
        2. verbose                          (boolean, optional, default=false) If true, returns list of all issue transactions, including follow-ons 
        3. count                            (number, optional, default=INT_MAX - all) The number of assets to display
        4. start                            (number, optional, default=-count - last) Start from specific asset, 0 based, if negative - from the end

        Result:
        An array containing list of defined assets

        Examples:
        > multichain-cli testchain listassets 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listassets", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def listassettransactions(self, *args) -> t.Dict:
        """
        listassettransactions "asset-identifier" ( verbose count start local-ordering )

        Lists transactions involving asset.

        Arguments:
        1. "asset-identifier"               (string, required) Asset identifier - one of the following: asset txid, asset reference, asset name.
        2. verbose                          (boolean, optional, default=false) If true, returns information about transaction 
        3. count                            (number, optional, default=10) The number of transactions to display
        4. start                            (number, optional, default=-count - last) Start from specific transaction, 0 based, if negative - from the end
        5. local-ordering                   (boolean, optional, default=false) If true, transactions appear in the order they were processed by the wallet,
                                                                               if false - in the order they appear in blockchain

        Result:
        "stream-items"                      (array) List of transactions.

        Examples:
        > multichain-cli testchain listassettransactions "test-asset"
        > multichain-cli testchain listassettransactions "test-asset" true 10 100
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listassettransactions", "params": ["test-asset", false, 20] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def listblocks(self, blocks: t.Union[str,list,dict], verbose: bool=False) -> list:
        """
        listblocks block-set-identifier ( verbose )

        Returns list of block information objects

        Arguments:
        1. "block-set-identifier"           (string, required) Comma delimited list of block identifiers: 
                                                               block height,
                                                               block hash,
                                                               block height range, e.g. <block-from>-<block-to>,
                                                               number of last blocks in the active chain (if negative),
         or
        1. block-set-identifier             (array, required)  A json array of block identifiers 
         or
        1. block-set-identifier             (object, required) A json object with time range
            {
              "starttime" : start-time      (numeric,required) Start time.
              "endtime" : end-time          (numeric,required) End time.
            }
        2. verbose                          (boolean, optional, default=false) If true, returns more information

        Result:
        An array containing list of block information objects

        Examples:
        > multichain-cli testchain listblocks "1000,1100-1120"
        > multichain-cli testchain listblocks "00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listblocks", "params": [1000] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def listlockunspent(self) -> t.Dict:
        """
        listlockunspent

        Returns list of temporarily unspendable outputs.
        See the lockunspent call to lock and unlock transactions for spending.

        Result:
        [
          {
            "txid" : "transactionid",       (string) The transaction id locked
            "vout" : n                      (numeric) The vout value
          }
          ,...
        ]

        Examples:

        List the unspent transactions
        > multichain-cli testchain listunspent 

        Lock an unspent transaction
        > multichain-cli testchain lockunspent false "[{\"txid\":\"a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0\",\"vout\":1}]"

        List the locked transactions
        > multichain-cli testchain listlockunspent 

        Unlock the transaction again
        > multichain-cli testchain lockunspent true "[{\"txid\":\"a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0\",\"vout\":1}]"

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listlockunspent", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def listpermissions(self, *args) -> t.Dict:
        """
        listpermissions ( "permission(s)" address(es) verbose )

        Returns a list of all permissions which have been explicitly granted to addresses.

        Arguments:
        1. "permission(s)"                  (string, optional) Permission strings, comma delimited. Possible values: connect,send,receive,issue,mine,admin,activate,create. Default: all. 
        2. "address(es)"                    (string, optional, default "*") The addresses to retrieve permissions for. "*" for all addresses
         or
        2. address(es)                      (array, optional) A json array of addresses to return permissions for
        3. verbose                          (boolean, optional, default=false) If true, returns list of pending grants 

        Result:
        An array containing list of permissions

        Examples:
        > multichain-cli testchain listpermissions connect,send,receive
        > multichain-cli testchain listpermissions all "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listpermissions", "params": [connect,send,receive] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def listreceivedbyaccount(self, *args) -> t.Dict:
        """
        listreceivedbyaccount ( minconf includeempty includeWatchonly )

        List balances by account.

        Arguments:
        1. minconf                          (numeric, optional, default=1) The minimum number of confirmations before payments are included.
        2. includeempty                     (boolean, optional, default=false) Whether to include accounts that haven't received any payments.
        3. includeWatchonly                 (bool, optional, default=false) Whether to include watchonly addresses (see 'importaddress').

        Result:
        [
          {
            "involvesWatchonly" : "true",   (bool) Only returned if imported addresses were involved in transaction
            "account" : "accountname",      (string) The account name of the receiving account
            "amount" : x.xxx,               (numeric) The total amount received by addresses with this account
            "confirmations" : n             (numeric) The number of confirmations of the most recent transaction included
          }
          ,...
        ]

        Examples:
        > multichain-cli testchain listreceivedbyaccount 
        > multichain-cli testchain listreceivedbyaccount 6 true
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listreceivedbyaccount", "params": [6, true, true] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def listreceivedbyaddress(self, *args) -> t.Dict:
        """
        listreceivedbyaddress ( minconf includeempty includeWatchonly )

        List balances by receiving address.

        Arguments:
        1. minconf                          (numeric, optional, default=1) The minimum number of confirmations before payments are included.
        2. includeempty                     (numeric, optional, default=false) Whether to include addresses that haven't received any payments.
        3. includeWatchonly                 (bool, optional, default=false) Whether to include watchonly addresses (see 'importaddress').

        Result:
        [
          {
            "involvesWatchonly" : "true",   (bool) Only returned if imported addresses were involved in transaction
            "address" : "receivingaddress", (string) The receiving address
            "account" : "accountname",      (string) The account of the receiving address. The default account is "".
            "amount" : x.xxx,               (numeric) The total amount in native currency received by the address
            "confirmations" : n             (numeric) The number of confirmations of the most recent transaction included
          }
          ,...
        ]

        Examples:
        > multichain-cli testchain listreceivedbyaddress 
        > multichain-cli testchain listreceivedbyaddress 6 true
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listreceivedbyaddress", "params": [6, true, true] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def listsinceblock(self, *args) -> t.Dict:
        """
        listsinceblock ( blockhash target-confirmations includeWatchonly )

        Get all transactions in blocks since block [blockhash], or all transactions if omitted

        Arguments:
        1. blockhash                        (string, optional) The block hash to list transactions since
        2. target-confirmations:            (numeric, optional) The confirmations required, must be 1 or more
        3. includeWatchonly:                (bool, optional, default=false) Include transactions to watchonly addresses (see 'importaddress')
        Result:
        {
          "transactions": [
            "account":"accountname",        (string) The account name associated with the transaction. Will be "" for the default account.
            "address":"address",            (string) The  address of the transaction. Not present for move transactions (category = move).
            "category":"send|receive",      (string) The transaction category. 'send' has negative amounts, 'receive' has positive amounts.
            "amount": x.xxx,                (numeric) The amount in btc. This is negative for the 'send' category, and for the 'move' category for moves 
                                                  outbound. It is positive for the 'receive' category, and for the 'move' category for inbound funds.
            "vout" : n,                     (numeric) the vout value
            "fee": x.xxx,                   (numeric) The amount of the fee in btc. This is negative and only available for the 'send' category of transactions.
            "confirmations": n,             (numeric) The number of confirmations for the transaction.
                                                      Available for 'send' and 'receive' category of transactions.
            "blockhash": "hashvalue",       (string) The block hash containing the transaction. Available for 'send' and 'receive' category of transactions.
            "blockindex": n,                (numeric) The block index containing the transaction. Available for 'send' and 'receive' category of transactions.
            "blocktime": xxx,               (numeric) The block time in seconds since epoch (1 Jan 1970 GMT).
            "txid": "transactionid",        (string) The transaction id. Available for 'send' and 'receive' category of transactions.
            "time": xxx,                    (numeric) The transaction time in seconds since epoch (Jan 1 1970 GMT).
            "timereceived": xxx,            (numeric) The time received in seconds since epoch (Jan 1 1970 GMT).
                                                      Available for 'send' and 'receive' category of transactions.
            "comment": "...",               (string) If a comment is associated with the transaction.
            "to": "...",                    (string) If a comment to is associated with the transaction.
          ],
          "lastblock": "lastblockhash"      (string) The hash of the last block
        }

        Examples:
        > multichain-cli testchain listsinceblock 
        > multichain-cli testchain listsinceblock "000000000000000bacf66f7497b7dc45ef753ee9a7d38571037cdb1a57f663ad" 6
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listsinceblock", "params": ["000000000000000bacf66f7497b7dc45ef753ee9a7d38571037cdb1a57f663ad", 6] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def liststreamblockitems(self, *args) -> t.Dict:
        """
        liststreamblockitems "stream-identifier" block-set-identifier ( verbose count start )

        Returns stream items in certain block range.

        Arguments:
        1. "stream-identifier"              (string, required) Stream identifier - one of the following: stream txid, stream reference, stream name.
        2. "block-set-identifier"           (string, required) Comma delimited list of block identifiers: 
                                                               block height,
                                                               block hash,
                                                               block height range, e.g. <block-from>-<block-to>,
                                                               number of last blocks in the active chain (if negative),
         or
        2. block-set-identifier             (array, required)  A json array of block identifiers 
         or
        2. block-set-identifier             (object, required) A json object with time range
            {
              "starttime" : start-time      (numeric,required) Start time.
              "endtime" : end-time          (numeric,required) End time.
            }
        3. verbose                          (boolean, optional, default=false) If true, returns information about item transaction 
        4. count                            (number, optional, default==INT_MAX) The number of items to display
        5. start                            (number, optional, default=-count - last) Start from specific item, 0 based, if negative - from the end

        Result:
        stream-items                        (array) List of stream items.

        Examples:
        > multichain-cli testchain liststreamblockitems "test-stream" 1000,1100-1120 
        > multichain-cli testchain liststreamblockitems "test-stream" 1000 true 10 100
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "liststreamblockitems", "params": ["test-stream", 1000, false, 20] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def liststreamitems(self, *args) -> t.Dict:
        """
        liststreamitems "stream-identifier" ( verbose count start local-ordering )

        Returns stream items.

        Arguments:
        1. "stream-identifier"              (string, required) Stream identifier - one of the following: stream txid, stream reference, stream name.
        2. verbose                          (boolean, optional, default=false) If true, returns information about item transaction 
        3. count                            (number, optional, default=10) The number of items to display
        4. start                            (number, optional, default=-count - last) Start from specific item, 0 based, if negative - from the end
        5. local-ordering                   (boolean, optional, default=false) If true, items appear in the order they were processed by the wallet,
                                                                               if false - in the order they appear in blockchain

        Result:
        "stream-items"                      (array) List of stream items.

        Examples:
        > multichain-cli testchain liststreamitems "test-stream"
        > multichain-cli testchain liststreamitems "test-stream" true 10 100
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "liststreamitems", "params": ["test-stream", false, 20] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def liststreamkeyitems(self, *args) -> t.Dict:
        """
        liststreamkeyitems "stream-identifier" "key" ( verbose count start local-ordering )

        Returns stream items for specific key.

        Arguments:
        1. "stream-identifier"              (string, required) Stream identifier - one of the following: stream txid, stream reference, stream name.
        2. "key"                            (string, required) Stream key
        3. verbose                          (boolean, optional, default=false) If true, returns information about item transaction 
        4. count                            (number, optional, default=10) The number of items to display
        5. start                            (number, optional, default=-count - last) Start from specific item, 0 based, if negative - from the end
        6. local-ordering                   (boolean, optional, default=false) If true, items appear in the order they were processed by the wallet,
                                                                               if false - in the order they appear in blockchain

        Result:
        "stream-items"                      (array) List of stream items for specific key.

        Examples:
        > multichain-cli testchain liststreamkeyitems "test-stream" "key01"
        > multichain-cli testchain liststreamkeyitems "test-stream" "key01" true 10 100
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "liststreamkeyitems", "params": ["test-stream", "key01", false 20] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def liststreamkeys(self, *args) -> t.Dict:
        """
        liststreamkeys "stream-identifier" ( key(s) verbose count start local-ordering )

        Returns stream keys.

        Arguments:
        1. "stream-identifier"              (string, required) Stream identifier - one of the following: stream txid, stream reference, stream name.
        2. "key"                            (string, optional, default=*) Stream key
         or
        2. key(s)                           (array, optional) A json array of stream keys 
        3. verbose                          (boolean, optional, default=false) If true, returns extended information about key 
        4. count                            (number, optional, default=INT_MAX - all) The number of items to display
        5. start                            (number, optional, default=-count - last) Start from specific item, 0 based, if negative - from the end
        6. local-ordering                   (boolean, optional, default=false) If true, items appear in the order they were processed by the wallet,
                                                                               if false - in the order they apppear in blockchain

        Result:
        "stream-keys"                       (array) List of stream keys.

        Examples:
        > multichain-cli testchain liststreamkeys "test-stream" 
        > multichain-cli testchain liststreamkeys "test-stream" "key01"
        > multichain-cli testchain liststreamkeys "test-stream" "*" true 10 100
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "liststreamkeys", "params": ["test-stream", "key01"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def liststreampublisheritems(self, *args) -> t.Dict:
        """
        liststreampublisheritems "stream-identifier" "address" ( verbose count start local-ordering )

        Returns stream items for specific publisher.

        Arguments:
        1. "stream-identifier"              (string, required) Stream identifier - one of the following: stream txid, stream reference, stream name.
        2. "address"                        (string, required) Publisher address
        3. verbose                          (boolean, optional, default=false) If true, returns information about item transaction 
        4. count                            (number, optional, default=10) The number of items to display
        5. start                            (number, optional, default=-count - last) Start from specific item, 0 based, if negative - from the end
        6. local-ordering                   (boolean, optional, default=false) If true, items appear in the order they were processed by the wallet,
                                                                               if false - in the order they appear in blockchain

        Result:
        "stream-items"                      (array) List of stream items for specific publisher.

        Examples:
        > multichain-cli testchain liststreampublisheritems "test-stream" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd"
        > multichain-cli testchain liststreampublisheritems "test-stream" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" true 10 100
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "liststreampublisheritems", "params": ["test-stream", "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", false, 20] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def liststreampublishers(self, *args) -> t.Dict:
        """
        liststreampublishers "stream-identifier" ( address(es) verbose count start local-ordering )

        Returns stream publishers.

        Arguments:
        1. "stream-identifier"              (string, required) Stream identifier - one of the following: stream txid, stream reference, stream name.
        2. "address(es)"                    (string, optional, default=*) Publisher addresses, comma delimited
         or
        2. address(es)                      (array, optional) A json array of publisher addresses 
        3. verbose                          (boolean, optional, default=false) If true, returns extended information about publisher 
        4. count                            (number, optional, default=INT_MAX - all) The number of items to display
        5. start                            (number, optional, default=-count - last) Start from specific item, 0 based, if negative - from the end
        6. local-ordering                   (boolean, optional, default=false) If true, items appear in the order they were processed by the wallet,
                                                                               if false - in the order they appear in blockchain

        Result:
        "stream-publishers"                 (array) List of stream publishers.

        Examples:
        > multichain-cli testchain liststreampublishers "test-stream" 
        > multichain-cli testchain liststreampublishers "test-stream" 1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd
        > multichain-cli testchain liststreampublishers "test-stream" "*" true 10 100
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "liststreampublishers", "params": ["test-stream", "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def liststreams(self, *args) -> t.Dict:
        """
        liststreams ( stream-identifier(s) verbose count start )

        Returns list of defined streams

        Arguments:
        1. "stream-identifier(s)"           (string, optional, default=*, all streams) Stream identifier - one of the following: issue txid, stream reference, stream name.
         or
        1. stream-identifier(s)             (array, optional) A json array of stream identifiers 
        2. verbose                          (boolean, optional, default=false) If true, returns stream list of creators 
        3. count                            (number, optional, default=INT_MAX - all) The number of streams to display
        4. start                            (number, optional, default=-count - last) Start from specific stream, 0 based, if negative - from the end

        Result:
        An array containing list of defined streams

        Examples:
        > multichain-cli testchain liststreams 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "liststreams", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def liststreamtxitems(self, *args) -> t.Dict:
        """
        liststreamtxitems "stream-identifier" "txid" ( verbose )

        Returns stream items.

        Arguments:
        1. "stream-identifier"              (string, required) Stream identifier - one of the following: stream txid, stream reference, stream name.
        2. "txid"                           (string, required) The transaction id
        3. verbose                          (boolean, optional, default=false) If true, returns information about item transaction 

        Result:
        "stream-items"                      (array) Array of stream items.

        Examples:
        > multichain-cli testchain liststreamtxitems "mytxid"
        > multichain-cli testchain liststreamtxitems "mytxid"  true
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "liststreamtxitems", "params": ["mytxid", false] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def listtransactions(self, *args) -> t.Dict:
        """
        listtransactions ( "account" count from includeWatchonly )

        Returns up to 'count' most recent transactions skipping the first 'from' transactions for account 'account'.

        Arguments:
        1. "account"                        (string, optional) The account name. If not included, it will list all transactions for all accounts.
                                                               If "" is set, it will list transactions for the default account.
        2. count                            (numeric, optional, default=10) The number of transactions to return
        3. from                             (numeric, optional, default=0) The number of transactions to skip
        4. includeWatchonly                 (bool, optional, default=false) Include transactions to watchonly addresses (see 'importaddress')

        Result:
        [
          {
            "account":"accountname",        (string) The account name associated with the transaction. 
                                                      It will be "" for the default account.
            "address":"address",            (string) The address of the transaction. Not present for 
                                                      move transactions (category = move).
            "category":"send|receive|move", (string) The transaction category. 'move' is a local (off blockchain)
                                                      transaction between accounts, and not associated with an address,
                                                      transaction id or block. 'send' and 'receive' transactions are 
                                                      associated with an address, transaction id and block details
            "amount": x.xxx,                (numeric)  The amount in btc. This is negative for the 'send' category, and for the
                                                      'move' category for moves outbound. It is positive for the 'receive' category,
                                                      and for the 'move' category for inbound funds.
            "vout" : n,                     (numeric) the vout value
            "fee": x.xxx,                   (numeric) The amount of the fee in btc. This is negative and only available for the 
                                                      'send' category of transactions.
            "confirmations": n,             (numeric) The number of confirmations for the transaction. Available for 'send' and 
                                                      'receive' category of transactions.
            "blockhash": "hashvalue",       (string) The block hash containing the transaction. Available for 'send' and 'receive'
                                                      category of transactions.
            "blockindex": n,                (numeric) The block index containing the transaction. Available for 'send' and 'receive'
                                                      category of transactions.
            "txid": "transactionid",        (string) The transaction id. Available for 'send' and 'receive' category of transactions.
            "time": xxx,                    (numeric) The transaction time in seconds since epoch (midnight Jan 1 1970 GMT).
            "timereceived": xxx,            (numeric) The time received in seconds since epoch (midnight Jan 1 1970 GMT). Available 
                                                      for 'send' and 'receive' category of transactions.
            "comment": "...",               (string) If a comment is associated with the transaction.
            "otheraccount": "accountname",  (string) For the 'move' category of transactions, the account the funds came 
                                                      from (for receiving funds, positive amounts), or went to (for sending funds,
                                                      negative amounts).
          }
        ]

        Examples:

        List the most recent 10 transactions in the systems
        > multichain-cli testchain listtransactions 

        List the most recent 10 transactions for the tabby account
        > multichain-cli testchain listtransactions "tabby"

        List transactions 100 to 120 from the tabby account
        > multichain-cli testchain listtransactions "tabby" 20 100

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listtransactions", "params": ["tabby", 20, 100] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def listunspent(self, *args) -> t.Dict:
        """
        listunspent ( minconf maxconf addresses )

        Returns array of unspent transaction outputs
        with between minconf and maxconf (inclusive) confirmations.
        Optionally filter to only include txouts paid to specified addresses.
        Results are an array of Objects, each of which has:
        {txid, vout, scriptPubKey, amount, confirmations}

        Arguments:
        1. minconf                          (numeric, optional, default=1) The minimum confirmations to filter
        2. maxconf                          (numeric, optional, default=9999999) The maximum confirmations to filter
        3. addresses                        (array, optional) A json array of addresses to filter
            [
              "address"                     (string) address
              ,...
            ]

        Result
        [                                   (array of json object)
          {
            "txid" : "txid",                (string) the transaction id 
            "vout" : n,                     (numeric) the vout value
            "address" : "address",          (string) the address
            "account" : "account",          (string) The associated account, or "" for the default account
            "scriptPubKey" : "key",         (string) the script key
            "amount" : x.xxx,               (numeric) the transaction amount in btc
            "confirmations" : n             (numeric) The number of confirmations
          }
          ,...
        ]

        Examples
        > multichain-cli testchain listunspent 
        > multichain-cli testchain listunspent 6 9999999 "[\"1PGFqEzfmQch1gKD3ra4k18PNj3tTUUSqg\",\"1LtvqCaApEdUGFkpKMM4MstjcaL4dKg8SP\"]"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listunspent", "params": [6, 9999999 "[\"1PGFqEzfmQch1gKD3ra4k18PNj3tTUUSqg\",\"1LtvqCaApEdUGFkpKMM4MstjcaL4dKg8SP\"]"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def listupgrades(self, *args) -> t.Dict:
        """
        listupgrades (upgrade-identifier(s))
        1. "upgrade-identifier(s)"          (string, optional, default=*, all upgrades) Upgrade identifier - one of the following:
                                                                                        upgrade txid, upgrade name.
         or
        1. upgrade-identifier(s)            (array, optional) A json array of upgrade identifiers 

        Returns list of defined upgrades

        Examples:
        > multichain-cli testchain listupgrades 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listupgrades", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def listwallettransactions(self, count: int=10, skip: int=0, includeWatchonly: bool=False, verbose: bool=False) -> t.List[t.Dict]:
        """
        listwallettransactions ( count skip includeWatchonly verbose )

        Lists information about the <count> most recent transactions in this nodeâ  s wallet.

        Arguments:
        1. count                            (numeric, optional, default=10) The number of transactions to return
        2. skip                             (numeric, optional, default=0) The number of transactions to skip
        3. includeWatchonly                 (bool, optional, default=false) Include transactions to watchonly addresses (see 'importaddress')
        4. verbose                          (bool, optional, default=false) If true, returns detailed array of inputs and outputs and raw hex of transactions

        Result:
        [
          {
            "balance": {...},               (object)  Changes in wallet balance. 
            {
              "amount": x.xxx,              (numeric) The amount in native currency. Negative value means amount was send by the wallet, positive - received
              "assets": {...},              (object)  Changes in asset amounts. 
            }
            "myaddresses": [...],           (array)   Array of wallet addresses involved in transaction   
            "addresses": [...],             (array)   Array of counterparty addresses  involved in transaction  
            "permissions": [...],           (array)   Changes in permissions 
            "issue": {...},                 (object)  Issue details  
            "data" : "metadata",            (array)   Hexadecimal representation of metadata appended to the transaction
            "confirmations": n,             (numeric) The number of confirmations for the transaction. Available for 'send' and 
                                                      'receive' category of transactions.
            "blockhash": "hashvalue",       (string)   The block hash containing the transaction. Available for 'send' and 'receive'
                                                       category of transactions.
            "blockindex": n,                (numeric)  The block index containing the transaction. Available for 'send' and 'receive'
                                                       category of transactions.
            "txid": "transactionid",        (string) The transaction id. Available for 'send' and 'receive' category of transactions.
            "time": xxx,                    (numeric)  The transaction time in seconds since epoch (midnight Jan 1 1970 GMT).
            "timereceived": xxx,            (numeric)  The time received in seconds since epoch (midnight Jan 1 1970 GMT). Available 
                                                       for 'send' and 'receive' category of transactions.
            "comment": "...",               (string) If a comment is associated with the transaction.
            "vin": [...],                   (array)  If verbose=true. Array of input details
            "vout": [...],                  (array)  If verbose=true. Array of output details
            "hex" : "data"                  (string) If verbose=true. Raw data for transaction
          }
        ]

        Examples:

        List the most recent 10 transactions in the systems
        > multichain-cli testchain listwallettransactions 

        List transactions 100 to 120 
        > multichain-cli testchain listwallettransactions 20 100

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listwallettransactions", "params": [20, 100] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def lockunspent(self, *args) -> t.Dict:
        """
        lockunspent unlock [{"txid":"txid","vout":n},...]

        Updates list of temporarily unspendable outputs.
        Temporarily lock (unlock=false) or unlock (unlock=true) specified transaction outputs.
        A locked transaction output will not be chosen by automatic coin selection, when spending assetss.
        Locks are stored in memory only. Nodes start with zero locked outputs, and the locked output list
        is always cleared (by virtue of process exit) when a node stops or fails.
        Also see the listunspent call

        Arguments:
        1. unlock                           (boolean, required) Whether to unlock (true) or lock (false) the specified transactions
        2. transactions                     (array, required) A json array of objects. Each object the txid (string) vout (numeric)
             [                              (json array of json objects)
               {
                 "txid":"id",               (string) The transaction id
                 "vout": n                  (numeric) The output number
               }
               ,...
             ]

        Result:
        true|false                          (boolean) Whether the command was successful or not

        Examples:

        List the unspent transactions
        > multichain-cli testchain listunspent 

        Lock an unspent transaction
        > multichain-cli testchain lockunspent false "[{\"txid\":\"a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0\",\"vout\":1}]"

        List the locked transactions
        > multichain-cli testchain listlockunspent 

        Unlock the transaction again
        > multichain-cli testchain lockunspent true "[{\"txid\":\"a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0\",\"vout\":1}]"

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "lockunspent", "params": [false, "[{\"txid\":\"a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0\",\"vout\":1}]"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def move(self, *args) -> t.Dict:
        """
        move "fromaccount" "toaccount" amount ( minconf "comment" )

        Move a specified amount from one account in your wallet to another.

        Arguments:
        1. "fromaccount"                    (string, required) The name of the account to move funds from. May be the default account using "".
        2. "toaccount"                      (string, required) The name of the account to move funds to. May be the default account using "".
        3. minconf                          (numeric, optional, default=1) Only use funds with at least this many confirmations.
        4. "comment"                        (string, optional) An optional comment, stored in the wallet only.

        Result:
        true|false                          (boolean) true if successfull.

        Examples:

        Move 0.01 btc from the default account to the account named tabby
        > multichain-cli testchain move "" "tabby" 0.01

        Move 0.01 btc timotei to akiko with a comment and funds have 6 confirmations
        > multichain-cli testchain move "timotei" "akiko" 0.01 6 "happy birthday!"

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "move", "params": ["timotei", "akiko", 0.01, 6, "happy birthday!"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def pause(self, *args) -> t.Dict:
        """
        pause "task(s)" 

        Pauses local mining or the processing of incoming transactions and blocks.

        Arguments:
        1. "task(s)"                        (string, required) Task(s) to be paused. Possible values: incoming,mining 

        Examples:
        > multichain-cli testchain pause incoming,mining
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "pause", "params": [incoming] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def ping(self) -> t.Dict:
        """
        ping

        Requests that a ping be sent to all other nodes, to measure ping time.
        Results provided in getpeerinfo, pingtime and pingwait fields are decimal seconds.
        Ping command is handled in queue with all other commands, so it measures processing backlog, not just network ping.

        Result:

        Examples:
        > multichain-cli testchain ping 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "ping", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def preparelockunspent(self, *args) -> t.Dict:
        """
        preparelockunspent asset-quantities ( lock )

        Prepares exchange transaction output for createrawexchange, appendrawexchange

        Arguments:
        1. asset-quantities                 (object, required) A json object of assets to send
            {
              "asset-identifier" : asset-quantity
              ,...
            }
        2. lock                             (boolean, optional, default=true) Lock prepared unspent output

        Result:
        {
          "txid": "transactionid",          (string) Transaction ID of the output which can be spent in createrawexchange or createrawexchange
          "vout": n                         (numeric) Output index
        }

        Examples:
        > multichain-cli testchain preparelockunspent "{\"12345-6789-1234\":100}"
        > multichain-cli testchain preparelockunspent "{\"12345-6789-1234\":100,\"1234-5678-1234\":200}"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "preparelockunspent", "params": ["{\"12345-6789-1234\":100,\"1234-5678-1234\":200}"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def preparelockunspentfrom(self, *args) -> t.Dict:
        """
        preparelockunspentfrom "from-address" asset-quantities ( lock )

        Prepares exchange transaction output for createrawexchange, appendrawexchange using specific address

        Arguments:
        1. "from-address"                   (string, required) Address to send from .
        2. asset-quantities                 (object, required) A json object of assets to send
            {
              "asset-identifier" : asset-quantity
              ,...
            }
        3. lock                             (boolean, optiona, default=true) Lock prepared unspent output

        Result:
        {
          "txid": "transactionid",          (string) Transaction ID of the output which can be spent in createrawexchange or createrawexchange
          "vout": n                         (numeric) Output index
        }

        Examples:
        > multichain-cli testchain preparelockunspentfrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "{\"12345-6789-1234\":100}"
        > multichain-cli testchain preparelockunspentfrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "{\"12345-6789-1234\":100,\"1234-5678-1234\":200}"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "preparelockunspentfrom", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "{\"12345-6789-1234\":100,\"1234-5678-1234\":200}"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def prioritisetransaction(self, *args) -> t.Dict:
        """
        prioritisetransaction txid priority-delta fee-delta
        Accepts the transaction into mined blocks at a higher (or lower) priority

        Arguments:
        1. txid                             (string, required) The transaction id.
        2. priority-delta                   (numeric, required) The priority to add or subtract.
                                            The transaction selection algorithm considers the tx as it would have a higher priority.
                                            (priority of a transaction is calculated: coinage * value_in_satoshis / txsize) 
        3. fee-delta                        (numeric, required) The fee value (in satoshis) to add (or subtract, if negative).
                                            The fee is not actually paid, only the algorithm for selecting transactions into a block
                                            considers the transaction as it would have paid a higher (or lower) fee.

        Result
        true                                (boolean) Returns true

        Examples:
        > multichain-cli testchain prioritisetransaction "txid" 0.0 10000
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "prioritisetransaction", "params": ["txid", 0.0, 10000] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def publish(self, *args) -> t.Dict:
        """
        publish "stream-identifier" "key"|keys "data-hex"|data-obj 

        Publishes stream item

        Arguments:
        1. "stream-identifier"              (string, required) Stream identifier - one of the following: stream txid, stream reference, stream name.
        2. "key"                            (string, required) Item key
         or
        2. keys                             (array, required) Array of item keys
        3. "data-hex"                       (string, required) Data hex string
         or
        3. data-json                        (object, required) JSON data object
            {
              "json" : data-json            (object, required) Valid JSON object
            }
         or
        3. data-text                        (object, required) Text data object
            {
              "text" : "data-text"          (string, required) Data string
            }

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain publish test "hello world" 48656C6C6F20576F726C64210A
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "publish", "params": ["test", "hello world", "48656C6C6F20576F726C64210A"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def publishfrom(self, *args) -> t.Dict:
        """
        publishfrom "from-address" "stream-identifier" "key"|keys "data-hex"|data-obj 

        Publishes stream item from specific address

        Arguments:
        1. "from-address"                   (string, required) Address used for issuing.
        2. "stream-identifier"              (string, required) Stream identifier - one of the following: stream txid, stream reference, stream name.
        3. "key"                            (string, required) Item key
         or
        3. keys                             (array, required) Array of item keys
        4. "data-hex"                       (string, required) Data hex string
         or
        4. data-json                        (object, required) JSON data object
            {
              "json" : data-json            (object, required) Valid JSON object
            }
         or
        4. data-text                        (object, required) Text data object
            {
              "text" : "data-text"          (string, required) Data string
            }

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain publishfrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" test "hello world" 48656C6C6F20576F726C64210A
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "publishfrom", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "test", "hello world", "48656C6C6F20576F726C64210A"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def resendwallettransactions(self) -> t.Dict:
        """
        resendwallettransactions

        Stop Resends wallet transactions.
        """

    def resume(self, *args) -> t.Dict:
        """
        resume "task(s)" 

        Resumes local mining or the processing of incoming transactions and blocks

        Arguments:
        1. "task(s)"                        (string, required) Task(s) to be resumed. Possible values: incoming,mining 

        Examples:
        > multichain-cli testchain resume incoming,mining
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "resume", "params": [mining] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def revoke(self, *args) -> t.Dict:
        """
        revoke "address(es)" "permission(s)" ( native-amount "comment" "comment-to" )

        Revoke permission from a given address. The amount is a real

        Arguments:
        1. "address(es)"                    (string, required) The addresses(es) to revoke permissions from
        2. "permission(s)"                  (string, required) Permission strings, comma delimited. 
                                                               Global: connect,send,receive,issue,mine,admin,activate,create 
                                                               or per-asset: asset-identifier.issue,admin,activate,send,receive 
                                                               or per-stream: stream-identifier.write,activate,admin 
        3. native-amount                    (numeric, optional) native currency amount to send. eg 0.1. Default - 0
        4. "comment"                        (string, optional) A comment used to store what the transaction is for. 
                                                               This is not part of the transaction, just kept in your wallet.
        5. "comment-to"                     (string, optional) A comment to store the name of the person or organization 
                                                               to which you're sending the transaction. This is not part of the 
                                                               transaction, just kept in your wallet.

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain revoke "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 connect,send,receive
        > multichain-cli testchain revoke "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 mine "permission to mine" "Rogue Miner"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "revoke", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", 0.1, admin "disabling temporary admin", "Admins Ltd."] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def revokefrom(self, *args) -> t.Dict:
        """
        revokefrom "from-address" "to-address(es)" "permission(s)" ( native-amount "comment" "comment-to" )

        Revoke permissions using specific address.

        Arguments:
        1. "from-address"                   (string, required) Addresses used for revoke.
        2. "to-address(es)"                 (string, required) The addresses(es) to revoke permissions from. Comma delimited
        3. "permission(s)"                  (string, required) Permission strings, comma delimited. 
                                                               Global: connect,send,receive,issue,mine,admin,activate,create 
                                                               or per-asset: asset-identifier.issue,admin,activate,send,receive 
                                                               or per-stream: stream-identifier.write,activate,admin 
        4. native-amount                    (numeric, optional) native currency amount to send. eg 0.1. Default - 0
        5. "comment"                        (string, optional) A comment used to store what the transaction is for. 
                                                               This is not part of the transaction, just kept in your wallet.
        6. "comment-to"                     (string, optional) A comment to store the name of the person or organization 
                                                               to which you're sending the transaction. This is not part of the 
                                                               transaction, just kept in your wallet.

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain revokefrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 connect,send,receive
        > multichain-cli testchain revokefrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 mine "permission to mine" "Rogue Miner"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "revokefrom", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", 0.1, admin "disabling temporary admin", "Admins Ltd."] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def send(self, *args) -> t.Dict:
        """
        send "address" amount|asset-quantities ( "comment" "comment-to" )

        Send an amount (or several asset amounts) to a given address. The amount is a real and is rounded to the nearest 0.00000001

        Arguments:
        1. address                          (string, required) The address to send to.
        2. amount                           (numeric, required) The amount in native currency to send. eg 0.1
         or
        2. asset-quantities                 (object, required) A json object of assets to send
            {
              "asset-identifier" : asset-quantity
              ,...
            }
        3. "comment"                        (string, optional) A comment used to store what the transaction is for. 
                                                               This is not part of the transaction, just kept in your wallet.
        4. "comment-to"                     (string, optional) A comment to store the name of the person or organization 
                                                               to which you're sending the transaction. This is not part of the 
                                                               transaction, just kept in your wallet.

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain send "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "{\"12345-6789-1234\":100,\"1234-5678-1234\":200}"
        > multichain-cli testchain send "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 "donation" "seans outpost"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "send", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", 0.1, "donation", "seans outpost"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def sendasset(self, *args) -> t.Dict:
        """
        sendasset "address" "asset-identifier" asset-qty ( native-amount "comment" "comment-to" )

        Send asset amount to a given address. The amounts are real.

        Arguments:
        1. "address"                        (string, required) The address to send to.
        2. "asset-identifier"               (string, required) Asset identifier - one of the following: issue txid, asset reference, asset name.
        3. asset-qty                        (numeric, required) Asset quantity to send. eg 0.1
        4. native-amount                    (numeric, optional) native currency amount to send. eg 0.1, Default: minimum-per-output.
        5. "comment"                        (string, optional) A comment used to store what the transaction is for. 
                                                               This is not part of the transaction, just kept in your wallet.
        6. "comment-to"                     (string, optional) A comment to store the name of the person or organization 
                                                               to which you're sending the transaction. This is not part of the 
                                                               transaction, just kept in your wallet.

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain sendasset "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 12345-6789-1234 100
        > multichain-cli testchain sendasset "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 12345-6789-1234 100 0.1 "donation" "seans outpost"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendasset", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", 12345-6789-1234, 100, 0.1, "donation", "seans outpost"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def sendassetfrom(self, *args) -> t.Dict:
        """
        sendassetfrom "from-address" "to-address" "asset-identifier" asset-qty ( native-amount "comment" "comment-to" )

        Send an asset amount using specific address. 

        Arguments:
        1. "from-address"                   (string, required) Address to send from. 
        2. "to-address"                     (string, required) The address to send to.
        3. "asset-identifier"               (string, required) Asset identifier - one of the following: issue txid, asset reference, asset name.
        4. asset-qty                        (numeric, required) Asset quantity to send. eg 0.1
        5. native-amount                    (numeric, optional) native currency amount to send. eg 0.1, Default: minimum-per-output.
        6. "comment"                        (string, optional) A comment used to store what the transaction is for. 
                                                               This is not part of the transaction, just kept in your wallet.
        7. "comment-to"                     (string, optional) A comment to store the name of the person or organization 
                                                               to which you're sending the transaction. This is not part of the 
                                                               transaction, just kept in your wallet.

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain sendassetfrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 12345-6789-1234 100
        > multichain-cli testchain sendassetfrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 12345-6789-1234 100 "donation" "seans outpost"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendassetfrom", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", 0.1, 12345-6789-1234, 100, "donation", "seans outpost"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def sendfrom(self, *args) -> t.Dict:
        """
        sendfrom "from-address" "to-address" amount|asset-quantities ( "comment" "comment-to" )

        Send an amount (or several asset amounts) using specific address.

        Arguments:
        1. "from-address"                   (string, required) Address to send from.
        2. "to-address"                     (string, required) The address to send to.
        3. amount                           (numeric, required) The amount in native currency to send. eg 0.1
         or
        3. asset-quantities                 (object, required) A json object of assets to send
            {
              "asset-identifier" : asset-quantity
              ,...
            }
        4. "comment"                        (string, optional) A comment used to store what the transaction is for. 
                                                               This is not part of the transaction, just kept in your wallet.
        5. "comment-to"                     (string, optional) A comment to store the name of the person or organization 
                                                               to which you're sending the transaction. This is not part of the 
                                                               transaction, just kept in your wallet.

        Result:
        "transactionid"  (string) The transaction id.

        Examples:
        > multichain-cli testchain sendfrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "{\"12345-6789-1234\":100,\"1234-5678-1234\":200}"
        > multichain-cli testchain sendfrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 "donation" "seans outpost"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendfrom", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", 0.1, "donation", "seans outpost"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def sendfromaccount(self, *args) -> t.Dict:
        """
        sendfromaccount "fromaccount" toaddress amount ( minconf "comment" "comment-to" )

        Sent an amount from an account to a address.
        The amount is a real and is rounded to the nearest 0.00000001.
        Arguments:
        1. "fromaccount"                    (string, required) The name of the account to send funds from. May be the default account using "".
        2. toaddress                        (string, required) The address to send funds to.
        3. amount                           (numeric, required) The amount in native currency. (transaction fee is added on top).
        4. minconf                          (numeric, optional, default=1) Only use funds with at least this many confirmations.
        5. "comment"                        (string, optional) A comment used to store what the transaction is for. 
                                                               This is not part of the transaction, just kept in your wallet.
        6. "comment-to"                     (string, optional) An optional comment to store the name of the person or organization 
                                                               to which you're sending the transaction. This is not part of the transaction, 
                                                               it is just kept in your wallet.

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:

        Send 0.01 btc from the default account to the address, must have at least 1 confirmation
        > multichain-cli testchain sendfromaccount "" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.01

        Send 0.01 from the tabby account to the given address, funds must have at least 6 confirmations
        > multichain-cli testchain sendfromaccount "tabby" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.01 6 "donation" "seans outpost"

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendfromaccount", "params": ["tabby", "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", 0.01, 6, "donation", "seans outpost"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def sendmany(self, *args) -> t.Dict:
        """
        sendmany "fromaccount" {"address":amount,...} ( minconf "comment" )

        Send multiple times. Amounts are double-precision floating point numbers.
        Arguments:
        1. "fromaccount"                    (string, required) The account to send the funds from, can be "" for the default account
        2. "amounts"                        (string, required) A json object with addresses and amounts
            {
              "address":amount              (numeric) The address is the key, the numeric amount in btc is the value
              ,...
            }
        3. minconf                          (numeric, optional, default=1) Only use the balance confirmed at least this many times.
        4. "comment"                        (string, optional) A comment

        Result:
        "transactionid"                     (string) The transaction id for the send. Only 1 transaction is created regardless of 
                                            the number of addresses.

        Examples:

        Send two amounts to two different addresses:
        > multichain-cli testchain sendmany "tabby" "{\"1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ\":0.01,\"1353tsE8YMTA4EuV7dgUXGjNFf9KpVvKHz\":0.02}"

        Send two amounts to two different addresses setting the confirmation and comment:
        > multichain-cli testchain sendmany "tabby" "{\"1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ\":0.01,\"1353tsE8YMTA4EuV7dgUXGjNFf9KpVvKHz\":0.02}" 6 "testing"

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["tabby", "{\"1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ\":0.01,\"1353tsE8YMTA4EuV7dgUXGjNFf9KpVvKHz\":0.02}", 6, "testing"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def sendrawtransaction(self, *args) -> t.Dict:
        """
        sendrawtransaction "tx-hex" ( allowhighfees )

        Submits raw transaction (serialized, hex-encoded) to local node and network.

        Also see createrawtransaction and signrawtransaction calls.

        Arguments:
        1. "tx-hex"                         (string, required) The hex string of the raw transaction)
        2. allowhighfees                    (boolean, optional, default=false) Allow high fees

        Result:
        "hex"                               (string) The transaction hash in hex

        Examples:

        Create a transaction
        > multichain-cli testchain createrawtransaction "[{\"txid\" : \"mytxid\",\"vout\":0}]" "{\"myaddress\":0.01}"
        Sign the transaction, and get back the hex
        > multichain-cli testchain sendrawtransaction "myhex"

        Send the transaction (signed hex)
        > multichain-cli testchain sendrawtransaction "signedhex"

        As a json rpc call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendrawtransaction", "params": ["signedhex"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def sendwithdata(self, *args) -> t.Dict:
        """
        sendwithdata "address" amount|asset-quantities data|publish-new-stream-item

        Send an amount (or several asset amounts) to a given address with appended metadata. 

        Arguments:
        1. "address"                        (string, required) The address to send to.
        2. amount                           (numeric, required) The amount in native currency to send. eg 0.1
         or
        2. asset-quantities                 (object, required) A json object of assets to send
            {
              "asset-identifier" : asset-quantity
              ,...
            }
        3. data|publish-new-stream-item     (string or object, required) Data, see help data-with for details. 

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain sendwithdata "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "{\"12345-6789-1234\":100,\"1234-5678-1234\":200}" 48656C6C6F20576F726C64210A
        > multichain-cli testchain sendwithdata "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 48656C6C6F20576F726C64210A
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendwithdata", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", 0.1, 48656C6C6F20576F726C64210A] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def sendwithdatafrom(self, *args) -> t.Dict:
        """
        sendwithdatafrom "from-address" "to-address" amount|asset-quantities data|publish-new-stream-item

        Send an amount (or several asset amounts) using specific address.

        Arguments:
        1. "from-address"                   (string, required) Address to send from.
        2. "to-address"                     (string, required) The address to send to.
        3. amount                           (numeric, required) The amount in native currency to send. eg 0.1
         or
        3. asset-quantities                 (object, required) A json object of assets to send
            {
              "asset-identifier" : asset-quantity
              ,...
            }
        4. data|publish-new-stream-item     (string or object, required) Data, see help data-with for details. 

        Result:
        "transactionid"                     (string) The transaction id.

        Examples:
        > multichain-cli testchain sendwithdatafrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "{\"12345-6789-1234\":100,\"1234-5678-1234\":200}" 48656C6C6F20576F726C64210A
        > multichain-cli testchain sendwithdatafrom "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 48656C6C6F20576F726C64210A
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendwithdatafrom", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", 0.1, 48656C6C6F20576F726C64210A] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def setaccount(self, *args) -> t.Dict:
        """
        setaccount "address" "account"

        Sets the account associated with the given address.

        Arguments:
        1. "address"                        (string, required) The address to be associated with an account.
        2. "account"                        (string, required) The account to assign the address to.

        Examples:
        > multichain-cli testchain setaccount "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ" "tabby"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "setaccount", "params": ["1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ", "tabby"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def setgenerate(self, *args) -> t.Dict:
        """
        setgenerate generate ( genproclimit )

        Set 'generate' true or false to turn generation on or off.
        Generation is limited to 'genproclimit' processors, -1 is unlimited.
        See the getgenerate call for the current setting.

        Arguments:
        1. generate                         (boolean, required) Set to true to turn on generation, off to turn off.
        2. genproclimit                     (numeric, optional, default = 1) Set the processor limit for when generation is on. Can be -1 for unlimited.

        Result
        [ blockhashes ]                     (array, -regtest only) hashes of blocks generated

        Examples:

        Set the generation on with a limit of one processor
        > multichain-cli testchain setgenerate true 1

        Check the setting
        > multichain-cli testchain getgenerate 

        Turn off generation
        > multichain-cli testchain setgenerate false

        Using json rpc
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "setgenerate", "params": [true, 1] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def setlastblock(self, *args) -> t.Dict:
        """
        setlastblock ( "hash"|height )

        Sets last block in the chain.
        Local mining and the processing of incoming transactions and blocks should be paused.

        Arguments:
        1. "hash"                           (string, optional) The block hash, if omitted - best chain is activated
         or
        1. height                           (numeric, optional) The block height in active chain or height before current tip (if negative)

        Result:
        "hash"                              (string) The block hash of the chain tip

        Examples:
        > multichain-cli testchain setlastblock "00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "setlastblock", "params": ["00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def setruntimeparam(self, *args) -> t.Dict:
        """
        setruntimeparam "parameter-name" parameter-value 

        Sets value for runtime parameter

        Arguments:
        1. "parameter-name"                 (string, required) Parameter name, one of the following:
                                                               miningrequirespeers,
                                                               mineemptyrounds,
                                                               miningturnover,
                                                               lockadminminerounds,
                                                               maxshowndata, 
                                                               bantx,
                                                               lockblock,
                                                               autosubscribe,
                                                               handshakelocal,
                                                               hideknownopdrops
        2. parameter-value                  (required) parameter value

        Result:

        Examples:
        > multichain-cli testchain setruntimeparam "miningturnover" 0.3
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "setruntimeparam", "params": ["miningturnover", 0.3] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def settxfee(self, *args) -> t.Dict:
        """
        settxfee amount

        Set the transaction fee per kB.

        Arguments:
        1. amount                           (numeric, required) The transaction fee in <native currency>/kB rounded to the nearest 0.00000001

        Result
        true|false                          (boolean) Returns true if successful

        Examples:
        > multichain-cli testchain settxfee 0.00001
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "settxfee", "params": [0.00001] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def signmessage(self, *args) -> t.Dict:
        """
        signmessage "address"|"privkey" "message"

        Sign a message with the private key of an address
        Arguments:
        1. "address"                        (string, required) The address to use for the private key.
         or
        1. "privkey"                        (string, required) The private key (see dumpprivkey and createkeypairs)
        2. "message"                        (string, required) The message to create a signature of.

        Result:
        "signature"                         (string) The signature of the message encoded in base 64

        Examples:

        Unlock the wallet for 30 seconds
        > multichain-cli testchain walletpassphrase "mypassphrase" 30

        Create the signature
        > multichain-cli testchain signmessage "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ" "my message"

        Verify the signature
        > multichain-cli testchain verifymessage "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ" "signature" "my message"

        As json rpc
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "signmessage", "params": ["1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ", "my message"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def signrawtransaction(self, *args) -> t.Dict:
        """
        signrawtransaction "tx-hex" ( [{"txid":"id","vout":n,"scriptPubKey":"hex","redeemScript":"hex"},...] ["privatekey1",...] sighashtype )

        Sign inputs for raw transaction (serialized, hex-encoded).
        The second optional argument (may be null) is an array of previous transaction outputs that
        this transaction depends on but may not yet be in the block chain.
        The third optional argument (may be null) is an array of base58-encoded private
        keys that, if given, will be the only keys used to sign the transaction.

        Arguments:
        1. "tx-hex"                         (string, required) The transaction hex string
        2. prevtxs                          (array, optional) An json array of previous dependent transaction outputs
             [                              (json array of json objects, or 'null' if none provided)
               {
                 "txid":"id",               (string, required) The transaction id
                 "vout":n,                  (numeric, required) The output number
                 "scriptPubKey": "hex",     (string, required) script key
                 "redeemScript": "hex"      (string, required for P2SH) redeem script
               }
               ,...
            ]
        3.privatekeys                       (array, optional) A json array of base58-encoded private keys for signing
            [                               (json array of strings, or 'null' if none provided)
              "privatekey"                  (string) private key in base58-encoding
              ,...
            ]
        4. "sighashtype"                    (string, optional, default=ALL) The signature hash type. Must be one of
               "ALL"
               "NONE"
               "SINGLE"
               "ALL|ANYONECANPAY"
               "NONE|ANYONECANPAY"
               "SINGLE|ANYONECANPAY"

        Result:
        {
          "hex": "value",                   (string) The raw transaction with signature(s) (hex-encoded string)
          "complete": true|false            (boolean) if transaction has a complete set of signature (0 if not)
        }

        Examples:
        > multichain-cli testchain signrawtransaction "myhex"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "signrawtransaction", "params": ["myhex"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def stop(self) -> t.Dict:
        """
        stop

        Shuts down the this blockchain node. Sends stop signal to MultiChain server.
        """

    def submitblock(self, *args) -> t.Dict:
        """
        submitblock hexdata ( "jsonparametersobject" )

        Attempts to submit new block to network.
        The 'jsonparametersobject' parameter is currently ignored.
        See https://en.bitcoin.it/wiki/BIP_0022 for full specification.

        Arguments
        1. hexdata                          (string, required) the hex-encoded block data to submit
        2. "jsonparametersobject"           (string, optional) object of optional parameters
            {
              "workid" : "id"               (string, optional) if the server provided a workid, it MUST be included with submissions
            }

        Result:

        Examples:
        > multichain-cli testchain submitblock "mydata"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "submitblock", "params": ["mydata"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def subscribe(self, *args) -> t.Dict:
        """
        subscribe entity-identifier(s) ( rescan )

        Subscribes to the stream.

        Arguments:
        1. "stream-identifier"              (string, required) Stream identifier - one of the following: stream txid, stream reference, stream name.
         or
        1. "asset-identifier"               (string, required) Asset identifier - one of the following: asset txid, asset reference, asset name.
         or
        1. entity-identifier(s)             (array, optional) A json array of stream or asset identifiers 
        2. rescan                           (boolean, optional, default=true) Rescan the wallet for transactions

        Note: This call can take minutes to complete if rescan is true.

        Result:

        Examples:

        Subscribe to the stream with rescan
        > multichain-cli testchain subscribe "test-stream"

        Subscribe to the stream without rescan
        > multichain-cli testchain subscribe "test-stream" false

        As a JSON-RPC call
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "subscribe", "params": ["test-stream", false] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def unsubscribe(self, *args) -> t.Dict:
        """
        unsubscribe entity-identifier(s)

        Unsubscribes from the stream.

        Arguments:
        1. "stream-identifier"              (string, required) Stream identifier - one of the following: stream txid, stream reference, stream name.
         or
        1. "asset-identifier"               (string, required) Asset identifier - one of the following: asset txid, asset reference, asset name.
         or
        1. entity-identifier(s)             (array, optional) A json array of stream or asset identifiers 

        Result:

        Examples:
        > multichain-cli testchain unsubscribe "test-stream"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "unsubscribe", "params": ["test-stream", false] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def validateaddress(self, *args) -> t.Dict:
        """
        validateaddress "address"|"pubkey"|"privkey"

        Return information about the given address or public key or private key.

        Arguments:
        1. "address"                        (string, required) The address to validate
          or 
        1. "pubkey"                         (string, required) The public key (hexadecimal) to validate
          or 
        1. "privkey"                        (string, required) The private key (see dumpprivkey) to validate

        Result:
        {
          "isvalid" : true|false,           (boolean) If the address is valid or not. If not, this is the only property returned.
          "address" : "address",            (string) The address validated
          "ismine" : true|false,            (boolean) If the address is yours or not
          "isscript" : true|false,          (boolean) If the key is a script
          "pubkey" : "publickeyhex",        (string) The hex value of the raw public key
          "iscompressed" : true|false,      (boolean) If the address is compressed
          "account" : "account"             (string) The account associated with the address, "" is the default account
        }

        Examples:
        > multichain-cli testchain validateaddress "1PSSGeFHDnKNxiEyFrD1wcEaHr9hrQDDWc"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "validateaddress", "params": ["1PSSGeFHDnKNxiEyFrD1wcEaHr9hrQDDWc"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def verifychain(self, *args) -> t.Dict:
        """
        verifychain ( checklevel numblocks )

        Verifies blockchain database.

        Arguments:
        1. checklevel                       (numeric, optional, 0-4, default=3) How thorough the block verification is.
        2. numblocks                        (numeric, optional, default=288, 0=all) The number of blocks to check.

        Result:
        true|false                          (boolean) Verified or not

        Examples:
        > multichain-cli testchain verifychain 
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "verifychain", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """

    def verifymessage(self, *args) -> t.Dict:
        """
        verifymessage "address" "signature" "message"

        Verify a signed message

        Arguments:
        1. "address"                        (string, required) The address to use for the signature.
        2. "signature"                      (string, required) The signature provided by the signer in base 64 encoding (see signmessage).
        3. "message"                        (string, required) The message that was signed.

        Result:
        true|false                          (boolean) If the signature is verified or not.

        Examples:

        Unlock the wallet for 30 seconds
        > multichain-cli testchain walletpassphrase "mypassphrase" 30

        Create the signature
        > multichain-cli testchain signmessage "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ" "my message"

        Verify the signature
        > multichain-cli testchain verifymessage "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ" "signature" "my message"

        As json rpc
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "verifymessage", "params": ["1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XZ", "signature", "my message"] }' -H 'content-type: text/plain;' http://127.0.0.1:6667

        """



