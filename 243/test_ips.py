import os
from pathlib import Path
from ipaddress import AddressValueError, IPv4Network
from urllib.request import urlretrieve
from contextlib import contextmanager

import pytest

from ips import (ServiceIPRange, parse_ipv4_service_ranges,
                 get_aws_service_range)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network('192.0.2.8/29')


@pytest.fixture(scope='module')
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


def test_parse_ipv4_service_ranges(json_file):
    ipv4_service_ranges = parse_ipv4_service_ranges(json_file)
    for r in ipv4_service_ranges:
        assert isinstance(r, ServiceIPRange)
        assert str(r) == f"{r.cidr} is allocated to the {r.service} " \
                f"service in the {r.region} region"
        assert isinstance(r.cidr, IPv4Network)


@contextmanager
def does_not_raise():
    yield


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("192.168.1.1", does_not_raise()),
        ("10.0.0.127", does_not_raise()),
        ("127.0.0.1", does_not_raise()),
        ("80.0.296.1", pytest.raises(ValueError)),
        ("80.0.29.347", pytest.raises(ValueError)),
        ("888.0.0.1", pytest.raises(ValueError)),
        ("10.259.9.1", pytest.raises(ValueError))
    ]
)
def test_bad_get_aws_service_range(test_input, expected, json_file):
    service_ranges = parse_ipv4_service_ranges(json_file)
    with expected:
        get_aws_service_range(address=test_input, service_ranges=service_ranges)


def test_dataclass_service_ip_range():
    s1 = ServiceIPRange("TEST", "test-region-1", IPv4Network("127.0.0.1"))
    assert s1.service == "TEST"
    assert s1.region == "test-region-1"
    assert s1.cidr == IPv4Network("127.0.0.1")
    