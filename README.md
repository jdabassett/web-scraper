# Web Scraper

### Authors:
Jacob Bassett

### Dates:
11/11/2023

### Description:
This is a simple web scrapper designed to find the number of elements within a wikipedia page that are missing citation and generate a report.

### Usage
Run the follow commands in the terminal to scrape a give wikipedia webpage. Must input a file name to save/append results into. Remember to avoid illegal characters in file name. (\ /:*?"<>|) Also supply wikipedia page url to be scraped.

```bash
# run script with output file name and url to be scraped
python3 scraper/scraper.py vodka https://en.wikipedia.org/wiki/Vodka
# output
2023-11-11 20:24

Website: https://en.wikipedia.org/wiki/Vodka

Number of 'Citation needed' in given website: 1
Report of paragraphs from website that need citation:
In some countries, black-market or "bathtub" vodka is widespread because it can be produced easily and avoids taxation. However, severe poisoning, blindness, or death can occur as a result of dangerous industrial ethanol substitutes being added by black-market producers.[54] In March 2007 in a documentary, BBC News UK sought to find the cause of severe jaundice among imbibers of a "bathtub" vodka in Russia.[55] The cause was suspected to be an industrial disinfectant (Extrasept)—95% ethanol but also containing a highly toxic chemical—added to the vodka by the illegal traders because of its high alcohol content and low price. Death toll estimates list at least 120 dead and more than 1,000 poisoned[vague]. The death toll is expected to rise due to the chronic nature of the cirrhosis that is causing jaundice.[citation needed]```
```

```
# vodka_report.txt
2023-11-11 20:24
Website: https://en.wikipedia.org/wiki/Vodka
Number of 'Citation needed' in given website: 1
1: In some countries, black-market or "bathtub" vodka is widespread because it can be produced easily and avoids taxation. However, severe poisoning, blindness, or death can occur as a result of dangerous industrial ethanol substitutes being added by black-market producers.[54] In March 2007 in a documentary, BBC News UK sought to find the cause of severe jaundice among imbibers of a "bathtub" vodka in Russia.[55] The cause was suspected to be an industrial disinfectant (Extrasept)—95% ethanol but also containing a highly toxic chemical—added to the vodka by the illegal traders because of its high alcohol content and low price. Death toll estimates list at least 120 dead and more than 1,000 poisoned[vague]. The death toll is expected to rise due to the chronic nature of the cirrhosis that is causing jaundice.[citation needed]
```

### Tests
Run to following command to run some unit tests. Note that two of the unit tests are based on the url "https://en.wikipedia.org/wiki/Vodka". If the number of 'citation needed' changes between the writing of this webscraper and the reading; then these tests will fail.

```bash
pytest tests/test_scraper.py
```

### Tools:
playwright==1.39.0
pytest==7.4.3
