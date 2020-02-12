FROM python:3.7-slim
ADD ./populator/main.py /
ADD ./source /source
RUN pip install elasticsearch requests markdown html2text bs4
CMD ["python", "-u", "main.py"]