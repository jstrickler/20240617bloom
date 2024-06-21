import requests

URL = 'https://www.python.org'

response = requests.get(URL)

if response.ok:
    for header, value in sorted(response.headers.items()): # response.headers is a dictionary of the headers
        print(f"{header:20.20s} {value}")
    print()

    # response.content  raw data
    # response.text   raw data converted to text  (response.content.decode())
    print(response.text[:500])   # The text is returned as a bytes object, so it needs to be decoded to a string; print the first 200 bytes
    print('...')
    print(response.text[-500:])   # print the last 200 bytes
