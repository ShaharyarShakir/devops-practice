FROM mysql:8.0.3
LABEL Project="Vprofile"
LABEL Author="Shaharyar"
RUN MY_ROOT_PASSWORD="vpropass"
RUN MY_DATABASE="accounts"
ADD db_backup.sql  docker-enterypoint-initdb.d/db_backup.sql