FROM python:3.12-slim AS venv

COPY requirements.txt requirements.txt
RUN --mount=type=ssh python -m pip install --upgrade pip \
    pip install --no-cache-dir -r requirements.txt -t /packages/


FROM python:3.12-slim AS app
WORKDIR /app/
ENV PATH /packages/bin:$PATH
ENV PYTHONPATH /packages

COPY --chmod=0744 ./deploy /
COPY --from=venv /packages /packages
COPY main.py /app/main.py
COPY ./app /app/app
COPY ./uploads /app/uploads
COPY ./reports /app/reports

EXPOSE 80
CMD /start.sh
