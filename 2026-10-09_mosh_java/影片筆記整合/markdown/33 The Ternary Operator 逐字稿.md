---
tags: [lecture/L2]
---

# L2 The Ternary Operator 逐字稿

> [!info] 本機 whisper 轉錄，==未經人工逐字校對==；英文術語有辨識誤差，正確用詞以整理稿為準。

- `(V1 113:30)` look at the ternary operator in Java so we're gonna continue with the example from the last tutorial we had this income variable imagine this is the
- `(V1 114:00)` income or customers now depending on their income you want to put these customers in different classes if their income is more than $100,000 you want to put them in the first class otherwise we want to put them in the economy class so here's one way to implement the scenario we declare this string variable class name note that we cannot call this class because class is a reserved keyword so class name now we write our first condition if income is greater than $100,000 we said class name to first
- `(V1 114:30)` otherwise we set it to economy now as you learn in the last tutorial this code looks very amateurish a professional programmer doesn't write code like this so one way to simplify this is to give this variable an initial value so we assume they are in the economy class and then we check this condition if this condition is true we put them in the first class so with this we can get rid of this else clause that
- `(V1 115:00)` is better now in the last tutorial I showed you how to simplify this even further but the technique you learned there cannot be used here in other words we cannot add income greater than $100,000 here because here we have a boolean expression but on the left side we have declared a string variable so we want to set this to a different string depending on the result of this expression and this is where we use the ternary operator so we start with our
- `(V1 115:30)` condition then we type a question mark if this condition is true we add this value here otherwise we add the other value so this question mark and colon is the ternary operator in Java it has three pieces first we have a condition if this condition is true this value will be returned and assigned to our class named variable otherwise this other value will be returned now we can
- `(V1 116:00)` completely get rid of this if statement so put the ternary operator in your tool box it's very helpful next we're going to look at switch statements in Java in
