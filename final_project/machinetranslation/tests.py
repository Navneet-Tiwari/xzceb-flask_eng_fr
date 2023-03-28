import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        # self.assertEqual(englishToFrench(''), 'Please provide a string to translate') # test null string.
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')  # test Hello        
        

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        # self.assertEqual(frenchToEnglish(''),'Please provide a string to translate') # test null string.
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')  # test Hello   
        
unittest.main()