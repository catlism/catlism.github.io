# Analysing the language of far-right groups on Twitter and Facebook

> The case study [utilised] in this section is based on the research conducted at Swansea University Department of Applied Linguistics under the supervision of Prof. Nuria Lorenzo-Dus, as part of the project ‘Developing Interdisciplinary and Industry Collaboration to Tackle Far-Right Extremist Use of Social Media for Propaganda and Recruitment’ (Principal Investigator Dr. Lella Nouri). Outputs from the research are published in {cite:p}`nouri_investigating_2019` and {cite:p}`lorenzo-dus_discourse_2021` , which served as the basis for the contents [described].[^sn1]

```{warning}
Similar to the tools and techiques described in [Twitter](../../data_collection/social_media_platforms/twitter/snscrape.md), as of late June 2023 a number of changes have made anonymous access to tweets impossible, and consequently rendering the use of the tool [`twint`](https://github.com/twintproject/twint) (a project abandoned in the spring of 2022) and the techniques exemplified below useless. They are included to support the contents of the book.
```
## Collecting Twitter data for the corpus
### Collecting Twitter data for the corpus using `twint`[^sn2]
```{code-block} bash
:name: c6-01
:caption: Command `[c6.01]` {octicon}`stop;1em;sd-text-danger`

twint -u Twitter –since 2015-06-16 -o twint_output.csv -csv
```

### Collecting Twitter data for the corpus using `snscrape`[^sn3]
```{code-block} bash
:name: c6-02
:caption: Command `[c6.02]` {octicon}`stop;1em;sd-text-danger`

snscrape -v --progress -jsonl twitter-search 'since:2015–06–16 from:Twitter' > snscrape_output.json
```

### Extract the data from `twint` output to XML format[^sn4]
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s6.02_extract_twint_csv.py
:name: s6-02
:caption: Script `[s6.02]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s6.02_extract_twint_csv.py)
:linenos: 
:lines: 20-
```

### Example of data extracted with `[s6.02]`[^sn5]
```{code-block} xml
:name: e6-04
:caption: Example `[e6.04]` 
:linenos:
<?xml version='1.0' encoding='UTF-8'?>
<corpus>
  <text id="1492120137205526528" csv_date_created="2022-02-11T12:55:37+00:00" csv_username="Twitter" csv_user_realname="Twitter" csv_urls_present="0" csv_isretweet="0">oh good you're up :grinning-face-with-big-eyes:, here are a million Tweets to look at</text>
  <text id="1491089523291394052" csv_date_created="2022-02-08T16:40:20+00:00" csv_username="Twitter" csv_user_realname="Twitter" csv_urls_present="0" csv_isretweet="0">@Seipati-Sanity guess what we voted</text>
</corpus>
```

## Collecting Wordpress blog data for the corpus

### Syntax used for the Wordpress blog pages[^sn6]
```{code-block} bash
:name: e6-05
:caption: Example `[e6.05]`

https://example.com/page/[N]/
```

### Collecting links to all the posts in a blog[^sn7]

> Script `[s6.03]` [uses] the module requests and BeautifulSoup [...] to crawl the blog pages containing links to the posts and to scrape each post’s URL, respectively. The procedure relies on the default structure of WordPress blogs, whereby users can browse all the available posts in pages where only a preview is shown; these pages are accessible through links formatted as in example `[e6.05]`, where `[N]` is an incremental number starting from 2 indicating the second – up to the *n*th – page of the blog (the first page is instead missing the `/page/[N]/` string); and the string page indicates the URL path under which the contents are archived. Depending on how the creator of a blog sets up the website, strings such as `blog`, `news`, and `articles` may appear instead of `page`; in such cases it is sufficient to replace the latter with the relevant label in script `[s6.03]`. A further step is then required to adapt it to any other blog built using WordPress by changing the starting web address of the blog in lines 30 and 34.[^sn8]

```{rli} https://github.com/catlism/catlism_scripts/raw/main/s6.03_collect_posts_urls.py
:name: s6-03
:caption: Script `[s6.03]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s6.03_collect_posts_urls.py)
:linenos: 
:lines: 20-
```

## Transliterating emojis in the corpus [^sn9]

### Function to transliterate emojis (using two different output formats)
The function defined in `[s6.04]` can be imported into any script and be used with the included syntax

```{code-block} python
demojize(INPUT, OUTPUT_FORMAT)
```

```{rli} https://github.com/catlism/catlism_scripts/raw/main/s6.04_demojize.py
:name: s6-04
:caption: Script `[s6.04]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s6.04_demojize.py)
:linenos:
:lines: 20-
```

### Example of message before the transliteration

```{code-block} bash
:name: e6-06
:caption: Example `[e6.06]`

oh good you’re up 😄, here are a million Tweets to look at
```

### Example `[e6.06]` after emojis transliteration through `[s6.04]`

```{code-block} xml
:name: e6-07
:caption: Example `[e6.07]`

# using option 'default'
<text>oh good you're up {grinning_face_with_smiling_eyes}, here are a million Tweets to look at</text>

# using option 'custom'
<text>oh good you're up {grinning^face^with^smiling^eyes}, here are a million Tweets to look at</text>
```
[^sn1]: `CATLISM, 330`
[^sn2]: `CATLISM, 337`
[^sn3]: `CATLISM, 338`
[^sn4]: `CATLISM, 338-340`
[^sn5]: `CATLISM, 340`
[^sn6]: `CATLISM, 342`
[^sn7]: `CATLISM, 342-344`
[^sn8]: `CATLISM, 341`
[^sn9]: `CATLISM`