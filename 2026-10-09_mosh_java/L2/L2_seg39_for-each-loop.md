---
tags: [lecture/L2]
---

# L2 For-Each Loop 逐字稿

> [!info] 本機 whisper 轉錄，==未經人工逐字校對==；英文術語有辨識誤差，正確用詞以整理稿為準。

- `(V1 138:30)` the last type of loop we want to look at is the for each loop in Java we use for
- `(V1 139:00)` each loops to iterate over arrays or collections let me show you so I'm going to start by declaring a string array called fruit and we initialize this with three items let's say Apple mango and orange now let's say we want to iterate over this array and print each item on a terminal we can use any of the loops you learn about earlier like a for loop or a while loop but we can also use the for each loop which is a bit easier let me show you first I'm going to use the for
- `(V1 139:30)` loop to iterate over this array so we type for here we declare our loop variable or loop counter into I we set it to zero as long as I is less than fruits that length we're going to increment I by one after each iteration and here we simply print fruits of I let's run the program and see what we get so we get each item on a new line beautiful now there is another way to
- `(V1 140:00)` write the same code using the for each loop here we type for in parentheses with declare and loop variable but the type of this variable should be based on the type of items in our array so here we have a string array and that means every item in this array is a string so here we should declare a string variable we call it fruit here we type a colon and then the name of our array fruits now in each iteration fruit will hold the value of one item in this array so
- `(V1 140:30)` here we don't have to declare a numeric counter we don't have to write a boolean expression like this we don't have to increment our counter it's much easier to iterate over an array now if we print fruit we get the exact same result as before take a look so the first three items are from our for loop and here's the result our for each loop so this is the for each loop however this for each loop has a couple of
- `(V1 141:00)` limitations one limitation is that it's always forward only so we cannot iterate over this array from the end to the beginning in contrast we can easily do this with a for loop so here we can initialize I to fruits that length then we change this operator to greater than and replace this value with zero so as long as I is greater than zero we're going to decrement I the second limitation of the for each loop is that here we don't have access to the index
- `(V1 141:30)` of each item all we have is this loop variable which holds the value of each item in this array in contrast in our for loops we can access both the index and the actual item so I represents the index of each item and fruits of I returns the item at the given index so if you need the index then you'll have to use the for loop otherwise it's much easier to use the for each loop
