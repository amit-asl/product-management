FROM python:3.10-alpine

WORKDIR /workspace

COPY . /workspace

RUN python3 -m venv venv && \
    source venv/bin/activate

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "5000", "app.main:app"]