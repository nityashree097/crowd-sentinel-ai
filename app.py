!pip -q install gradio ultralytics opencv-python

import gradio as gr
import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_image(img, threshold):

    if img is None:
        return None, "0", "WAITING..."

    frame = np.array(img)

    results = model(frame, classes=0, conf=0.4)

    count = len(results[0].boxes)

    plotted = results[0].plot()
    plotted = cv2.cvtColor(plotted, cv2.COLOR_BGR2RGB)

    status = "🚨 ALERT" if count > threshold else "✅ NORMAL"

    return plotted, str(count), status


with gr.Blocks() as demo:

    gr.Markdown("# 🛡️ Crowd Sentinel v2")

    img = gr.Image(type="pil")
    threshold = gr.Slider(1, 50, value=10, label="Alert Threshold")
    btn = gr.Button("Run Detection")

    out_img = gr.Image()
    count = gr.Textbox(label="People Count")
    status = gr.Textbox(label="Status")

    btn.click(detect_image, inputs=[img, threshold], outputs=[out_img, count, status])

demo.launch() 

# ============================================================
# CROWD SENTINEL – v3 (BETTER ACCURACY)
# ============================================================

!pip -q install gradio ultralytics opencv-python

import gradio as gr
import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_image(img, threshold):

    if img is None:
        return None, "0", "WAITING..."

    frame = np.array(img)

    results = model(frame, classes=0, conf=0.4)

    boxes = results[0].boxes.xyxy.cpu().numpy()

    filtered = []
    for box in boxes:
        x1,y1,x2,y2 = box
        keep = True
        for f in filtered:
            fx1,fy1,fx2,fy2 = f
            if abs(x1-fx1) < 30 and abs(y1-fy1) < 30:
                keep = False
                break
        if keep:
            filtered.append(box)

    count = len(filtered)

    plotted = results[0].plot()
    plotted = cv2.cvtColor(plotted, cv2.COLOR_BGR2RGB)

    status = "🚨 ALERT" if count > threshold else "✅ NORMAL"

    return plotted, str(count), status


with gr.Blocks() as demo:

    gr.Markdown("# 🛡️ Crowd Sentinel v3")

    img = gr.Image(type="pil")
    threshold = gr.Slider(1, 50, value=10)
    btn = gr.Button("Run Detection")

    out_img = gr.Image()
    count = gr.Textbox(label="People Count")
    status = gr.Textbox(label="Status")

    btn.click(detect_image, inputs=[img, threshold], outputs=[out_img, count, status])

demo.launch()
