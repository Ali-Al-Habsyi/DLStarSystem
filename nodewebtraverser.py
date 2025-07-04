################################################################################
# TOWARDS MACHINE ONE
# VIRTUAL DEVICES #1: NODE-GENERATION BY WEB-TRAVERSION OF MINIMAL SCALE
################################################################################
# --> (CURRENT) --> COLLECTORS OVER WWW
# DATA STORED, BUILD COLLECTOR MANUALLY
# NODE-GENERATOR EXAMPLE
# CURRENT RUNTIME UNTIL DATA LOADED: APPROX. 4 HOURS (PARAMETER DEPENDENT)
##########################################################################

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
import requests
import keras
import numpy as np

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

def getAllExternalLinks(siteUrl, counter, recursion_null, recursion_limit):
    
    recursion_null += 1
    if recursion_null == recursion_limit:
        return
    
    try:
        html = urlopen(siteUrl)   
        domain = '{}://{}'.format(urlparse(siteUrl).scheme,
            urlparse(siteUrl).netloc)
        bs = BeautifulSoup(html, 'html.parser')
        internalLinks = getInternalLinks(bs, domain)
        externalLinks = getExternalLinks(bs, domain)
    except Exception as e:
        return
        
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(counter)
            print(link)
            
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link, counter, recursion_null, recursion_limit)
    return
 
################################################################################
# <> WEB TRAVERSOR <>
################################################################################  

global allExtLinks
global allIntLinks 
recursion_limit = 4
recursion_null = 0
node_count = 4
count = 0
Starting_link = "https://keras.io/examples/generative/text_generation_with_miniature_gpt/"
Outer_link = []
Inner_link_dict = {}
Outer_link.append(Starting_link)
allExtLinks = set()
allIntLinks = set()
getAllExternalLinks(Starting_link, count, recursion_null, recursion_limit)
Inner_link_dict[Starting_link] = allIntLinks

for link in allExtLinks:
    Outer_link.append(link)      

for i in range(node_count):
    count += 1
    
    try:
        Next_Start = Outer_link.pop(4)
        
        allExtLinks = set()
        allIntLinks = set()
        getAllExternalLinks(Next_Start, count, recursion_null, recursion_limit)

        print(Next_Start)
        Inner_link_dict[Next_Start] = allIntLinks
        
        for link in allExtLinks:
            Outer_link.append(link)
    except Exception as e:
        continue

################################################################################
# <> HTML COLLECTOR <> works!
################################################################################  

Inner_link_dict_keys = Inner_link_dict.keys()
HTMLCollection = {}
for outer_link in Inner_link_dict.keys():
    HTMLCollection[outer_link] = {}
    for inner_link in Inner_link_dict[outer_link]:
        HTMLCollection[outer_link][inner_link] = {}

for outer_link in Inner_link_dict_keys:
    for inner_link in Inner_link_dict[outer_link]:
        
        # Fix HTML reader: Under construction (search for proper encoders/decoders) **********
        try:
            TraverseLocation = inner_link
            fp = urllib.request.urlopen(TraverseLocation)
            mybytes = fp.read()
            mystr = mybytes.decode("utf8")
        except Exception:
            continue
        HTMLCollection[outer_link][inner_link] = mystr 

################################################################################
print("========= MILEPOINT HTML COLLECTION COMPLETE =========")    

################################################################################

################################################################################
# <> LSTM INFERENCE <> |Under Construction and upgrade later|
# HTML COLLECTOR COMPLETE
# COMPLETE CONSTRUCTION OF LEARNING SYSTEM
################################################################################  

NodeTraverseSurface = Inner_link_dict
Root_Nodes = Inner_link_dict.keys()

Outer_Node_batch = []

NodeLearner = {}
for outer_link in NodeTraverseSurface.keys():
    NodeLearner[outer_link] = {}
    for inner_link in NodeTraverseSurface[outer_link]:
        NodeLearner[outer_link][inner_link] = {}

for outer_link in Root_Nodes:
    
    Inner_Node_batch = []
    for inner_link in NodeTraverseSurface[outer_link]:
        
        print("========= MILEPOINT LSTM INFERENCE INITIATED =========")    
        
        maxlen = 60
        step = 3
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
        for j, sentence in enumerate(sentences):
            for t, char in enumerate(sentence):
                x[j, t, char_indices[char]] = 1
            y[j, char_indices[next_chars[j]]] = 1
            
            
        Node = keras.models.Sequential()
        Node.add(keras.layers.LSTM(128, input_shape=(maxlen, len(chars))))
        Node.add(keras.layers.Dense(len(chars), activation='softmax'))
        optimizer = keras.optimizers.RMSprop(lr=0.01)
        Node.compile(loss='categorical_crossentropy', optimizer=optimizer)
        Node.fit(x, y, batch_size=128, epochs=1)

            
        Inner_Node_batch.append(Node)
    Outer_Node_batch.append(Inner_Node_batch)
   
################################################################################
print("========= MILEPOINT INFERENCE COMPLETE =========")        
exit()
################################################################################

# CODE BIN

################################################################################
# <----> MILEPOINT FULLY FUNCTIONAL <---->
################################################################################  

def HTMLCollector(Starting_link, node_count, expansion_limit):
    
    NodeTraverseSurface = NodeTraverseSurface(Starting_link, node_count, expansion_limit)   
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

NodeTraverseSurface = Inner_link_dict
Root_Nodes = Inner_link_dict.keys()

#NodeTraverseSurface = NodeTraverseSurface(Starting_link)   
#Root_Nodes = NodeTraverseSurface.keys()

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

# APPLY TO STAR-SYSTEM 
# EXTENSION TOWARDS GTP LEARNER (SEE KERAS DOCS)