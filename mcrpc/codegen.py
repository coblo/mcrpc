# -*- coding: utf-8 -*-
import os
from string import Template
from textwrap import indent
import yaml
from mcrpc.client import RpcClient

HERE = os.path.dirname(__file__)


def get_stub_template():
    filepath = os.path.join(HERE, 'client.tpl')
    with open(filepath) as f:
        return Template(f.read())


def get_method_template():
    return Template(
        '    def $method(self$sig) -> $rtype:\n'
        '        """\n'
        '$help\n'
        '        """\n\n'
    )


def get_signature_meta():
    filepath = os.path.join(HERE, 'client.yml')
    with open(filepath) as f:
        meta = yaml.load(f)
    return meta


def get_api_methods(client):
    text = client.help()
    methods = []
    for line in text.splitlines():
        if not line or line.startswith('='):
            continue
        else:
            meth_name = line.split()[0]
            meth_sig = ' '.join(line.split()[1:])
            methods.append((meth_name, meth_sig))
    return methods


def build_stubs(client):
    methods = ""
    method_tpl = get_method_template()
    meta = get_signature_meta()
    for method, help_sig in sorted(get_api_methods(client)):
        help_ = client._call('help', method)
        sig = meta.get(method, [None])[0]
        if not sig and not help_sig:
            sig = ''
        elif not sig:
            sig = ', *args'
        else:
            sig = ', ' + sig
        rtype = meta.get(method, [None, None])[1] or 't.Dict'
        methods += method_tpl.substitute(
            method=method,
            sig=sig,
            rtype=rtype,
            help=indent(help_, 8 * ' '))
    stub = get_stub_template().substitute(methods=methods)
    out_path = os.path.join(HERE, 'client.pyi')
    with open(out_path, 'w') as outf:
        outf.write(stub)


def generate_code():
    client = RpcClient('127.0.0.1', '7010', 'testuser', 'testpassword', False)
    build_stubs(client)


if __name__ == '__main__':
    generate_code()

