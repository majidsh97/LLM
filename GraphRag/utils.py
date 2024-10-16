import litellm
import os
from json_repair import loads


os.environ["OPENAI_API_KEY"] = "any"
BASE_URL = "http://localhost:8080/"
MODEL_NAME = "gpt-4o"
litellm.set_verbose = False

sys_msg = ""

def completion(msg,JSON=True):
    """
    global sys_msg needs to be defined!
    """
    global sys_msg
    messages = [{"role":"system","content":sys_msg},
                     {"role": "user", "content":msg }]
    r= litellm.completion(
        model=MODEL_NAME,
        messages=messages,
        base_url=BASE_URL,
        safety_settings=[
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE",
            },
        ], 
        response_format={"type": "json_object"}
    
    )
     
    j= r.choices[0].message.content
    return loads(j) if JSON else j