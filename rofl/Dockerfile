FROM python:3.12-slim
WORKDIR /app

# install deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY app.py .

# expose & launch
ENV PYTHONUNBUFFERED=1
CMD ["python", "app.py"]
