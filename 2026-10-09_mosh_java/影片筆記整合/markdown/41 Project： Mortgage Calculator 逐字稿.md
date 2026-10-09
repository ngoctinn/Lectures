---
tags: [lecture/L2]
---

# L2 Project: Mortgage Calculator 逐字稿

> [!info] 本機 whisper 轉錄，==未經人工逐字校對==；英文術語有辨識誤差，正確用詞以整理稿為準。

- `(V1 142:00)` all right now let's get back to our mortgage calculator and implement some basic error handling so here I've changed this question by adding this label that identifies the range of values we can enter so the minimum amount of loan we can get is $1,000 and maximum is 1 million dollars so if I enter 1 here I get this message enter a number between one thousand and one million and now we are asked this question one more time if I keep
- `(V1 142:30)` entering invalid values I get asked the same question now let's enter a valid value like 1 million dollars next we'll have to enter the annual interest rate now here we need to enter a value that is greater than 0 and less than or equal to 30 so if I enter 0 we get this message enter a value greater than 0 and less than or equal to 30 once again we're asked this question one more time so let's enter a valid value like 3.9 to here we need to enter a
- `(V1 143:00)` value between 1 and 30 so if you enter 0 we get an error message and we're asked the same question so let's enter 30 and finally we get the result here's our mortgage or monthly payments so go ahead and spend five to ten minutes on extending this mortgage calculator by adding error-handling to it you'll see my solution X
