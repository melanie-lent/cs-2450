FROM python:latest
RUN pip install flask tinydb timeago selenium
COPY youface.py ./youface.py
ADD . / 
EXPOSE 5000
CMD ["python3", "./youface.py"]

