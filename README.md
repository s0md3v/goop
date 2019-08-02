<h1 align="center">
  <br>
  <a href="https://github.com/s0md3v/goop"><img src="https://i.ibb.co/LrCjHVT/googly-logo.png" alt="goop"></a>
  <br>
  goop
  <br>
</h1>

<h4 align="center">Google Search Scraper</h4>

<p align="center">
  <a href="https://github.com/s0md3v/goop/releases">
    <img src="https://img.shields.io/github/release/s0md3v/goop.svg">
  </a>
  <a href="https://github.com/s0md3v/goop/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues-closed-raw/s0md3v/goop.svg">
  </a>
</p>

### Contents

- [Introduction](https://github.com/s0md3v/googly#introduction)
- [How it works?](https://github.com/s0md3v/googly#how-it-works)
- [Usage](https://github.com/s0md3v/googly#usage)
    - [Installation](https://github.com/s0md3v/googly#installation)
    - [Example](https://github.com/s0md3v/googly#example)
- [Legal](https://github.com/s0md3v/googly#legal)

### Introduction
goop can perform google searches without being blocked by the CAPTCHA or hitting any rate limits.

### How it works?
Facebook provides a [debugger tool](https://developers.facebook.com/tools/debug/echo/?q=https://example.com) for its scraper.
Interestingly, Google doesn't limit the requests made by this debugger (whitelisted?) and hence it can be used to scrap the google search results without being blocked by the CAPTCHA.\
Since facebook is involved, a facebook session `Cookie` must be supplied to the library with each request.
### Usage
#### Installation
```
pip install goop
```
#### Example
```python
from goop import goop

page_1 = goop.search('red shoes', '<your facebook cookie>')
page_2 = goop.search('red_shoes', '<your facebook cookie>', page='1')
include_omitted_results = goop.search('red_shoes', '<your facebook cookie>', page='8', full=True)
```
The returned is a `dict` of following structure

```
{
    "0": {
        "url": "https://example.com",
        "text": "Example webpage",
        "summary": "This is an example webpage whose aim is to demonstrate the usage of ..."
    },
    "1": {
...
```

`cli.py` demonstrates the usage by performing google searches from the terminal with the following command
```
python cli.py <query> <number_of_pages>
```

![goop-cli](https://i.ibb.co/30Vsk87/Screenshot-2019-08-02-22-42-53.png)

### Legal & Disclaimer
Scraping google search results is illegal. This library is merely a proof of concept of the bypass. The author isn't responsible for the actions of the end users.
