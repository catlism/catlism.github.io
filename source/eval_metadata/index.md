# Metadata evaluation

As results (traces) of "the types of interactions the platform allows users to perform"[^sn2], metadata data points play a central role in the *broad view of corpus approaches* the book and this compendium propose.  
Consequently this section includes **interactive versions of the metadata evaluation tables** included in the book. The evaluation system in based on {cite:t}`gigliettoOpenLaboratoryLimits2012`, expanding the original framework to include further nuances and options. The aim is to provide "a simple categorisation meant to help [researchers] quickly decide whether a piece of information may be relevant"[^sn2] to their efforts by taking into account:

- what each data point ***represents*** inside the '*raw*' data (while bearing in mind that data is always 'cooked' and never 'raw', cf. {cite:t}`bowkerDataFlakesAfterword2013`);
- the ***analytical purpose*** each data point may have for the social sciences 

The evaluation system is described further below, and each table contains the column `Int. Data` where "the labels AID, SID, PID, and CID are used to refer to one or more of the four types of interactions data [...]. Data points containing a JSON object, an array of JSON objects, or a list of strings are assigned a label in square brackets (e.g. [SID]) to evaluate the array or object itself and not its contents – which may belong to different types of interaction data."[^sn3] 


> - **Audience interaction data** (AID) is a quantitative description of the amount of interactions involving access to the content. It is a measure of how many accesses the content was subjected to but does not indicate what users did once the content was accessed (this may not be true for the content creator, who may have access to additional non-public metrics). The word *access* is preferred over other potential candidates (e.g. *exposure*) in order to exclude ambiguous scenarios: in the case of YouTube, if the ‘autoplay’ option is enabled, the platform will automatically load a new video once the current video is finished, with the new one either selected by the user (e.g. as part of a playlist or video queue) or by YouTube algorithms. In this case the user may not be exposed to the content (e.g. they may have left YouTube running while they are not in front of the PC), but the interaction of accessing the content is stored by the platform nonetheless.
> - **Social interaction data** (SID) describes those data points that measure or describe deliberate actions undertaken by either the creator of the content or a user interacting with it; it is the result of a human decision to leave a digital trace in relation to the content. Comments, replies, likes, reshares, photos, videos, are all examples of social interaction data.
> - **Platform interaction data** (PID) are those data points resulting from the platform (i.e. the computer or the server hosting the content) interacting with the contents uploaded/posted by a user or with other data points generated by a computer. Metadata falling under this category measures operations among digital devices and tools, such as the unique ID assigned by the platform to newly created content, used, for example, in Twitter data to link a reply to a tweet with the tweet it replies to (see [Twitter metadata table](../eval_metadata/twitter/tw_snscrape-metadata.md)).
> - **Collection interaction data** (CID) contains information resulting from the actions of collecting the data. It is the case of the data point `_type` included by [`snscrape`] when scraping data from social media platforms [...] or the metadata containing information on the user who worked on spreadsheets created with Excel or LibreOffice Calc and included in the file.[^sn1]

## Contents
```{toctree}
facebook/index.md
instagram/index.md
twitter/index.md
youtube/index.md
```

[^sn1]: `CATLISM, 50`
[^sn2]: `CATLISM, 49`
[^sn3]: `CATLISM, 51`