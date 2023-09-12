# BeautifulSoup

Data collection can be achieved through the creation of *ad-hoc* scripts employing `BeautifulSoup`, a Python library that coordinates several modules and further libraries for "pulling data out of HTML and XML files" {cite}`richardson_beautiful_2023`.  
Scripts included here (and in the book) represent a simplified version of the ones included in {cite}`bondi_morethesiscorpus_2023`.

## Extracting the data
### Extract links from HTML pages[^sn1]

```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.01-collect_links.py
:name: s5-01
:caption: Script `[s5.01]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.01-collect_links.py)
:linenos:
:lines: 20-
```

### Download HTML pages[^sn2]
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.02a-collect_pages.py
:name: s5-02a
:caption: Script `[s5.02a]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.02a-collect_pages.py)
:linenos:
:lines: 20-
```

### Use `requests` in script `[s5.02a]`[^sn3]
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.02b-collect_pages__native.py
:name: s5-02b
:caption: Script `[s5.02b]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.02b-collect_pages__native.py)
:linenos:
:lines: 20-
```

### Extract metadata from the downloaded HTML pages[^sn4]
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.03-extract_metadata.py
:name: s5-03
:caption: Script `[s5.03]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.03-extract_metadata.py)
:linenos:
:lines: 20-
```

### Download PDF files linked in HTML pages[^sn5]
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.04-download_pdf.py
:name: s5-04
:caption: Script `[s5.04]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.04-download_pdf.py)
:linenos:
:lines: 20-
```

### Extract the contents of PDF files as plain-text[^sn6]
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.05-extract_pdf-textract.py
:name: s5-05
:caption: Script `[s5.05]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.05-extract_pdf-textract.py)
:linenos:
:lines: 20-
```

### Create an XML corpus combining the metadata from HTML pages and the contents of PDF files[^sn7]
```{rli} https://github.com/catlism/catlism_scripts/raw/main/s5.06-create_XML.py
:name: s5-06
:caption: Script `[s5.06]` [{octicon}`download;1em;sd-text-primary`](https://github.com/catlism/catlism_scripts/raw/main/s5.06-create_XML.py)
:linenos:
:lines: 20-
```

### Basic structure of the metadata table included in [MoreThesis](https://morethesis.unimore.it/) pages[^sn8]

```{code-block} html
:name: e5-08
:caption: Example `[e5.08]`
:linenos:

<table border="3" cellpadding="5" cellspacing="5" class="metadata_table">
    <tbody>
        <tr>
            <th width="30%">Tipo di tesi</th>
            <td width="70%">TYPE OF THESIS</td>
        </tr>
        <tr>
            <th>Autore</th>
            <td>SURNAME, NAME</td>
        </tr>
        [...]
        <tr>
            <th>Commissione</th>
            <td>
                <table>
                    <tbody>
                        <tr>
                            <th align="left">Nome Commissario</th>
                            <th align="left">Qualifica</th>
                        </tr>
                        <tr>
                            <td align="left">SURNAME NAME</td>
                            <td align="left">Primo relatore</td>
                        </tr>
                        <tr>
                            <td align="left">SURNAME NAME</td>
                            <td align="left">Coordinatore Dott Ric</td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
        <tr>
            <th>Parole chiave</th>
            <td>
                <ul>
                    <li>KEYWORD1
                    </li>
                    <li>KEYWORD2
                    </li>
                    <li>KEYWORD3
                    </li>
                    <li>KEYWORD4
                    </li>
                    <li>KEYWORD5
                    </li>
                </ul>
            </td>
        </tr>
        [...]
        <th>File</th>
        <td>
            <table border="2" cellpadding="3" cellspacing="3">
                <tbody>
                    [...]
                    <tr align="center">
                        <td> </td>
                        <td align="left"><a
                                href="/theses/available/etd-NNNNNNNN-NNNNNN/unrestricted/FILENAME.pdf"><b>FILENAME.pdf</b></a>
                        </td>
                        <td>5.93 Mb</td>
                        <td bgcolor="#cccccc">00:27:28</td>
                        <td>00:14:07</td>
                        <td bgcolor="#cccccc">00:12:21</td>
                        <td>00:06:10</td>
                        <td bgcolor="#cccccc">00:00:31</td>
                    </tr>
                    [...]
                </tbody>
            </table>
        </td>
    </tbody>
</table>
```

[^sn1]: `CATLISM, 162-163`
[^sn2]: `CATLISM, 164-166`
[^sn3]: `CATLISM, 166`
[^sn4]: `CATLISM, 166; 168-171`
[^sn5]: `CATLISM, 174-175`
[^sn6]: `CATLISM, 176`
[^sn7]: `CATLISM, 177-180`
[^sn8]: `CATLISM, 171-173`