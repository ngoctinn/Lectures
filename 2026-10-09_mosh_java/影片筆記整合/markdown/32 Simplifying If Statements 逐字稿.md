---
tags: [lecture/L2]
---

# L2 Simplifying If Statements 逐字稿

> [!info] 本機 whisper 轉錄，==未經人工逐字校對==；英文術語有辨識誤差，正確用詞以整理稿為準。

- `(V1 110:00)` cool technique for simplifying if statements so let's start by declaring a variable called income and set it to 120,000 now here we can use an
- `(V1 110:30)` underscore in between these three digits to make our code more readable now let's say we want to declare a boolean variable called has high income if the income is more than $100,000 you want to set this to true otherwise we want to set this to false so here we can write an if statement like this if income is greater than $100,000 we want to set has high income to true however we get a
- `(V1 111:00)` compilation error here let's take a look declaration not allowed here so we cannot declare a variable here we can only declare variables inside code blocks like this code block over here so to declare this variable we need to add curly braces to define a new code block now we have a different problem this variable that we have defined is scoped
- `(V1 111:30)` to this code block so it's only available here we cannot access it outside of this block let me show you so if we print has high income you can see we have a compilation error cannot resolve symbol has high income because this variable is not available outside of the block in which it's declared so to solve this problem we can declare this variable after setup this block boolean has high income and then we can simply set it to true in this block now
- `(V1 112:00)` we don't need these braces anymore so let's simplify the code we add an else clause otherwise we said has high income to false let's remove this print method we don't need it anymore so this is one way to implement this scenario but this code looks very amateurish a professional programmer doesn't write code like this let's improve it step by step one way to improve this is to give this boolean variable an initial value for example we can set it to false
- `(V1 112:30)` initially and then we implement this condition so if the income is more than $100,000 then we set this variable to true with this we no longer need is else Clause so that was one improvement but it's still not ideal in situations like this we can completely get rid of this if statement here let me show you instead of hard-coding false here we type our
- `(V1 113:00)` expression income is greater than $100,000 so here we have a boolean expression if this boolean expression evaluates to true this boolean variable is going to be true otherwise it's going to be false so this is the simplest the most elegant and the most professional way to implement this scenario now one more improvement before we finish this tutorial I personally prefer to wrap this expression in parentheses even though technically we don't need parentheses here but these parentheses make our code
- `(V1 113:30)` more clear more readable let me show you so I'm gonna wrap this inside these parentheses now it's very clear we're obviously on the right side of this assignment operator we have a boolean expression in this tutorial we're gonna
