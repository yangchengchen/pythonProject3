import pytest
class Test_s:
    def setup_class(self):
        print('用例类开始')

    def teardown_class(self):
        print('用例类结束')

    @pytest.fixture()
    def mysetup(self):
        print('开始')
        yield
        print('结束')

    def test_01(self):
        print('01')

    def test_02(self,mysetup):
        print('02')

