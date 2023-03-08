FROM python:3.10.6-buster

COPY well /well
COPY requirements.txt /requirements.txt
COPY raw_data/DialoGPT-small /DialoGPT-small

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python -c "from transformers import AutoModel; AutoModel.from_pretrained('/DialoGPT-small')"

CMD uvicorn well.api.main:app --host 0.0.0.0 --port $PORT
