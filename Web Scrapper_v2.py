import requests
import re
from bs4 import BeautifulSoup
from collections import defaultdict
from difflib import SequenceMatcher

# ----------------------------
# Utility Functions
# ----------------------------

def clean_text(text):
    cleaned = re.sub(r'^\d+\s*', '', text)
    cleaned = re.sub(r'^\d+Watch:\s*', 'Watch: ', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def is_similar(a, b, threshold=0.85):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio() > threshold

def filter_blacklist(text, blacklist_phrases):
    return any(phrase.lower() in text.lower() for phrase in blacklist_phrases)

def deduplicate_headlines(headlines):
    unique = []
    for h in headlines:
        if not any(is_similar(h, u) for u in unique):
            unique.append(h)
        else:
            for i, u in enumerate(unique):
                if is_similar(h, u) and len(h) > len(u):
                    unique[i] = h
    return unique

def extract_ranked_headlines(soup, blacklist_phrases, tags_to_test=['h1', 'h2', 'h3', 'a', 'span']):
    tag_texts = defaultdict(list)

    for tag_name in tags_to_test:
        for tag in soup.find_all(tag_name):
            text = tag.get_text(strip=True)
            if 30 <= len(text) <= 150 and not filter_blacklist(text, blacklist_phrases):
                cleaned = clean_text(text)
                tag_texts[tag_name].append(cleaned)

    tag_ranking = sorted(tag_texts.items(), key=lambda x: len(x[1]), reverse=True)
    top_tags = [tag for tag, texts in tag_ranking if len(texts) >= 3]

    final_headlines = []
    for tag in top_tags:
        final_headlines.extend(tag_texts[tag])

    return final_headlines

# ----------------------------
# Scraping Logic
# ----------------------------

def scrape_url(url):
    try:
        print(f"🔗 Scraping: {url}")
        res = requests.get(url, timeout=10)
        res.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Failed to fetch {url}: {e}")
        return []

    soup = BeautifulSoup(res.text, "html.parser")
    blacklist = ["cookies", "sign in", "login", "accessibility", "terms", "privacy"]
    headlines = extract_ranked_headlines(soup, blacklist)
    return headlines

# ----------------------------
# Main
# ----------------------------

def main():
    print("📥 Enter URLs of news websites (one per line).")
    print("Type 'done' when finished:\n")

    urls = []
    while True:
        url = input("URL: ").strip()
        if url.lower() == 'done':
            break
        elif url.startswith("http"):
            urls.append(url)
        else:
            print("⚠️  Please enter a valid URL starting with http or https.")

    if not urls:
        print("❌ No URLs entered. Exiting.")
        return

    all_headlines = []
    for url in urls:
        headlines = scrape_url(url)
        all_headlines.extend(headlines)

    unique_headlines = deduplicate_headlines(all_headlines)

    with open("hybrid_headlines.txt", "w", encoding="utf-8") as file:
        for idx, headline in enumerate(unique_headlines, 1):
            file.write(f"{idx}. {headline}\n")

    print("\n✅ Headline scraping complete!")
    print(f"Total unique headlines saved: {len(unique_headlines)}\n")

    for idx, headline in enumerate(unique_headlines, 1):
        print(f"{idx}. {headline}")

# ----------------------------
# Run
# ----------------------------

if __name__ == "__main__":
    main()
