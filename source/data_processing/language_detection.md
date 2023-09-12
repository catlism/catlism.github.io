# Language detection

Recognition of language(s) in a document can be achieved through various tools, such as [`langid`](https://github.com/saffsd/langid.py) or its newest and updated fork [`py3langid`](https://github.com/adbar/py3langid) (by Adrien Barbaresi, the author of [Trafilatura](../data_collection/general_purpose/trafilatura.md)).  
  
Following what included in the book, only `langid` is exemplified in the following script. Usage of `py3langid` will be included in future versions of the compendium.  
   
Options and arguments for `langid` can be found in the [official documentation](https://github.com/saffsd/langid.py/blob/master/README.rst).  

## Identify a set of predefined languages in .txt files and write a summary report in spreadsheet format[^sn1]
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.16_detect_languages_langid.py
:name: s5-16
:caption: Script `[s5.16]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.16_detect_languages_langid.py)
:linenos:
:lines: 20-
```


[^sn1]: `CATLISM, 281-283`