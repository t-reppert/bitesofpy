from cisco_nxapi import nxapi_show_version


def test_return_function():
    assert nxapi_show_version() == "9.2(1)"