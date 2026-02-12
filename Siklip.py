#SIKLIP - Sike + clip

import pyperclip
import streamlit as st
import json
import datetime

def Prompt_History():
    file_path="history.json"
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for entry in data:
                if len(entry["message"])<=1:
                    continue
                st.write("Timestamp:",entry["timestamp"])
                
                st.markdown("## Clip:\n")
                st.code(entry["message"]+"\n",language="text")

                st.markdown("---")
    except (FileNotFoundError, json.JSONDecodeError):
        print("No valid data found.")

def write_to_json(message):
    file_path="history.json"
    timestamp = datetime.datetime.now().isoformat()
    new_entry = {"timestamp": timestamp, "message": message}
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):  # Ensure data is a list
                data = []
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data=[new_entry]+data
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


text=pyperclip.paste()
write_to_json(text)
Prompt_History()