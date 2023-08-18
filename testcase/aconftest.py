import pytest
from unit.read_yaml import YamlUtil


# 清除装饰器，使用前置：在使用变量之前先清除 extract.yaml 文件内容
@pytest.fixture(scope='session', autouse=True)
def clear_token():
    YamlUtil('./extract.yaml').clear_yaml()
