import cv2
from ultralytics import YOLO
import streamlit as st
from find import find

def prediction():
    # Load the model
    model = YOLO("./expirement/train/weights/best.pt")

    cap = cv2.VideoCapture(1)
    img = st.empty()
    data = st.empty()

    while cap.isOpened() and not(st.session_state["checkout"]):
        success, frame = cap.read()

        if success:
            results = model(frame, conf=0.7)
            for result in results:
                json_result = result.to_json()
            
            if not(json_result == "[]"):
                find(json_result)

            annotated_frame = results[0].plot()
            img.image(annotated_frame)

            data.dataframe(st.session_state["goods_list"])
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
    st.rerun()