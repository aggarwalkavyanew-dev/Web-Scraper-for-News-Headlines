[auto_detected_headlines.txt](https://github.com/user-attachments/files/22534596/auto_detected_headlines.txt)# Web-Scraper-for-News-Headlines
Python script to automatically extract and rank potential news headlines from the BBC News homepage using BeautifulSoup, tag frequency analysis, and basic content filtering.

# 📰 BBC News Headline Extractor (Auto Detection Script)

This Python script automatically scrapes and identifies potential news headlines from the [BBC News homepage](https://www.bbc.com/news). It uses HTML parsing and filtering logic to detect meaningful headlines based on tag frequency and text patterns — no hardcoded selectors required.

---

## 🔍 Features

- ✅ Scrapes the latest content from `https://www.bbc.com/news`
- ✅ Tests multiple HTML tags (`h1`, `h2`, `h3`, `a`, `span`) for headline-like content
- ✅ Filters out boilerplate, footer links, cookie messages, and other irrelevant text
- ✅ Ranks tags by quantity of relevant content detected
- ✅ Outputs a clean list of unique headlines to a `.txt` file
- ✅ Prints a readable summary to the console

---

## 📂 Output

A file called `auto_detected_headlines.txt` will be created with all the detected headlines.

Example:

[Uploading auto_detecte1. Denmark says 'professional actor' behind drone incursions over its airports
2. Trump demands inquiry over UN 'triple sabotage' after escalator and teleprompter mishaps
3. Over 1,000 children fall ill from free school lunches in Indonesia
4. Kindergarten parents told to pay thousands for kids' art - sparking uproar and a midnight heist
5. Woman in Spanish cold case identified after 20 years
6. Australian film altered in China to make gay couple straight
7. India imposes curfew in Ladakh after statehood protests turn violent
8. India legal setback for Elon Musk's X in free speech fight
9. The sun sets on India's iconic and controversial Soviet fighter jet
10. Nicolas Sarkozy found guilty of criminal conspiracy in Libya case
11. What we know about the suspect in the ICE facility shooting in Dallas
12. 'Film me all you want' - teenage girls with no fear of police tormenting a UK high street
13. China makes landmark pledge to cut its climate emissions
14. 'No warning' - residents reel from deadly flood after typhoon bursts Taiwan lake
15. 'There's no way we can afford $100,000': Small firms scramble over Trump's new visa fees
16. Two photos that shaped the long run to sporting equality
17. From Bayern despair to Liverpool brilliance - the rise of Ryan Gravenberch
18. Matthew McConaughey on starring with his family in film about California's deadliest wildfire
19. Moment sinkhole pulls down power lines in busy Bangkok street
20. Watch: White House replaces President Biden portrait with image of an autopen
21. Watch: Moment water shatters glass doors of Hong Kong hotel
22. Syrian leader addresses UN General Assembly for first time in almost 60 years
23. Watch: Typhoon Ragasa leaves trail of destruction in China
24. 'Anti-ICE' message on ammunition at Dallas shooting that killed immigration detainee
25. UK considers financial support for Jaguar Land Rover suppliers after cyber-attack
26. America's blame game over Canada's wildfire smoke misses the point, experts say
27. Jimmy Kimmel's return draws record ratings despite limited showing
28. Howling winds and sheets of rain: Inside Chinese city battered by Typhoon Ragasa
29. Russia will expand aggression beyond Ukraine if not stopped, Zelensky warns
30. 'Film me all you want' - teenage girls with no fear of police torment one High Street
31. White House says to prep for mass firings if government shuts down
32. Born in India, but not Indian: 'Stateless' man fights for citizenship
33. England 'don't need to be perfect' in World Cup final
34. From Bayern despair to Liverpool brilliance - the rise of Gravenberch
35. Europe 'fuelled by something money can’t buy' - Donald
36. Cameron elevated to world champion as Taylor takes break
37. Javelin hero ready to pour a pint for podium stars
38. Forest's European return: How is Angeball working after Betis draw?
39. When will £18m Lammens get his chance at Man Utd?
40. LIVEWhat we know about the suspect in the ICE facility shooting in Dallas
d_headlines.txt…]()

 
---

## 📦 Dependencies

- `requests`
- `beautifulsoup4`

Install them via pip:

```bash
pip install requests beautifulsoup4

