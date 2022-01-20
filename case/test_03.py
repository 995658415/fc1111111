import pytest
# from 第一层 import Grouping

from loguru import logger

from api.grouping02 import Grouping


class TestGrouping:
    def setup_class(self):
        self.group = Grouping()

    # @pytest.mark.smoke
    # @pytest.mark.parametrize('a,check', [(1, 200), (2, 200)], ids=('ONE', 'TWO'))
    # @pytest.mark.smoke
    # @pytest.mark.parametrize('check', (200), ids='TWO')
    @pytest.mark.parametrize('check', [200], ids=['通过'])
    def test_tjfz1(self, check):
        a = self.group.tjfz()
        assert a.status_code == check  # 断言
        logger.info(a.json()) # 日志


    def test_tjgs1(self):
        a = self.group.tjgs()
        assert a.status_code == 200
        logger.info(a.json())
    def test_scfz(self):
        a = self.group.scfz()
        assert a.status_code == 300
        # assert r.status_code == check
        logger.info(a.json())

# def test01(self):
#     def setup_class(self):
# self.group = Grouping()

# def test_tjfz1(self):


# a=TestGrouping
# a.test_01()
