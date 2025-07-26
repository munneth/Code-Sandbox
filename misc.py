
# fetch api data with error handling
def fetchOptions(date):
    url = f'link-put-variables-in-{curly-braces}'
    r = requests.get(url)
    data = r.json()
    if 'data' in data:
        return data['data']
    else:
        print("Warning: 'data' key not found in API response:", data)
        return []