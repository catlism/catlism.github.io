# Text normalisation[^sn1]

```{hint}
In addition to the procedures documented below, normalisation of texts may include segmenting pieces of text where two or more words are grouped together; in such cases the procedure documented for the treatment of [hashtags](hashtags.md) may be employed.
```

Normalisation of text files (`.txt` as well as `.xml`) can be achieved through [VARD](https://ucrel.lancs.ac.uk/vard/about/) {cite:p}`baron_vard_2008`, an interactive tool (written in Java) to conduct semi-automated normalisation. Originally designed for Early Modern English spelling variation, it can be adapted to (virtually) any type of variations through ready-made vocabularies (e.g. the online-language specific [Twitter setup](https://ucrel.lancs.ac.uk/vard/download/)) or by creating a custom dictionary trained on a batch of the files to be normalised.  
Further options and a user guide can be found in the tool [official documentation](https://ucrel.lancs.ac.uk/vard/userguide/).

## Using the tool

:::{figure-md} fig5-8
:class: figure

<img src="figures/Figure5.8.jpg" alt="Figure 5.8 Example of recognised spelling variants in VARD" class="bg-primary mb-1" width="400px">

*Figure 5.8* Example of recognised spelling variants in VARD
:::

:::{figure-md} fig5-9
:class: figure

<img src="figures/Figure5.9.jpg" alt="Figure 5.9 Example of unrecognised spelling variants in VARD" class="bg-primary mb-1" width="400px">

*Figure 5.9* Example of unrecognised spelling variants in VARD
:::

## Example of normalised data in XML format generated with VARD

```{code-block} xml
:name: e5-21
:caption: Example `[e5.21]`

<normalised orig="Plz" auto="false">Please</normalised>pick up<normalised orig="moooore" auto="false">more</normalised>steak<normalised orig="n" auto="false">and</normalised>pretzels thank<normalised orig="u" auto="false">you</normalised><normalised orig="luv" auto="false">love</normalised><normalised orig="u" auto="false">you</normalised> mommy
```

[^sn1]: `CATLISM, 274-278`