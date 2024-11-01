import streamlit as st

import os.path as osp
import sys
import uuid

from pydantic import BaseModel

script_dir = osp.dirname(__file__)
sys.path.insert(0, osp.dirname(script_dir))
from _ui.generaloptions import change_button_style, detect_browser


class ChatBotApp():
    title:str = 'My First LLM Chat'
    buttons: tuple = (
        ('Button 1', 'This is my short instruction content, with multiline instruction'),
        ('Button 2', 'This is my short instruction content, with multiline instruction'),
        ('Button 3', 'This is my short instruction content, with multiline instruction'),
    )

    def _apppagedefault(self, title="Chat Bot App", icon="🦜"):
        st.set_page_config(
            page_title = title,
            page_icon = icon
        )

    def _render(self):
        "Renders the chatbot UI"
        st.title(self.title)

        cols = st.columns(len(self.buttons))
        for i, entry in enumerate(self.buttons):   
            cols[i].button(entry[0], key=f"button_{i}")
            change_button_style(entry[0], entry[0], entry[1])

        prompt = st.chat_input("Say something")
        if prompt:
            with st.chat_message("user"):
                st.write(f"User has sent the following prompt: {prompt}")
            with st.chat_message("assistant"):
                st.write("Hello 👋, I am the Assistant")

    @staticmethod
    def _zcheck():
        "Static Method to check browser"
        with st.container():
            detect_browser()
        
    def __call__(self, debug:str = False):
        if debug:
            self._render
            self._zcheck
        else:
            # Runs methods alphabetically, not ideal
            for method in dir(self): 
                if callable(getattr(self, method)) and not method.startswith("__"):
                    getattr(self, method)()


if __name__=="__main__":
    ui = ChatBotApp()
    ui(False)
    