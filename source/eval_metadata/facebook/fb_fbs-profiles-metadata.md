# Facebook metadata for profiles

```{hint}
Consult [](../index.md) for an explanation of the evaluation system included in the column *Int. Data*.
```

## Data points from `facebook-scraper` for profiles[^sn1]
#### *Table 5.22* {octicon}`git-pull-request;1em;sd-text-warning`
[^sn1]: `CATLISM, 233-235`

| Attribute name    | Type   | Int. Data | Description                                                                                                                          |
|-------------------|--------|-----------|--------------------------------------------------------------------------------------------------------------------------------------|
| `top_post.*`        | array  | [SID]     | A JSON object containing details about the “top post” of the profile; it uses the structure for posts (see [Table 5.21](./facebook-posts-metadata.md#table-5-21))               |
| `Friend_count`      | number | SID       | The total number of friends                                                                                                          |
| `Follower_count`    | number | SID       | The total number of followers                                                                                                        |
| `Following_count`   | number | SID       | The total number of accounts the user follows                                                                                        |
| `cover_photo_text`  | string | SID       | Caption for the user’s cover photo                                                                                                   |
| `cover_photo`       | string | PID       | Direct link to the user’s cover photo                                                                                                |
| `profile_picture`   | string | PID       | Direct link to the user’s profile photo                                                                                              |
| `id`                | string | PID       | Unique ID of the account                                                                                                             |
| `Name`              | string | SID       | Full name, as specified by the user                                                                                                  |
| `Work`              | string | SID       | A text-formatted version of the list of works (workplace, year, description) as inserted by the user                                 |
| `Education.*`       | array  | [SID]       | A dictionary containing key:values for each item the user included in the field “Education”, e.g. “University” : “BA in Linguistics” |
| `Places lived.*`    | array  | [SID]     | An array containing JSON objects, each one describing the specified locations                                                        |
| `Places lived.link` | string | PID       | The link to the location’s Facebook page                                                                                             |
| `Places lived.text` | string | PID       | The textual description of the location, e.g. “London, UK”                                                                           |
| `Places lived.type` | string | PID       | Textual description of the type of location, e.g. “Current town/city” or “Home town”                                                 |
| `Contact Info`      | array  | [SID]       | A JSON object containing key:values for each item, e.g. “Address” : “221B Baker Street, London”                                      |
| `Basic info`        | string | SID       | Text containing details – if inserted by the user – such as date of birth, gender, languages                                         |
| `Family members`    | string | SID       | Text containing the names (as they appear on Facebook) of users the user has tagged as family members                                |
| `About`             | string | SID       | A string containing free text as inserted by the user in the “About” field                                                           |
| `Life events`       | string | SID       | A text-formatted version of the list of life events inserted by the user                                                             |
| `Favourite quotes`  | string | SID       | A text-formatted version of the list of quotes as inserted by the user                                                               |
| `Other names`       | array  | [SID]       | A dictionary containing key:values for each item, e.g. “Nickname” : “Zimmy”                                                          |
| `Relationship`      | string | SID       | A text-formatted version of the current relationship, e.g. “Married with X since DD MONTH YYYY”                                      |