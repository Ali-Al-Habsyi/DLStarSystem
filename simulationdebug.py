
# DRAWING BOARD --> CODE
# FOCUS ON DL, KEEP DATA-COLLECTION PURE
import urllib.request
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random
import urllib.request
from urllib.error import HTTPError




Outer_link = []
for i in range(50):
    Outer_link.append(i)
    
print(Outer_link)
Next_Start = Outer_link.pop(0)
print(Outer_link)
print(Next_Start)

global allExtLinkstest
global allIntLinkstest
#global expansion_limit
#expansion_limit = 0

allExtLinkstest = set()
allIntLinkstest = set()

Outer_link = []
Inner_link_dict = {}
node_count = 10
#expansion_limit = 19

# WORKS
def NodeTraverseSurface(Starting_link, node_count):
    
    iterator = []
    for i in range(node_count):
        iterator.append(i)
        
    #Outer_link = []
    Inner_link_dict = {}

    #Outer_link.append(Starting_link)
    
    allExtLinkstest = set()
    allIntLinkstest = set()
    for j in range(50):
        allExtLinkstest.add(j)
        allIntLinkstest.add(j)
    
    Inner_link_dict[Starting_link] = allIntLinkstest

    
    for i in range(node_count):

        #Next_Start = Outer_link.pop(0)
        
        allExtLinkstest = set()
        allIntLinkstest = set()
        
        for j in range(node_count * i):
            allExtLinkstest.add(j)
            allIntLinkstest.add(j)

        Inner_link_dict[i] = allIntLinkstest
        
            
        #if len(allExtLinks) == 0:
        #    return "len(allExtLinks) = 0"
        #else:
        #    for link in allExtLinks:
        #        Outer_link.append(link)
                    
    return Inner_link_dict # type check
        


Starting_link = "https://keras.io/examples/generative/text_generation_with_miniature_gpt/"
NodeTraverseSurface = NodeTraverseSurface(Starting_link, node_count) 

print(NodeTraverseSurface)
    
exit()