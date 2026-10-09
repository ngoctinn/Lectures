---
tags: [lecture/L2]
---

# L2 Project: Mortgage Calculator 逐字稿

> [!info] 本機 whisper 轉錄，==未經人工逐字校對==；英文術語有辨識誤差，正確用詞以整理稿為準。

- `(V1 90:30)` right now it's time for a project I want you to use what you have learned in a section and build a mortgage calculator like this so when you run this program we get a few questions the first question is the principal or the amount
- `(V1 91:00)` of loan we want to get let's say $100,000 the second question is the annual interest rate let's say three point nine two percent and the third question is period in years let's say you want to get a loan for thirty years so this program calculates our monthly payments and displays it as a currency this is a great exercise for you to practice all the materials you learn in this section now before you get started I want to give you a few hints here is a
- `(V1 91:30)` formula for calculating the mortgage or the monthly payments I found this page on wikiHow comm is called calculate mortgage payments so let's see how this works mortgage equals P or principal or the amount we're gonna loan multiplied by R which is our monthly interest rate this is very important so this number that we get here is our annual interest rate we need to divide this by 12 also take into account that this number is represented as a percent to calculate
- `(V1 92:00)` the actual interest rate you need to divide this number by 100 so in this example the interest rate is zero point zero three nine two so whatever the user enters divided by 100 and then divided by twelve to get to the monthly interest rate now we have this monthly interest rate we need to multiply this by this expression here we need to add 1 to this interest rate and raise it to the power of n where n is the number of payments so we need to multiply this number by 12
- `(V1 92:30)` or 12 months to calculate the number of payments now to raise this number to the power of n you need to use the power method of the math class so this math class has this power or power method that takes two arguments or two values a and B so go ahead and spend ten to fifteen minutes on this exercise when you're done come back see my solution
