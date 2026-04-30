# ============================================================
# CROWD SENTINEL – FAST + IMPROVED ACCURACY (ONE CELL)
# ============================================================

!pip -q install gradio ultralytics opencv-python imageio imageio-ffmpeg

import gradio as gr
import cv2
import numpy as np
import imageio
from ultralytics import YOLO

# ============================================================
# MODEL
# ============================================================
model = YOLO("yolov8n.pt")

# ============================================================
# IMAGE DETECTION
# ============================================================
def detect_image(img, threshold):

    if img is None:
        return None, "0", "AWAITING INPUT..."

    frame = np.array(img)

    results = model(frame, classes=0, imgsz=640, conf=0.4, verbose=False)

    boxes = results[0].boxes.xyxy.cpu().numpy()

    # Duplicate filter
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

    status = "🚨 CROWD ALERT" if count > threshold else "✅ NORMAL"

    return plotted, str(count), status


# ============================================================
# VIDEO DETECTION (FAST + ACCURATE)
# ============================================================
def detect_video(video, threshold):

    if video is None:
        return None, "0", "NO VIDEO"

    reader = imageio.get_reader(video)
    output = "/content/output.mp4"

    writer = imageio.get_writer(output, fps=6, codec="libx264")

    peak = 0
    frame_id = 0

    for frame in reader:

        # optimized skip
        if frame_id % 10 == 0:

            # better resize (accuracy boost)
            small = cv2.resize(frame, (416, 234))

            results = model(
                small,
                classes=0,
                imgsz=416,
                conf=0.4,
                verbose=False
            )

            boxes = results[0].boxes.xyxy.cpu().numpy()

            # duplicate suppression
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
            peak = max(peak, count)

            plotted = results[0].plot()
            final = cv2.resize(plotted, (640, 360))

            writer.append_data(final)

        frame_id += 1

    writer.close()
    reader.close()

    status = "🚨 CROWD ALERT" if peak > threshold else "✅ NORMAL"

    return output, str(peak), status


# ============================================================
# CSS (DARK CYBER UI)
# ============================================================
css = """
html, body, .gradio-container {
background:#05070d !important;
color:#00eaff !important;
}

.gradio-container * {
background-color: transparent !important;
}

.gradio-container .gr-box,
.gradio-container .gr-group,
.gradio-container .gr-form {
background:#0a0f1c !important;
border:1px solid rgba(0,255,255,0.25) !important;
}

input, textarea {
background:#0a0f1c !important;
color:#00eaff !important;
border:1px solid rgba(0,255,255,0.25) !important;
}

.gr-image, .gr-video {
background:#0a0f1c !important;
border:1px dashed rgba(0,255,255,0.3) !important;
}

button {
background:transparent !important;
color:#00eaff !important;
border:1px solid #00eaff !important;
font-weight:700 !important;
}

button:hover {
background:#00eaff !important;
color:#000 !important;
}

button[role="tab"] {
border:1px solid rgba(0,255,255,0.3) !important;
}

button[aria-selected="true"] {
background:#00eaff !important;
color:#000 !important;
}

input[type=range] {
accent-color:#00eaff;
}

.cyber {
font-size:55px;
font-weight:900;
letter-spacing:3px;
color:#00eaff;
text-shadow:0 0 20px #00eaff;
}

footer {display:none !important;}
"""

# ============================================================
# UI
# ============================================================
with gr.Blocks(css=css, theme=gr.themes.Base()) as demo:

    gr.HTML("<div class='cyber'>🛡️ CROWD SENTINEL</div>")

    with gr.Tabs():

        with gr.Tab("IMAGE SCAN"):

            with gr.Row():

                with gr.Column():
                    img = gr.Image(type="pil", label="DROP IMAGE HERE")
                    threshold1 = gr.Slider(1, 50, value=10, step=1, label="ALERT THRESHOLD")
                    btn1 = gr.Button("RUN DETECTION")

                with gr.Column():
                    out_img = gr.Image(label="// IMAGE OUTPUT")
                    count1 = gr.Textbox(label="PEOPLE COUNT", value="0")
                    status1 = gr.Textbox(label="STATUS", value="AWAITING INPUT...")


        with gr.Tab("VIDEO SWEEP"):

            with gr.Row():

                with gr.Column():
                    vid = gr.Video(label="DROP VIDEO HERE")
                    threshold2 = gr.Slider(1, 50, value=10, step=1, label="ALERT THRESHOLD")
                    btn2 = gr.Button("RUN VIDEO")

                with gr.Column():
                    out_vid = gr.Video(label="// VIDEO OUTPUT")
                    count2 = gr.Textbox(label="PEOPLE COUNT", value="0")
                    status2 = gr.Textbox(label="STATUS", value="AWAITING INPUT...")


    btn1.click(detect_image, [img, threshold1], [out_img, count1, status1])
    btn2.click(detect_video, [vid, threshold2], [out_vid, count2, status2])

demo.launch(share=True)
