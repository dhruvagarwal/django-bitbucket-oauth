from requests_oauthlib import OAuth2Session
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


client_id = '6VvbvhmWmRrJf6G6Vk'
client_secret = 'qPCCXekhz7ZQ4EyrGdjtPVYC5B9Smm45'
authorization_base_url = 'https://bitbucket.org/site/oauth2/authorize'
token_url = 'https://bitbucket.org/site/oauth2/access_token'


def login(request):
    bitbucket = OAuth2Session(client_id)
    authorization_url, state = bitbucket.authorization_url(authorization_base_url)

    request.session['oauth_state'] = state
    print dict(request.session)

    return HttpResponseRedirect(redirect_to=authorization_url)


def callback(request):
    bitbucket = OAuth2Session(client_id=client_id, state=request.session['oauth_state'])
    token = bitbucket.fetch_token(token_url, client_secret=client_secret,
                                    authorization_response=request.get_full_path())

    return HttpResponse('{token}'.format(token=token))
