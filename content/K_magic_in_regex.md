Title: \K magic in regex
Date: 2019-08-08 03:14
Category: Development
Tags: perl,regex
Authors: Ace Fei


[TOC]


First of all, Let us see a question, how to get `123 789` from the string `abc: 123 def 456 ghi: 789` by shell one liner.

The elegant way I can figure out is to use **lookbehind assertion** `(?<=...)`.
```
$echo "abc: 123 def 456 ghi: 789" | grep -Po '(?<=:\s)\d+'
123
789
```

However, the string is changed to `abc: 123 def 456 ghi:  789` with multiple spaces after `:`,  **lookbehind assertion** won't work in this case, as it only supports fixed length pattern.
```
$echo "abc: 123 def 456 ghi: 789" | grep -Po '(?<=:\s+)\d+'
grep: lookbehind assertion is not fixed length
```

Now we just need to a small change, to use `\K` instead of `(?<=...)`
```
$echo "abc: 123 def 456 ghi: 789" | grep -Po ':\s*\K\d+'
123
789
```

### Further reading
[Understanding \G and \K in regex](https://stackoverflow.com/questions/28842979/understanding-g-and-k-in-regex)
