################################################################################
# TOWARDS MACHINE ONE
# VIRTUAL DEVICES #1: NODE-GENERATION BY WEB-TRAVERSION OF MINIMAL SCALE
################################################################################
# --> (CURRENT) --> COLLECTORS OVER WWW
# DATA STORED, BUILD COLLECTOR MANUALLY
#########################################################
# TOWARDS MACHINE ONE: COMPLETE FIRST NODE GENERATOR
#########################################################


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

#######################################################
# EXTEND THE BELOW TO FULL (DATAGENERATOR ESSENTIAL)
# DATA CONVOLUTED
#######################################################
# CONTINUE LATER


# SYSTEM CONPATIBLE SET-UP
# 1 DATA NODE FOR 1 SITE

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
            
            
pages = set()
random.seed(datetime.datetime.now())
#Retrieves a list of all Internal links found on a page
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

#Retrieves a list of all external links found on a page
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
                    

# NODE LABELING BY LINK (FIRST LANDING HTML-PLATFORM FOR EXTERNAL)
# COLLECT LINKS: EXTERNAL -> INTERNAL
# CRAWL OVER EXTERNAL ONCE EVERY N INTERNAL CRAWLS
# FULL SCOPE LINKS EXTERNAL

def getAllExternalLinksnew(siteUrl):

    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme,
    urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)
    
    for link in externalLinks:
        if link not in externalLinks:
            externalLinks.add(link)
            print(link)
            
        for link in internalLinks:
            if link not in internalLinks:
                internalLinks.add(link)
                getAllExternalLinks(link)
    return externalLinks
     
# Collects a list of all external URLs found on the site
allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme,
    urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
            for link in internalLinks:
                if link not in allIntLinks:
                    allIntLinks.add(link)
                    getAllExternalLinks(link)


allIntLinks.add('http://oreilly.com')
getAllExternalLinks('http://oreilly.com')

exit()     
            
     
# FULL TRAVERSION ONE SITE
def getAllInternalLinks(siteUrl):
    
    allIntLinks = set()
    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme,
    urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
 
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllInternalLinks(link)
    return allIntLinks     

# TRAVERSE NEXT SITE IN COLLECTION EXTERNAL LINKS
def getAllExternalLinks(siteUrl):
    
    allExtLinks = set()
    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme,
    urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
        for link in internalLinks:
            if link not in internalLinks:
                internalLinks.add(link)
                getAllExternalLinks(link)
    
    return allExtLinks
  
################################################################################
# <----> MILEPOINT FULLY FUNCTIONAL <---->
################################################################################  
  
# COLLECT ALL ERROR CASES

########################################################################
# FULL INTERNAL TRAVERSION STARTING SITE 
# EXTERNAL-TRAVERSE STARTING SITE IN FULL -> COLLECT IN OUTER_LINKS
# ITERATE UNTIL BREAK CONDITION
    # FULL INTERNAL TRAVERSION NEXT ENTRY OUTER_LINKS SITE X
    # EXTERNAL-TRAVERSE SITE X IN FULL -> COLLECT IN OUTER_LINKS
########################################################################

# if "main" == __main__ 
Starting_link = 'https://deepmind.google/technologies'  
internalTraverse = getAllInternalLinks(Starting_link)
print(internalTraverse)


def NodeTraverseSurface(Starting_link):
    
    Outer_link = []
    Inner_link_dict = {}

    Outer_link.append(Starting_link)
    internalTraverse = getAllInternalLinks(Starting_link)
    
    if len(internalTraverse) == 0:
        return None
    else:
        Inner_link_dict[Starting_link] = internalTraverse
        allexternallinks = getAllExternalLinks(Starting_link)
        if len(allexternallinks) == 0:
            return "Error Root_site closed site"
        else:
            for link in allexternallinks:
                Outer_link.append(link)
    
    Next_Start = Outer_link.pop(0)
    
    Outer_link.append(Next_Start)
    internalTraverse = getAllInternalLinks(Next_Start)
    
    if len(internalTraverse) == 0:
        return None
    else:
        Inner_link_dict[Next_Start] = internalTraverse
        allexternallinks = getAllExternalLinks(Starting_link)
        if len(allexternallinks) == 0:
            return "Error Root_site closed site"
        else:
            for link in allexternallinks:
                Outer_link.append(link)
                           
    return Inner_link_dict

