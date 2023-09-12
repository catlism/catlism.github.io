# Instagram metadata for comments
```{hint}
Consult [](index.md) for an explanation of the evaluation system included in the column *Int. Data*.
```


## Data points from `instaloader` for comments[^sn1]
#### *Table 5.18*
[^sn1]: `CATLISM, 218`


| Attribute name               | Type   | Int. Data | Description                                                                                                |
|-----------|-----------|-----------|-----------------------------------------|
| `node.id`                    | number | PID       | Unique ID of the comment                                                                                   |
| `node.created_at`            | number | SID + PID | Timestamp in Unix time format of the creation date and time of the comment                                 |
| `node.text`                  | string | SID       | Plain-text content of the comment                                                                          |
| `node.owner.*`               | object | [SID]     | A JSON object containing details about the author of the comment                                           |
| `node.owner.id`              | number | PID       | Unique ID of the account                                                                                   |
| `node.owner.is_verified`     | bool   | SID       | Whether the account is verified or not                                                                     |
| `node.owner.profile_pic_url` | string | PID       | Direct URL to the account's profile image                                                                  |
| `node.owner.username`        | string | SID       | Plain-text version of the account's username                                                               |
| `node.likes_count`           | number | SID       | The number of likes the comment has received                                                               |
| `node.answers.*`             | array  | [SID]     | An array of JSON objects containing the replies to the comments -- each one structured as the main comment |
