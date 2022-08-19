FROM python
WORKDIR /core
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000