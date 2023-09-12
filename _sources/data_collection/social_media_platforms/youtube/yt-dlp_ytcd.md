# Youtube

```{warning}
As of March 2023 the tool [`youtube-dl`](https://github.com/ytdl-org/youtube-dl/) (release `2021.12.17`) suggested in the book has a number of issues and cannot therefore be used to correctly download data from Youtube.  
The commands below make use of [`yt-dlp`](https://github.com/yt-dlp/yt-dlp), an alternative tool (forked from `youtube-dl` with fixed issues and additional options) whose basic usage is identical to `youtube-dl`. **Any command included in the book and using `youtube-dl` can be replicated with `yt-dlp` instead** - as done in the contents below.
```
Data collection from Youtube (and [more than 1,200 platforms - the same ones supported by `youtube-dl`](http://ytdl-org.github.io/youtube-dl/supportedsites.html)) can be obtained using [`yt-dlp`](https://github.com/yt-dlp/yt-dlp).  
Options and arguments for the tool can be found in the [official documentation](https://github.com/yt-dlp/yt-dlp/blob/master/README.md).  
  
```{note}
While `yt-dlp` supports the extraction of comments (`youtube-dl` does not have such option), this page currently follows the contents of the book, where comments are downloaded using [`youtube-comment-downloader`](https://github.com/egbertbouman/youtube-comment-downloader).  
**Future versions of the compendium will include options for downloading comments using `yt-dlp`**.
```



## Installing the tools[^sn1]
```{code-block} bash
:name: c5-28
:caption: Command `[c5.28]` {octicon}`git-pull-request;1em;sd-text-warning`

pip install yt-dlp
```

:::{dropdown} {octicon}`video;2em` `[c5.28]`
```{eval-rst}
.. asciinema:: 607195

```
:::

```{code-block} bash
:name: c5-30
:caption: Command `[c5.30]`

pip install youtube-comment-downloader
```

:::{dropdown} {octicon}`video;2em` `[c5.30]`
```{eval-rst}
.. asciinema:: 607196

```
:::

## Using the tools[^sn2]

```{code-block} python
:name: c5-29
:caption: Command `[c5.29]` {octicon}`git-pull-request;1em;sd-text-warning`

yt-dlp 'URL' --write-info-json --skip-download --write-annotations --write-description
```

```{code-block} python
:name: c5-32
:caption: Command `[c5.32]` {octicon}`git-pull-request;1em;sd-text-warning`

yt-dlp 'URL' --write-info-json --skip-download --write-subs --sub-langs LL --sub-format FORMAT
```


```{code-block} python
:name: c5-31
:caption: Command `[c5.31]` {octicon}`git-pull-request;1em;sd-text-warning`

youtube-comment-downloader --url "URL" --output FILE.jsonl
```

## Extracting the data
### Extract collected Youtube data (everything except comments) to XML format[^sn3]
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.13_youtube-dl_subs-to-XML.py
:name: s5-13
:caption: Script `[s5.13]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.13_youtube-dl_subs-to-XML.py)
:linenos:
:lines: 20-
```

#### How to use script `[s5.13]`{octicon}`repo-template;1em;sd-text-success`
Copy/download the file `s5.13_youtube-dl_subs-to-XML.py` inside the folder where the data downloaded through `ytp-dl` (e.g. through `c5.29` and `c5.32`) resides; then browse inside the folder through the terminal, e.g.

```{code-block} bash
cd Downloads/youtube_data/
```

At last, run the script from the terminal:

```{code-block} bash
python s5.13_youtube-dl_subs-to-XML.py
```

### Extract collected Youtube comments to XML format[^sn4]
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.14_youtube-comments_to_XML.py
:name: s5-14
:caption: Script `[s5.14]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.14_youtube-comments_to_XML.py)
:linenos:
:lines: 20-
```

## Example of data extracted with `[s5.13]`[^sn5]
```{code-block} xml
:name: e5-18
:caption: Example `[e5.18]`
:linenos:

<?xml version='1.0' encoding='UTF-8'?>
<text uploader="USERNAME" date="YYYYMMMDD" views="NUMBER" likes="NUMBER" title="TITLE_OF_THE_VIDEO" format="FORMAT_NAME" autocaption="TRUE_OR_FALSE">
  <p time="NUMBER" is_ac="TRUE_OR_FALSE">SUBTITLES LINE</p>
</text>
```

## Example of data extracted with `[s5.14]`[^sn6]
```{code-block} xml
:name: e5-19
:caption: Example `[e5.19]`
:linenos:

<?xml version='1.0' encoding='UTF-8'?>
<text id="TEXT_ID">
  <comment comment_id="UNIQUE_ID" comment_reply_to="UNIQUE_ID_OF_THE_COMMENT_OR_NA" username="USERNAME" votes="NUMBER" heart="TRUE_OR_FALSE" date_d="NUMBER" date_m="NUMBER" date_y="NUMBER" date_time="NUMBER">TEXTUAL CONTENT OF THE COMMENT</comment>
</text>
```

## Example of subtitle formats
### TTML format [^sn7]

```{code-block} xml
:name: e5-14
:caption: Example `[e5.14]`
:linenos:
<?xml version="1.0" encoding="utf-8"?>
<tt xml:lang="en" xmlns="http://www.w3.org/ns/ttml" xmlns:ttm="http://www.w3.org/ns/ttml#metadata" xmlns:tts="http://www.w3.org/ns/ttml#styling" xmlns:ttp="http://www.w3.org/ns/ttml#parameter" ttp:profile="http://www.w3.org/TR/profile/sdp-us">
    <head>
        <styling>
            <style xml:id="s1" tts:textAlign="center" tts:extent="90% 90%" tts:origin="5% 5%" tts:displayAlign="after" />
            <style xml:id="s2" tts:fontSize=".72c" tts:backgroundColor="black" tts:color="white" />
        </styling>
        <layout>
            <region xml:id="r1" style="s1" />
        </layout>
    </head>
    <body region="r1">
        <div>
            <p begin="00:00:09.870" end="00:00:16.110" style="s2">
                In light of recent events concerning newscasters
                <br />
                being lost in the fog of… memory.
            </p>
        </div>
    </body>
</tt>
```

### SRV format without auto-captioning[^sn8]

```{code-block} xml
:name: e5-15
:caption: Example `[e5.15]`
:linenos:
<?xml version="1.0" encoding="utf-8"?>
<timedtext format="3">
    <body>
        <p t="9870" d="6240">In light of recent events concerning newscasters
being lost in the fog of… memory.</p>
        <p t="16110" d="4340">It may be pertinent to ask:
can we trust the news media?</p>
    </body>
</timedtext> 
```
### SRV format with auto-captioning[^sn9]
```{code-block} xml
:name: e5-16
:caption: Example `[e5.16]`
:linenos:

<?xml version="1.0" encoding="utf-8"?>
<timedtext format="3">
    <head>
        <ws id="0" />
        <ws id="1" mh="2" ju="0" sd="3" />
        <wp id="0" />
        <wp id="1" ap="6" ah="20" av="100" rc="2" cc="40" />
    </head>
    <body>
        <w t="0" d="957600" id="1" wp="1" ws="1" />
        <p t="1040" d="3360" w="1">
            <s ac="255">welcome</s>
            <s t="320" ac="255"> to</s>
            <s t="560" ac="255"> super</s>
            <s t="799" ac="255"> mario</s>
            <s t="1040" ac="255"> bros</s>
            <s t="1280" ac="255"> chaos</s>
        </p>
        <p t="2710" d="1690" w="1" a="1"></p>
        <p t="2720" d="2960" w="1">
            <s ac="255">edition</s>
            <s t="320" ac="255"> enjoy</s>
            <s t="719" ac="255"> the</s>
            <s t="800" ac="255"> peaceful</s>
            <s t="1199" ac="255"> music</s>
            <s t="1520" ac="255"> while</s>
        </p>
    </body>
</timedtext>
```

[^sn1]: `CATLISM, 247`
[^sn2]: `CATLISM, 247;254;263`
[^sn3]: `CATLISM, 264-269`
[^sn4]: `CATLISM, 269-272`
[^sn5]: `CATLISM, 264`
[^sn6]: `CATLISM, 264`
[^sn7]: `CATLISM, 252-253`
[^sn8]: `CATLISM, 253`
[^sn9]: `CATLISM, 253-254`