from collections import defaultdict, OrderedDict
from typing import List, Dict

import ast
import builtins


class AstVisitor(ast.NodeVisitor):
    def __init__(self, code: str = None) -> None:
        """Initialize the object

        attrs:
        -----
        - code: source code provided as text (if not None, trigger its parsing)
        """
        super().__init__()
        self.all_builtins = set(dir(builtins))
        self.imports = set()
        self.aliases = {}
        self.calls = defaultdict(list)
        self.subimports = {}
        self.parse(code)


    def parse(self, code: str) -> ast.Module:
        """Parse input code into an AST tree"""
        tree = ast.parse(code)
        self.visit(tree)
        return tree

    def visit_Import(self, node: ast.AST) -> None:
        """Parse an ast.Import node"""
        names = [x.name for x in node.names]
        aliases = [x.asname for x in node.names]
        for x,y in zip(names, aliases):
            self.imports.add(x)
            self.aliases[y] = x
        # do not remove this
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.AST) -> None:
        """Parse an ast.ImportFrom node"""
        self.imports.add(node.module)
        names = [x.name for x in node.names]
        aliases = [x.asname for x in node.names]
        if aliases != [None]:
            for x,y in zip(names, aliases):
                self.subimports[x] = node.module
                self.aliases[y] = x
        else:
            for x in names:
                self.subimports[x] = node.module
        # do not remove this
        self.generic_visit(node)

    def visit_Call(self, node: ast.AST) -> None:
        """Parse an ast.Call node"""
        if isinstance(node.func, ast.Name):
            call_name = node.func.id
            if call_name in self.subimports:
                call_name = self.subimports[call_name] + "." + call_name
        elif isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name):
                id = node.func.value.id
                attr = node.func.attr
                if id in self.aliases:
                    id = self.aliases[id]
                call_name = id+"."+attr
            elif isinstance(node.func.value, ast.Attribute):
                id = node.func.value.value.id
                attr1 = node.func.value.attr
                attr2 = node.func.attr
                if id in self.aliases:
                    id = self.aliases[id]
                call_name = id+"."+attr1+"."+attr2
        call_lineno = node.lineno
        if '.' in call_name:
            if call_name.split('.')[0] in self.imports:
                self.calls[call_name].append(call_lineno)
        else:
            self.calls[call_name].append(call_lineno)
        # do not remove this
        self.generic_visit(node)

    def builtins(self, valid: List[str] = None) -> List[str]:
        """Return the list of tracked builtins functions

        Attrs:
        ------
        - valid: optional list of builtins to search for
        """
        bins = []
        if valid:
            for v in valid:
                if v in self.all_builtins:
                    for item in self.calls.keys():
                        if item == v:
                            bins.append(item)
        else:
            for item in self.calls.keys():
                if item in self.all_builtins:
                    bins.append(item)
        return bins

    def builtins_lineno(self, valid: List[str] = None) -> Dict[str, List[int]]:
        """Return a dictionary mapping builtins to line numbers

        Attrs:
        ------
        - valid: optional list of builtins to search for
        """
        bins_lineno = OrderedDict()
        if valid:
            for v in valid:
                if v in self.all_builtins:
                    for item, value in self.calls.items():
                        if item == v:
                            bins_lineno[item] = value
        else:
            for item, value in self.calls.items():
                if item in self.all_builtins:
                    bins_lineno[item] = value
        return dict(bins_lineno)
        

    def modules(self, valid: List[str] = None) -> List[str]:
        """Return a dictionary mapping module calls to line numbers, with:
        - name aliases resolves
        - names in full dotted notation

        Attrs:
        ------
        - valid: optional list of builtins to search for
        """
        return_list = []
        if valid:
            for v in valid:
                if v in self.imports:
                    return_list.append(v)
                elif v in self.aliases:
                    return_list.append(self.aliases[v])
            return sorted(return_list)
        else:
            return sorted(list(self.imports))

    def modules_lineno(self, valid: List[str] = None) -> List[str]:
        """Return a dictionary mapping modules calls to line numbers (with aliasing resolved, and names in full dotted notation)

        attrs:
        ------
        - valid: optional list of builtins to search for
        """
        bins_lineno = OrderedDict()
        if valid:
            for v in valid:
                if v not in self.all_builtins:
                    if v in self.aliases:
                        v = self.aliases[v]
                    for item, value in self.calls.items():
                        if "." in item:
                            if item.split('.')[0] == v:
                                bins_lineno[item] = value
        else:
            for item, value in self.calls.items():
                if item not in self.all_builtins:
                    if "." in item:
                        bins_lineno[item] = value
        return dict(bins_lineno)

    def report(self, valid_builtins: List[str] = None, valid_modules: List[str] = None):
        """Print on stdout builtins and modules tracking info"""
        print(f"builtins: {self.builtins(valid_builtins)}")
        print(f"modules: {self.modules(valid_modules)}")
        print(f"builtins_lineno: {self.builtins_lineno(valid_builtins)}")
        print(f"modules_lineno: {self.modules_lineno(valid_modules)}")

# a reference example
if __name__ == "__main__":
    code = """
import pandas as pd
import numpy as np
from argparse import ArgumentParser

print("this is a test")

parser = ArgumentParser()
len("12345")

df_tmp = pd.DataFrame(range(10), column=['x'])
df_tmp.loc[:, 'y'] = df_tmp[x] + 1

np.random.random()
"""

    vst = AstVisitor(code)
    vst.report()