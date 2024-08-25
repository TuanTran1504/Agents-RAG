# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:17:01 2024

@author: mathe
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:49:22 2024

@author: mathe
"""
import tkinter as tk
from tkinter import scrolledtext
#from langgraph.graph import StateGraph, END
#from research import ResearchState
from langchain.llms import Ollama

llm = Ollama(base_url = "http://localhost:11434",
                model = "llama3")

#from error_agent import Error_Handler_Agent
from gen_agent import Generative_Agent
#from lan_agent import Language_Detector_Agent
from plan_agent import Planner_Agent
from task_agent import Task_Identifier_Agent
#from editor import EditorAgent
from lan_detect import Language_detector
#from translation_agent import TranslationAgent
from english_translator import English_translator
from translator_llm import Translator

class AgentManager:
    def __init__(self):
    
        #self.error_agent = Error_Handler_Agent(llm)
        self.generative_agent = Generative_Agent(llm)
        #self.language_agent = Language_Detector_Agent(llm)
        self.planner_agent = Planner_Agent(llm)
        self.task_identifier = Task_Identifier_Agent(llm)
        #self.editor= EditorAgent(llm)
        self.Language_detector = Language_detector(llm)
        #self.translation = TranslationAgent()
        self.english_tr = English_translator(llm)
        self.translator_llm = Translator(llm)
        
    def handle_input(self, user_input): 
        eng_det = self.english_tr.english_tr(user_input)
        detect = self.Language_detector.detect_language(user_input)
        task = self.task_identifier.Task(eng_det)
        plan = self.planner_agent.Plan(task) 
        response = self.generative_agent.generate(plan)
        translation = self.translator_llm.translation(response,detect)
        return translation
  
agentmanager = AgentManager()      

def send():
    user_input = user_input_box.get("1.0", tk.END).strip()
    if user_input:
        chat_window.insert(tk.END, "You: " + user_input + "\n")
        response = agentmanager.handle_input(user_input)
        chat_window.insert(tk.END, "Bot: " + response + "\n")
    user_input_box.delete("1.0", tk.END)

# Set up the main window
root = tk.Tk()
root.title("Chatbot Interface")

# Create a scrolled text area widget
chat_window = scrolledtext.ScrolledText(root, height=20, width=60)
chat_window.pack(pady=10)

# Create a text input box
user_input_box = tk.Text(root, height=3, width=40)
user_input_box.pack(pady=10)

# Create a Send button
send_button = tk.Button(root, text="Send", command=send)
send_button.pack()

# Start the GUI loop
root.mainloop()
# agentmanager = AgentManager()
# response = agentmanager.handle_input("I want to know about Parramatta")
# print(response)  # This will print the output from the handle_input method

