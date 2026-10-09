---
tags: [lecture/L2]
---

# L2 Multi-Dimensional Arrays 逐字稿

> [!info] 本機 whisper 轉錄，==未經人工逐字校對==；英文術語有辨識誤差，正確用詞以整理稿為準。

- `(V1 58:30)` so yeah I've learned that we use arrays to store a list of objects in Java we can also create multi-dimensional arrays for example we can create a two-dimensional array to store a matrix or we can create a three-dimensional
- `(V1 59:00)` array to store data for cube these are useful in scientific computations let me show you so here we have a single dimensional array to convert this to a two-dimensional array we need to add another pair of square brackets now we have a compilation error because we need to repeat these brackets on the other side so let's say we want to create a 2 by 3 matrix so 2 rows and 3 columns we add in other brackets here and change these lengths to 2 and 3 so now we have
- `(V1 59:30)` 2 rows and 3 columns now to access individual items in this array we need to supply two indexes first the index of the row so we can go to the first row and then the first column and initialize that to 1 now let us print this so and so you t-tap once again we use our arrays class dot to string and pass this
- `(V1 60:00)` object take a look once again we get this weird string because here we're dealing with a multi-dimensional array to solve this problem we need to use another method in this class called deep to string use this for printing multi-dimensional arrays take a look now we have this matrix which has two rows and in each row we have three columns we can also create a three dimensional array all we have to do is to add another pair of
- `(V1 60:30)` brackets and specify the length of that dimension pretty easy now what about the curly brace syntax let me show you so let's revert this back to a two dimensional array we're gonna get rid of the new operator and use curly braces now let's say in this matrix we're gonna have two rows and three columns so each row is an array itself because it's a list of items right so we add another array here let's say 1 2 3 then comma now we add the second row
- `(V1 61:00)` which is another array in this row we're gonna have 3 numbers 4 5 &amp; 6 now let's remove this line we don't need it anymore and print this array so here's the end result you have learned a lot about variables ya learned that when
