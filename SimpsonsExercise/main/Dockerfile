FROM python:latest

COPY ./lisa_level.py /app/
COPY ./requirements.txt /app/

WORKDIR /app/

RUN mkdir 'Lisa Simpson'
RUN mkdir 'Homer Simpson'
RUN mkdir General

RUN pip install requests beautifulsoup4 python-dotenv
RUN pip3 install numpy
RUN pip3 install -r requirements.txt
CMD ["python", "lisa_level.py"]