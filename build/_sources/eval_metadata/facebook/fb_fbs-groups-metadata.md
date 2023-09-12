# Facebook metadata for groups

```{hint}
Consult [](../index.md) for an explanation of the evaluation system included in the column *Int. Data*.
```

## Data points from `facebook-scraper` for groups[^sn1]
#### *Table 5.23* {octicon}`git-pull-request;1em;sd-text-warning`
[^sn1]: `CATLISM, 236`

| Attribute name     | Type   | Int. Data   | Description                                                                                                |
|--------------------|--------|-------------|------------------------------------------------------------------------------------------------------------|
| `id`                 | string | PID         | Unique ID of the group, as assigned by Facebook                                                            |
| `name`               | string | SID         | Textual name of the group as assigned by its administrators                                                |
| `type`               | string | PID + SID   | Textual label identifying the accessibility of the group, e.g. “Private group”                             |
| `members`            | number | SID         | Total number of members at the time of scrape                                                              |
| `about`              | string | SID         | Textual description of the group, as assigned by its administrators                                        |
| `admins.*`           | array  | [PID + SID] | Array of JSON objects, each one containing details about the users with administrative rights in the group |
| `admins.name`        | string | SID         | Text string full name of the administrator                                                                 |
| `admins.link`        | string | PID         | Link to the administrator’s profile page                                                                   |
| `other_members.*`    | array  | [PID + SID] | Array of JSON objects, each one containing details about the non-administrator members of the group        |
| `other_members.name` | string | SID         | Text string full name of the member                                                                        |
| `other_members.link` | string | PID         | Link to the member’s profile page                                                                          |