import requests
import json
from datetime import datetime, date

file_path = "/workspaces/practice_python/url.json"

def is_todays_daytime(date_added_str):
    try:
        date_added = datetime.strptime(date_added_str, "%Y-%m-%d %H:%M:%S UTC")
    except ValueError:
        print(f"Invalid date_added string format: {date_added_str}")
        return False

    today = datetime.now().date() 
    return date_added.date() == today

def match_tag(tags):
    if tags is not None:
        for tag in tags:
            if ('exe' in tag):
                return True
    return False


def filter_urls_with_exe(urls):
    temp = []
    if urls is not None:
            for url_object in urls:
                if is_todays_daytime(url_object["date_added"]):
                    tags = url_object["tags"]
                    if match_tag(tags):
                        temp.append(url_object["url"])
    return temp

def store_urls(json_response, file_path):
    """
    Stores URLs with the "exe" tag from the given JSON response into a file.

    Args:
        json_response: The JSON response containing the URLs.
        file_path: The path to the file where URLs will be stored.
    """

    try:
        urls = json_response["urls"]  # Extract the 'urls' list from the response

        # Filter URLs with the "exe" tag
        urls_with_exe = filter_urls_with_exe(urls)
    
        # Write the updated data back to the file
        with open(file_path, "w") as file:
            json.dump(urls_with_exe, file, indent=4)

        print("Data appended successfully.")

    except FileNotFoundError:
        # Create a new file if it doesn't exist
        with open(file_path, "w") as file:
            json.dump(urls_with_exe, file, indent=4)
        print("New file created and URLs stored successfully.")

    except KeyError:
        print("Error: 'urls' key not found in the JSON response.")

    except json.JSONDecodeError:
        print("Error: Invalid JSON data in the file.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")







def query_urlhaus(auth_key, url):
    # Construct the HTTP request
    data = {
        'url' : url
    }
    # Set the Authentication header
    headers = {
        "Auth-Key": auth_key
    }

    response = requests.get(url, data, headers=headers)
    
    # Parse the response from the API
    json_response = response.json()

    if json_response['query_status'] == 'ok':
        store_urls(json_response, file_path)

    elif json_response['query_status'] == 'no_results':
        print("No results")
    else:
        print(json_response['query_status'])




auth_key = "" #obtain and paste here
url = "https://urlhaus-api.abuse.ch/v1/urls/recent/"
query_urlhaus(auth_key, url)