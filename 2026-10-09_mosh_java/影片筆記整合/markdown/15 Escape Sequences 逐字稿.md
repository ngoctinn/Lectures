---
tags: [lecture/L2]
---

# L2 Escape Sequences 逐字稿

> [!info] 本機 whisper 轉錄，==未經人工逐字校對==；英文術語有辨識誤差，正確用詞以整理稿為準。

- `(V1 50:30)` our strings like a tab or a new line or a backslash or double quotes so in this tutorial I'm gonna show you how to include these special characters in your strings so here we have the string hello Marsh let's say we want to surround
- `(V1 51:00)` Marsh with double quotes now here's the problem if we add a double quote here Java compiler thinks this is the termination of our string so it doesn't stand what we have after that's why we have a compilation error the fixes problem we need to prefix this double code with a backslash so using this backslash we have escaped the double quote now one more time let's add backslash double code here now let's run the program and see what we get so
- `(V1 51:30)` we get hello Marsh in double quote beautiful so double quote is one of those special characters that you need to be aware of another special character is backslash let's say we want to store the pass to a directory on a Windows machine so that will look like this C Drive backslash windows backslash whatever now if you want to store this in a string we need to escape each backslash let me show you so C Drive backslash now we
- `(V1 52:00)` have a problem Java compiler thinks we're escaping the double code here so it thinks our string is not terminated with another double code but that's not what we want you want to add a backslash here so we need to prefix our backslash with another backslash now we type windows one more time something let's run the program so even though we have two backslashes in our code we actually see one backslash in a terminal window in other escape
- `(V1 52:30)` sequences backslash N and we use that to add a new line to our strings so let's change this to backslash N and run the program to see what happens now our string is broken down onto multiple lines by the first line we have C Drive then we have Windows so wherever we had a backslash n Java will insert a new line we can also add a tab in our strings so if you add backslash T here there will be a tab which means C Drive and
- `(V1 53:00)` windows let's take a look so C Drive here we have a tab and then windows now in Java we have a few more escape sequences but quite honestly they're hardly used so remember these four escape sequences that we cover in this tutorial
