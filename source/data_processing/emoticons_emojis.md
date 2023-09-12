# Emoticons and emojis

Transliteration of **emojis** can be achieved through the use of the Python module [`emoji`](https://github.com/carpedm20/emoji/), while **emoticons** can be processed - and converted - using regular expressions as exemplified in [`[s6.06]`](../case_studies/og/index.md#s6-06).  
  
Options and arguments for `emoji` can be found in the [official documentation](https://carpedm20.github.io/emoji/docs/).  

## Install the required module{octicon}`repo-template;1em;sd-text-success`

```bash
pip install emoji
```

## Function to transliterate emojis (using two different output formats)[^sn1]
The function defined in `[s6.04]` can be imported into any script and be used with the included syntax

```python
demojize(INPUT, OUTPUT_FORMAT)
```
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s6.04_demojize.py
:name: s6-04
:caption: Script `[s6.04]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s6.04_demojize.py)
:linenos:
:lines: 20-
```

[^sn1]: `CATLISM, 345-346`