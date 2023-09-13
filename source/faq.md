# {fa}`circle-question` FAQs

## How do I cite your work?
When using materials from this online compendium you may wish to cite both the book and the compendium itself - or alternatively the scripts only if you are only using the latter ones.

**Citing the book**  
  
> Di Cristofaro, Matteo. Corpus Approaches to Language in Social Media. New York: Routledge, 2023. https://doi.org/10.4324/9781003225218.

:::{dropdown} BibTeX
```bib
@book{di_cristofaro_corpus_2023,
	address = {New York},
	title = {Corpus {Approaches} to {Language} in {Social} {Media}},
	isbn = {978-1-00-322521-8},
	publisher = {Routledge},
	author = {Di Cristofaro, Matteo},
	year = {2023},
	doi = {10.4324/9781003225218},
}
```
:::

**Citing the online compendium**  

> Di Cristofaro, Matteo. ‘Catlism/Catlism.Github.Io: V1.0.0’. Zenodo, 12 September 2023. https://doi.org/10.5281/zenodo.8338243.

:::{dropdown} BibTeX
```bib
@software{matteo_di_cristofaro_2023_8338243,
  author       = {Matteo Di Cristofaro},
  title        = {{catlism/catlism.github.io: v1.0.0}},
  month        = sep,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {v1.0.0},
  doi          = {10.5281/zenodo.8338243},
  url          = {https://doi.org/10.5281/zenodo.8338243}
}
```
:::

**Citing the scripts**

> Di Cristofaro, Matteo. ‘Catlism/Catlism_scripts: V1.0.0’. Zenodo, 12 September 2023. https://doi.org/10.5281/zenodo.8338207.

:::{dropdown} BibTeX
```bib
@software{matteo_di_cristofaro_2023_8338207,
  author       = {Matteo Di Cristofaro and
                  catlism},
  title        = {catlism/catlism\_scripts: v1.0.0 Initial release},
  month        = sep,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {v1.0.0},
  doi          = {10.5281/zenodo.8338207},
  url          = {https://doi.org/10.5281/zenodo.8338207}
}
```
:::

## Can I use/modify script X for my own purposes/publication?
Absolutely. All scripts are released through [GNU GPLv3 open source licence](https://choosealicense.com/licenses/gpl-3.0/) meaning that you may **use** (even for commercial/patent/private use), **(re)distribute**, and **modify** them **as long as you acknowledge the source and distribute the modified version using the same GPLv3 licence**.
In doing so, please use the citations described in [How do I cite your work?](#how-do-i-cite-your-work).

## A script/command is not working, can you help?
I can try {far}`face-smile-beam`. Send an email to `catlism[at]infogrep[dot]it` describing the issue, along with the following details:

- the operating system you are using;
- the Python version you are using;
- the version of the involved modules (in a script, these are the names following the occurrences of `import`); 
- whether you are using Conda or any other virtual environment;
- if possible, a sample of the data you are trying to process would be helpful

## I have found an error in a script, can you fix it?
I'd be glad to; submit the problem in one of the two following ways:

1. File an issue in the [repository issue tracker](https://github.com/catlism/catlism.github.io/issues) (a Github account is required)
2. Send an email with a description of the problem and a link to the relevant page(s) to `catlism[at]infogrep[dot]it`, along with the following details:
	- the operating system you are using;
	- the Python version you are using;
	- the version of the involved modules (in a script, these are the names following the occurrences of `import`);
	- whether you are using Conda or any other virtual environment
	- if possible, a sample of the data you are trying to process would be helpful


## I have found an error in a webpage, can you fix it?
I'd be glad to; submit the problem in one of the two following ways:

- File an issue in the [repository issue tracker](https://github.com/catlism/catlism.github.io/issues) (a Github account is required)
- Send an email with a description of the problem and a link to the relevant page(s) to `catlism[at]infogrep[dot]it`

## I have found an error in the book, can you add it to the [Errata](from_the_book/errata.md) section?
Certainly. Send the error and the page on which it appears via mail to `catlism[at]infogrep[dot]it`.

## I have feedback/suggestions, how can I share it/them with you?
The quickest way is to send me an email at `catlism[at]infogrep[dot]it`.  
Thanks {far}`face-smile`

## Can I download the online compendium for local/offline use?
Sure! A .zip file containing a 1:1 copy of the latest release of the compendium (all the pages plus all the scripts) can be downloaded through the button below.
```{eval-rst}
You are currently reading release |version| |release|.
```



```{button-link} https://github.com/catlism/catlism.github.io/archive/refs/tags/v0.0.0.zip
:color: info
:expand:
{octicon}`download;1.5em` Download the latest release of the compendium
```

Unzip the contents (be sure to preserve the folders and subfolders structure) and open the file `index.html` with your favourite browser.  Older releases are  available in the ["Releases" page on Github](https://github.com/catlism/catlism.github.io/releases).


## Can I download all the scripts (and only the scripts) at once?
Sure! All the scripts are hosted on a [separate Github repository](https://github.com/catlism/catlism_scripts/), and are automatically included inside the online compendium whenever changes are made. The latest release can be downloaded through the button below; older releases are available in the [Github repository "Releases" page](https://github.com/catlism/catlism_scripts/releases).

```{button-link} https://github.com/catlism/catlism_scripts/archive/refs/tags/v1.0.0.zip
:color: info
:expand:
{octicon}`download;1.5em` Download the latest release of the scripts
```


## The website looks too dark!
You may click on the {fas}`moon` at the top of the website to switch off the "dark" mode and enable the "light" mode {fas}`sun`
