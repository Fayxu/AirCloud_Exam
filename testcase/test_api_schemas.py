import pytest
import requests
from unit.requests_util import RequestsUtil
from unit.read_yaml import YamlUtil
from unit.get_all_files_path import get_all_files


case_files1 = get_all_files('E:\Mycode\Selflearn_Framework\AirCloud_Exam\data')[1]


class TestSchemas01:

    @pytest.mark.parametrize("caseinfo", YamlUtil(case_files1).read_case_yaml())
    def test_get_schrmas(self, caseinfo):
        """
        2001 Schemas_API
        :return:
        """
        # read variables through yaml
        token = YamlUtil('./extract.yaml').read_yaml().get("token")
        caseinfo['requests']['headers']['Authorization'] = "Bearer {}".format(token)

        # read testcase through yaml
        method = caseinfo['requests']['method']
        url = caseinfo['requests']['host'] + caseinfo['requests']['url']
        data = caseinfo['requests']['data']
        headers = caseinfo['requests']['headers']

        # send post_method
        get_Schemas = RequestsUtil().all_requests(method=method, url=url, json=data, headers=headers)

        # get response
        result = get_Schemas.json()
        print(result)
        # return result


