Title: Iron Blogging - Inequality Indices For Platform Accountability
Date: 2015-11-13
Modified: 2015-11-13
kind: article
Author: Jacob Thebault-Spieker
published: true

> _This post is a part of the GroupLens Iron Blogging effort, so take that for what you will._

I've been thinking about systemic accountability recently: _how can we hold systems accountable to a set of expectations?_

In Ecology, the ecological systems (or, you know, _ecosystems_, I guess) they study exist in a world where they need to be valued by humans for conservation to occur. One framing for this value is [Ecosystem Services](https://en.wikipedia.org/wiki/Ecosystem_services), which, as I understand it, has been pretty significant as a conservation argument for the preservation of some ecosystems.

Broadly, ecosystem services give ecologists a way to talk about the specific things that ecosystems do, and actionable metrics on which to gauge what "value" the ecosystem provides.

When we think about sociotechnical platforms, a different set of metrics might be important, but it seems useful to think about _what_ and _how_ the platform or system is producing or providing.

There are straightforward approaches to some kinds metrics, specifically for inequality (like the Gini coefficient, or the lesser-known Theil Index), but in a geographic context, these, like most other statistical measures, break down because of [Tobler's First Law of Geography](https://en.wikipedia.org/wiki/Tobler%27s_first_law_of_geography), and the spatial auto-correlation that comes from it.

However, the Theil Index is [decomposable](https://en.wikipedia.org/wiki/Theil_index#Decomposability), which means that it is an average of weighted subgroups, plus the inequality within these subgroups. Spatially, one could use the spatial autocorrelation (using something like a standard neighbors-weights matrix that reflects how related neighbors are to each other) to define subgroups, and compute spatially distinct subgroups[^1]. This decomposability means that we can derive the amount of inequality within each subgroup, and how much each subgroup contributes to overall inequality.

More broadly though, this seems like it also gives us a straightforward metric through which we can start understanding _how equal the platform is spatially_. Inequality metrics are often used for things like housing, or income inequality, but what about sociotechnical platforms that interact in the physical world? How does this metric enable us to hold platforms accountable to geographic equality? What does that sort of transparency and accountability look like?

In a follow-up post, I hope to have an example of a spatial version of the Theil index, because I think this might be an interesting design direction.

[^1]: I'm glossing over some details here because I am not intimately familiar with the math.
