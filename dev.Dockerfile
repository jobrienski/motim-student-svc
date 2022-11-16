FROM motimatic-student-base:latest

VOLUME /opt/student-svc

ENTRYPOINT ["/opt/student-svc-site-packages/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]

EXPOSE 8001
