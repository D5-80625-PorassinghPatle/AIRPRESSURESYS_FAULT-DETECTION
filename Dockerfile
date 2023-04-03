FROM python:3.8
USER root
RUN mkdir /app
COPY ./app/
WORKDIR /app/
RUN pip3 install -r requirements.txt
ENV AIRFLOW_HOME="/app/airflow"
ENV AIRFLOW__CORE__DAGBAG__IMPORT__TIMEOUT=1000
ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING=True
RUN airflow db init
RUN airflow users create -e poraspatle@gmail.com -f Poras -l Patle -p admin -r admin -u admin
RUN apt update -y && apt install awscli -y
ENTRYPOINT ["/bin/sh"]
CMD ["Start.sh"]

