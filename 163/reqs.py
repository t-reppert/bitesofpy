def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    from pkg_resources import parse_version
    upgraded = []
    for old, new in zip(old_reqs.split(), new_reqs.split()):
        if old != new:
            old_name, old_version = old.split('==')
            new_name, new_version = new.split('==')
            if parse_version(old_version) < parse_version(new_version):
                upgraded.append(new_name)
    return upgraded