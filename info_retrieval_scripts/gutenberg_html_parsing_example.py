import requests
from bs4 import BeautifulSoup

URL = "https://www.gutenberg.org/cache/epub/55/pg55-images.html"
headers = {"User-Agent": "NLP-Classroom-Example/1.0"}

try:
    response = requests.get(URL, headers=headers, timeout=30)
    response.raise_for_status()
except requests.RequestException as error:
    print(f"Request error: {error}")
    raise SystemExit(1)

soup = BeautifulSoup(response.text, "html.parser")

print("Page title:")
print(soup.title.get_text(" ", strip=True) if soup.title else "No title")
print("\n" + "-------------------------------------------------")

paragraphs = soup.find_all("p")
print("Paragraph elements found:", len(paragraphs))
print("-------------------------------------------------")

# Display the first 10 non-empty paragraphs.
shown = 0
for paragraph in paragraphs:
    text = paragraph.get_text(" ", strip=True)
    if not text:
        continue

    print(text)
    print("-------------------------------------------------")
    shown += 1

    if shown == 10:
        break
