# Analysing crypto-drug market fora

> The case study [utilised] in this section is based on the research conducted at Swansea University Department of Applied Linguistics under the supervision of Prof. Nuria Lorenzo-Dus and in collaboration with the Global Drug Policy Observer[^sn2] (GDPO) as part of the project ‘Trust in Crypto-Drug Markets’ funded by EPSRC–CHERISH-DE (Principal Investigator: Prof. Nuria Lorenzo-Dus). Outputs from the research are published in {cite:p}`horton-eddison_hard_2017`, {cite:p}`di_cristofaro_corpus_2017`, and {cite:p}`lorenzo-dus_i_2018`, which served as basis for the [contents described].[^sn1]

:::{card} Sample selection of HTML files from Silk Road 1 and 2[^sn3] 
A sample selection of HTML files from Silk Road 1 and 2, sourced from [the Darknet Market Archives](https://gwern.net/dnm-archive) {cite:p}`branwen_dark_2015`, may be downloaded by clicking the button below. The file shown in the book is named `index.php?topic=101030.0`.

```{button-link} sr1_2_sample-files.zip
:color: info
:expand:
{octicon}`download;1.5em` Download sample of Silk Road 1 and 2 HTML files
```
:::



## Overall structure of a post in Silk Road 1[^sn4]
```{code-block} html
:name: e6-01
:caption: Example `[e6.01]` 
:linenos:

<div id="forumposts">
  <div class="windowbg">
    <span class="topslice"><span></span></span>
    <div class="post_wrapper">
      <div class="poster">
        <h4>
          <a href="[link to the user's profile]" title="View the profile of [USERNAME]">[USERNAME]</a>
        </h4>
        <ul class="reset smalltext" id="msg_[post ID]_extra_info">
          <li class="postgroup">[group to which the user belongs to]</li>
          <li class="stars">
            [this section includes links to the icons used to visualise the user's achievements]
          </li>
          <li class="postcount">Posts: [number of posts written by the user]</li>
          <li class="karma">Karma: +[number]/-[number]</li>
          <li class="profile">
            <ul>
              <li>
                <a href="[link to the user's profile]"><img src="[link to the user's profile image]" alt="View Profile"
                    title="View Profile" /></a>
              </li>
            </ul>
          </li>
        </ul>
      </div>
      <div class="postarea">
        <div class="flow_hidden">
          <div class="keyinfo">
            <div class="messageicon">
              <img src="[link to the icon used for the message]" alt="" />
            </div>
            <h5 id="subject_[post ID]">
              <a href="[link to the post]" rel="nofollow">[title of the post]</a>
            </h5>
            <div class="smalltext">
              &#171; <strong> on:</strong> [date on which the message was posted, in the format January 06, 2013, 03:29
              am &#187];
            </div>
            <div id="msg_[post ID]_quick_mod"></div>
          </div>
        </div>
        <div class="post">
          <div class="inner" id="msg_[post ID]">
            [text of the post]
          </div>
        </div>
      </div>
      <div class="moderatorbar">
        <div class="smalltext modified" id="modified_[post ID]"></div>
        <div class="smalltext reportlinks">
          <img src="http://dkn255hz262ypmii.onion/Themes/default/images/ip.gif" alt="" />
          Logged
        </div>
      </div>
    </div>
    <span class="botslice"><span></span></span>
  </div>
</div>
```

### Extracting the data from HTML pages to XML format[^sn5]
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s6.01_extract_XML_from_SR1-SR2.py
:name: s6-01
:caption: Script `[s6.01]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s6.01_extract_XML_from_SR1-SR2.py)
:linenos:
:lines: 20-
```

## Meta-representation of contents extracted in XML format through `[s6.01]` (Silk Road corpus)
```{code-block} xml
:name: e6-02
:caption: Example `[e6.02]` 
:linenos:

<?xml version='1.0' encoding='UTF-8'?>
<doc filename="FILENAME" id="UNIQUE_ID_FROM_FILENAME">
    <text title="TITLE" subforum_label="[SUBFORUM_LABEL]" subforum="FULL_NAME_OF_THE_SUBFORUM_SECTION" author="[USERNAME]" post_number="NUMBER" date_d="NUMBER" date_m="NUMBER" date_y="NUMBER" date_time="NUMBER">
        MESSAGE, INCLUDING A
        <url orig="ORIGINAL_HYPERLINK">
            URL
        </url>
        IN ITS CONTENTS
    </text>
```

## Meta-representation of the XML structure of the reference corpus (DPM corpus)[^sn6]
```{code-block} xml
:name: e6-03
:caption: Example `[e6.03]` 
:linenos:
<?xml version='1.0' encoding='UTF-8'?>
<text id="[UNIQUE_NUMERICAL_ID]" cqpyear="YYYY" cqpdescription="TITLE_OF_THE_REPORT">
    TEXTUAL CONTENT OF THE DOCUMENT
</text>
```

## Example of page from Silk Road 1 forum

:::{figure-md} fig6-1
:class: figure

<img src="figures/Figure6.1.jpg" alt="Figure 6.1 Example of a page collected from the Silk Road 1 forum" class="bg-primary mb-1" width="400px">

*Figure 6.1* Example of a page collected from the Silk Road 1 forum
:::

[^sn1]: `CATLISM, 314`
[^sn2]: www.swansea.ac.uk/gdpo/
[^sn3]: `CATLISM, 317`
[^sn4]: `CATLISM, 320-321`
[^sn5]: `CATLISM, 323-328`
[^sn6]: `CATLISM, 328`