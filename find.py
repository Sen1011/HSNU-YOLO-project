import streamlit as st
import json
from time import time

def find(json_result):
    json_result = json.loads(json_result)
    file = open("./goods.json", "r")
    goods_data = json.load(file)
    
    for result in json_result:
        for goods in goods_data:
            if result["name"] == goods["name"] and int(time()) - goods["last_detection"] >= 10:
                st.session_state["goods_list"]["item"].append(goods["name"])
                st.session_state["goods_list"]["price"].append(goods["price"])
                goods["last_detection"] = int(time())

                file.close()
                with open("./goods.json", "w") as write:
                    json.dump(goods_data, write, indent=4)
                break