NodeTraverseSurface = NodeTraverseSurface(Starting_link)     
Root_Nodes = NodeTraverseSurface.keys()

#######################################################################################
# EXTRACT HTML PLATFORMS FOR LINKS, AND APPLY DIRECTLY (UNPROCESSED) TO LEARNING SYSTEM
#######################################################################################

# COLLECT HTML IN DICT OF NodeTraverseSurface HULL


def HTMLCollector(Starting_link):
    
    NodeTraverseSurface = NodeTraverseSurface(Starting_link)   
    Root_Nodes = NodeTraverseSurface.keys()
    
    HTMLCollection = {}
    for outer_link in NodeTraverseSurface.keys():
        HTMLCollection[outer_link] = {}
        for inner_link in NodeTraverseSurface[outer_link]:
            HTMLCollection[outer_link][inner_link] = {}
        
    for outer_link in Root_Nodes:
        for inner_link in NodeTraverseSurface[outer_link]:

            TraverseLocation = inner_link

            fp = urllib.request.urlopen(TraverseLocation)
            
            mybytes = fp.read()
            mystr = mybytes.decode("utf8")
            fp.close()
            
            HTMLCollection[outer_link][inner_link] = mystr
            
    return HTMLCollection

######################################################################## 
# NODE LEARNING (LSTM GENERATIVE FOR NEURALNET ACCESS) #################
########################################################################

import keras
import numpy as np

# TEXT IS PURE HTML

def NodeLSTMLearner(Starting_link, maxlen, step):
    
    NodeTraverseSurface = NodeTraverseSurface(Starting_link)   
    Root_Nodes = NodeTraverseSurface.keys()
    
    NodeLearner = {}
    for outer_link in NodeTraverseSurface.keys():
        NodeLearner[outer_link] = {}
        for inner_link in NodeTraverseSurface[outer_link]:
            NodeLearner[outer_link][inner_link] = {}

    

    HTMLCollection = HTMLCollector(Starting_link)
    for outer_link in Root_Nodes:
        for inner_link in NodeTraverseSurface[outer_link]:
            
            maxlen = maxlen
            step = step
            sentences = []
            next_chars = []
            text = HTMLCollection[outer_link][inner_link] 
            
            for i in range(0, len(text) - maxlen, step):
                
                sentences.append(text[i: i + maxlen])
                next_chars.append(text[i + maxlen])
                print('Number of sequences:', len(sentences))
                chars = sorted(list(set(text)))
                print('Unique characters:', len(chars))
                char_indices = dict((char, chars.index(char)) for char in chars)
                print('Vectorization...')
                x = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
                y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
                for i, sentence in enumerate(sentences):
                    for t, char in enumerate(sentence):
                        x[i, t, char_indices[char]] = 1
                    y[i, char_indices[next_chars[i]]] = 1
                    
                Node = keras.models.Sequential()
                Node.add(keras.layers.LSTM(128, input_shape=(maxlen, len(chars))))
                Node.add(keras.layers.Dense(len(chars), activation='softmax'))
                optimizer = keras.optimizers.RMSprop(lr=0.01)
                Node.compile(loss='categorical_crossentropy', optimizer=optimizer)
                Node.fit(x, y, batch_size=128, epochs=1)
  

  
  

  
  
# ====> PROCEED LEARNING           
# EXPERIMENT: 1 DATA-NODE TRAVERSED OVER EXTENT OF INTERNET ONLY LIMITED BY COMPUTER
# TRAVERSER ONE !
# CONTINUE CONSTRUCTION
exit()


# NODE GENERATION BY WEB-TRAVERSION EXTEND ON THE ABOVE BASIS
    # GTP LEARNER (SEE KERAS DOCS)
    # DOMAIN EXTRACTOR AFTER EXTERNAL EXPANSION (USE REGEX)
    # PAGE DATA CHARACTERIZATION
    # ... EXTEND FIRST