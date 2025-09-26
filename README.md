[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=20736068&assignment_repo_type=AssignmentRepo)
# Assignment 1 — Country Dictionary (BeautifulSoup)

Build a nested dictionary of countries from: https://www.scrapethissite.com/pages/simple/

- Top-level keys: country names (e.g., "Andorra")
- Values: dict with keys "Capital", "Population", "Area"

Example:
```python
{
  "Andorra": {"Capital": "Andorra la Vella", "Population": 84000, "Area": 468.0},
  ...
}
```

## Your Tasks
1. Implement `build_country_dict()` in `src/countrydict/scraper.py` using BeautifulSoup.
2. Use `soup.find_all("div", class_="country")` to iterate blocks (you may also use the more specific selector "col-md-4 country").
3. Extract:
   - `<h3 class="country-name">` -> country name
   - `<span class="country-capital">` -> capital
   - `<span class="country-population">` -> population (int)
   - `<span class="country-area">` -> area (float, km^2)
4. When run as a script, write `countries.json` to the project root.

## Run
```bash
pip install -r requirements.txt
python -m unittest -v
python -m countrydict.scraper           # writes countries.json
```

## Notes & Hints
- `class` is a Python keyword; BeautifulSoup uses `class_` instead.
- Class matching is token-based, so `class_="country"` does not match "country-info".
- Use `.get_text(strip=True)`, and clean numbers with `.replace(",", "")`.
- Include a small timeout and a friendly User-Agent.
