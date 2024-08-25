# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:46:27 2024

@author: mathe
"""
from langchain.llms import Ollama

llm = Ollama(base_url = "http://localhost:11434",
                model = "llama3")

import logging
class Planner_Agent:
    def __init__(self,llm):
        self.llm = llm
        logging.basicConfig(level=logging.INFO)
        
    def Plan(self,input_data):
       """
       Parameters
       ----------
       input_data : str
           A string representing the user's query.

       Returns
       -------
       A string which generates a plan for the task in a student-friendly, concise format.
       """ 
       prompt = (f"Hey, I got this query from a student: {input_data}."
                  f"Can enerative agenet what to generate for this query :{input_data}."
                  f"You just have to give the bullet points, no explanations please!")  
       try:  
            plan  = self.llm.generate([prompt])
            plan = plan.generations[0][0].text
            logging.info("Plan generated successfully") 
            return plan
       except Exception as e: 
            logging.error(f"Error occured during generating:{e}")
            return "There was an error during generation"
    

