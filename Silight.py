import pyautogui as pya
import pyperclip  
import time
import streamlit as st

def copy_clipboard():
    pyperclip.copy("") 
    pya.hotkey('ctrl', 'c')
    time.sleep(.01)  
    return pyperclip.paste()

st.title("Page not empty just ReLoad")
var = copy_clipboard()
st.code(var,language="text")