import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
import os
from IPython.display import Markdown
# Used to securely store your API key

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

def summarize_function(text):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')

        response = model.generate_content(f"Split the following texts by context and give me a summary of each block, include the time frames that the blocks happen: {text}.")
        return response
    except Exception as e:
        return str(e)
def find_best(text):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')

        response = model.generate_content(f"I will provide a transcript for a video with the timestamps for it, give me the most interesting intervals of the video and that have the most potential to go viral by themselves(They should be 40-80 second long intervals): {text}")
        return response
    except Exception as e:
        return str(e)

# call the function to test
sample = f"""0.04 - 2.7600000000000002: so what do you do for
3.26 - 6.32: [Music]
8.24 - 14.0: work around you're just really boring
11.36 - 17.8: should we get [ __ ] up wait gople shots
14.0 - 19.6: please over here somea please thank you
17.8 - 22.080000000000002: so what were you saying that was an
19.6 - 24.039: example of a good date someone you'd
22.08 - 27.0: want to be on a date with however there
24.039 - 30.279000000000003: are many people on Tik Tok telling
27.0 - 31.72: stories about bad dates they've been on
30.279 - 32.96: so we're going to go through those and
31.72 - 35.12: we're going to listen and we're going to
32.96 - 36.64: we're going to react so this is dates
35.12 - 38.559: from hell what's the worst first date
36.64 - 40.559: I've ever been on I'm so glad you asked
38.559 - 42.16: I'm going to tell you right now before I
40.559 - 44.519999999999996: met my smoke show of a husband I was on
42.16 - 46.038999999999994: dating apps as you do this man messages
44.52 - 48.559000000000005: me out the blue and he goes I like your
46.039 - 51.079: face let's go get some food um I love
48.559 - 52.76: food are you my soulmate he says meet me
51.079 - 54.559: at my house I will drive us to the
52.76 - 57.039: restaurant together why did we not just
54.559 - 58.32: meet there I have no idea I drive 45
57.039 - 59.719: minutes to his house he's standing
58.32 - 61.28: outside of it he walks up to my car and
59.719 - 62.92: he go was I've lost my keys can you
61.28 - 65.08: drive us there should I have just left
62.92 - 67.43900000000001: him right there and gone home yes did I
65.08 - 68.96: absolutely not he gets in starts giving
67.439 - 70.19999999999999: me turn by turn directions he could have
68.96 - 71.52: been leading me to an abandoned
70.2 - 75.68: warehouse and he still would have been
71.52 - 79.15899999999999: like left at this stop sign okay we end
75.68 - 81.60000000000001: up at a Taco Bell which is
79.159 - 82.92: fine I'm like d in or drive-thru and
81.6 - 85.52: he's like driveth through I'm like great
82.92 - 87.43900000000001: he has a plan we get to the speaker and
85.52 - 90.439: he just leans over and goes I would like
87.439 - 93.72: 100 hard shell tacos thank you no
90.439 - 97.79899999999999: [ __ ] way no [ __ ] way was it Tim
93.72 - 99.15899999999999: Robinson 55 Tac 55 Burgers 55 was it him
97.799 - 101.0: you should have known this was like an
99.159 - 103.119: absurdist date that's the point this was
101.0 - 105.32: an artiste all right it's an artist he's
103.119 - 106.6: doing performance art that's what he is
105.32 - 109.55999999999999: that's what he's doing you got to just
106.6 - 110.96: go with it please 100 tacos please like
109.56 - 112.36: he's tried to throw you off twice
110.96 - 114.6: already and you're still going with it
112.36 - 115.88: so now he's the 100 tacos thing is his
114.6 - 117.079: next attempt he's like oh I really got
115.88 - 118.56: to turn it up here I'm not trying to
117.079 - 121.03899999999999: creep her out I'm trying to weird her
118.56 - 123.24000000000001: out you know
121.039 - 124.88: we get to the window he does one of
123.24 - 126.88: these numbers and I'm like did you
124.88 - 128.56: forget your wallet and he's like yeah I
126.88 - 131.599: was like do you need me to pay he's like
128.56 - 134.8: yeah I'm like
131.599 - 136.72: yeah I buy the 100 tacos and I'm like
134.8 - 139.08: where tun next I feel like sometimes
136.72 - 141.76: some people use dating apps just to find
139.08 - 143.4: people to like get into like hij Jinks
141.76 - 145.07999999999998: you know it's like they have a [ __ ]
143.4 - 146.12: stupid Quest that they're going to go on
145.08 - 147.84: they know that they're going to do it
146.12 - 149.959: they know they have no one else to do it
147.84 - 151.12: with cuz like I don't know maybe they're
149.959 - 152.599: they don't have friends or maybe their
151.12 - 153.44: friends have jobs or something so
152.599 - 155.2: they're like I'm just going to hit up
153.44 - 157.2: someone on a dating app I need a partner
155.2 - 159.11999999999998: for this weird [ __ ] Quest I'm about
157.2 - 160.28: to go on and he goes back to my house
159.12 - 164.8: and I was
160.28 - 166.76: like okay this is happening I'm just I'm
164.8 - 169.12: committed to this now it's
166.76 - 170.35999999999999: happening we get to his house we walk in
169.12 - 172.64000000000001: his dad is on the couch I'm like he
170.36 - 174.48000000000002: lives with his dad it's fine the Hoops I
172.64 - 177.159: am teleporting
174.48 - 178.79999999999998: through to convince myself that this
177.159 - 182.72: decision that I have made is okay is
178.8 - 185.36: just Why wild walk past his dad into the
182.72 - 187.879: kitchen he just starts emptying the
185.36 - 190.44000000000003: boxes of tacos just releasing them onto
187.879 - 192.51899999999998: the table puts two chairs at the table
190.44 - 196.2: sits down and he just screams at the top
192.519 - 196.20000000000002: of his lungs let's
196.28 - 202.12: Feast I am just this guy sounds like a
199.76 - 204.39999999999998: [ __ ] Legend
202.12 - 206.31900000000002: honestly I think that I think that you
204.4 - 209.519: were a fool not to marry this guy he
206.319 - 211.159: sounds so fun so fun this one of those
209.519 - 214.08: dudes that just flies by the seat of his
211.159 - 215.28: pants you know I feel like any any other
214.08 - 217.04000000000002: person would have been like would have
215.28 - 218.4: canceled it at the I can't find my keys
217.04 - 220.159: part it's just would have been like I
218.4 - 221.799: listen I can't meet you there I'm not
220.159 - 223.84: going to ask you to pick me up I can't
221.799 - 225.36: find my keys we let's just reschedule
223.84 - 226.799: it's not the right day you know my my
225.36 - 228.36: shit's all over the place I don't got my
226.799 - 230.15900000000002: [ __ ] together today this guy was like no
228.36 - 232.079: I'm I'm going to have her pick me up
230.159 - 233.439: this this is not stopping the plan we're
232.079 - 235.72: going to go to Taco Bell and I'm just
233.439 - 238.84: going to order whatever comes to me
235.72 - 241.28: whatever thine Holy Spirit commands me
238.84 - 242.28: to order I'm going to order that hello
241.28 - 245.72: welcome to
242.28 - 245.72: Tac 100
247.519 - 251.72: tacos 100 and now he's [ __ ] stoked
250.2 - 253.0: cuz he has 100 tacos you're never
251.72 - 254.599: running out that's why he's pumped he's
253.0 - 257.16: in the kitchen he's like let's [ __ ]
254.599 - 259.32: go baby we can each have 50 of these
257.16 - 262.44: [ __ ] things
259.32 - 264.15999999999997: calmly unwrapping my taco and taking a
262.44 - 265.71999999999997: bite of it we are eating hard chill
264.16 - 268.639: tacos in complete silence you can hear
265.72 - 270.91900000000004: both of us chewing it's absolute chaos
268.639 - 273.40000000000003: the dad walks up grabs a taco there's a
270.919 - 275.4: hundred of them we have so many to spare
273.4 - 276.96: he's eating over us just like standing
275.4 - 279.4: doesn't sit stands right next to the
276.96 - 282.19899999999996: table crunch his mouthful he just looks
279.4 - 284.15999999999997: at me and he goes do you want to see my
282.199 - 287.36: studio and I was like I have never
284.16 - 289.6: wanted to see anything less in my entire
287.36 - 291.32: life it was that moment that I decided
289.6 - 293.16: this date was completely over or else I
291.32 - 296.36: was going to be killed
293.16 - 299.47900000000004: 100% I am now just like collecting the
296.36 - 301.40000000000003: tacos because I paid for them I walk out
299.479 - 302.56: with boxes of tacos in my purse I look
301.4 - 304.479: back and I was like thank you for this
302.56 - 307.199: experience you will never hear from me
304.479 - 309.59999999999997: again okay I'm just trying to figure out
307.199 - 311.44: what the [ __ ] happened like he knew that
309.6 - 312.759: he wasn't paying the whole time so he
311.44 - 315.4: was just like I'm just going to get a
312.759 - 317.12: lot and he needed lunch he didn't have a
315.4 - 318.67999999999995: [ __ ] wallet his dad was asleep on the
317.12 - 320.039: couch he's like how the [ __ ] am I going
318.68 - 321.56: to get out of here get lunch I don't
320.039 - 323.68: have any money and this is a this is a
321.56 - 325.12: scheme you got scammed you got scammed
323.68 - 326.639: that's what it is it's a scam but he he
325.12 - 329.8: was like nice enough to like let you eat
326.639 - 331.199: some at his place you got scammed and he
329.8 - 333.28000000000003: was like let's have lunch together at
331.199 - 335.68: least like here you [ __ ] you paid for
333.28 - 337.08: all these you can have I mean as many as
335.68 - 338.479: you can eat which is probably two so
337.08 - 339.4: when he saw you collecting them too he's
338.479 - 342.28: probably like you're probably going to
339.4 - 343.88: get like 20 I still get the LI The Lion
342.28 - 346.79999999999995: Share of these [ __ ] things you know
343.88 - 348.44: I'm still walking away with 60 at least
346.8 - 351.319: Chuck them in the freezer I mean that'll
348.44 - 354.88: feed you for weeks months even you could
351.319 - 357.84000000000003: have six tacos a day two for each meal
354.88 - 359.44: for 10 days you got scammed you got you
357.84 - 361.52: know who this was it was probably like
359.44 - 364.0: who who's the guy from Catch Me If You
361.52 - 365.56: Can you know the the when you know Leo
364.0 - 366.919: played him it's like the I forget his
365.56 - 368.88: name but he was like the con artist he
366.919 - 370.12: was like pilot and then a doctor and the
368.88 - 372.15999999999997: and then he was like kind of whatever
370.12 - 373.84000000000003: you got you go on a date with that guy
372.16 - 376.16: that's what it was he's like I'm a
373.84 - 378.56: [ __ ] crazy dating app guy I don't
376.16 - 381.199: know hun tacos please sorry I lost my
378.56 - 383.28000000000003: wallet thank you here it is thank you
381.199 - 385.68: thank you so much you got scammed by Tim
383.28 - 387.88: Robinson that's [ __ ] crazy dating a
385.68 - 390.28000000000003: nice guy he controlled everything and
387.88 - 393.479: made me feel awkward who is filming
390.28 - 395.11999999999995: their dates he thank you taking me here
393.479 - 396.56: you're welcome all right I'll get those
395.12 - 398.479: going and then I'll come back and grab
396.56 - 399.68: thank you very much all right so I liked
398.479 - 401.479: what she had mentioned about the
399.68 - 403.96: scallops I thought that sounded really
401.479 - 405.96: good I'm a big seafood fan so I think
403.96 - 408.12: I'm going to do that let me order for
405.96 - 409.35999999999996: you I'll surprise you I know what you I
408.12 - 411.12: hate
409.36 - 413.319: surprises you know this place better
411.12 - 417.199: than be yes I
413.319 - 418.91900000000004: do his [ __ ] voice dude Yes I Do by
417.199 - 421.24: the way this is definitely fake it's
418.919 - 423.15999999999997: fake it has to be what the [ __ ] what is
421.24 - 425.12: this are you just holding your phone
423.16 - 426.759: like this I mean I guess maybe if she
425.12 - 429.24: was like weirding him out or if he was
426.759 - 431.599: weirding her out before this then maybe
429.24 - 434.199: maybe it was real maybe it's real you
431.599 - 434.199: I'm getting the
435.12 - 439.36: revive so what are you going to order
437.16 - 442.40000000000003: for me then the ribeye with the mesh oh
439.36 - 444.319: okay really ni you don't want you don't
442.4 - 448.19899999999996: like red not good here or something well
444.319 - 451.52000000000004: you don't want to add on any Cal to you
448.199 - 451.52000000000004: oh my god
451.919 - 455.68: oh my God was he trying to be like the
453.879 - 457.72: 50 Shades of Gray guy is that what this
455.68 - 459.40000000000003: is but just accidentally being super
457.72 - 462.03900000000004: insulting well you don't want to add on
459.4 - 465.919: any extra calories do you poor key the
462.039 - 467.4: Pig I mean [ __ ] sorry oh no but I
465.919 - 469.4: mean we're on a nice little date so I
467.4 - 471.599: think I can ignore it for now I'll order
469.4 - 474.039: you a drink that'll that'll suit what
471.599 - 476.28: you're looking for what the hell am I
474.039 - 477.87899999999996: looking for something with less calories
476.28 - 479.96: yeah that is true I mean wine does have
477.879 - 483.0: a lot of sugar I tend to know what
479.96 - 485.08: like yeah that's good that's good cuz
483.0 - 487.479: not many guys do but I'm definitely A
485.08 - 490.4: Cut Above the
487.479 - 493.199: Rest I [ __ ] even if this is fake man I
490.4 - 494.84: definitely A Cut Above the Rest and I
493.199 - 496.72: think if you use that phrase it
494.84 - 499.35999999999996: automatically disqualifies you from
496.72 - 500.879: being A Cut Above the Rest well I'm A
499.36 - 502.40000000000003: Cut Above the Rest all right are you a
500.879 - 503.8: steak are you a steak is that what
502.4 - 506.56: you're saying that's why I'm ordering
503.8 - 510.639: the prime rib because I am the prime rib
506.56 - 513.279: of dates M all will be having the prime
510.639 - 516.44: rib and for the lady over here she will
513.279 - 522.4399999999999: be having the broccolini stems please
516.44 - 525.48: with a water shaken not stirred thank
522.44 - 528.519: you yeah I think I think I'm going to
525.48 - 530.24: he's like shut up I'm going to do it no
528.519 - 533.0: I got I'm going to do it I'm the alpha
530.24 - 534.64: I'm going to do it she's actually going
533.0 - 538.36: to have what I'm going to have what's
534.64 - 540.16: that uh I'm going to have the uh either
538.36 - 542.24: one if you like to add super for salad
540.16 - 543.6: tonight yeah I was going that was funny
542.24 - 544.839: he kind of he kind of like he wasn't
543.6 - 546.5600000000001: really prepared I don't know if that was
544.839 - 548.44: an awkward pause in the editing or what
546.56 - 550.0: but he was like so pumped to order for
548.44 - 552.12: her that he forgot what both of them
550.0 - 553.6: were having that would be [ __ ] funny
552.12 - 554.88: he's like waiting he's like actually I'm
553.6 - 557.839: going to order for
554.88 - 561.279: her okay what are you guys getting he's
557.839 - 565.24: like well we're going to
561.279 - 567.56: um I actually see the menu sorry oh
565.24 - 571.04: Wonder Entre wasn't it did you guys you
567.56 - 573.399: had like um what was it the date's like
571.04 - 575.56: prime prime rib prime rib prime rib I
573.399 - 577.56: said it I remembered before she said
575.56 - 579.68: anything so we'll get to prime rib and
577.56 - 583.399: she will have that as well too as well
579.68 - 587.8389999999999: also thank you this suit is that okay
583.399 - 590.24: that's fine oh my God I can't even
587.839 - 592.519: [ __ ] talk okay I can't even order he
590.24 - 596.72: thinks he's being so
592.519 - 596.72: nice updates it
597.48 - 601.5600000000001: it's know this G to be me well if you
600.399 - 605.079: don't mind I'm going to take care of my
601.56 - 606.3199999999999: bill um because I I do mind I I will go
605.079 - 608.0: ahead and take care of no no no no
606.32 - 609.72: listen I've had an experience like this
608.0 - 613.279: in the past and I do not want to repeat
609.72 - 617.279: so I will definitely well that's not me
613.279 - 618.88: I will not embarrassment okay it's not
617.279 - 620.56: an embarrassment like I can also just
618.88 - 621.76: cash out you no it is is very much an
620.56 - 623.64: embarrassment okay okay don't don't
621.76 - 625.079: worry about it just not make a seem I
623.64 - 627.279: forgot you like to open the door thank
625.079 - 628.7199999999999: you that's really nice of you all right
627.279 - 630.16: I'm just going to run into the the car
628.72 - 632.9200000000001: if that's okay
630.16 - 635.0: no no it's not oh my God
632.92 - 636.5999999999999: okay I could have gotten in there a lot
635.0 - 640.2: faster if I just ran gentleman has to
636.6 - 642.9590000000001: get the door that's fine thank
640.2 - 644.72: you I feel like it was fake it's so
642.959 - 646.3199999999999: funny the type of guy that watches 50
644.72 - 648.839: Shades of Gray and it's like I'm going
646.32 - 651.519: to do that that's me but like just does
648.839 - 653.7600000000001: not have like the charm or like anywhere
651.519 - 655.8: close to like the charm or like the
653.76 - 657.4399999999999: suaveness to pull it off they just
655.8 - 659.8389999999999: they're just a nerd that just comes
657.44 - 661.6: across as like just mean and just dumb
659.839 - 664.1600000000001: she said I want the scallops he said no
661.6 - 666.16: you don't no I do I do I actually I do I
664.16 - 668.1999999999999: just I I mean I just said it I read it
666.16 - 670.279: on there they sound really good no they
668.2 - 672.519: don't okay well it's subjective and I I
670.279 - 673.8: think they do you want the ribeye are
672.519 - 675.6: you trying to hypnotize me or what's
673.8 - 679.079: happening here what's going on you are
675.6 - 681.9200000000001: sexually attracted to me yes yes I am
679.079 - 683.959: these people got RZ there's some [ __ ]
681.92 - 686.8389999999999: Riz out there that we don't even know
683.959 - 689.04: about you know off theark Alpha nerd
686.839 - 691.8800000000001: domz that's what that was one before
689.04 - 693.04: that Tim Robinson RZ Tim risbon what do
691.88 - 694.56: we got here thinking about the time I
693.04 - 696.1999999999999: showed up to a Tinder date 7 months
694.56 - 697.5999999999999: pregnant knowing he didn't have a clue
696.2 - 698.839: and we just both sat at the Mexican
697.6 - 700.519: restaurant and had lunch whilst
698.839 - 702.7600000000001: pretending my belly wasn't in the room
700.519 - 702.76: with
703.92 - 708.76: us that's a pretty funny detail to leave
707.0 - 710.32: out I don't even know what I think about
708.76 - 712.079: that I think like if you're pregnant
710.32 - 713.399: should you have to be like Hey listen
712.079 - 714.56: I'm pregnant but if you're the dude I'm
713.399 - 717.04: sure you'd want to know like it
714.56 - 719.5999999999999: definitely like changes the the like
717.04 - 722.1999999999999: scenario a little bit I kind of respect
719.6 - 724.48: it because I feel like a lot of dudes
722.2 - 726.2: would be scared off if you said that
724.48 - 727.36: beforehand they would cancel the date
726.2 - 729.36: and maybe you guys would have gotten
727.36 - 730.8000000000001: along [ __ ] amazing and he'd be he'd
729.36 - 732.36: be like you know what let's [ __ ] get
730.8 - 733.68: married I will raise that child I like
732.36 - 734.88: you so much I'm going to raise you that
733.68 - 736.2399999999999: I'm going to raise that [ __ ] child
734.88 - 737.32: there's a chance that would happen you
736.24 - 738.6: know what's the worst that's going to
737.32 - 740.1990000000001: happen the guy's going to be like oh
738.6 - 741.32: cool we went on a date Mexican
740.199 - 743.56: restaurant probably wasn't that
741.32 - 745.7600000000001: expensive you know I mean maybe maybe I
743.56 - 747.5189999999999: don't know it was like Javier or
745.76 - 748.72: something be a little bit expensive but
747.519 - 750.32: you know whatever maybe they went out
748.72 - 752.36: had a nice meal maybe he was like Hey
750.32 - 754.0400000000001: listen not down for the baby thing she
752.36 - 756.36: be like okay but the best that could
754.04 - 758.04: happen would be that they hit it off and
756.36 - 760.0790000000001: then in the future he's wearing a shirt
758.04 - 761.92: that says I'm not the stepdad I'm the
760.079 - 763.12: dad that stepped up boom which by the
761.92 - 764.519: way I'm reading in the comments that
763.12 - 766.24: like this has happened before you know
764.519 - 767.519: met my husband on Bumble when I was 16
766.24 - 769.6800000000001: weeks pregnant he was there for the
767.519 - 770.839: birth and has been with her ever since I
769.68 - 772.399: went on a date when I was 4 months
770.839 - 773.9200000000001: pregnant we're married now this happen
772.399 - 775.519: all the time my mom did this and she
773.92 - 778.959: later ran into him when I was born and
775.519 - 781.24: now he's my dad 24 years later boom Ste
778.959 - 782.5999999999999: out had origin stories everywhere tell
781.24 - 784.279: me a first date story when you realized
782.6 - 787.24: they were not getting another date I'll
784.279 - 790.199: go first so we met on a dating app so on
787.24 - 792.48: this damn this is [ __ ] 2021 Tik Tok
790.199 - 795.88: right here I'll go first I was on this
792.48 - 797.36: first date this one time and the guy
795.88 - 798.92: sits down and he rolls up his sleeves
797.36 - 801.519: and he has a dinosaur tattoo on his
798.92 - 802.92: forearm and I was like and it was Diplo
801.519 - 805.0: hey what's the story behind this and he
802.92 - 808.199: goes do you not know who that is and I
805.0 - 810.0: was like no who is that and he goes
808.199 - 812.12: That's the T-Rex from from Jurassic Park
810.0 - 814.0: and I was like oh why do you have the
812.12 - 817.519: T-Rex from the Jurassic Park tattooed on
814.0 - 818.88: your arm and he says cuz it's cool cuz
817.519 - 822.199: it's scary and
818.88 - 824.48: cool why do I have the T-Rex
822.199 - 826.3599999999999: from because you can rip your freaking
824.48 - 829.9590000000001: throat out if you wanted to all right
826.36 - 831.24: [ __ ] why I have a T-Rex from [ __ ] uh
829.959 - 832.399: I'm sorry my teacher told me there's no
831.24 - 834.279: such thing as a stupid question but I
832.399 - 835.839: think I I think he's proved them wrong
834.279 - 837.6: [ __ ] so what they have tiny arms they
835.839 - 839.1600000000001: make up with they huge legs and their
837.6 - 840.6: mouth it's like one of the coolest dinur
839.16 - 842.079: on Earth well technically used to be on
840.6 - 843.9200000000001: earth that when he was little his
842.079 - 846.12: parents were always really busy so
843.92 - 848.04: movies basically raised him and the
846.12 - 850.6: T-Rex from Jurassic Park is like a
848.04 - 850.5999999999999: father to
851.16 - 858.12: him holy
853.6 - 861.8000000000001: [ __ ] what an awesome response this is my
858.12 - 864.92: stepdad right here this is not a T-Rex
861.8 - 864.92: this is the tea that rexed
866.44 - 873.36: up a I'm done later like and Zade if you
871.839 - 875.8800000000001: make me have really small arms right now
873.36 - 875.88: I'm going be
876.759 - 882.16: pissed don't do it bro don't do it don't
880.0 - 885.28: make me look like a T-Rex Tinder date
882.16 - 891.86: was mad that she had to split the
885.28 - 892.52: [Music]
891.86 - 895.64: [Laughter]
892.52 - 895.64: [Music]
895.88 - 904.16: bill what' you say why are we SP the
899.44 - 905.72: bill well I mean it's our first date so
904.16 - 908.079: I thought we should
905.72 - 911.639: maybe go
908.079 - 915.2399999999999: H I can't believe you made us split the
911.639 - 917.199: bill I mean this [ __ ] is fake as [ __ ]
915.24 - 919.199: why does anyone make real [ __ ] videos
917.199 - 921.639: anymore God damn it you're saying this
919.199 - 923.12: footage just started when she said I
921.639 - 925.72: can't believe you made this you made me
923.12 - 927.72: split the bill [ __ ] annoying you
925.72 - 930.9200000000001: ordered an appetizer that I didn't even
927.72 - 933.6800000000001: touch why did you think that I should
930.92 - 937.4399999999999: pay for you asked me
933.68 - 939.5999999999999: out I know but you ordered something
937.44 - 943.399: asked me out all right I'll just take
939.6 - 946.399: you home and all right see you I know
943.399 - 948.12: there's like this is the most like
946.399 - 949.44: debated thing ever I think the dude
948.12 - 950.839: should pay on the first dat that's what
949.44 - 953.0400000000001: I think he wanted to impress the
950.839 - 955.44: internet Bros with this one it is funny
953.04 - 956.8389999999999: thinking about this if it was real as
955.44 - 959.3190000000001: soon as he saw her like get a little
956.839 - 961.839: pissed he's like a [ __ ] yeah I'm about
959.319 - 963.8: to get some likes on Twitter baby I went
961.839 - 965.36: to a standup show for a date God made
963.8 - 968.92: fun of and then ended up crying in front
965.36 - 970.639: of my date let's go yes it was my fourth
968.92 - 972.88: date with her and I really liked her and
970.639 - 974.36: enjoyed seeing her but now I'm [ __ ] so
972.88 - 975.92: she had the idea to go to a standup
974.36 - 977.44: event where different amateur Comics
975.92 - 979.079: came up and did their set three out of
977.44 - 980.3190000000001: five of the comments made me a part of
979.079 - 983.04: their
980.319 - 985.12: routine three out of five what were you
983.04 - 986.48: like wearing they all just went in on me
985.12 - 988.0: for the way I looked dressed and
986.48 - 989.5600000000001: constantly made it a point that the girl
988.0 - 992.079: I was seeing was out of my my league one
989.56 - 994.319: asked how much I paid for her to be my
992.079 - 995.8389999999999: date damn dude I tried to be
994.319 - 997.56: good-natured about it I tried not to let
995.839 - 999.519: it get to me but honestly my self-esteem
997.56 - 1001.199: is such [ __ ] anyways and I couldn't help
999.519 - 1002.92: to take everything they said personally
1001.199 - 1007.04: because all of it was true I ended up
1002.92 - 1007.04: crying by the time the last comment came
1008.0 - 1013.44: up I'm sorry I'm sorry I'm sorry for
1011.48 - 1016.3190000000001: laughing this is a really unfortunate
1013.44 - 1018.2790000000001: situation but the crying is pretty funny
1016.319 - 1020.4799999999999: like I'm just thinking like the fourth
1018.279 - 1022.04: comic coming up you know like the first
1020.48 - 1023.639: three have all made fun of him the
1022.04 - 1025.039: fourth comes up like comes back from the
1023.639 - 1026.88: Green Room hasn't seen the other one
1025.039 - 1028.4: sets walks up on stage and just looks at
1026.88 - 1031.3190000000002: the guy and he's like oh and the dude
1028.4 - 1034.0790000000002: just [ __ ] no please not again starts
1031.319 - 1035.72: crying oh this is rough dude I ended up
1034.079 - 1037.1599999999999: crying by the time the last comment came
1035.72 - 1038.6000000000001: up and the girl noticed and said that we
1037.16 - 1040.0790000000002: should leave I dropped her off and I
1038.6 - 1041.7199999999998: tried texting her apologizing for
1040.079 - 1044.1989999999998: ruining the date and I haven't gotten a
1041.72 - 1047.319: response I'm such a [ __ ] loser what a
1044.199 - 1049.3200000000002: horrible way to end the post such a
1047.319 - 1052.0: [ __ ] loser listen I I think this is
1049.32 - 1053.6789999999999: probably the only time that you I'm
1052.0 - 1057.4: trying to think is this like the only
1053.679 - 1058.8400000000001: time where heckling would be good that
1057.4 - 1061.4: would would be accepted you know what
1058.84 - 1063.48: I'm saying if three comics in a row are
1061.4 - 1065.52: embarrassing you in front of your date
1063.48 - 1067.64: whom you like you got to just be like yo
1065.52 - 1070.72: shut the [ __ ] up dude pick on someone
1067.64 - 1072.6000000000001: else no you're a [ __ ] she is out of my
1070.72 - 1074.559: league lowkey one of my biggest fears in
1072.6 - 1076.6789999999999: my life that I forgot I had tonight my
1074.559 - 1078.12: fear has been validated edit just to be
1076.679 - 1079.48: clear I feel like there's some confusion
1078.12 - 1081.84: nothing happened to me I've never been
1079.48 - 1083.44: to a comedy never been to a comedy is
1081.84 - 1085.6789999999999: that like is this like a New Zealand
1083.44 - 1087.64: post or something I've never been to a
1085.679 - 1089.3600000000001: comedy is that what you call it there a
1087.64 - 1092.48: comedy we're heading to the comedy
1089.36 - 1094.559: tonight crying is like the that's just
1092.48 - 1096.84: probably the worst possible thing you
1094.559 - 1100.799: could ever do in that situation she's
1096.84 - 1102.3999999999999: like stop stop yeah that's when I think
1100.799 - 1103.9189999999999: you just sit there and you go just then
1102.4 - 1105.72: every single joke they tell afterwards
1103.919 - 1108.1200000000001: you
1105.72 - 1109.799: go you know just heckle heckle them
1108.12 - 1114.559: weirdly nice
1109.799 - 1116.96: joke I love jokes yo I love jokes and
1114.559 - 1118.1589999999999: that was one of them you know I don't
1116.96 - 1119.559: know maybe that makes you look more
1118.159 - 1121.8400000000001: pathetic I don't know maybe you got to
1119.559 - 1123.6789999999999: just like [ __ ] get up and take a [ __ ]
1121.84 - 1125.24: on the table or something something
1123.679 - 1126.6000000000001: crazy you know just make everyone forget
1125.24 - 1128.0: about the crying I don't know that is
1126.6 - 1129.32: kind of a scenario from a nightmare
1128.0 - 1130.64: though truly what's the weirdest date
1129.32 - 1132.039: you've been on I'll go first we were
1130.64 - 1133.48: going to see a movie and didn't buy
1132.039 - 1134.8799999999999: tickets in advance and couldn't get two
1133.48 - 1136.159: tickets next to each other so we ended
1134.88 - 1137.48: up sitting on opposite sides of the
1136.159 - 1140.64: theater and then the movie ended and we
1137.48 - 1142.48: were like okay cool bye that's awesome
1140.64 - 1144.0: about a month ago I went out with a guy
1142.48 - 1145.88: who I thought was cool since we had
1144.0 - 1147.84: martial arts in common I like that not
1145.88 - 1150.2800000000002: doing martial arts just we had martial
1147.84 - 1152.6789999999999: arts in common what are you about
1150.28 - 1154.2: martial arts no [ __ ] we have that in
1152.679 - 1155.52: common on the second date things started
1154.2 - 1157.3600000000001: to get weird because he kept pretending
1155.52 - 1159.4: to punch and kick me in the face it got
1157.36 - 1160.76: annoying fast then he kept grabbing my
1159.4 - 1162.76: hands and cracking each and every
1160.76 - 1165.0: knuckle in my finger even the fingertip
1162.76 - 1166.4: ones ouch I told him to stop and that it
1165.0 - 1168.12: was apparently a deal breaker that I
1166.4 - 1169.72: didn't know that I had we had to stop at
1168.12 - 1171.2399999999998: my house to get get a package off my
1169.72 - 1173.08: porch and while we were there he told me
1171.24 - 1174.96: my dog stunk and sprayed him with f
1173.08 - 1177.84: Breeze needless to say no third day this
1174.96 - 1179.8400000000001: guy sounds awesome just constantly
1177.84 - 1180.9599999999998: like no no I'm [ __ ] around I'm
1179.84 - 1183.76: [ __ ]
1180.96 - 1186.64: around no I'm [ __ ] around I'm [ __ ]
1183.76 - 1189.08: around oh oh you got to watch yourself
1186.64 - 1190.919: you got to watch yourself
1189.08 - 1192.84: seriously it's like a big brother you
1190.919 - 1194.8400000000001: know had a very cute girl come up and
1192.84 - 1196.32: start talking to me in the gym ooh gave
1194.84 - 1198.1589999999999: me her number and asked me if I wanted
1196.32 - 1200.0: to grab coffee sometime I was single at
1198.159 - 1201.7990000000002: that point decided sure she was very
1200.0 - 1203.12: cute and seemed nice started texting me
1201.799 - 1204.6399999999999: every day nothing too aggressive but
1203.12 - 1206.4399999999998: clearly showing interest in something
1204.64 - 1208.24: well fast forward to the coffee date her
1206.44 - 1210.2: and her boyfriend show up turns out they
1208.24 - 1211.52: are Amway reps and were trying to wrote
1210.2 - 1213.039: me in based on the fact that I had
1211.52 - 1214.12: experienced owning a real business I
1213.039 - 1215.36: didn't make a big deal about it but I
1214.12 - 1217.1589999999999: did text her after saying it was very
1215.36 - 1218.6789999999999: misleading and dishonest on her part and
1217.159 - 1219.919: that I wasn't interested in a pyramid
1218.679 - 1221.64: scheme she actually tried to keep
1219.919 - 1223.48: pitching it even after she admitted that
1221.64 - 1225.2: she understands she misled me she just
1223.48 - 1227.039: doubled down by saying she believed this
1225.2 - 1228.76: would be such a great opportunity for me
1227.039 - 1231.4: that's [ __ ] crazy it's crazy cuz I I
1228.76 - 1234.76: think like a lot of people that are in
1231.4 - 1236.48: mlms don't think that they are they
1234.76 - 1238.64: think that they're doing like legitimate
1236.48 - 1241.72: business but if you're using like sex
1238.64 - 1243.88: and attraction to like deceive people
1241.72 - 1245.919: into becoming a client or whatever like
1243.88 - 1247.5200000000002: that's got to feel wrong right that's
1245.919 - 1249.48: not normal that's what you do if you're
1247.52 - 1252.24: doing crime listen I know you wanted to
1249.48 - 1254.88: like get to know me and everything but
1252.24 - 1257.2: how would you like to get to know my 6'5
1254.88 - 1259.7990000000002: boyfriend as well he's really cool
1257.2 - 1261.1200000000001: seriously he's really cool this is ched
1259.799 - 1264.0: and no no don't leave don't leave
1261.12 - 1265.52: because guess what guess what we have an
1264.0 - 1267.48: opportunity you're going to want to hear
1265.52 - 1269.32: this out all right well was it Amway
1267.48 - 1272.039: what the [ __ ] is Amway why is it always
1269.32 - 1275.36: some like [ __ ] health supplement
1272.039 - 1276.72: company oh my god dude this is so funny
1275.36 - 1278.9599999999998: an entrepreneur-led health and
1276.72 - 1280.88: well-being company based in Ada Michigan
1278.96 - 1283.159: Amway enables independent business
1280.88 - 1285.5590000000002: owners to earn extra income at their own
1283.159 - 1288.0800000000002: pace be in business for yourself but
1285.559 - 1289.52: never by yourself is this a protein bar
1288.08 - 1291.6: company why wouldn't it just be like we
1289.52 - 1293.679: just sell supplements that make you feel
1291.6 - 1296.0: good what made you walk out of a date he
1293.679 - 1297.76: started rapping loudly and poorly to no
1296.0 - 1299.0: beat the first half of the DAT was so
1297.76 - 1300.84: normal that when he started his
1299.0 - 1302.679: freestyle I was convinced cameras were
1300.84 - 1304.12: going to pop up and tell me I was on a
1302.679 - 1305.64: hidden camera show after the six most
1304.12 - 1307.1999999999998: mortifying minutes of my life I stood up
1305.64 - 1308.3600000000001: put my hand over his mouth and told him
1307.2 - 1310.52: I was going to call it a night he
1308.36 - 1312.6399999999999: continued to rap under my hand and I got
1310.52 - 1314.76: my Pur and left the last text I got and
1312.64 - 1318.96: ignored was sorry for the awkward
1314.76 - 1320.799: situation Contin to wap on her M or I
1318.96 - 1322.96: said listen
1320.799 - 1326.36: what and
1322.96 - 1329.44: I that's so funny to be on a date that's
1326.36 - 1330.7199999999998: going well like normal you know it's
1329.44 - 1333.919: just you're both like laughing and
1330.72 - 1338.2: having a good time and you're
1333.919 - 1340.72: like H these Arta chokes are pretty good
1338.2 - 1342.64: I'm trying to think of
1340.72 - 1343.76: a this probably what that guy was
1342.64 - 1346.1200000000001: thinking I'm trying to think of like
1343.76 - 1348.52: Rhymes right now yeah yeah that's so
1346.12 - 1351.1589999999999: funny yeah no my aunt is also from m
1348.52 - 1354.2: Michigan that's [ __ ] crazy no that's
1351.159 - 1356.72: wild uh
1354.2 - 1358.279: these no yeah no my friend has a SCH
1356.72 - 1360.4: snower yeah I know they're the best
1358.279 - 1362.679: they're the best kind of dogs ah I'm
1360.4 - 1364.919: digging these art of chokes but the fact
1362.679 - 1366.799: they came with no sauce is kind of a
1364.919 - 1369.1200000000001: joke after this should we get a couple
1366.799 - 1372.0: drinks maybe make a toast to the two of
1369.12 - 1375.6789999999999: us and the life we might have that's for
1372.0 - 1377.48: show oh my God holy [ __ ] I feel like
1375.679 - 1379.2: that dude just got bad advice you know
1377.48 - 1380.88: you know he match for this girl maybe
1379.2 - 1382.6000000000001: he' just gotten out of long a long
1380.88 - 1384.159: relationship or he didn't you know he'
1382.6 - 1386.08: never been on a date before he has one
1384.159 - 1388.24: of his boys and they were like whatever
1386.08 - 1389.8799999999999: you do just make sure you freestyle
1388.24 - 1391.279: ladies love it so dat's going well and
1389.88 - 1393.0800000000002: all of a sudden that memory pops into
1391.279 - 1396.44: his head I haven't freestyled yet oh
1393.08 - 1398.279: [ __ ] ah what was your worst date I order
1396.44 - 1400.039: water she ordered a Coke when the waiter
1398.279 - 1401.96: left she burst into tears saying her and
1400.039 - 1404.44: her ex-boyfriend used to get the same
1401.96 - 1407.32: thing okay my ex-boyfriend always used
1404.44 - 1409.76: to get water just everything everything
1407.32 - 1412.3999999999999: makes me think of him you got water what
1409.76 - 1414.48: are the odds what are the odds God damn
1412.4 - 1416.039: it I said I wasn't going to cry what are
1414.48 - 1418.3600000000001: the odds probably going to get ice in it
1416.039 - 1420.4: too aren't you okay after that she was
1418.36 - 1422.36: inconsolable and thought I was going to
1420.4 - 1424.1200000000001: ditch her when she went to the bathroom
1422.36 - 1425.9599999999998: then she tried to get me to go get her
1424.12 - 1427.9189999999999: nipples pierced at the mall next to the
1425.96 - 1429.44: restaurant we were at poor girl man LW
1427.919 - 1431.44: she sounds super stable honestly she
1429.44 - 1433.559: sounds cool honestly you know probably
1431.44 - 1434.88: kind of fun for one date right why not
1433.559 - 1436.72: go get the [ __ ] nipples Pierce why
1434.88 - 1438.7990000000002: not she sounds [ __ ] batshit insane
1436.72 - 1441.3600000000001: that's fine for one date lean into it it
1438.799 - 1442.96: have fun get your nipples pierced too as
1441.36 - 1444.76: well also all right guys that's it for
1442.96 - 1446.48: this one hope you enjoyed uh if you have
1444.76 - 1448.52: a bad date story I'd actually love to
1446.48 - 1450.679: hear it so leave a comment with your
1448.52 - 1452.6399999999999: best date story or your worst date story
1450.679 - 1455.8400000000001: sorry and we'll go through all of them
1452.64 - 1459.6000000000001: and we'll compile a list for uh dates
1455.84 - 1462.1699999999998: from Hell episode 2 hope you enjoyed I
1459.6 - 1466.6789999999999: love you
1462.17 - 1466.679: [Music]
1467.36 - 1474.36: goodbye why play something these SMS a
1470.679 - 1478.44: like try I know they like twister you to
1474.36 - 1478.4399999999998: R celebrity over """
print(find_best(sample).text)