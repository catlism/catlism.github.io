# Hashtags (word segmentation)
Segmentation of hashtags **with English words** can be achieved through the Python module [`wordsegment`](https://github.com/grantjenks/python-wordsegment).  
Word segmentation techniques for languages other than English require a different tool - or to train `wordsegment` on non-English data. Suggestions of tools for non-English texts are included at the end of this page.  
Word segmentation techniques may also be employed for [text normalisation](text_normalisation.md) procedures, since the tool works with any piece of text where two or more words are grouped together.

## Install the required module{octicon}`repo-template;1em;sd-text-success`

```bash
pip install wordsegment
```


## Segment hashtags and transform them into XML tags in a XML corpus file

```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.17_wordsegment_hashtags.py
:name: s5-17
:caption: Script `[s5.17]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.17_wordsegment_hashtags.py)
:linenos:
:lines: 20-
```

## Example of hashtags transformed through `[s5.17]`

```{code-block} xml
:name: e5-23
:caption: Example `[e5.23]` 
:linenos:
When did I become such a girl....<exhashtag orig="overanalyzingeverything">overanalyzing everything</exhashtag> <exhashtag orig="thisisntlikeme">this isn't like me</exhashtag>
```

## Word segmentation tools for languages other than English

The following table collects **Python tools** for applying word segmentation to languages other than English.  
Tools are selected from the [Github list of tools tagged as `word-segment`](https://github.com/topics/word-segmentation) and **have not been tested**!

| tool              | URL                                                                                            | supported language(s)                                                                                                |
|-------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| `PyThaiNLP`         | [https://github.com/PyThaiNLP/pythainlp](https://github.com/PyThaiNLP/pythainlp)               | Thai                                                                                                                 |
| `symspellpy`        | [https://github.com/mammothb/symspellpy](https://github.com/mammothb/symspellpy)               | Chinese, English, French, German, Hebrew, Italian, Russian, Spanish                                                  |
| `nagisa`            | [https://github.com/taishi-i/nagisa](https://github.com/taishi-i/nagisa)                       | Japanese                                                                                                             |
| `PyCantonese`       | [https://github.com/jacksonllee/pycantonese](https://github.com/jacksonllee/pycantonese)       | Cantonese                                                                                                            |
| `hashformers`       | [https://github.com/ruanchaves/hashformers](https://github.com/ruanchaves/hashformers)         | Any language supported by [Hugging Face models](https://huggingface.co/models) (virtually >200 as of September 2023) |
| `CKIP Transformers` | [https://github.com/ckiplab/ckip-transformers](https://github.com/ckiplab/ckip-transformers)   | Chinese                                                                                                              |
| `Myan-word-breaker` | [https://github.com/stevenay/myan-word-breaker](https://github.com/stevenay/myan-word-breaker) | Burmese                                                                                                              |