from io import BytesIO

from darbia.labels import code128_only


def test_creates_bytes() -> None:
    assert isinstance(code128_only(["tests"]), BytesIO)
