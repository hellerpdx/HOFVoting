from collections import Counter
import requests
from operator import itemgetter
from bs4 import BeautifulSoup, SoupStrainer

r = requests.get('http://bbwaa.com/14-hof-ballots/')

pick_table = SoupStrainer("tbody",class_="row-hover")

soup = BeautifulSoup(r.text, parse_only=pick_table)

yesplayer = "Mattingly"
noplayer = "Biggio"

def StolenVotes(noplayer):
    BSwriters = soup.find_all(class_="column-1")
    BSpicks = soup.find_all(class_="column-3")
    picks = []

    for i in BSpicks:
        picks.append(i.get_text().split())
    
    novotes = [i for i in picks if noplayer not in i]
    votes = []

    for i in novotes:
        for i in i:
            votes.append(i)

    vote_takers = Counter(votes).items()

    print "Total Published Ballots:", len(BSwriters)
    print "Ballots without " + noplayer, len(novotes)
    print "% without " + noplayer, round((float(len(novotes)) / float(len(BSwriters))) * 100, 2)

    print "These candidates recevieved votes from writers who did not vote for " + noplayer

    for i in sorted(vote_takers, key=itemgetter(1), reverse=True):
        print str(i[0]), i[1]

def a_not_b(a, b):
    picks_set = {}

    for writer in soup.find_all(class_="column-1"):
        BSpicks = writer.find_next_sibling(class_="column-3")
        picks_set[writer.get_text()] = BSpicks.get_text().split()
        
    writers = []
    for k, v in picks_set.items():
        if a in v:
            if b not in v:
                writers.append(k)
    print str(len(writers)) + " writer(s) picked "+ yesplayer +" but not " + noplayer + ":"
    for i in writers:
        print i

a_not_b(yesplayer, noplayer)

#StolenVotes(noplayer)






    





