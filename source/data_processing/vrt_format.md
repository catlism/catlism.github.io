# Verticalised (.vrt) format

Resembling - and making use of - XML syntax, the *verticalised* format (VRT, VeRticalised text) is a "token-oriented columnar text format"[^sn1] where the `tab` character (<kbd>Tab ↹</kbd>) is used to separate a token from its POS and lemma details (and potentially, any further annotation detail as well). It is the default accepted format for the [IMS Corpus Workbench](https://cwb.sourceforge.io/) ({cite:p}`evertTwentyfirstCenturyCorpus2011`) as well as a number of other corpus tools (e.g. SketchEngine). 

In example `[e5.29]` (showing a sample of the format) the symbol `→` is the graphical representation of the `tab` character.

```{code-block} xml
:name: e5-29
:caption: Example `[e5.29]` 
:linenos:

<?xml version='1.0' encoding='UTF-8'?>
<text>
    <s n="1">
        And→and→CCONJ
        now→now→ADV
        ,→,→PUNCT
        for→for→ADP
        something→something→PRON
        completely→completely→ADV
        different→different→ADJ
        !→!→PUNCT
    </s>
</text>

```

[^sn1]: https://www.kielipankki.fi/development/korp/corpus-input-format/