FROM openfabric/openfabric-pyenv:0.1.9-3.8

RUN mkdir cognitive-assistant
WORKDIR /cognitive-assistant
COPY . .
RUN poetry install -vvv --no-dev
RUN pip install -r requirements.txt
RUN pip install --upgrade pip && pip install $(pip freeze | awk '{split($0,a,"=="); print a[1]}') | grep -v "@" || true
EXPOSE 5000
CMD ["sh","start.sh"]