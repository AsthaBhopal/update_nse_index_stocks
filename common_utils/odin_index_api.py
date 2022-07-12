import requests


def get_odin_index_details():
    url = "https://asthasecurewaveapi.odinwave.com/nontransactional/101/v1/getIndexDetails"

    payload={}
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6OTA5MDkwLCJ1c2VyaWQiOjkwOTA5MCwidGVuYW50aWQiOjkwOTA5MCwibWVtYmVySW5mbyI6eyJ0ZW5hbnRJZCI6IjEwMSIsImdyb3VwSWQiOiJITyIsInVzZXJJZCI6IkFGMDYxNyIsInRlbXBsYXRlSWQiOiJESUVUMzYiLCJ1ZElkIjoiQUIwOTVCRkQtQTMwMi00OTE0LUIxQzctOTFFNkNBRDhFNURBIiwib2NUb2tlbiI6IjB4MDE0RDEwQUZBRTZCNjM4NkEzNTU5MkEyMEQwMzI5IiwidXNlckNvZGUiOiJPREpTUyIsImdyb3VwQ29kZSI6IkFBQUFBIiwiYXBpa2V5RGF0YSI6eyJDdXN0b21lcklkIjoiMTAxIiwiZXhwIjoxNjU4ODk2MjAwLCJpYXQiOjE2MjczNjAyMzV9LCJzb3VyY2UiOiJNT0JJTEVBUEkifSwiZXhwIjoxNjczODkzNzk5LCJpYXQiOjE2NTU5NzExNjB9.fCpzKqab_DNVTXNj0iDsH37b6I8HaIh-DsFDtukjzIY',
    'x-api-key': 'pPB3vi7IjK1thsTmvKhx3oiVlP1aUt06zi8gFKma'
    }

    response = requests.request("GET", url, headers=headers, data=payload).json()
    # print(response.text)

    return response['result']



if __name__ == '__main__':
    print(get_odin_index_details())