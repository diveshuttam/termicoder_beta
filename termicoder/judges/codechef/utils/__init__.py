import requests
import click
from requests_oauthlib import OAuth2


def login_client():
    home_page = 'http://termicoder.diveshuttam.me/'
    click.echo(
        "Browser window will launch, authorize termicoder with CodeChef.\n"
        "After authenticating, copy-paste the code returned by the page.")
    click.confirm("Continue?", default=True, abort=True)
    click.launch(home_page)

    # access_token
    access_token = input('code :')
    test_api_url = "https://api.codechef.com/contests/PRACTICE/problems/SALARY"
    api_call_headers = {'Authorization': 'Bearer ' + access_token}
    api_call_response = requests.get(test_api_url, headers=api_call_headers)

    print(api_call_response.text)

    # TODO do everything with oauth2
    OAuth2()


__all__ = ['login_client']
