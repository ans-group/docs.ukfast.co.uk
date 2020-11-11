FROM python:3.7-slim
ADD ./populator /
ADD ./source /source
RUN pip install -r requirements.txt
CMD ["python", "-u", "main.py"]