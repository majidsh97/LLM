KEYWORDS={
        #----------------------form--------------------------------------
       'first name':['firstname','first_name','forename','first','first-name'],
       'last name':['lastname','last_name','surename','last','last-name'] ,
       'email':['email','e-mail','username','user_name','user-name','type="email"'], 
       'password':['password'], 
       'cv':['cv','resume','curriculum','vitae'],
       'birth date':['birthdate','birth','dateofbirth','date-of-birth','birth-date'],
       'phone number':['phonenumber','phone','telephone','tel'],
       'house number':['hausnummer'],
       'resident country':['resident','country'],
       'citizen country':['citizen','citizenship','city'],
       'transcript':['transcript'],
       'cover letter':['coverletter','cover', 'letter'], 
       'picture':['picture'], 
       'address':['address','location'],
       'linkedin':['linkedin'],
       'github':['github'],
       'xing':['xing'],
       'twitter':['twitter'],
       'website':['website'],
       'zip':['postalcode','zip','zip-code','postal'],
       'city':['city'],
       'salary':['salary'],
       'sex':['sex','gender'], 
       'available from':['noticeprieod'],
       #'file':['type="file"'],
       
       'captcha':['captcha'],
       'submit':['apply','type="submit"'],
       'cancel':['cancel'],
       'fake':['fake'],
       'custom question':['question'],
       'privacy':['agree'],

       'recommend':['recommendation'],
       'work here before':['workherebefore'],
       'find us':['find'],
       'dropbox':['dropbox'],
       'google drive':['google drive'],
       'work hours':['workhours'],
       'workduration':[''],
       'visa':['visa'],
       #'eligible':['eligible'],
       'german language level':['germanlevel'],
       'company':[''],#current company
       'willing to relocate':[''],
       'university enrollment':[],#are a student?
       'english language level':[],
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
        'other':['other'],
        'newsletter':[]
       #'apply':['apply'],
       #-------------------------------------------------------------------

       }

LABEL_INDEX_TO_KEY = list(KEYWORDS.keys())

i =0
LABEL_KEY_TO_INDEX = {}
for key in KEYWORDS:
            LABEL_KEY_TO_INDEX[key] =i
            i+=1 