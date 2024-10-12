# Uncomment the imports below before you add the function code
# import requests
import os
from dotenv import load_dotenv
import requests
load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# def get_request(endpoint, **kwargs):
# Add code for get requests to back end
def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print(f"Network exception occurred 3: {e}")

# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments
# def analyze_review_sentiments(text):
#     request_url = sentiment_analyzer_url+"analyze/"+text
#     try:
#         # Call get method of requests library with URL and parameters
#         response = requests.get(request_url)
#         return response.json()
#     except Exception as err:
#         print(f"Unexpected {err=}, {type(err)=}")
#         print("Network exception occurred")


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        response = requests.get(request_url, timeout=10)
        response.raise_for_status()  # Raise an error if the HTTP request failed

        try:
            return response.json()  # Assuming the response is valid JSON
        except ValueError:
            print("Error: Response is not in JSON format.")
            return {"sentiment": "unknown"}  # Default if JSON parsing fails
    except requests.exceptions.RequestException as err:
        # Log the error for debugging
        print(f"ConnectionError: {err}")
        return {"sentiment": "unknown"}  # Return a default sentiment in case of error


# def post_review(data_dict):
# Add code for posting review
def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except Exception as e:
        print(f"Network exception occurred 2: {e}")
