import json
import random
import re
def load_rulesfile(path="rules.json"):
    with open(path,"r",encoding="utf-8")as f:
        data=json.load(f)
        return data

contractions = {"i'm": "i am", "don't": "do not", "it's": "it is"}
def expand_contractions(text):
    for k, v in contractions.items():
        text = text.replace(k, v)
    return text
    
def format(text):
    text=text.lower().strip()
    expand_contractions(text)
    text=re.sub(r"[^\w\s]","",text)
    return text

def find_user_intent(text,rules):
    text=format(text)
    for intent,value in rules.items():
        value=value.get("patterns",[])
        for pattern in value:
            pattern=format(pattern)
            if pattern in text or text in pattern:
                if re.search(r"\b" + re.escape(pattern) + r"\b", text):
                    return intent
    return None
 
def get_user_response(intent,rules):
    if intent is None or intent not in rules:
        return "Sorry, I couldn't get that. Can you please rephrase it?. That might help"
    return random.choice(rules[intent]["responses"])
