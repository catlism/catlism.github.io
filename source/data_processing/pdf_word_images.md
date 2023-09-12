# PDF, Word, images

## Extract text from PDF and other multimedia formats[^sn1]
[`textract`](https://github.com/deanmalmgren/textract) is a Python module and tool acting as a "single interface for extracting content from any type of fle, without any irrelevant markup"[^sn2]; as such it can be used to process a variety of formats containing some form of language (including images and audio files; [consult the list of all supported formats](https://textract.readthedocs.io/en/stable/#currently-supporting)). Processing of images and audio files requires the installation of additional modules. Options and further arguments may be found in the [official documentation](https://textract.readthedocs.io/en/stable/).

### Installing the tool
```{code-block} bash
:name: c5-33
:caption: Command `[c5.33]`

pip install textract
```

:::{dropdown} {octicon}`video;2em` `[c5.33]`
```{eval-rst}
.. asciinema:: 607199

```
:::

### Using the tool
Usage as a Python module is exemplified in [`[s5.05]`](../data_collection/general_purpose/beautifulsoup.md#s5-05), CLI usage is exemplified below.

```{code-block} bash
:name: c5-34
:caption: Command `[c5.34]` {octicon}`git-pull-request;1em;sd-text-warning`

textract filename.extension -o output.extension
```

:::{dropdown} {octicon}`video;2em` `[c5.34]`
```{eval-rst}
.. asciinema:: 607203

```
:::

[^sn1]: `CATLISM, 278-279`
[^sn2]: [https://textract.readthedocs.io/en/stable/](https://textract.readthedocs.io/en/stable/)