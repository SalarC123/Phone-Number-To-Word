# Phone-Number-To-Word

## What Does It Do?

This **Python** code takes any phone number in the format of either *111-222-3333, 1112223333,* or *111.222.3333* and converts the numbers after the area code into a word. This can be helpful for companies wanting to acquire phone numbers which spell out words that relate to their company and are easy to remember.

**For Example:**
![1800flowers](https://user-images.githubusercontent.com/68439561/89322413-ca1bd600-d649-11ea-8679-5381f2d4b19c.jpg)

## How Do I Use It?

`reversephone('123.883.6745','7-0')`

When you call the function, put your phone number as the *first* argument (keeping in mind that it has to be in one of the mentioned formats above) and can not include a 0 or 1 because they do not correlate to any letters on the digit pad

![06phone-pad](https://user-images.githubusercontent.com/68439561/89323622-993ca080-d64b-11ea-9296-806302028877.png)

In the *second* argument, put one of these:

```
'7-0'  -->   for one seven letter word
'3-4'  -->   for a three letter word followed by a four letter word
'4-3'  -->   for a four letter word followed by a three letter word
'2-5'  -->   for a two letter word followed by a five letter word
'5-2'  -->   for a five letter word followed by a two letter word
'6-1'  -->   for any six letter word followed by a single letter
'1-6'  -->   for any single letter followed by a six letter word
```

The code will not return nonsense because every word that is returned is checked through an english dictionary
