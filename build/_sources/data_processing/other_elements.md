# Other elements

Transformation of various elements (e.g. URLs, email addresses) from their original format into XML elements may be obtained by using specific regular expressions in conjunction with with script [`[s5.17]`](hashtags.md#s5-17). As noted in the volume

> while more efficient and safer options exist (i.e. the use of the `lxml` module to modify an existing XML file to avoid the deletion of elements that may result in a malformed structure), the advantage of this strategy is that it can be applied to any type of file (`.txt`, `.csv`, `.xml`, `.json`, `etc.`) and adapted to transform [any element] into any required syntax[^sn5] 

Each regular expression is complemented with a direct link to its respective interactive version of [RegExr](https://regexr.com/) ({cite:p}`skinner_regexr_2022`), the tool suggested in the book for the inspection and creation of regular expressions.

## Regular expression to capture usernames (e.g. `@matteodic`)[^sn1]
```{code-block} bash
:name: e5-24
:caption: Example `[e5.24]` 
:linenos:
(?<=^|\s)(@[\w.]+)(?<!\.)
```

```{button-link} https://regexr.com/7j6rf
:color: primary
:expand:
Inspect regular expression `[e5.24]` on RegExr
```

## Regular expression to capture simple URLs (e.g. `http://example.com` and `https://example.com`)[^sn2]
```{code-block} bash
:name: e5-25
:caption: Example `[e5.25]` 
:linenos:
http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+
```

```{button-link} https://regexr.com/7j6ro
:color: primary
:expand:
Inspect regular expression `[e5.25]` on RegExr
```

## Regular expression to capture complex URLs (e.g. simple URLs plus email addresses, `mailto:` links, URLs with optional parameters)[^sn3]
```{code-block} bash
:name: e5-26
:caption:  Example `[e5.26]` 
:linenos:

((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[.\!\/\\w]*))?)
```

```{button-link} https://regexr.com/7j6rr
:color: primary
:expand:
Inspect regular expression `[e5.26]` on RegExr
```

## Regular expression to capture cashtags (e.g. `$EUR`)[^sn4]
```{code-block} bash
:name: e5-27
:caption:  Example `[e5.27]` 
:linenos:

(?:^|\s)([\$]{1})(\w+)
```

```{button-link} https://regexr.com/7j6s1
:color: primary
:expand:
Inspect regular expression `[e5.27]` on RegExr
```


[^sn1]:  `CATLISM, 289`
[^sn2]:  `CATLISM, 289`
[^sn3]: Adapted from [https://blog.mattheworiordan.com/post/13174566389/url-regular-expression-for-links-with-or-without](https://blog.mattheworiordan.com/post/13174566389/url-regular-expression-for-links-with-or-without); `CATLISM, 289`
[^sn4]:  `CATLISM, 289`
[^sn5]: `CATLISM, 287`