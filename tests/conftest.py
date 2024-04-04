import pytest
import pymssql


@pytest.fixture(scope='module')
def cnxn():
    """Pytest fixture to establish connection to DB"""
    cnxn = pymssql.connect(
        host='192.168.1.7',
        user='MyLogin',
        password='Fv064564@',
        database='TRN',
        port=1433)

    yield cnxn


@pytest.fixture
def cursor(cnxn):
    """Pytest fixture for creating cursor"""
    cursor = cnxn.cursor()
    yield cursor
    cnxn.rollback()
