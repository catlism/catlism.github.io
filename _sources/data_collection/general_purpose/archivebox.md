# Archivebox
Data collection from websites can be obtained using [`Archivebox`](https://archivebox.io/).  
Options and arguments for the tool can be found in the [official documentation](https://github.com/ArchiveBox/ArchiveBox/wiki).


## Installing the tool[^sn1]

```{code-block} bash
:name: c5-01
:caption: Command `[c5.01]`

pip install archivebox
```

:::{dropdown} {octicon}`video;2em` `[c5.01]`
```{eval-rst}
.. asciinema:: 606990

```
:::

## Using the tool[^sn2]

```{code-block} bash
:name: c5-02
:caption: Command `[c5.02]`

archivebox init --setup
```

```{code-block} bash
:name: c5-03
:caption: Command `[c5.03]`

archivebox server
```

In the video, a local folder for storing `archivebox` settings and downloaded data is created through the command `mkdir archivebox_folder`, only available in Unix-like systems  ({fab}`linux` and {fab}`apple`).  
Windows user should instead employ `md archivebox_folder` ({fab}`windows`).  
Once `[c5.03]` is issued, it is possible to access the web application by browsing the address `htpp://127.0.0.1:8000` (as indicated in the CLI).

:::{dropdown} {octicon}`video;2em` `[c5.02-03]`
```{eval-rst}
.. asciinema:: 606999

```
:::

## Extracting the data[^sn3]

:::{figure-md} fig5-3
:class: figure

<img src="figures/Figure5.3.jpg" alt="Figure 5.3 Archivebox main page" class="bg-primary mb-1" width="400px">

*Figure 5.3* Archivebox main page
:::

:::{figure-md} fig5-4
:class: figure

<img src="figures/Figure5.4.jpg" alt="Figure 5.4 Archivebox URLs collection page" class="bg-primary mb-1" width="400px">

*Figure 5.4* Archivebox URLs collection page
:::

:::{figure-md} fig5-5
:class: figure

<img src="figures/Figure5.5.jpg" alt="Figure 5.5 Archivebox main page showing the list of collected web pages" class="bg-primary mb-1" width="400px">

*Figure 5.5* Archivebox main page showing the list of collected web pages
:::

[^sn1]: `CATLISM, 152`
[^sn2]: `CATLISM, 153`
[^sn3]: `CATLISM, 153-155`