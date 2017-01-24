Title: Iron Blogging - In Defense of 'Hybrid'
Date: 2016-04-23
Modified: 2016-04-23
kind: article
author: Jacob Thebault-Spieker

> _This post is a part of the GroupLens Iron Blogging effort, so take that for what you will._

[Michael Ekstrand](https://twitter.com/mdekstrand) recently [wrote up](https://md.ekstrandom.net/blog/2016/04/using-r/) his reasons for sticking to using R for data analysis, which included computational efficiency, `ggplot2`, and comfort with the workflow.

I don't have any problem with his argument, mostly, people should use what they want to use. You may recall, I [recently](http://jacob.thebault-spieker.com/ephemera/2016/01/26/iron-blogging-simplifying-workflows/) discovered Python/Pandas/GeoPandas/Jupyter, and the benefits that it has for geographic analysis. Michael too has discovered the power of Jupyter, saying:

> Even though we’ll keep using R, there’s one huge benefit that we get from the Python data ecosystem: I’ve mostly switched from RStudio to using Jupyter notebooks with IRKernel. It is _fantastic._ We’ve also been using Anaconda to install R and it’s worked pretty well.

This is the thing that I think is interesting: he's decided to stay in R-land, while taking advantage of Jupyter. Don't get me wrong, more power to him, if that's what works, it's what he should use.

Personally, I've been doing something a little bit different, mostly (although not entirely) as a crutch so I don't have to jump in the Python deep end and re-learn the things I know how to do in R; I'm using the Rpy2 `magic` in Jupyter, which lets me switch environments whenever I want.

For instance, I can connect to a Postgres+PostGIS database with GeoPandas, and load up a GeoPandas DataFrame. I can then use the `%Rpush`magic to push this DataFrame into R, plot it with `ggplot2`, and go back to Python for geographic operations or analysis. I have a notebook now that does all the data manipulation in Python, but I knew the `Wilcox.test` command in R, so I just ran that test with the R cell magic.

Stepping back a bit, it seems that a significant amount of the power, at least for me, that comes from Jupyter Notebook, and it's ability use things like IRKernel (and Rpy2), is flexibility. I'm using the tools that are best (or easiest, which _is_ best when you're time-constrained) for the job. Michael should do what he needs to do, sounds like R is the best tool for him.

I just also think that it needn't be either-or.
