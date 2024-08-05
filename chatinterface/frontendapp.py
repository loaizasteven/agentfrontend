import streamlit as st

import os.path as osp
import sys

import pydantic

script_dir = osp.dirname(__file__)
sys.path.insert(0, osp.dirname(script_dir))
from _ui.generaloptions import change_button_style, detect_browser

class ChatBotApp():
    title:str = 'My First LLM Chat'

    def _render(self):
        "Renders the chatbot UI"
        st.title(self.title)
        st.button('Start Chat', key='test123')
        change_button_style('Start Chat', 'Start Chat', 'Let me add more info to my content')

        prompt = st.chat_input("Say something")
        if prompt:
            with st.chat_message("user"):
                st.write(f"User has sent the following prompt: {prompt}")
            with st.chat_message("assistant"):
                st.write("Hello 👋, I am the Assistant")

    @staticmethod
    def _check():
        "Static Method to check browser"
        with st.container():
            detect_browser()
        
    def __call__(self, debug:str = False):
        if debug:
            self._render
            self._check
        else:
            # Runs methods alphabetically, not ideal
            for method in dir(self): 
                if callable(getattr(self, method)) and not method.startswith("__"):
                    print(method)
                    getattr(self, method)()


if __name__=="__main__":
    ui = ChatBotApp()
    ui(True)
    