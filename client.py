import requests
import json
import cv2
from argparse import ArgumentParser

def preprocess(image):
    """Preprocess image for tesseract."""
    raise NotImplementedError
    

def send_inference_request(server_url, image, lang, config):
    """Service request to tesseract container."""

    formatted_json_input = json.dumps(
        {
            "image_data": image.tolist(),
            "lang": lang,
            "config": config
        }
    )

    headers = {"content-type": "application/json"}

    server_response = requests.post(
        server_url, data=formatted_json_input, headers=headers
    )

    return server_response


def main(args):
    image = cv2.imread(args.img, 0)
    result = send_inference_request(args.url, image, args.lang, args.config)
    result = json.loads(result.text)

    print(result["output"] if result["output"] else result["error"])


if __name__ == "__main__":
    parser = ArgumentParser("Sample client-side driver code.")
    parser.add_argument("--img", type=str, required=True, help="Path to image")
    parser.add_argument("--lang", type=str, default='', help="Language name")
    parser.add_argument("--config", type=str, default='', help='Config string, enclose in ""')
    parser.add_argument("--url", type=str, required=True, help="Server url")
    args = parser.parse_args()

    main(args)
