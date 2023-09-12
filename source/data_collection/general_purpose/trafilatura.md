# Trafilatura

Data collection from websites can be obtained using the corpus-linguistics-oriented [`Trafilatura`](https://trafilatura.readthedocs.io).  
Options and arguments for the tool can be found in the [official documentation](https://trafilatura.readthedocs.io).


## Installing the tool[^sn1]
```{code-block} bash
:name: c5-04
:caption: Command `[c5.04]` {octicon}`git-pull-request;1em;sd-text-warning`

pip install trafilatura
```

:::{dropdown} {octicon}`video;2em` `[c5.04]`
```{eval-rst}
.. asciinema:: 607000

```
:::

```{code-block} bash
:name: c5-07
:caption: Command `[c5.07]` {octicon}`stop;1em;sd-text-danger`
pip install gooey
```

## Using the tool[^sn2]

```{code-block} bash
:name: c5-05
:caption: Command `[c5.05]`

trafilatura
```

```{code-block} bash
:name: c5-06
:caption: Command `[c5.06]`

trafilatura_gui
```

```{code-block} python
:name: c5-08
:caption: Command `[c5.08]`

trafilatura -i list.txt -o txtfiles
```

:::{dropdown} {octicon}`video;2em` `[c5.09]`
In the video the argument `-vv` is used to print `trafilatura` messages to the console; otherwise no messages will be printed if the operation succeeds.

```{eval-rst}
.. asciinema:: 607188

```
:::


```{code-block} python
:name: c5-09
:caption: Command `[c5.09]`

trafilatura --xml -i list.txt -o xmlfiles
```

:::{dropdown} {octicon}`video;2em` `[c5.09]`
In the video the argument `-vv` is used to print `trafilatura` messages to the console; otherwise no messages will be printed if the operation succeeds.

```{eval-rst}
.. asciinema:: 607189

```
:::

```{code-block} python
:name: c5-10
:caption: Command `[c5.10]`

 trafilatura --xml --formatting --link --images --inputdir localHTML -o xmlfiles
```

:::{dropdown} {octicon}`video;2em` `[c5.10]`
In the video the argument `-vv` is used to print `trafilatura` messages to the console; otherwise no messages will be printed if the operation succeeds.

```{eval-rst}
.. asciinema:: 607190

```
:::

## Example of data extracted with Trafilatura[^sn3]

```{code-block} xml
:name: e5-04
:caption: Example `[e5.04]`
:linenos:

<doc sitename="The Guardian" title="‘Mind-blowing’: Ai-Da becomes first robot to paint like an artist" author="Caroline Davies" date="2022-04-04" source="https://www.theguardian.com/technology/2022/apr/04/mind-blowing-ai-da-becomes-first-robot-to-paint-like-an-artist" hostname="theguardian.com" excerpt="AI algorithms prompt robot to interrogate, select, decision-make to create a painting" categories="Technology" tags="Robots,Technology,Artificial intelligence (AI),Art,Computing,Consciousness" fingerprint="ETYg93u3aaAiAbJW0sOWW472T+4=">
    <main>
        <p>Brush clamped firmly in bionic hand, Ai-Da’s robotic arm moves slowly, dipping in to a paint palette then making slow, deliberate strokes across the paper in front of her.</p>
        <p>This, according to Aidan Meller, the creator of the world’s first ultra-realistic humanoid robot, Ai-Da, is “mind-blowing” and “groundbreaking” stuff.</p>
        [...]
        <graphic src="https://i.guim.co.uk/img/media/bce15258910b44eefb4855a9cdd5f87d76725d59/0_168_5068_3042/master/5068.jpg?width=620&amp;quality=85&amp;fit=max&amp;s=e724f5ca70f9995e856648c2556a7637" alt="Ai-Da takes more than five hours to make a painting, but no two works are exactly the same." />
        <p>
            With rapidly developing
            <ref target="https://www.theguardian.com/technology/artificialintelligenceai">artificial intelligence</ref>
            , growing accessibility to super computers and machine learning on the up, Ai-Da – named after the computing pioneer Ada Lovelace – exists as a “comment and critique” on rapid technological change.
        </p>
        <graphic src="https://i.guim.co.uk/img/media/c52e761d528cc2685705ba8a19956155389ccd5b/0_8_4480_5600/master/4480.jpg?width=380&amp;quality=85&amp;fit=max&amp;s=36006bc6f77064e854f4c2301804bc78" alt="Ai-Da Robot with creator Aidan Meller." />
    </main>
    <comments />
</doc>
```

[^sn1]: `CATLISM, 156`
[^sn2]: `CATLISM, 156-157; 159`
[^sn3]: `CATLISM, 158-159`