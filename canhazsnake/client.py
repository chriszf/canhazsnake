import requests

class Client(object):
    BASE_URL = "https://api.cheezburger.com/v1/"
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.token = None
        pass

    def ohai(self):
        pass

    def _basic_request(self, endpoint, **kwargs):
        payload = {"access_token": self.token}
        payload.update(kwargs)
        return requests.get(self.BASE_URL + endpoint, params=payload).json

    def get_auth_url(self, redirect_uri = "https://api.cheezburger.com/oauth/login_success"):
        return "https://api.cheezburger.com/oauth/authorize?client_id=%s&response_type=code&redirect_uri=%s"%(self.api_key, redirect_uri)


    def get_token(self, code="code", redirect_uri = "https://api.cheezburger.com/oauth/login_success"):
        payload = {"client_id": self.api_key,
                  "client_secret": self.api_secret,
                  "redirect_uri": redirect_uri,
                  "grant_type": "authorization_code",
                  "code": code}
        target_url = "https://api.cheezburger.com/oauth/access_token"
        results = requests.post(target_url, data=payload).json
        self.token = results['access_token']
        return results

    def ohai(self, message):
        return self._basic_request("ohai", message=message)

    def me(self):
        return self._basic_request("me")
        
    def site(self, site_id):
        return self._basic_request("sites/%d"%site_id)

    def site_types(self):
        return self._basic_request("sitetypes")

    def my_sites(self):
        return self._basic_request("my/sites")

    def user(self, user_id):
        return self._basic_request("users/%s"%user_id)

    def asset(self, asset_id):
        return self._basic_request("assets/%d"%asset_id)

    def asset_types(self):
        return self._basic_request("assettypes")
