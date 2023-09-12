# Facebook
Data collection from Facebook can be obtained using [`facebook-scraper`](https://github.com/kevinzg/facebook-scraper).  
Options and arguments for the tool can be found in the [official documentation](https://github.com/kevinzg/facebook-scraper/blob/master/README.md).


## Installing the tool[^sn1]
```{code-block} bash
:name: c5-26
:caption: Command `[c5.26]`

pip install facebook-scraper
```

:::{dropdown} {octicon}`video;2em` `[c5.26]`
```{eval-rst}
.. asciinema:: 607194

```
:::

## Using the tool[^sn2]

```{code-block} python
:name: c5-27
:caption: Command `[c5.27]`

facebook-scraper --filename OUTPUT.json --format json --comments --pages N PROFILE_NAME
```

## Extracting the data
### Extract data from posts[^sn3]
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.10_extract_facebookscraper-posts_json.py
:name: s5-10
:caption: Script `[s5.10]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.10_extract_facebookscraper-posts_json.py)
:linenos:
:lines: 20-
```

#### How to use script `[s5.10]`{octicon}`repo-template;1em;sd-text-success`
Copy/download the file `s5.10_extract_facebookscraper-posts_json.py` inside the folder where the data downloaded through `facebook-scraper` (e.g. through `c5.27`) resides; then browse inside the folder through the terminal, e.g.

```{code-block} bash
cd Downloads/facebook_data/
```

At last, run the script from the terminal:

```{code-block} bash
python s5.10_extract_facebookscraper-posts_json.py
```

### Extract data from profiles[^sn4]
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.11_get_profile_details.py
:name: s5-11
:caption: Script `[s5.11]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.11_get_profile_details.py)
:linenos:
:lines: 20-
```

### Implement the collection of profile details (`[s5.11]`) into `[s5.10]`[^sn5]
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.12_use_module_in_s5.10.py
:name: s5-12
:caption: Script `[s5.12]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.12_use_module_in_s5.10.py)
:linenos:
:lines: 20-
```

### Example of data extracted with `[s5.10]`[^sn6]
```{code-block} xml
:name: e5-12
:caption: Example `[e5.12]`
:linenos:

<?xml version='1.0' encoding='UTF-8'?>
<text>
  <post id="UNIQUE_POST_ID" author="USER_FULL_NAME" author_id="UNIQUE_AUTHOR_ID" comments="NUMBER" shares="NUMBER" date_d="NUMBER" date_m="NUMBER" date_y="NUMBER" likes="NUMBER" reactions_count="NUMBER" reaction_sad="NUMBER">
    POST TEXTUAL CONTENTS
    <comment type="c" comment_to="UNIQUE_POST_ID" id="UNIQUE_COMMENT_ID" author="USER_FULL_NAME" author_id="UNIQUE_AUTHOR_ID" date_d="NUMBER" date_m="NUMBER" date_y="NUMBER">COMMENT TEXTUAL CONTENTS</comment>
    <comment type="r" comment_to="UNIQUE_COMMENT_ID" id="UNIQUE_COMMENT_ID" author="USER_FULL_NAME" author_id="UNIQUE_AUTHOR_ID" date_d="NUMBER" date_m="NUMBER" date_y="NUMBER">REPLY TEXTUAL CONTENTS</comment>
  </post>
</text>
```

[^sn1]: `CATLISM, 227`
[^sn2]: `CATLISM, 227`
[^sn3]: `CATLISM, 237-242`
[^sn4]: `CATLISM, 242-245`
[^sn5]: `CATLISM, 245-246`
[^sn6]: `CATLISM, 236-237`