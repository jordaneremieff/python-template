import pytest

from {{ cookiecutter.package_name }} import hello


@pytest.mark.parametrize("wrong", [2, 3, 4, 5])
def test_hello(wrong):
    assert hello() != wrong
