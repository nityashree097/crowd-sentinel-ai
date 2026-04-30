!pip -q install gradio ultralytics opencv-python

import gradio as gr
import cv2
import numpy as np
from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.pt")

# Simple detection
def detect_image(img):

    if img is None:
        return None, "0"

    frame = np.array(img)

    results = model(frame, classes=0)

    count = len(results[0].boxes)

    plotted = results[0].plot()
    plotted = cv2.cvtColor(plotted, cv2.COLOR_BGR2RGB)

    return plotted, str(count)


# UI (very basic)
with gr.Blocks() as demo:

    gr.Markdown("# Crowd Detection (Prototype)")

    img = gr.Image(type="pil")
    btn = gr.Button("Run")

    out_img = gr.Image()
    count = gr.Textbox(label="People Count")

    btn.click(detect_image, inputs=img, outputs=[out_img, count])

demo.launch()
