# following descriptions from https://hub.docker.com/_/postgres

FROM postgres:12.1

# set German encoding
RUN localedef -i de_DE -c -f UTF-8 -A /usr/share/locale/locale.alias de_DE.UTF-8
ENV LANG de_DE.utf8

EXPOSE 5432

