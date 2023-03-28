#```py
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = '2018-05-01'
#```
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version= version,
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


def englishToFrench(englishText):
    #write the code here
    if englishText is None:
        frenchText='Please provide a string to translate'
    else:
        translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
        # frenchText= json.dumps(translation, indent=2, ensure_ascii=False)
        frenchText= translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    if frenchText is None:
        englishText='Please provide a string to translate'
    else:
        translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
        # englishText= json.dumps(translation, indent=2, ensure_ascii=False)
        englishText= translation['translations'][0]['translation']
    return englishText