# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 10:37:47 2024

@author: mathe
"""


from langchain.llms import Ollama

llm = Ollama(base_url = "http://localhost:11434",
                model = "llama3")

class Language_detector:
    def __init__(self,llm):
        self.llm = llm
        
    def detect_language(self,text):
        '''
        

        Parameters
        ----------
        input_text : str
            A sting with user's query.

        Returns
        -------
        str
            The name of the language in which the input is.

        '''
        
        prompt = (f"Identify the language used in {text}"
                  f"Only output the name of the language in english without any explanation or commentary please.")
        
        lan = self.llm.generate([prompt])
        if text == "english":
            print("english")
        else:
            language = lan.generations[0][0].text 
            return language


