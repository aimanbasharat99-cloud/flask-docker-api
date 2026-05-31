from flask import Flask, request, send_file, jsonify
from PIL import Image
from datetime import datetime
import io

app = Flask(__name__)

@app.route('/datetime', methods=['GET'])
def get_datetime():
    return jsonify({"datetime": str(datetime.now())})

@app.route('/flip', methods=['POST'])
def flip_image():
    if 'image' not in request.files:
        return "No image uploaded", 400

    image = Image.open(request.files['image'])
    flipped = image.transpose(Image.FLIP_LEFT_RIGHT)

    img_io = io.BytesIO()
    flipped.save(img_io, 'JPEG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)