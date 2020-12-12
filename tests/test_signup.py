import pytest

from authentication import signup

def test_function_exists():
        assert signup() == 1
