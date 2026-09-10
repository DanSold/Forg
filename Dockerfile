FROM python:3.12

WORKDIR /app

COPY game.py .

CMD ["python", "game.py"]