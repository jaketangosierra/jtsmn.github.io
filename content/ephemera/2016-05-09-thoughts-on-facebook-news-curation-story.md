Title: Thoughts On Facebook News Curation Story
Date: 2016-05-09
Modified: 2016-05-09
kind: article
author: Jacob Thebault-Spieker

There's an [article going around today](http://gizmodo.com/former-facebook-workers-we-routinely-suppressed-conser-1775461006) reporting that the news curation team at Facebook (the team that chooses what shows as Trending) would either "inject" stories into the platform, or de-value/blacklist stories (in some cases with a conservative bent).

The article states

> In other words, Facebook’s news section operates like a traditional newsroom, reflecting the biases of its workers and the institutional imperatives of the corporation.

which seems likely true. This case reads, to me, as another example of tech companies, and the people they hire, not having a wide-enough view of the world they act in (with large amounts of platform-based power). I'm uncomfortable about that, as I expect many are. This story doesn't strike me as surprising in that context, but it does serve as another reminder.

The interesting part to me, as someone in the field, comes from two directions.

### Algorithm/Software as Fact
It seems like the underlying tone of the article  is summed up by the quote above: this system still acts like previous systems, with people making decisions. The tone of the article is surprise and injustice, and I'm sympathetic to that view, but the core point is this: _we expected the trending news to be computationally driven, and when people stick things into it, it breaks what I came to understand about trending news_.

Software, and the stories we tell around software (or fail to tell) shape how people think about interacting with the software. I expected the trending news to be, you know, _trending_ (which most of it sounds like it is, though the article doesn't say how much injection or silencing was occurring). I didn't expect the trending news section to be curated or under editorial control (as a newspaper would be).

This expectation comes with a set of assumptions that were broken, and, at least for me, is why the "Facebook is being insidious" conclusion jumps to the forefront.

### Transparency
[Aaron Halfaker](http://www-users.cs.umn.edu/~halfak/) has talked about the role of transparency in "algorithms in social spaces" (he's thinking specifically about [ORES](https://meta.m.wikimedia.org/wiki/Research:Revision_scoring_as_a_service), and I believe informed by [Zeynep Tufekci](https://twitter.com/zeynep)), and how for us to be able to understand the role of this technology, it's almost an obligation that the providers of the technology provide mechanisms for understanding how they work.

In a world where so much of what humans understand is mediated through technology, Aaron's point seems to extend further: understanding which parts are explicitly human (and thus given the benefit of the doubt, or granted to be operating in good-faith, e.g. newspapers), and which parts are highly automated (though today, this automation is still informed by human judgement) feels important. In the ORES case (automated revision scoring), algorithms are deciding if an edit to Wikipedia is harmful, and above a certain threshold, automatically reverting this edit. These algorithms are informed by human judgements, but have learned to statistically model how humans make those judgements, and can act on that model. Below that threshold though, humans get brought into the loop explicitly, and make a decision about harm of the edit prior to reverting (or not).

I can tell you, broadly, how the revision-revert process works in Wikipedia, because it is documented, and because the ORES work is being done in public. Aaron is putting this information in public, and talking about the models he's using. Facebook's "now trending" section of the site (and the people behind it), are not. So here's my question: __would the Gizmodo article be as shocked, surprised, and concerned about insidiousness if we fully understood that there were/are humans making curatorial and editorial decisions about what gets called 'trending'__?
