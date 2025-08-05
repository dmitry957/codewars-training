import requests 
# It is recommended to use this header along with your request.
headers = {'Accept-Encoding': 'gzip,deflate'}
def wikidata_scraper(url):
    response = requests.get(url, headers=headers)
    data = response.json()
    item_id = list(data['entities'].keys())[0]
    entity = data['entities'][item_id]
    label = entity.get("labels", {}).get("en", {}).get("value", "No Label")
    description = entity.get("descriptions", {}).get("en", {}).get("value", "No Description")

    return {
        "ID": item_id,
        "LABEL": label,
        "DESCRIPTION": description
    }