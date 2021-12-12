import inspect


def get_classes(mod):
    """Return a list of all classes in module 'mod'"""
    return [ a[0] for a in inspect.getmembers(mod, inspect.isclass) if a[0][0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' ]