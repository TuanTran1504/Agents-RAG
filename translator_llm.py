# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:07:16 2024

@author: mathe
"""

from langchain.llms import Ollama

llm = Ollama(base_url = "http://localhost:11434",
                model = "llama3")

class Translator:
    def __init__(self,llm):
        self.llm = llm
        
    def translation(self,text,target_language):
        '''
        

        Parameters
        ----------
        text : str
            A string which is the output to the user's query.
        target_language : str
            A string which says the language to which the text should be converted.

        Returns
        -------
        A translated version of the text given.

        '''
        prompt = (f"Translate the following {text} to :{target_language}."
                  f"Only output the translated text without any explanation or commentary please.")
        
        translate = self.llm.generate([prompt])
        if target_language== "en":
            return text
        else:
            translation = translate.generations[0][0].text
            return translation
        
        
        
        
        
        
# text = ("Increasingly in the digital age data plays an important role in most, if not all," 
#       "occupations. Extracting information from data has become a science in itself, blending skill sets from mathematics," 
#       "statistics and computing. With a strong applications focus, this program covers the nature of data including"
#       " Big and Unstructured Data, how to embark on data driven investigations and visual and computational analytics."
#       " The program graduates will have the knowledge and skills required to operate effectively in a data driven world.")
# translator = Translator(llm)
# chinese = translator.translation(text, "malayalam");print("Chinese","\n",chinese)
#vietnamese = translator.translation(text,"vi");print("Vietnamese","\n",vietnamese)
