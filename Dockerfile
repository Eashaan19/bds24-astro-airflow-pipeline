FROM apache/airflow:2.7.0-python3.11

COPY packages.txt /tmp/packages.txt

RUN pip install --no-cache-dir -r /tmp/packages.txt

COPY dags/ /opt/airflow/dags/
COPY airflow_settings.yaml /opt/airflow/airflow_settings.yaml
