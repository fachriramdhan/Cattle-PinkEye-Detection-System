from flask import Flask, render_template, request
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2
import os
import time

app = Flask(__name__)

# ========================== LOAD YOLO MODEL ==========================
def load_model(cfg_path, weights_path, labels_path):
    labels = open(labels_path).read().strip().split("\n")
    np.random.seed(42)
    colors = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")
    net = cv2.dnn.readNetFromDarknet(cfg_path, weights_path)
    layer_names = net.getLayerNames()
    layer_names = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    return [net, layer_names, labels, colors]

model_info = load_model("configs/yolov4-tiny-custom.cfg", "weights/YOLOV4.weights", "coco.names")

# ========================== IMAGE PROCESSING ==========================
def process_image(img, model_info, score_threshold=0.3, overlap_threshold=0.3):
    net, layer_names, labels, colors = model_info
    image = img.copy()
    H, W = image.shape[:2]

    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416,416), swapRB=True, crop=False)
    net.setInput(blob)
    layerOutputs = net.forward(layer_names)

    boxes, scores, classIDs = [], [], []

    for output in layerOutputs:
        for detection in output:
            confidences = detection[5:]
            classID = np.argmax(confidences)
            score = confidences[classID]
            if score >= score_threshold:
                box = detection[0:4] * np.array([W, H, W, H])
                centerX, centerY, width, height = box
                x = int(centerX - width/2)
                y = int(centerY - height/2)
                boxes.append([x, y, int(width), int(height)])
                scores.append(float(score))
                classIDs.append(classID)

    idxs = cv2.dnn.NMSBoxes(boxes, scores, score_threshold, overlap_threshold)

    font = ImageFont.truetype(
        font='fonts/FiraMono-Medium.otf', 
        size=max(10, int(np.floor(0.01*(W+H)+0.5)))
    )
    thickness = max(1, (H+W)//420)

    img_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    final_classIDs, final_scores = [], []

    if len(idxs) > 0:
        for i in idxs.flatten():
            x, y, w, h = boxes[i]
            left, top, right, bottom = x, y, x+w, y+h
            draw = ImageDraw.Draw(img_pil)
            color = tuple([int(c) for c in colors[classIDs[i]]])
            label = "{}: {:.2f}".format(labels[classIDs[i]], scores[i])

            # Draw bounding box
            for j in range(thickness):
                draw.rectangle([left+j, top+j, right-j, bottom-j], outline=color)
            # Draw label background
            bbox = draw.textbbox((0,0), label, font=font)
            label_width = bbox[2] - bbox[0]
            label_height = bbox[3] - bbox[1]
            origin = np.array([left, top - label_height if top - label_height >= 0 else top+1])
            draw.rectangle([tuple(origin), tuple(origin + np.array([label_width,label_height]))], fill=color)
            draw.text(tuple(origin), label, fill=(0,0,0), font=font)
            del draw

            final_classIDs.append(classIDs[i])
            final_scores.append(scores[i])

    result_img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
    return result_img, final_classIDs, final_scores

# ========================== ROUTE ==========================
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        f = request.files.get("image")
        if not f:
            return render_template("index.html", error="Tidak ada file yang diunggah.")

        score_threshold = float(request.form.get("score_threshold", 0.3))
        overlap_threshold = float(request.form.get("overlap_threshold", 0.3))

        os.makedirs("static", exist_ok=True)
        input_path = os.path.join("static", "input.jpg")
        f.save(input_path)

        img = cv2.imread(input_path)
        if img is None:
            return render_template("index.html", error="File gambar tidak valid.")

        start = time.time()
        result_img, classIDs, scores = process_image(img, model_info, score_threshold, overlap_threshold)
        end = time.time()

        result_path = os.path.join("static", "result.jpg")
        cv2.imwrite(result_path, result_img)

        labels = model_info[2]

        if len(classIDs) == 0:
            results = [{"label": "Tidak terdeteksi", "score": 0}]
        else:
            results = [{"label": labels[classIDs[i]], "score": scores[i]} for i in range(len(classIDs))]

        return render_template(
            "index.html",
            input_image="static/input.jpg",
            result_image="static/result.jpg",
            results=results,
            duration=round(end - start, 2),
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
