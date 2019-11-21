import requests

# This function take a string as a parameter.
# It must test:
# 1. The string must end with one of the following four top level
# domains: .com, .net, .edu, .gov. This means checking the last three
# characters. If this test fails, the function should return None
# If the url is okay, then this function should return a string of the URL.


def is_domain(name):
    print ("Inside is_domain")
    domains = ["com", "net", "edu", "gov"]
    last_three = name[-3:]
    if last_three in domains:
        return name
    else:
        return None


# This function takes a url as a
# string as a parameter.
# First, use the URL verification function above to verify, fix, or fail
# the URL. If that function returns None, this function should return None.
# Second, once the URL is checked and fixed as needed the function will
# use the requests library to make a GET request to that url and store
# the status code to a variable called sc. Return the status code.
# NOTE: there are other libraries that could be used, but you must
# use the requests library for this to be correct.


def basic_request(a_url):
    print ("Inside basic_request")
    sc = ""
    results = is_domain(a_url)
    print (results)
    if results == "none":
        return None
    else:
        sc = requests.get(a_url)
        print (sc)
        print (sc.status_code)
        return sc.status_code


# This function takes two parameters.
# The first parameter will be a URL. Again, check it with the first
# function you created.
# The second parameter will be a string that is the user agent. User
# agent is a code that gets sent with a request that identifies the
# program making the request. If this parameter is not a string, return
# None.
# Your function must then make a request to the URL parameter using
# the user agent. You'll need to read the documentation for requests
# if you want to do this part.
# You should return the text of the response. It is a secret code
# that is on a live server and is needed to pass the unittest.

def request_user_agent(a_url, agent):
    print("inside request_user_agent")
    results = is_domain(a_url)
    if results:
        if isinstance(agent, str):
            headers = {
                'user-agent': agent,
            }
            response = requests.get(a_url, headers=headers)
            print(response)
            return response
        else:
            return None
    else:
        return None

# This function takes a url and
# a dictionary as parameters.
# Again use your verification function to check the URL
# If the URL is not good, return None.
# You'll also need to check the data coming in as the second
# parameter. We won't do anything more than verify that it is not
# empty. So if the data is empty or None or not a dictionary, then
# your function should return None.
# If the parameters check out, then your function should send a post
# request to the URL.
# When you make this call, correctly, the server will send back a
# code as the text property of the response (as in the
# request_user_agent() function above).
# Your function will return the code.



def request_post(a_url, a_dict):
    print("inside request_post")
    results = is_domain(a_url)
    if results:
        if isinstance(a_dict, dict) and a_dict != {}:
            results = requests.post(a_url)
            print (results)
            return results
    else:
        return None


