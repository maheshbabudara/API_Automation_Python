import os
import json
import pytest
from datetime import datetime

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir='Reports'
    now=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f'{report_dir}/report_{now}.html'

@pytest.fixture(autouse=True,scope='session')
def setup_teardown():
    print("BEFORE SETTING UP")
    yield
    print("AFTER SETTING UP")

@pytest.fixture
def loaduser_data():
    file_path=os.path.join(os.path.dirname(__file__),'Data','test_data.json')
    with open(file_path) as file:
        data=json.load(file)
        return data

