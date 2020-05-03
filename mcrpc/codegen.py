# -*- coding: utf-8 -*-
import os
from string import Template
from textwrap import indent
from mcrpc.exceptions import RpcError
from mcrpc.client import RpcClient


HERE = os.path.dirname(__file__)

IGNORE = ["purgefeed"]


resp_tpl = """
class {classname}:
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        {setters}

    def as_dict(self):
        return self._kwargs

    def __repr__(self):
        return repr(self._kwargs)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._kwargs == other._kwargs
        else:
            return False\n
"""


def get_stub_template():
    filepath = os.path.join(HERE, "client.tpl")
    with open(filepath, "rt", encoding="utf-8") as f:
        return Template(f.read())


def get_api_methods(client):
    text = client.help()
    methods = []
    for line in text.splitlines():
        if not line or line.startswith("="):
            continue
        else:
            meth_name = line.split()[0]
            meth_sig = " ".join(line.split()[1:])
            methods.append((meth_name, meth_sig))
    return methods


def build_response_class(method, resp):
    result = ""
    if not isinstance(resp, dict):
        return result

    setters = []
    for field in sorted(resp.keys()):
        setter = 'self.{} = kwargs["{}"]'.format(field, field)
        setters.append(setter)
    setters = "\n        ".join(setters)
    return resp_tpl.format(classname=method.title(), setters=setters)


def build_code(client):
    """Build a best effort base class"""

    base_head = (
        "# -*- coding: utf-8 -*-\n"
        "# WARNING: Autogenerated code. Do not edit manually.\n"
        "from mcrpc.responses import *\n\n\n"
        "class BaseApiMethods:\n\n"
    )
    base_tpl = Template(
        "    def $method(self$sig):\n" '        return self._call("$method"$call)\n\n'
    )
    base_tpl_obj = Template(
        "    def $method(self$sig):\n"
        '        data = self._call("$method"$call)\n'
        "        return $resp_class(**data)\n\n"
    )
    base_out = base_head

    stub_tpl = Template(
        "    def $method(self$sig)$rtype:\n" '        """\n' "$help\n" '        """\n\n'
    )
    stub_out = ""

    resp_out = (
        "# -*- coding: utf-8 -*-\n"
        "# WARNING: Autogenerated code. Do not edit manually.\n\n"
    )

    for method, sig in get_api_methods(client):
        if method in IGNORE:
            continue
        help_ = indent(client._call("help", method), 8 * " ")
        if not sig:
            # We can reliably build methods, stubs and response types/objects
            rtype = ""
            is_obj_resp = False
            if method != "stop":
                try:
                    resp = client._call(method)
                    if isinstance(resp, dict):
                        resp_out += build_response_class(method, resp)
                        rtype = " -> " + method.title()
                        is_obj_resp = True
                    else:
                        rtype = resp.__class__.__name__
                        rtype = " -> " + rtype if rtype != "NoneType" else " -> None"
                except RpcError:
                    pass
            stub_out += stub_tpl.substitute(
                method=method, sig="", rtype=rtype, help=help_
            )
            if is_obj_resp:
                base_out += base_tpl_obj.substitute(
                    method=method, sig="", call="", resp_class=method.title()
                )
            else:
                base_out += base_tpl.substitute(method=method, sig="", call="")
        else:

            sig_clean = (
                sig.replace("from ", "from_")
                .replace("hex ", "hex_")
                .replace("open ", "open_")
                .replace("globals ", "globals_")
                .replace("( ", "(")
                .replace(" )", ")")
                .replace('"', "")
                .replace("|", "_or_")
                .replace("-", "_")
                .replace("(s)", "s")
                .replace("(es)", "es")
            )

            is_clean = not any(c in sig_clean for c in "{")

            if is_clean:
                # we can build base class and stub signatures
                args_kwargs = sig_clean.split("(")
                args = args_kwargs[0].split()
                kwargs = (
                    args_kwargs[1].strip(")").split() if len(args_kwargs) > 1 else []
                )

                # special case new 'options' kwarg that is not in brackets
                if args and args[-1] == "options":
                    args = args[:-1]
                    kwargs.append("options")

                call = ", ".join(args + kwargs)
                sig_kwargs = ["{}=None".format(kw) for kw in kwargs]
                sig = ", ".join(args + sig_kwargs)

                base_out += base_tpl.substitute(
                    method=method, sig=", " + sig, call=", " + call
                )
                stub_out += stub_tpl.substitute(
                    method=method, sig=", " + sig, rtype="", help=help_
                )
                print(method, "->", sig_clean, "->", args, "->", kwargs)
            else:
                # we can build basic help stubs
                stub_out += stub_tpl.substitute(
                    method=method, sig=", *args", rtype="", help=help_
                )

    base_out_path = os.path.join(HERE, "base.py")
    base_out = base_out.strip() + "\n"
    with open(base_out_path, "wt", encoding="utf-8") as outf:
        outf.write(base_out)

    stub_out_path = os.path.join(HERE, "client.pyi")
    stub_out = get_stub_template().substitute(methods=stub_out)
    stub_out = stub_out.strip() + "\n"
    with open(stub_out_path, "wt", encoding="utf-8") as outf:
        outf.write(stub_out)

    resp_out_path = os.path.join(HERE, "responses.py")
    resp_out = resp_out.strip() + "\n"
    with open(resp_out_path, "wt", encoding="utf-8") as outf:
        outf.write(resp_out)


def generate_code():
    client = RpcClient("127.0.0.1", "9000", "testuser", "testpassword", False)
    build_code(client)


if __name__ == "__main__":
    generate_code()
