# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:01:16 2024

@author: mathe
"""

from langchain.llms import Ollama

llm = Ollama(base_url = "http://localhost:11434",
                model = "llama3")

class Task_Identifier_Agent:
    def __init__(self, llm):
        self.llm = llm
        
    def Task(self, input_data):
        """
        Parameters
        ----------
        input_data : str
            A string representing the user's query.

        Returns
        -------
        A string which breakdowns and explains the task in a student-friendly, concise format.
        """
        prompt = (
            f"Hey, I got this query from another student: '{input_data}'. Can you tell the planner"
            "what the query is. You should sound like a student asking query."
            "Keep it short and straight forward please."
        )
        
        try:
            task_response = self.llm.generate([prompt])
            task = task_response.generations[0][0].text.strip()
        except Exception as e:
            task = f"Oops, ran into a bit of trouble: {str(e)}"
        
        return task


