import re
string="http://www.zombie-bites.com"
string2="http://google.com"

rmStr= string2.replace("http://","").replace("www.","")
print(rmStr[0:rmStr.index(".")])

def domain_name(url):
    from re import findall, VERBOSE
    
    try:
        url = findall("""\A
                        (?: http
                        s?
                        ://)?         # matches http:// or https:// or nothing
                        
                        (?: www.)?    # matches www. or nothing
                        
                        ([- a-z]+)    # matches a sequence of letters and dashes
                        
                        (?: .com|.ru)     # matches either .com or .ru
                        (?: [/ a-z]+)?    # matches a sequence or letters and slashes
                        \Z""", url, VERBOSE)
        return url[0]
    except:
        return "Invalid URL."
#print(matches)