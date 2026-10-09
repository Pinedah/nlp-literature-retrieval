import json
import requests

API_URL = "https://api.steampowered.com/IUserReviewsService/GetAppReviews/v1/"

# Example application: Counter-Strike 2
APP_ID = 730

# Request parameters for IUserReviewsService/GetAppReviews.
request_data = {
    "appid": APP_ID,
    "filter": 1,          # Recent
    "languages": ["english"],
    "review_type": 0,     # All reviews
    "purchase_type": 1,   # All purchase types
    "num_per_page": 10
}

params = {
    "input_json": json.dumps(request_data)
}

try:
    response = requests.get(API_URL, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

except requests.RequestException as error:
    print(f"Request error: {error}")
    raise SystemExit(1)

except ValueError as error:
    print(f"Invalid JSON response: {error}")
    raise SystemExit(1)


# ----------------------------------------------------------------------
# Inspect the JSON structure
# ----------------------------------------------------------------------

print("Top-level keys:")
print(data.keys())

# The Steam API places the actual result inside the "response" object.
api_response = data.get("response", {})

print("\nResponse keys:")
print(api_response.keys())


# ----------------------------------------------------------------------
# Extract reviews
# ----------------------------------------------------------------------

reviews = api_response.get("reviews", [])

print(f"\nReviews returned: {len(reviews)}")

if reviews:
    print("\nFields available in the first review:")
    print(reviews[0].keys())

    print("\nFirst review:")
    print(json.dumps(reviews[0], indent=2, ensure_ascii=False))
else:
    print("\nNo reviews were returned by this request.")


# ----------------------------------------------------------------------
# Inspect the pagination cursor
# ----------------------------------------------------------------------

cursor = api_response.get("cursor")

print("\nCursor returned by the API:")
print(cursor)
