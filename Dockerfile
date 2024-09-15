FROM python:3.9.20-slim

RUN pip install --upgrade pip && pip install tqdm pytubefix

WORKDIR /app

COPY app/minimal-yt-downloader.py .

VOLUME ["/app/Videos Downloaded"]

CMD ["python", "minimal-yt-downloader.py"]