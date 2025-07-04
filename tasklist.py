# TODO: () Get keras.model.predict method working: Matrix-to-matrix prediction is essential #FIX: Apply predict on arrays
# TODO: () Get smallest scale system functional: perform keras model fit on matrix to matrix inference between different dimensions #BUG:zsh killed (fixed)
# TODO: Code bigger systems. Use Time-Series datasets (for automatic stratification) if stratified sampling rare 
# TODO: () Get a most straightforward Network up-and-running (only direct links between data-nodes), guaranteed to predict reasonably between data-environments for at least one benchmark
# TODO: Suggest more ways of inter-data-environmental inference (upgrades over DL)
# TODO: Template-data for construction need search (For the moment use any arbitrary databank)
# TODO: Work needs structure
# TODO: Find methods of extracting features from data, feature-confirmation results from confirmed relevance in inference
# TODO: Plan for revenue: software for specialized hardware. One computer in one case, comparable to a macbook
# TODO: Construct, optimize, and demonstrate, include self-loops on Node

# TODO: GET ONE NODE-GENERATOR FUNCTIONAL AND STARSYSTEM-COMPATIBLE (MINIMAL COMPLETE)
# TODO: GET ONE STARSYSTEM FUNCTIONAL, GENERALIZED, OPTIMIZED (CURRENT TASK)
# TODO: TEMPORARILY, COLLECT ANY ENVIRONMENT BY SEIZING MANUALLY 

# TODO: FOCUS ON THE LEARNING SYSTEMS, SIMULATE ALL ENVIRONMENTS OF DEPLOYMENT FOR CONSTRUCTION



##########################################################################################
# TODO: DSM solution k-means clustering
##########################################################################################


#Next_Start = Outer_link.pop(0)
#internalTraverse = getAllExternalLinks(Next_Start)[0]


def getAllExternalLinks(siteUrl, expansion_limit):
    
    #expansion_tracker = 0
    
    try:
        html = urlopen(siteUrl)
    except HTTPError as e:
        print("404")
        internalLinks = [siteUrl]
        externalLinks = []
        return [internalLinks, externalLinks]
    
    domain = '{}://{}'.format(urlparse(siteUrl).scheme,
    urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)
    
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            #print(link)
    
    ####################################################### 
    #if len(allExtLinks) > expansion_limit:
    #    return [internalLinks, externalLinks]
    #######################################################  
        
    for link in internalLinks:
        if link not in allIntLinks:
            print(link)
            allIntLinks.add(link)
            #expansion_tracker += 1
            getAllExternalLinks(link, expansion_limit)
                
    return [allExtLinks, allIntLinks]




def getAllExternalLinks(siteUrl, expansion_limit):
    
    try:
        html = urlopen(siteUrl)
    except HTTPError as e:
        print("404")
        internalLinks = [siteUrl]
        externalLinks = []
        return [internalLinks, externalLinks]
    
    domain = '{}://{}'.format(urlparse(siteUrl).scheme,
    urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)
    
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            #print(link)
    
    ####################################################### 
    if len(allExtLinks) > expansion_limit:
        return [allIntLinks, allExtLinks]
    #######################################################  
        
    for link in internalLinks:
        if link not in allIntLinks:
            print(link)
            allIntLinks.add(link)
            getAllExternalLinks(link, expansion_limit) 
         
    return [allExtLinks, allIntLinks]

