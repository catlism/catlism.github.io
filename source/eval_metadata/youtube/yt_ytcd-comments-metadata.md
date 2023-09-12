# Youtube metadata for comments

```{hint}
Consult [](../index.md) for an explanation of the evaluation system included in the column *Int. Data*.
```

## Data points from `youtube-comment-downloader` for comments[^sn1]
#### *Table 5.29*
[^sn1]: `CATLISM, 262`

| Attribute name | Type | Int. Data | Description                                                                                                                                                                              |
|--------------------|----------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cid`                | string   | SID + PID     | The unique ID of the comment                                                                                                                                            |
| `text`               | string   | SID           | The plain-text format of the comment                                                                                                                                                     |
| `time`               | string   | CID           | When the comment was posted, relative to the collection date                                                                                                            |
| `author`             | string   | SID           | The name of the author of the comment                                                                                                                                                    |
| `channel`            | string   | PID           | The unique ID of the page of the user who wrote the comment                                                                                                                              |
| `votes`              | string   | SID           | The number of likes the comment has received                                                                                                                                             |
| `photo`              | string   | PID           | Direct link to the writer’s profile picture                                                                                                                                              |
| `heart`              | bool     | SID           | Whether the creator of the content that received the comment has “hearted” the comment (this is a function available to the content’s creator to show their appreciation of the comment) |
| `time_parsed`        | number   | SID           | The date and time on which the comment was posted                                                                                                                       |
