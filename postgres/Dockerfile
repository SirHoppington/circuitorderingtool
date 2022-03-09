# Download base image
FROM postgres

#information about custom image

LABEL maintainer="nickhopgood@gmail.com"
LABEL version="0.1"
LABEL description="This is custom docker image for Postgresql DB"

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

# Updata software repository
#RUN apt update

## Download and install Postgres

CMD ["psql", "-h", "localhost", "-U", "postgres", "-d", "postgres"]


## Run the rest of the commands as Postgre user

#RUN psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" && \createdb -O docker docker



#RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf


#RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf


#EXPOSE 5432


#VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]


#CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D", "/var/lib/postgresql/9.3/main", "-c", "config_file=/etc/postgresql/9.3/main/postgresql.conf"]