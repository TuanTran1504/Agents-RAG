# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 21:28:23 2024

@author: mathe
"""
from langchain.llms import Ollama

llm = Ollama(base_url = "http://localhost:11434",
                model = "llama3")

class  English_translator:
    def __init__(self,llm):
        self.llm = llm
        
    def english_tr(self,input_text):
        '''
        

        Parameters
        ----------
        input_text : str
            A sting with user's query.

        Returns
        -------
        str
            The english translation of the given input.

        '''
        
        prompt = (f"Translate the {input_text} into english."
                  f"Only output the translated text without any explanation or commentary please.")
        
        en_tr = self.llm.generate([prompt])
        if input_text == "english":
            return input_text
        else:
            english = en_tr.generations[0][0].text 
            return english




# from googletrans import Translator

# class:
#     def __init__(self):
#         self.english_translator = Translator()
        
        
#     def english_tr(self,input_text):
#         if input_text == "en":
#             return input_text
#         else:
#             english = self.english_translator.translate(input_text,dest="en").text
#             return english
        
# english = English_translator(llm)
# response = english.english_tr("请介绍一下西悉尼大学")
# response2 = english.english_tr("Hãy cho tôi biết về Đại học Western Sydney")
# print("Chinese:",response)
# print("Vietnamese:",response2)
    