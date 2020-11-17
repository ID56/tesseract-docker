import pytesseract as pt
from flask import Flask, request, jsonify

app = Flask(__name__)

def predict(image, lang, config):
    """Runs inference on a single image."""
    
    return pt.image_to_string(
        image,
        lang=lang,
        config=config
    )

@app.route(f'/engine/', methods=["POST"])
def engine():
    """Entry point."""

    result = {'output': None, 'error': None}

    try:
        image_data = request.json['image_data']
        lang = request.json['lang']
        config = request.json['config']

        result['output'] = run_inference(image_data, lang, config)
    except Exception as e:
        result['error'] = str(e)

    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)