import requests

API_URL = "https://api.stackexchange.com/2.3/questions"

params = {
    "site": "ai",
    "pagesize": 10,
    "order": "desc",
    "sort": "creation",
    "filter": "withbody"
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

print("Top-level keys:")
print(data.keys())

questions = data.get("items", [])

print("\nQuestions returned:", len(questions))
print("Has more:", data.get("has_more"))
print("Quota remaining:", data.get("quota_remaining"))
print("-----------------------------------------------")

for question in questions:
    print("QUESTION ID:")
    print(question.get("question_id"))

    print("\nTITLE:")
    print(question.get("title"))

    print("\nBODY:")
    print(question.get("body"))

    print("\nTAGS:")
    print(question.get("tags"))

    print("\nCREATION DATE (Unix timestamp):")
    print(question.get("creation_date"))

    print("\nSCORE:")
    print(question.get("score"))

    print("\nANSWER COUNT:")
    print(question.get("answer_count"))

    print("\nACCEPTED ANSWER ID:")
    print(question.get("accepted_answer_id"))

    print("\nLINK:")
    print(question.get("link"))

    print("\n" + "------------------------------------------------")
