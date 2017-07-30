FROM python:latest
ADD bridge.py        /bridge.py
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8206
CMD python bridge.py
