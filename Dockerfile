FROM python:3.10.4
RUN mkdir -p /home/project/app
WORKDIR /home/project/app
COPY . .
EXPOSE 5000
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3","index.py"]