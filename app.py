import streamlit as st
from predict import prediction

if "checkout" not in st.session_state:
    st.session_state["checkout"] = None

def goods_detection():
    st.session_state["goods_list"] = {"item": [], "price": []}
    st.header("商品辨識", divider='rainbow')
    if st.button("辨識完成"):
        st.session_state["checkout"] = True
    prediction()

    if st.button("辨識完成"):
        st.session_state["checkout"] = True

def checkout():
    st.title("結帳")

    choice1 = st.radio("選擇以下選擇", ("悠遊卡", "信用卡", "付現"))
    st.write("你選擇的是:",choice1)
    choice2 = st.radio("是否需要統一編號", ("是", "否"))
    if(choice2=="是"):
        user_input1 = st.text_input("請在此輸入您的統一編號")
    choice3 = st.radio("是否需要載具", ("是", "否"))
    if(choice3=="是"):
        user_input2 = st.text_input("請在此輸入您的載具")
    st.write("點選以下按鈕來付款")
    if(st.button(choice1)):
        if(choice2=="是"):
            if not(user_input1):
                if(choice3=="是"):
                    if not(user_input2):
                        st.write("付款失敗，請輸入統一編號")
                        st.write("付款失敗，請輸入載具")
                else:
                    st.write("付款失敗，請輸入統一編號")
            else:
                if(choice3=="是"):
                    if not(user_input2):
                        st.write("付款失敗，請輸入載具")
                    else:
                        st.write("成功付款")
                else:
                    st.write("成功付款")
        else:
            if(choice3=="是"):
                if not(user_input2):
                    st.write("付款失敗，請輸入載具")
                else:
                    st.write("成功付款")
            else:
                st.write("成功付款")


if st.session_state["checkout"]:
    checkout()
else:
    goods_detection()