try :
    from googlesearch import search
    import pandas as pd
    #import tldextract
except ImportError:
    print ("No module named google found")
import re

def reg_exp_setting(website,domain):
    match = re.search("[.](.+?)[.][in]",website);
    if match:
        return match.group(0)

def get_websites(query, domain):
    for j in search(query, tld=domain, num=50, stop=100, pause=2):

        match = reg_exp_setting(str(j),domain)
        if match != None:
            print j
            print match
        if match != None and query in match:
            print match

        # if query in match:
        #     print match




get_websites("protein", "com")

