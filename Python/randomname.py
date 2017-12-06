#This module is the result of my early efforts to learn Python.  Basically I thought
#that Python would be well suited to a task that had defeated me previously in my
#attempts to do it in other languages, which was to write a random-name generator.
#(The sort of thing that might come in handy if you play roguelike games).
#I found it so easy that I decided to write a whole bunch of 'extras' to accompany the
#original function (now called namer3s).  Here they all are.

#namer3s generates a long-ish name.
def namer3s():
    Inconst = ['W', 'R', 'T', 'W', 'W', 'W', 'W', 'W', 'W', 'U', 'P', 'S', 'D', 'F', 'G', 'H', 'J']
    Insyllb = ['art', 'av', 'eun', 'em', 'ill', 'it', 'ol', 'ower', 'ull', 'ulc']
    Ensyllb = ['ax', 'ea', 'ia', 'on', 'ur']
    import random
    First = random.choice(Inconst)
    Second = random.choice(Insyllb)
    Third = random.choice(Ensyllb)
    gummy = "%s%s%s" % (First, Second, Third)
    return gummy

#namer2s generates a short name.  In its current form it has a very limited range of
#syllables to choose from, but that's easily remedied.
def namer2s():
    Inconst = ['W', 'R', 'T', 'W', 'B', 'W', 'W', 'G', 'H', 'U', 'P', 'S', 'D', 'F', 'G', 'H', 'J']
    Ensyllb = ['ald', 'eve', 'iotr', 'olov', 'ume', 'ull', 'ara']
    import random
    First = random.choice(Inconst)
    Second = random.choice(Ensyllb)
    gummy = "%s%s" % (First, Second)
    return gummy

#lnamer generates a short name followed by a longer name.  It merely calls the two functions
#above in succession and whacks them into a string.
def lnamer():
    gummy = "%s %s" % (namer2s(), namer3s())
    return gummy

#rnamer randomly chooses to run either namer2s, namer3s, or lnamer. Wow.
def rnamer():
    coinflip = [1, 2, 3]
    import random
    side = random.choice(coinflip)
    if side == 1:
        gummy = namer3s()
    elif side == 2:
        gummy = namer2s()
    else:
        gummy = lnamer()
    return gummy

#xnamer takes a different approach altogether.  It only has one list of components,
#from which it takes from 1-7 items and knocks them together.  In some ways more
#interesting names are produced, but unpronouncables are far more common also.
def xnamer():
    import random, string
    letters = ['w', 'r', 't', 'b', 'x', 'a', 'd', 'e', 'm', 'u', 'k', 's', 'd', 'f', 'g', 'h', 'j',
               'art', 'av', 'eun', 'em', 'ill', 'it', 'ol', 'ower', 'ull', 'ulc',
               'ax', 'ea', 'ia', 'on', 'ur', 'ald', 'eve', 'iotr', 'olov', 'ume', 'mm',
               'ge', 'gu', 'ma', 'y', 'to', 'even', 'st', 'anforth', 'th', 'th', 'p',
               'qu', 'oi', 'ja', 'lle', 'z', 'v', 'c', 'b', 'mn', 'nm', 'y', 'ir',
               'an', 'da', 'is', 'ge', 'or', 'gi', 'a', 'al', 'ter', 'lly', 'oto']
    parts = [1, 2, 3, 4, 5, 6, 7]
    numparts = random.choice(parts)
    repeater = range(numparts)
    gummy = ""
    for item in repeater:
        gummy = gummy + random.choice(letters)
    gummy = string.capitalize(gummy)
    return gummy

#lengthnamer generates xnamer names until it gets one of the desired length.
#note that asking for a long name (more than about 15 characters) will cause
#an indefinitely long loop.  Avoid, dude.  Also note that it is the only one of
#these functions that actually takes an argument.
def lengthnamer(namelength):
    gummy = ""
    while len(gummy) != namelength:
        gummy = xnamer()
    return gummy

#getter gets you a name of a specific length with a specific initial
def getter(initial, length):
    import string
    gummy = "@"
    initial = string.capitalize(initial)
    begin = "%c" % (initial)
    while gummy[0] != begin:
        gummy = lengthnamer(length)
    return gummy
