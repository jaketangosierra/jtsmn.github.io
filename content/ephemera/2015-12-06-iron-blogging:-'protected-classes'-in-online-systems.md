Title: Iron Blogging - 'Protected Classes' in Online Systems
Date: 2015-12-06
Modified: 2015-12-06
kind: article
Author: Jacob Thebault-Spieker
published: true

> _This post is a part of the GroupLens Iron Blogging effort, so take that for what you will._

[Aaron Halfaker](http://socio-technologist.blogspot.com/2015/12/disparate-impact-of-damage-detection-on.html) just (like, you know, _today_) posted some of his thoughts and early work based on a conversation we had about disparate impact in Wikipedia, both in terms of actual effect on individuals, and as a metaphor or framing for how to think about issues of bias and systemic disparity. Go read his thing, he does a good job of introducing the topic, and that's not my point here.

He says:

> __Protected Class__. In US law, it seems that this term is generally reserved for race, gender, and ability.  In the case of Wikipedia, we don't know these demographics.  They could be involved and I think they likely are, but I think that anonymous editors and newcomers should also be considered a protected class in Wikipedia.

There's some interesting stuff here that I want to try to unpack.

Aaron is right, __protected class__ has a legal definition [^1]. Laws are the societally defined set of ways we delineate what is acceptable. Societally, we have decided that there are (and ought to be) legal ramifications if there is discrimination (or disparately impactful discriminatory processes), in the United States.

He also argues for _expanding_ the definition of __protected class__, because the sociotechnical systems that Wikipedia has built (like ORES) put barriers in place for newcomers and anonymous editors to be successful. Wikipedia (or really, people who work on Wikipedia) has a community-defined set of ways to delineate what is acceptable.

In general society, the groups of people we consider members of a protected class are defined in law, based on history and value judgements made at the time (Voting Rights Act, etc.). If, at some point in time, society sought to change these categories, there would be an expectation of accountability to this process, and one would be expected to show strong evidence that any groups being removed wouldn't be harmed, and that groups being added have received a certain degree of societal harm (i.e. it would be difficult to argue that white men who make $1,000,000 or more ought to be a protected class).

In Wikipedia, the algorithms and statistics that back them decides who gets treated as a protected class, this is the point Aaron is seeking to address. But what does accountability of this process look like? What is the _computationally actionable_ threshold for adding or removing groups from the models being used? _Who_ decides which groups hit this threshold? _How_ do groups who do feel they're being disparately impacted voice this concern and build their case? Can this be dynamically, sociotechnically available?

I don't raise these questions to suggest mistrust towards Aaron nor Wikimedia (the shepherds of ORES right now), quite the opposite. I'm very excited by the work he and they are doing, I think ORES has a strong ability to even out some of the disparities that likely exist. However, I also believe this is _only true_ when ORES is able to dynamically mitigate disparate impact for groups that are being disadvantaged.

I'm super interested in these ideas, and Aaron and I will keep talking about them, but I'd be interested in other's thoughts as well.

[^1]: via [Wikipedia](https://en.wikipedia.org/wiki/Protected_class#cite_note-Finduslaw-1), which cites law
