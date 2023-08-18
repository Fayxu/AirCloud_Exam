import os
import time

import pytest
from unit.read_yaml import YamlUtil

if __name__ == '__main__':
    pytest.main(['-vs'])
    time.sleep(3)
    os.system('allure generate ./temps -o ./reports --clean')
    # YamlUtil('./extract.yaml').write_yaml({"sex": "male",
    #                                                     "name": "jack",
    #                                                     "age": 20
    #                                                     })