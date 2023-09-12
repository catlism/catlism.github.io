# Using `conda`[^sn1]

Installation instructions for different operating systems may be found on [Miniconda official download page](https://docs.conda.io/en/latest/miniconda.html). Make sure you select the appropriate installation file for your Operating System and architecture (32 or 64 bit).

## Install `conda` (through Miniconda) on Linux {fab}`linux` {octicon}`repo-template;1em;sd-text-success`
The following CLI commands are from the [official documentation](https://docs.conda.io/projects/miniconda/en/latest/#quick-command-line-install).

```{code-block} bash
:name: c0-01
:caption: Command `[c0.01]`
:linenos:

mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

:::{dropdown} {octicon}`video;2em` `[c0.01]`
```{eval-rst}
.. asciinema:: 606981
```
:::

## `conda` basic commands

```{code-block} bash
:name: e4-01
:caption: Example `[e4.01]`

(base) catlism@debian:~$
```

```{code-block} bash
:name: c4-01
:caption: Command `[c4.01]`

conda create --name myenv
```

```{code-block} bash
:name: c4-02
:caption: Command `[c4.02]`

conda activate myenv
```

```{code-block} bash
:name: e4-02
:caption: Example `[e4.02]`

(myenv) catlism@debian:~$
```

```{code-block} bash
:name: c4-03
:caption: Command `[c4.03]`

conda deactivate
```

:::{dropdown} {octicon}`video;2em` `[c4.01-03]`
```{eval-rst}
.. asciinema:: 606982
```
:::

## Install `pip` through `conda`

```{code-block} bash
:name: c4-04
:caption: Command `[c4.04]`

conda install -c anaconda pip
```

:::{dropdown} {octicon}`video;2em` `[c4.04]`
```{eval-rst}
.. asciinema:: 606983
```
:::

[^sn1]: `CATLISM, 101`