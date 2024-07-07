KEYWORDS = {
    # ----------------------form--------------------------------------
    "first name": ["firstname", "first_name", "forename", "first", "first-name"],
    "last name": ["lastname", "last_name", "surename", "last", "last-name"],
    "email": ["email", "e-mail", "username", "user_name", "user-name", 'type="email"'],
    "password": ["password"],
    "cv": ["cv", "resume", "curriculum", "vitae"],
    "birth date": ["birthdate", "birth", "dateofbirth", "date-of-birth", "birth-date"],
    "phone number": ["phonenumber", "phone", "telephone", "tel"],
    "house number": ["hausnummer"],
    "resident country": ["resident", "country"],
    "citizen country": ["citizen", "citizenship", "city"],
    "transcript": ["transcript"],
    "cover letter": ["coverletter", "cover", "letter"],
    "picture": ["picture"],
    "address": ["address", "location"],
    "linkedin": ["linkedin"],
    "github": ["github"],
    "xing": ["xing"],
    "twitter": ["twitter"],
    "website": ["website"],
    "zip": ["postalcode", "zip", "zip-code", "postal"],
    "city": ["city"],
    "salary": ["salary"],
    "sex": ["sex", "gender"],
    "available from": ["noticeprieod"],
    #'file':['type="file"'],
    "captcha": ["captcha"],
    "submit": ["apply", 'type="submit"'],
    "cancel": ["cancel"],
    "fake": ["fake"],
    "custom question": ["question"],
    "privacy": ["agree"],
    "recommender": ["recommendation"],
    "work here before": ["workherebefore"],
    "find us": ["find"],
    "dropbox": ["dropbox"],
    "google drive": ["google drive"],
    "work hours": ["workhours"],
    "workduration": [""],
    "visa": ["visa"],
    #'eligible':['eligible'],
    "german language level": ["germanlevel"],
    "company": [""],  # current company
    "willing to relocate": [""],
    "university enrollment": [],  # are a student?
    "english language level": [],
    # important about job
    # important about jobplace?
    # -------------------------------------------------------------------
    # -----------------------------------btns ---------------------------
    "login": ["login", "sign"],
    "username": ["username"],
    "register": ["register", "sign"],
    "cookie": ["cookie"],
    "next": ["apply now", "next"],
    "search": [],
    "other": ["other"],
    "newsletter": [],
    #'apply':['apply'],
    # -------------------------------------------------------------------
}

# LABEL_INDEX_TO_KEY = list(KEYWORDS.keys())

LABEL_INDEX_TO_KEY = [
    "birth",
    "major",
    "cookie",
    "search",
    "city",
    "English language level",
    "years of experience",
    "forgot password",
    "next",
    "username",
    "address",
    "website language",
    "latitude",
    "distance",
    "cv",
    "phone number",
    "transcript",
    "english language level",
    "register",
    "pronoun",
    "university",
    "cancel",
    "job",
    "company",
    "longitude",
    "age",
    "house number",
    "skill",
    "italian language level",
    "visa",
    "title",
    "twitter",
    "captcha",
    "civic number",
    "zip",
    "find us",
    "recommender",
    "available from",
    "linkedin",
    "submit",
    "email",
    "salary",
    "newsletter",
    "first name",
    "German language level",
    "show password",
    "last name",
    "ethnicity",
    "github",
    "cover letter",
    "graduation year",
    "sex",
    "password",
    "privacy",
    "login",
    "job title",
    "subscribe",
    "picture",
    "country",
    "xing",
    "career level",
]
i = 0
LABEL_KEY_TO_INDEX = {}
for key in KEYWORDS:
    LABEL_KEY_TO_INDEX[key] = i
    i += 1





import os
from bs4 import BeautifulSoup,PageElement,Comment
import pandas as pd


def preprocess_form(form):
    if isinstance(form,str):
        form = BeautifulSoup(form,'html.parser')
        
    form:PageElement
    comments=form.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment.extract()
    all_tags = form.find_all()

    # Remove all tags except for 'link', 'input', and 'select' tags
    for i,element in enumerate(all_tags):
        element:PageElement
        for k in ['style','class','bounding_box_rect','is_clickable']:
            if k in element.attrs:
                    del element[k]
                    pass
           
        if 'type' in element.attrs and element.attrs['type']=='hidden':
            element.unwrap()
            pass
            
        
        #if element.name  in ['div','text']: 
        if element.name not in ['a', 'input', 'select','radio','button','textarea','checkbox','option']:
            
            element.unwrap()
            #print(element)
            pass
        else:
            #element['backend_node_id']=i
            pass

            
                
            
    #print(form.prettify() )
    return form
    
import re

def get_query_element(f):
    query_element=[]
    mytext  = ''
    texts = []
    
    for element in f:
        # Get the text before the element
        #print('-----------------------------')
        if element.name == None:
            t = element.text.replace('\n','').replace('\t','').strip()
            if t!='' and len(t)>2:
                #mytext+=t+'\n '
                texts.append(t)
        else:
            
            
            mytext = ''.join(texts[-1:]) +' '+ element.text.strip()
            element : PageElement
            nid = element['nid']
            visible = element['visible']
            del element['nid']
            del element['visible']
            
            query_element.append({'query':mytext,'element': str(element).replace('\n','').replace('  ','').strip(),'nid':nid,'visible':visible})
            
            mytext =''
            texts=[]
        
    return query_element


def get_query_html(f):
    f:PageElement
    childs = f.find_all(string=True,recursive=False)
    for c in childs:
        print('---------------------')
        print(c)
    pass
    
    
    
