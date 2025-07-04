################################################################################
# TOWARDS MACHINE ONE
# VIRTUAL DEVICES #1: NODE-GENERATION BY WEB-TRAVERSION OF MINIMAL SCALE
################################################################################
# --> (CURRENT) --> COLLECTORS OVER WWW
# DATA STORED, BUILD COLLECTOR MANUALLY

# NODE-GENERATOR EXAMPLE
#######################################

# DRAWING BOARD --> CODE
# FOCUS ON DL, KEEP DATA-COLLECTION PURE
from ast import Try
import urllib.request
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random
import urllib.request
from urllib.error import HTTPError

#fp = urllib.request.urlopen("http://www.python.org")
#mybytes = fp.read()

#mystr = mybytes.decode("utf8")
#fp.close()

#print(mystr)

# SYSTEM CONPATIBLE SET-UP
# 1 DATA NODE FOR 1 SITE
################################################################################
################################################################################
# INTRALINK LEARNING BY INTERNAL LINK SAMPLING
def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme,
    urlparse(includeUrl).netloc)
    internalLinks = []
    #Finds all links that begin with a "/"
    for link in bs.find_all('a',
    href=re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith('/')):
                    internalLinks.append(
                    includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

# DATA NODE EXPANSION BY TRAVERSING EXTERNAL LINKS
def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    #Finds all links that start with "http" that do
    #not contain the current URL
    for link in bs.find_all('a',
        href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


# LIMIT ITERARTION EXPANSION

global allExtLinks
global allIntLinks 
#global expansion_limit
#expansion_limit = 0

allExtLinks = set()
allIntLinks = set()

# ADD ERROR HANDLER
def getAllExternalLinks(siteUrl):
    
    try:
        html = urlopen(siteUrl)   
        domain = '{}://{}'.format(urlparse(siteUrl).scheme,
            urlparse(siteUrl).netloc)
        bs = BeautifulSoup(html, 'html.parser')
        internalLinks = getInternalLinks(bs, domain)
        externalLinks = getExternalLinks(bs, domain)
    except HTTPError as error:
        return
        
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            #print(link)
            
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link)
    return
 
################################################################################
################################################################################

########################################################################
# FULL INTERNAL TRAVERSION STARTING SITE 
# EXTERNAL-TRAVERSE STARTING SITE IN FULL -> COLLECT IN OUTER_LINKS
# ITERATE UNTIL BREAK CONDITION
    # FULL INTERNAL TRAVERSION NEXT ENTRY OUTER_LINKS SITE X
    # EXTERNAL-TRAVERSE SITE X IN FULL -> COLLECT IN OUTER_LINKS
########################################################################

# if "main" == __main__ 
########################################################################
########################################################################
########################################################################
########################################################################
# LINK INTERNAL AND EXTERNAL FUNCTUINAL UP TO 404 ERROR HANDLER
# SOLUTION BY INTERNAL LINK COLLECTOR FIX OR NODE REDEFENITION
# PROCEED WITH STAR-SYSTEM COMPANTIBILITY



# NODE LABELING BY LINK (FIRST LANDING HTML-PLATFORM FOR EXTERNAL)
# COLLECT LINKS: EXTERNAL -> INTERNAL
# CRAWL OVER EXTERNAL ONCE EVERY N INTERNAL CRAWLS
# FULL SCOPE LINKS EXTERNAL








# TEST PYTHON DICTIONARIES
#node_count = 10
#Starting_link = "https://keras.io/examples/generative/text_generation_with_miniature_gpt/"

#allExtLinks = set()
#allIntLinks = set()
#getAllExternalLinks(Starting_link) # <- fix...

#print(len(allExtLinks))
#print(len(allIntLinks))


#allExtLinks = set()
#allIntLinks = set()

#print(len(allExtLinks))
#print(len(allIntLinks))

#getAllExternalLinks(Starting_link) # <- fix...

#print(len(allExtLinks))
#print(len(allIntLinks))

#exit()


Inner_link_dict = {}

# TEST PYTHON DICTIONARIES
node_count = 10



allExtLinks = set()
allIntLinks = set()

print("-------------------------------------")

Starting_link = "https://keras.io/examples/generative/text_generation_with_miniature_gpt/"
print(Starting_link)

getAllExternalLinks(Starting_link) # <- fix...

Inner_link_dict[Starting_link] = allIntLinks

allExtLinkslist = []
allIntLinkslist = []
# fix this
for link in allIntLinks:
    allIntLinkslist.append(link)
# fix this
for link in allExtLinks:
    allExtLinkslist.append(link)
# fix this, fixed

print(len(allExtLinkslist))
print(len(allIntLinkslist))


print("Inner_link_dict")
print(Inner_link_dict.keys())

print("-------------------------------------")

ext_1 = allExtLinkslist[0]
print(ext_1)

allExtLinks = set()
allIntLinks = set()

getAllExternalLinks(ext_1) # <- fix new bug ...

Inner_link_dict[ext_1] = allIntLinks

allExtLinkslist = []
allIntLinkslist = []
for link in allIntLinks:
    allIntLinkslist.append(link)
    
for link in allExtLinks:
    allExtLinkslist.append(link)

print("-------------------------------------")
#print(ext_1)

ext_1 = allExtLinkslist[0]
print(ext_1)

allExtLinks = set()
allIntLinks = set()

getAllExternalLinks(ext_1) # <- fix new bug ...

Inner_link_dict[ext_1] = allIntLinks

allExtLinkslist = []
allIntLinkslist = []
for link in allIntLinks:
    allIntLinkslist.append(link)
    
for link in allExtLinks:
    allExtLinkslist.append(link)

print("-------------------------------------")


ext_1 = allExtLinkslist[0]

allExtLinks = set()
allIntLinks = set()

getAllExternalLinks(ext_1) # <- fix new bug ...

Inner_link_dict[ext_1] = allIntLinks

allExtLinkslist = []
allIntLinkslist = []
for link in allIntLinks:
    allIntLinkslist.append(link)
    
for link in allExtLinks:
    allExtLinkslist.append(link)



#getAllExternalLinks(ext_1) # <- fix new bug ...

#allExtLinkslist = []
#allIntLinkslist = []
#for link in allIntLinks:
#    allIntLinkslist.append(link)
    
#for link in allExtLinks:
#    allExtLinkslist.append(link)

print(len(allExtLinks))
print(len(allIntLinks))
print("-------------------------------------")

print(ext_1)

Inner_link_dict[ext_1] = allIntLinks
print("Inner_link_dict")
print(Inner_link_dict.keys())
print(len(Inner_link_dict))
print("-------------------------------------")



ext_2 = allExtLinkslist[0]

allExtLinks = set()
allIntLinks = set()
print(ext_1)

print("-------------------------------------")







getAllExternalLinks(ext_2) # <- fix new bug ...




allExtLinkslist = []
allIntLinkslist = []

for link in allIntLinks:
    allIntLinkslist.append(link)
    
for link in allExtLinks:
    allExtLinkslist.append(link)
    


print(len(allExtLinks))
print(len(allIntLinks))
print("-------------------------------------")

ext_3 = allExtLinkslist[0]
print(ext_1)

Inner_link_dict[ext_3] = allIntLinks
print("Inner_link_dict")
print(Inner_link_dict.keys())
print(len(Inner_link_dict))
print("-------------------------------------")

# Extend solution to nodetraverser.py


exit()




print("--debug node works --> nodetraverser works")

allExtLinks = set()
allIntLinks = set()
getAllExternalLinks(Starting_link) # <- fix...
print(len(allExtLinks))
print(len(allIntLinks))

    
    
        
    
        
    
 
    
        
    
        
    
        
    
        
    
        
    
    
    
#print(Outer_link)
#Next_Start = Outer_link.pop(0)
#print(Outer_link)
#print(Next_Start)





Outer_link = []
for i in range(50):
    Outer_link.append(i)
    
print(Outer_link)
Next_Start = Outer_link.pop(0)
print(Outer_link)
print(Next_Start)


Outer_link = []
Inner_link_dict = {}
node_count = 10
#expansion_limit = 19


# DEBUG FURTHER

def NodeTraverseSurface(Starting_link, node_count):
    
    Outer_link = []
    Inner_link_dict = {}

    Outer_link.append(Starting_link)
    
    allExtLinks = set()
    allIntLinks = set()
    getAllExternalLinks(Starting_link) # <- fix...

    Inner_link_dict[Starting_link] = allIntLinks
      
    if len(allExtLinks) == 0:
        if len(Outer_link) == 0:
            return Inner_link_dict
    else:
        for link in allExtLinks:
            Outer_link.append(link)   
               
    for i in range(node_count):

        if len(Outer_link) == 0:
            return Inner_link_dict
        Next_Start = Outer_link.pop(0)
        
        allExtLinks = set()
        allIntLinks = set()
        getAllExternalLinks(Next_Start)

        print(Next_Start)
        Inner_link_dict[Next_Start] = allIntLinks
         
        if len(allExtLinks) == 0:
            if len(Outer_link) == 0:
                return Inner_link_dict
        else:
            for link in allExtLinks:
                Outer_link.append(link) # assume >= 1 entry extlinks
                    
    return Inner_link_dict # type check
        



Starting_link = "https://keras.io/examples/generative/text_generation_with_miniature_gpt/"
NodeTraverseSurface = NodeTraverseSurface(Starting_link, node_count)     

count = 0

Starting_link = "https://keras.io/examples/generative/text_generation_with_miniature_gpt/"

Outer_link = []
Inner_link_dict = {}

Outer_link.append(Starting_link)

allExtLinks = set()
allIntLinks = set()
getAllExternalLinks(Starting_link, count) 

Inner_link_dict[Starting_link] = allIntLinks

for link in allExtLinks:
    Outer_link.append(link)      

for i in range(node_count):
    count += 1
    
    try:
        Next_Start = Outer_link.pop(0)
        
        allExtLinks = set()
        allIntLinks = set()
        getAllExternalLinks(Next_Start, count)

        print(Next_Start)
        Inner_link_dict[Next_Start] = allIntLinks
        
        if len(allExtLinks) > 0:
            for link in allExtLinks:
                Outer_link.append(link) # assume >= 1 entry extlinks
    except HTTPError:
        break
                
print(len(Inner_link_dict))
print(Inner_link_dict.keys())
print(NodeTraverseSurface)
print(len(NodeTraverseSurface))
print(type(NodeTraverseSurface))


exit()

################################################################################
# <----> MILEPOINT FULLY FUNCTIONAL <---->
################################################################################  

# IF URL SCRAPING TOO SPECIALIZED, EXTRACT DATA FROM DATABANK AND PROCEED LEARNER FURTHER

################################################################################
# <^^^> WEBSCRAPE PART <^^^>
################################################################################  

################################################################################
# <> DATA COLLECTION PART <>
################################################################################  

