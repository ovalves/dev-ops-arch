FROM ubuntu:19.10

RUN echo "echo INIT Spreadsheet Exporter" > docker_entrypoint.sh
RUN echo "INIT Spreadsheet Exporter"
RUN sleep 5
RUN echo "END Spreadsheet Exporter"


ENTRYPOINT ["/usr/bin/bash", "--", "docker_entrypoint.sh"]