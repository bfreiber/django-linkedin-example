from django.shortcuts import render, redirect
from linkedin import linkedin
import oauth2 as oauth
import urlparse
import urllib2
import json

########## PAGES ##########

def home(request):
    return render(request, 'landing.html')

########## FUNCTIONS ##########

CONSUMER_KEY = '****************'
CONSUMER_SECRET = '**************'
CONSUMER = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
CLIENT = oauth.Client(CONSUMER)
USER_TOKEN = '**********************'
USER_SECRET = '***************************'
RETURN_URL = 'http://localhost:8000'
PREDEFINED_STATE = 'DCEEFWF45453sdffef424' #NEEDS TO BE UPDATED
REDIRECT_URI_FINAL = 'http://0.0.0.0:5000/resultsontheway'

def linkedintest2(request):
	API_KEY = CONSUMER_KEY
	SCOPE = 'r_fullprofile%20r_emailaddress%20r_network'
	STATE = PREDEFINED_STATE
	REDIRECT_URI = REDIRECT_URI_FINAL
	redirect_url = "https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id=%s&state=%s&redirect_uri=%s" % (API_KEY, STATE, REDIRECT_URI)
	return redirect(redirect_url)

def resultsontheway(request):
	current_url = request.get_full_path()
	authorization_code_position = current_url.find('code=')
	state_position = current_url.find('&state=')
	authorization_code = current_url[authorization_code_position+5:state_position]
	state = current_url[state_position+7:]
	if state == PREDEFINED_STATE:
		AUTH_CODE = authorization_code
		REDIRECT_URI = REDIRECT_URI_FINAL
		API_KEY = CONSUMER_KEY
		SECRET_KEY = CONSUMER_SECRET
		post_url = "https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code&code=%s&redirect_uri=%s&client_id=%s&client_secret=%s" % (AUTH_CODE, REDIRECT_URI, API_KEY, SECRET_KEY)
		data = {} #Empty dictionary so urllib2.Request performs a POST rather than GET request
		req = urllib2.Request(post_url, data)
		response = urllib2.urlopen(req)
		the_page = response.read()
		json_response_object = json.loads(the_page)
		access_token = json_response_object['access_token']
		ready_access_token = 'oauth2_access_token='+access_token

		#get_url = "https://api.linkedin.com/v1/people/~?%s" % ready_access_token

		########## DOES NOT WORK - ERROR:401 UNAUTHORIZED ##########
		get_url = "https://api.linkedin.com/v1/people/~/connections?%s" % ready_access_token
		req = urllib2.Request(get_url)
		response = urllib2.urlopen(req)
		the_page = response.read()
		return render(request, 'results.html',
			{'current_url': current_url,
			'authorization_code': authorization_code,
			'state': state,
			'the_page': the_page,
			'access_token': access_token})
	else:
		return render(request, 'results.html')
