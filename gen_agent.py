# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 11:47:57 2024

@author: mathe
"""

from langchain.llms import Ollama

llm = Ollama(base_url = "http://localhost:11434",
                model = "llama3")

class Generative_Agent:
    def __init__(self,llm):
        self.llm = llm
        
    def generate(self,input_data):
        '''
        Generate on the plan given by planning agent
        '''
        prompt = (f"you are a geneartive agent"
                  f"you will receive a wonderful plan from a student"
                  f"you have to generate a meaningful description on the plan given in the {input_data} "
                  f"your output must me accurate and precise to the {input_data}"
                  f"you should limit the output within 350 words"
                  f"you must structure the output as paragraphs"
                  f"the words used should be simple and easy to understand"
                  f"Your output should just be the output you should not mention anythinf else in the output")
        
        generate = self.llm.generate([prompt])
        generate = generate.generations[0][0].text
        return generate
    
