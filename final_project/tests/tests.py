import unittest
import machinetranslation
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(''), 'Please provide a string to translate') # test null string.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test Hello        
        

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(''),'Please provide a string to translate') # test null string.
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  # test Hello   
        
unittest.main()