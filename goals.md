
Machine Classification.

With quant analysis, generally the first few things you are taught are "patterns" Head and shoulders, teacup, and whatever else.

So what is the theory behind these patterns? The idea is that the prices of stocks or various forex ratios are a direct reflection of the psychology of the people trading, ie: the traders (either people or computers) are making decisions, based on a bunch of variables. The theory is that, when those same variables present themselves again, we get a repeat of actions that creates a similar "pattern," then the outcome as well is likely to be similar, because the variables are almost the same.

So what we're going to do here is

1. Create a machine learned batch of what will end up being millions of patterns with their results, which can be used to predict future outcomes.

2. Test this.

You may have learned a few simple patterns, but everyone knows these. What if you could know every pattern in history? Pretty hard for you to remember them all, but not too hard for a computer.

Our entire system is really built on the inference of pattern recognition, so if patterns change due to new data, that's really built in and is done by programming that was done before results.

This allows backtesting to actually serve a very truthful and accurate purpose. If a machine learned live algo passes the back test, it is highly likely to continue performing well in the future, not because it passed a back test, but because our hypothesis and entire model passed the backtest... unlike finding the best algo at the time and backtesting for great results.

With that, what we will do is take a range of data in succession, and create a pattern with it. How we're going to do this is going to be with % change.

We want to have the data normalized as best we can, so it can be used no matter what the price was. We're just going to use a succession of % change for it.

To start, we'll do forward percent change, from starting point. This means, the longer the pattern, the more likely the END is to be less similar, but the actual direction of the pattern will be more similar. This can be useful, since some patterns might take more time to react than others, and we want the build up to be most accurate, but we might actually prefer the end to be more accurate in the future, so we could do reverse percent change. We can also do a point-to-point percent change as well. Trust me, when it comes to variables, we're gonna be very busy.

Now what that means is first we just need to store a bunch of patterns, in their percent change format.

Finding percentage change(%)
```python
def percentChange(startPoint,currentPoint):
    return ((currentPoint-startPoint)/startPoint)*100.00

```
