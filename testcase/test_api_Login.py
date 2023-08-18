import pytest
from unit.requests_util import RequestsUtil
from unit.read_yaml import YamlUtil
from unit.get_all_files_path import get_all_files


case_files0 = get_all_files('E:\Mycode\Selflearn_Framework\AirCloud_Exam\data')[0]


class TestUserRegister01:

    @pytest.mark.parametrize("caseinfo", YamlUtil(case_files0).read_case_yaml())
    def test_getlist(self, caseinfo):
        """
        1001 login_API

        :param getlist_url:
        :return:
        """
        # print(caseinfo)

        # reading yaml testcase
        method = caseinfo['requests']['method']
        url = caseinfo['requests']['host'] + caseinfo['requests']['url']
        # data = caseinfo['requests']['data']
        headers = caseinfo['requests']['headers']

        # send post_method
        login_res = RequestsUtil().all_requests(method=method, url=url, headers=headers)
        # get response results
        result = login_res.json()
        # print(result)

        # write variables through yaml
        YamlUtil('./extract.yaml').write_yaml({"token": result['token']})

        # Assert status_code；
        if login_res.status_code == 200:
            print('API status_code is 200, Success！')
        else:
            print(f'Status_code error: {login_res.status_code}, Failed！')



