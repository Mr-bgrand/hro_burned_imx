import requests

# API endpoint URL
url = "https://api.x.immutable.com/v1/assets?status=burned&collection=0x8cb332602d2f614b570c7631202e5bf4bb93f3f6"
filtered_assets = []
cursor = None
page = 0

# Function to extract relevant fields from an asset
def extract_fields(asset):
    return {
        'user': asset['user'],
        'token_id': asset['token_id'],
        'status': asset['status'],
        'name': asset['name'],
        'metadata_name': asset['metadata']['name'],
        'metadata_uuid': asset['metadata']['uuid'],
        'metadata_mintNumber': asset['metadata']['mintNumber'],
        'metadata_totalMinted': asset['metadata']['totalMinted'],
        'metadata_cardId': asset['metadata']['cardId'],
        'updated_at': asset['updated_at']
    }

# Loop through API pages until there are no more results or the cursor is not provided
while True:
    # Check if there is a cursor, if so, append it to the URL
    if cursor:
        request_url = f"{url}&cursor={cursor}"
    else:
        request_url = url

    # Make a request to the API endpoint
    response = requests.get(request_url)

    # If the response status is 200 (successful), process the data
    if response.status_code == 200:
        data = response.json()

        # Extract the assets from the response
        assets = data['result']

        # Increment the page counter and print the progress
        page += 1
        print(f"Processing page {page}, filtered assets found: {len(filtered_assets)}")

        # Loop through the assets and filter the ones with mintNumber < 100
        for asset in assets:
            mint_number = asset['metadata']['mintNumber']
            if mint_number < 100:
                filtered_assets.append(extract_fields(asset))

        # Get the cursor and remaining values from the response
        cursor = data.get('cursor')
        remaining = data.get('remaining')

        # If there is no cursor or remaining is 0, break the loop
        if not cursor or remaining == 0:
            break
    else:
        # If the response status is not 200, print an error message and break the loop
        print(f"Error: {response.status_code}")
        break

# Print the filtered assets
print("Filtered assets:", filtered_assets)
