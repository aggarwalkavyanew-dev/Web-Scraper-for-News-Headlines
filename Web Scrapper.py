import requests
import re
from bs4 import BeautifulSoup
from collections import defaultdict

# Step 1: Fetch page content
URL = "https://www.bbc.com/news"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Tags we want to test for headlines
tags_to_test = ['h1', 'h2', 'h3', 'a', 'span']

# Step 3: Store found texts by tag
tag_texts = defaultdict(list)
blacklist_phrases = [
    "British Broadcasting Corporation",
    "Read about our approach",
    "external linking",
    "cookies",
    "sign in",
    "accessibility",
    "terms of use",
]

# Step 4: Extract and filter text
for tag_name in tags_to_test:
    for tag in soup.find_all(tag_name):
        text = tag.get_text(strip=True)
        # Filter: non-empty, not too short or too long
        if 30 <= len(text) <= 150:
            if any(phrase.lower() in text.lower() for phrase in blacklist_phrases):
                continue  # skip it
            cleaned = re.sub(r'^\d+\s*', '', text)  # removes "1 ", "2 ", etc.
            cleaned = re.sub(r'^\d+Watch:\s*', 'Watch: ', cleaned)  # optional fix
            tag_texts[tag_name].append(cleaned)

# Step 5: Rank tags by how many valid texts they found
tag_ranking = sorted(tag_texts.items(), key=lambda x: len(x[1]), reverse=True)

# Step 6: Use top N tag(s) for final headline extraction
top_tags = [tag for tag, texts in tag_ranking if len(texts) >= 3]

# Collect final headlines
final_headlines = []
for tag in top_tags:
    final_headlines.extend(tag_texts[tag])


# Remove duplicates
unique_headlines = list(dict.fromkeys(final_headlines))

# Save to file
with open("auto_detected_headlines.txt", "w", encoding="utf-8") as file:
    for idx, headline in enumerate(unique_headlines, 1):
        file.write(f"{idx}. {headline}\n")

# Output summary
print("✅ Auto headline detection complete!")
print(f"Tags used: {', '.join(top_tags)}")
print(f"Headlines saved: {len(unique_headlines)}")
print()

for id, k in enumerate(unique_headlines, start=1):
    print(id, k)
