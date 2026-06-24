# Using the online compendium

```{important}
Descriptions and further details for scripts and code originally available in the book are left out of this compendium. Scripts and code exclusive to this online compendium are fully described and detailed in each relevant page/section.  
A number of answers to common questions are included in the [{fa}`circle-question` FAQs](faq.md) section.
```

Contents in the site are organised thematically, employing a structure somewhat different from the one adopted in the book that will - through updates and new contents - make this website a standalone resource for the ***broad view of corpus approaches*** the volume proposes.  
All scripts, commands, and examples are labelled according to the format employed in the book - with the syntax `[sX.YZ]`, `[cX.YZ]`, and `[eX.YZ]` respectively. `X` indicates the number of the book chapter where the content appears, while `YZ` is a progressive number; contents only included in this online compendium are marked with `X` equal to `0` - e.g. [`[c0.01]`](./setup_env/conda.md#c0-01)
  
Readers reaching the site from the volume *Corpus Approaches to Language in Social Media* should consult the section [](./from_the_book/index.md).

## `asciinema` interactive videos
A number of commands included in the book are documented through [`asciinema`](https://asciinema.org/), an open source project that allows users to record and share terminal sessions through an **interactive replay of the CLI**, where **displayed contents can be selected and copied directly from the video**. Two details should be noted:
- when typing a **password no character is shown** (not either asterisks), as per CLI default behaviour - see e.g. [`[c5.02-03]`](./data_collection/general_purpose/archivebox.md#c5-02)
- typing the first few letters of a command or path and pressing the <kbd>Tab ↹</kbd> key will autofill the command/path name; this is used across all `asciinema` videos
  
"The choice of employing asciinema should let readers who have no experience with working through the CLI become acquainted with the type of interactions documented [in the book and in this compendium] by seeing the behaviour that each command produces"[^sn2], in line with the aims outlined in [](./on_scripts.md).

## Legend
Table below describes the meaning of the symbols used throughout the compendium.

| Symbol | Meaning |
| ------ | ------- |
| {octicon}`repo-template;2em;sd-text-success` | Indicates **additional** contents (commands, scripts, etc...) not included in the volume |
| {octicon}`git-pull-request;2em;sd-text-warning` | Indicates **updated** contents (commands, scripts, etc...); these differ from the version available in the book - an explanation of the difference is provided for each case |
| {octicon}`stop;2em;sd-text-danger` | Indicates **deprecated** contents (commands, scripts, etc...) available in the book but not longer working, and kept in the compendium for documentation purposes |
| {octicon}`download;2em;sd-text-primary` | Indicates **downloadable** contents (scripts or other files); clicking the icon will start the download |
| {octicon}`copy;2em` | Available in all code-blocks: clicking on this symbol will **copy the contents of the block into the clipboard** |
| {octicon}`link-external;2em;sd-text-primary` | Indicates a **link to an external content** |
| {octicon}`archive;2em;sd-text-primary` | Indicates a **link to a [preservation copy](./from_the_book/preservation_links.md) of an external content** |
| {octicon}`video;2em;` | Indicates an [**interactive `asciinema` video**](#asciinema-interactive-videos) |
| {fab}`linux` / {fab}`windows;2em;sd-text-primary` / {fab}`apple;2em` | Indicates a content only available/applicable to Linux ({fab}`linux;2em`), Windows ({fab}`windows;2em`) or macOS ({fab}`apple;2em;`). When **no symbol appears then the content is multiplatform**.  |

[^sn2]: `CATLISM, 100`