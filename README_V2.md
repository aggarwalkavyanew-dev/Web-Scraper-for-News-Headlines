# 📰 Hybrid News Headline Extractor

A Python script that scrapes and extracts meaningful news headlines from multiple news websites.  
It features advanced deduplication, tag ranking, and blacklist filtering to provide clean, unique headlines.
I have taken help from CHAT-GPT.

---

## 🔍 Features

- 🖥️ Accepts multiple URLs for scraping in a single run  
- 🎯 Extracts headlines from common HTML tags (`h1`, `h2`, `h3`, `a`, `span`)  
- 🚫 Filters out unwanted text like cookie notices, sign-in prompts, and privacy info  
- 🔍 Deduplicates similar headlines using fuzzy string matching (85% similarity threshold)  
- 🏆 Ranks HTML tags by headline density for smarter extraction  
- 📄 Saves unique headlines to `hybrid_headlines.txt`  
- ⚠️ Gracefully handles network errors and invalid URLs

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.x installed along with the following packages:

```bash
pip install requests beautifulsoup4
