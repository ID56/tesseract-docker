# tesseract-docker
Minimalistic tesseract docker service.

## Setup
Build image:
```
cd tesseract-docker
docker build -t tesseract-docker .
```

Set up local environment:
```
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Run
Mount your local `$TESSDATA` directory, in order to use your available languages.
```
TESSDATA=/usr/share/tesseract-ocr/4.00/tessdata

docker run -d --rm -p 5000:5000 \
           -v $TESSDATA:$TESSDATA \
           tesseract-docker:latest
```

Run client:
```
python client.py --img <path/to/image> \
                 --lang <language_name> \
                 --config <config str, e.g. "--psm 6"> \
                 --url http://0.0.0.0:5000/engine/
```

## Additional Notes
- No preprocessing has been added, as various images require various forms of processing. May add a default preprocessing mode later. As of now, input images should be in the binarized, 'black text on white background' format that tesseract-4 prefers.
- If you do not want to bind mount your `$TESSDATA` directory, you can alternatively copy your language.traineddata file to the repository, and uncomment line 20 in the Dockerfile before building.