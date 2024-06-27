KEYWORDS={
        #----------------------form--------------------------------------
       'firstname':['firstname','first_name','forename','first','first-name'],
       'lastname':['lastname','last_name','surename','last','last-name'] ,
       'email':['email','e-mail','username','user_name','user-name','type="email"'], 
       'password':['password'], 
       'cv':['cv','resume','curriculum','vitae'],
       'birthdate':['birthdate','birth','dateofbirth','date-of-birth','birth-date'],
       'phonenumber':['phonenumber','phone','telephone','tel'],
       'housenumber':['hausnummer'],
       'residentcountry':['resident','country'],
       'citizencountry':['citizen','citizenship','city'],
       'transcript':['transcript'],
       'coverletter':['coverletter','cover', 'letter'], 
       'picture':['picture'], 
       'address':['address','location'],
       'linkedin':['linkedin'],
       'github':['github'],
       'xing':['xing'],
       'twitter':['twitter'],
       'website':['website'],
       'postalcode':['postalcode','zip','zip-code','postal'],
       'city':['city'],
       'housenumber':['housenumber'], 
       'salary':['salary'],
       'sex':['sex','gender'], 
       'availablefrom':['noticeprieod'],
       #'file':['type="file"'],
       
       'captcha':['captcha'],
       'submit':['apply','type="submit"'],
       'cancel':['cancel'],
       'fake':['fake'],
       'question':['question'],
       'agree':['agree'],
       'other':['other'],
       'apply':['apply'],
       'recommendation':['recommendation'],
       'workherebefore':['workherebefore'],
       'findus':['find'],
       'dropbox':['dropbox'],
       'googledrive':['google drive'],
       'workhours':['workhours'],
       'workduration':[''],
       'visa':['visa'],
       'eligible':['eligible'],
       'germanlevel':['germanlevel'],
       'company':[''],#current company
       'relocate':[''],
       'universityenrollment':[],#are a student?
       'englishlevel':[],
       #important about job
       #important about jobplace?
              
       #-------------------------------------------------------------------
       #-----------------------------------btns ---------------------------
       'login':['login','sign'],
       'username':['username'],
       'register':['register','sign'],
       'cookie':['cookie'],
       'next':['apply now','next'],
       'search':[],
       #-------------------------------------------------------------------
       
       
       
       
       }


LABEL_INDEX_TO_KEY = list(KEYWORDS.keys()) #self.personal_data.columns
i =0
LABEL_KEY_TO_INDEX = {}
for key in KEYWORDS:
            LABEL_KEY_TO_INDEX[key] =i
            i+=1 