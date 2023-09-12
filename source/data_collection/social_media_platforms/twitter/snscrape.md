# Twitter

```{warning}
As of late June 2023 a number of changes have made anonymous access to tweets impossible, consequently rendering the use of tools such as `snscrape` and other "API-less" ones useless. Apparently Twitter will reinstate anonymous access in the future (see [this discussion from `snscrape` issue pages](https://github.com/JustAnotherArchivist/snscrape/issues/996)), but **as of 10th September 2023 a number of commands and scripts included in this page - and marked with {octicon}`stop;1em;sd-text-danger` are not working**. They are included to support the contents of the book, and new (working) ones will be included if anything changes.
```

Data collection from Twitter can be obtained using [`snscrape`](https://github.com/JustAnotherArchivist/snscrape).  
Options and arguments for the tool can be found in the [official documentation](https://github.com/JustAnotherArchivist/snscrape).

## Installing the tool[^sn1]
```{code-block} bash
:name: c5-11
:caption: Command `[c5.11]`

pip install snscrape
```

:::{dropdown} {octicon}`video;2em` `[c5.11]`
```{eval-rst}
.. asciinema:: 607191

```
:::

## Using the tool[^sn2]

```{code-block} python
:name: c5-12
:caption: Command `[c5.12]`

snscrape [GLOBAL-OPTIONS] SCRAPER-NAME [SCRAPER-OPTIONS] [SCRAPER-ARGUMENTS ... ]
```

```{code-block} python
:name: c5-13
:caption: Command `[c5.13]`

snscrape SCRAPER-NAME --help
```

```{code-block} python
:name: c5-14
:caption: Command `[c5.14]` {octicon}`stop;1em;sd-text-danger`

snscrape -v --progress --jsonl twitter-search '[QUERY]' > OUTPUT.jsonl
```

```{code-block} python
:name: c5-15
:caption: Command `[c5.15]` {octicon}`stop;1em;sd-text-danger`

snscrape -v --progress --jsonl twitter-search '("technology" OR "physics") ("space" OR "rockets")' > OUTPUT.jsonl
```

```{code-block} python
:name: c5-16
:caption: Command `[c5.16]`

("technology" OR "physics") ("space" OR "rockets")
```

```{code-block} python
:name: c5-17
:caption: Command `[c5.17]`

(techology OR physics) (space OR rokets)
```

```{code-block} python
:name: c5-18
:caption: Command `[c5.18]`

("technology" OR "physics") -("games" OR "console")
```

```{code-block} bash
:name: c5-19
:caption: Command `[c5.19]`

(🏴 OR 🌈) since_time:1654034400 until_time:1656626399
```

```{code-block} python
:name: c5-20
:caption: Command `[c5.20]`

source:twitter_web_app since_time:1654038000 until_time:1659308400 @POTUS -from:POTUS -filter:media
```

### Collecting tweets from a list of search terms[^sn3]

#### Install the required modules
```{code-block} python
:name: c5-21
:caption: Command `[c5.21]`

pip install pandas
```

:::{dropdown} {octicon}`video;2em` `[c5.21]`
```{eval-rst}
.. asciinema:: 607192

```
:::

#### Script to read the list of search terms and download tweets
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.07_snscrape_from_list.py
:name: s5-07
:caption: Script `[s5.07]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.07_snscrape_from_list.py) {octicon}`stop;1em;sd-text-danger`
:linenos:
:lines: 20-
```

#### Using script `[s5.07]`
From the terminal, once inside the folder where script `snscrape_from_list.py` has been saved and where the `SEARCH_LIST.txt` file resides, run command `[c5.22]` after changing `--max N` to the desired value (e.g. `--max 10`).
```{code-block} python
:name: c5-22
:caption: Command `[c5.22]` {octicon}`stop;1em;sd-text-danger`

python snscrape_from_list.py SEARCH_LIST.txt --max N
```

#### Example of filename saved by script `[s5.07]`
```{code-block} bash
:name: e5-09
:caption: Example `[e5.09]`

(🏴 OR 🌈) since_time-1654034400 until_time-1656626399.csv
```

## Extracting the data[^sn4]
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.08_extract_snscrape_jsonl.py
:name: s5-08
:caption: Script `[s5.08]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.08_extract_snscrape_jsonl.py)
:linenos:
:lines: 20-
```

#### How to use script `[s5.08]`{octicon}`repo-template;1em;sd-text-success`
Copy/download the file `s5.08_extract_snscrape_jsonl.py` inside the folder where the output file `snscrape_output.jsonl` downloaded through `snscrape` (e.g. through `c5.14`) resides; then browse inside the folder through the terminal, e.g.

```{code-block} bash
cd Downloads/twitter_data/
```

At last, run the script from the terminal:

```{code-block} bash
python s5.08_extract_snscrape_jsonl.py
```


## Example of data extracted with `[s5.08]`[^sn5]

```{code-block} xml
:name: e5-10
:caption: Example `[e5.10]`
:linenos:

<?xml version='1.0' encoding='UTF-8'?>
<corpus>
  <text id="ID_NUMBER" date="YYYY-MM-DDThh:mm:ssTZD" username="USERNAME" user_realname="USER_REAL_NAME" urls_present="0_OR_1" isretweet="0_OR_1">TWEET TEXT</text>
</corpus>
```

[^sn1]: `CATLISM, 183`
[^sn2]: `"CATLISM, 183; 191-192`
[^sn3]: `CATLISM, 193-196`
[^sn4]: `CATLISM, 204-206`
[^sn5]: `CATLISM, 204`