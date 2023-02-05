# -*- cording：utf-8 -*-
# @function：canshuhuashili
import pytest
def sum(x,y):
    return x+y
params=[
        [1,1,2],
        [1,2,3],
    ]

class Test_Data:
    @pytest.mark.parametrize('x,y,z',params)
    def test_sum(self,x,y,z):
        assert sum(x,y)==z
