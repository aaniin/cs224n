import pytest
from utils import Batch

def test_Batch():

    b1 = Batch(None, None, 1500)
    b2 = Batch(None, None, 5)
    b3 = Batch(None, None, 123)

    batch_list = [b1, b2, b3]
    s = sorted(batch_list)
    assert s[0].batch_loss == 5
    assert s[1].batch_loss == 123
    assert s[2].batch_loss == 1500
