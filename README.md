# Scrabble words

Simple scrapy spider to scrape words from [allscrabblewords](http://www.allscrabblewords.com/).
The words are saved in .xls with one worksheet per word length.

## How to use

```
git clone https://github.com/tkleyton/scrabble-words
cd scrabble-words

scrapy crawl words
```
Make sure to install the requirements:
```
pip install -r requirements.txt
```

## Modifying the script

Words list for each length are extracted by [`scrabble/spiders/words.py`](scrabble/spiders/words.py) as a single item and then processed by [`ScrabblePipeline`](scrabble/pipelines.py)

Currently, up to 16 concurrent requests are performed, which means the worksheets are written unsorted.
The module `xlwt` doesn't support worksheet sorting. A workaround to get the sheets sorted by word length is to set `CONCURRENT_REQUESTS = 1` in [scrabble/settings.py](scrabble/settings.py).
