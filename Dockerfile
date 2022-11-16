FROM motimatic-student-base:latest AS builder


FROM gcr.io/distroless/python3.10-debian10

WORKDIR /opt/student-svc

# Weird bug in the Python distroless docker image, its missing a Python dependency
COPY --from=builder /usr/local/lib/libpython3.10m.so.1.0 /usr/local/lib/libpython3.10m.so.1.0
COPY --from=builder /usr/lib/x86_64-linux-gnu/libpython3.10m.so.1.0 /usr/lib/x86_64-linux-gnu/libpython3.10m.so.1.0

COPY --from=builder /opt/student-svc-site-packages site-packages
COPY alembic.ini .
COPY app app

RUN python -m compileall .

USER 65534

ENV PYTHONPATH=/opt/student-svc/site-packages

CMD ["./site-packages/bin/gunicorn", "app.main:app", "-b", ":8001", "-w", "4", "-k", "uvicorn.workers.UvicornWorker"]

EXPOSE 8001
