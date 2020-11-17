FROM ubuntu:18.04
LABEL maintainer="mashrurmahmud@iut-dhaka.edu"

RUN apt-get update && apt-get upgrade -y && apt-get clean
RUN apt-get install -y curl python3.7 python3.7-dev python3.7-distutils
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
RUN update-alternatives --set python /usr/bin/python3.7

RUN curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py --force-reinstall && \
    rm get-pip.py

RUN apt install -y libsm6 libxext6
RUN apt-get -y install tesseract-ocr

COPY . /app
WORKDIR /app

#RUN mv <lang_name>.traineddata /usr/share/tesseract-ocr/4.00/tessdata

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]