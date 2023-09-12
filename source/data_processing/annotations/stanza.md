# Annotations
A wide variety of options are available to annotate digital textual data; a first distinction is between **automated** and **manual** annotation. Only the former technique is included; **manual** annotation can easily be achieved through [INCEpTION](https://inception-project.github.io/), a multi-platform open source tool (written in Java) for interactive annotation - the [official documentation](https://inception-project.github.io/documentation/) includes guides and video tutorials.

```{note}
Further automated annotation tools (such as [PyMUSAS](https://github.com/UCREL/pymusas) for semantic annotations) will be documented in future versions of the compendium.
```

## Stanza[^sn1]

`Stanza` uses [universal POS (UPOS)](https://universaldependencies.org/u/pos/) tags, [treebank-specific POS (XPOS)](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html) tags, and [universal morphological features (UFeats)](https://universaldependencies.org/u/feat/index.html) for Part-Of-Speech annotations[^sn2] - accessible through `pos`, `xpos`, and `ufeats` respectively. Scripts `[s5.19]` (lines `33` and `39`) and `[s5.20]` (line `34`) both employ *universal POS* tags (`pos`).

### Installing the tool
```{code-block} bash
:name: c5-35
:caption: Command `[c5.35]`

pip install stanza
```

### Importing the module and installing a language model

```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.18_install_stanza_language-models.py
:name: s5-18
:caption: Script `[s5.18]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.18_install_stanza_language-models.py)
:linenos:
:lines: 20-
```

### Annotating textual data from `.txt` files into XML format

```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.19_use_stanza-XML.py
:name: s5-19
:caption: Script `[s5.19]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.19_use_stanza-XML.py)
:linenos:
:lines: 20-
```

#### How to use script `[s5.19]`{octicon}`repo-template;1em;sd-text-success`
Copy/download the file `s5.19_use_stanza-XML.py` inside the folder where the data to be annotated (in `.txt` format) resides; then browse inside the folder through the terminal, e.g.

```{code-block} bash
cd Downloads/corpus_txt_data/
```

At last, run the script from the terminal:

```{code-block} bash
python s5.19_use_stanza-XML.py
```


### Annotating textual data from `.txt` files into verticalised XML format
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.20_use_stanza-vrt.py
:name: s5-20
:caption: Script `[s5.20]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.20_use_stanza-vrt.py)
:linenos:
:lines: 20-
```

#### How to use script `[s5.20]`{octicon}`repo-template;1em;sd-text-success`
Copy/download the file `s5.20_use_stanza-vrt.py` inside the folder where the data to be annotated (in `.txt` format) resides; then browse inside the folder through the terminal, e.g.

```{code-block} bash
cd Downloads/corpus_txt_data/
```

At last, run the script from the terminal:

```{code-block} bash
python s5.20_use_stanza-vrt.py
```

### Example of data extracted with script `[s5.19]`
```{code-block} xml
:name: e5-28
:caption: Example `[e5.28]` 
:linenos:

<?xml version='1.0' encoding='UTF-8'?>
<text>
  <s n="1">
    <w pos="CCONJ" lemma="and">And</w>
    <w pos="ADV" lemma="now">now</w>
    <w pos="ADP" lemma="for">for</w>
    <w pos="PRON" lemma="something">something</w>
    <w pos="ADV" lemma="completely">completely</w>
    <w pos="ADJ" lemma="different">different</w>
    <c pos="PUNCT" lemma="!">!</c>
  </s>
</text>

```


[^sn1]: `CATLISM, 290-295`
[^sn2]: https://stanfordnlp.github.io/stanza/pos.html#description