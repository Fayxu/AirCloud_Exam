import pytest
import requests


class TestLogin:

    def test_login_01(self):

        url = 'https://api-staging.airwallex.com/api/v1/authentication/login'
        headers = {
            "x-client-id": "kw5x9DYqRtGuBkNYrLCfQw",
            "x-api-key": "22c85b1d3a7f74dfce22bc46e075a3bd2a164e082184de00865fb96375590a41ce2619fa07e82bf52c21c882f9a81532"
        }

        data = {"bank_country_code": "HK",
                "account_currency": "HKD",
                "entity_type": "PERSONAL",
                "payment_method": "LOCAL"
                }

        login_res = requests.post(url=url, data=data, headers=headers)
        result = login_res.json()

        # assert login_res.status_code == 200

        if login_res.status_code == 200:
            print('API status_code is 200, Success！')
        else:
            print(f'Status_code error: {login_res.status_code}, Failed！')

        print(result)


if __name__ == '__main__':
    pytest.main()





