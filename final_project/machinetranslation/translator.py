'''
doc string
'''
import os
#import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'
#```
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version= VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)

# Translate
# translation = language_translator.translate(
#     text=text_to_translate,
#     model_id=model_id).get_result()

# # Print results
# print(json.dumps(translation, indent=2, ensure_ascii=False))

# translation = language_translator.translate(
#     text= 'Hello, how are you today?',
#     model_id='en-fr').get_result()
# print(json.dumps(translation, indent=2, ensure_ascii=False))
# res= translation['translations'][0]['translation']
# print(res)


def english_to_french(english_text):
    ''' translate English to French'''
    #write the code here
    if english_text:
        translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        # frenchText= json.dumps(translation, indent=2, ensure_ascii=False)
        french_text= translation['translations'][0]['translation']
    else:
        french_text='Please provide a string to translate'
    return french_text

def french_to_english(french_text):
    ''' translate french to english'''
    #write the code here
    if french_text:
        translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        # englishText= json.dumps(translation, indent=2, ensure_ascii=False)
        english_text= translation['translations'][0]['translation']
    else:
        english_text='Please provide a string to translate'
    return english_text
