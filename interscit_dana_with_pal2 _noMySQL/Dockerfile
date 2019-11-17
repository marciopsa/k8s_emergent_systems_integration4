
FROM ubuntu:18.10

# installing and running MySQL 
RUN apt update
RUN apt install mysql-server -y
RUN apt install libmysqlclient20
CMD chown -R mysql:mysql /var/lib/mysql
CMD usermod -d /var/lib/mysql/ mysql
RUN /etc/init.d/mysql start
CMD service mysql stop
CMD service mysql start

# copy and configuration of interscity-dana project
COPY ./dana ./home/marciopsa/dana 
COPY ./interscity_dana_project_version2 ./home/marciopsa/interscity_dana_project_version2
COPY start.sh /home/marciopsa/interscity_dana_project_version2/pal/start.sh
COPY assembly.sh /home/marciopsa/interscity_dana_project_version2/pal/assembly.sh
COPY learner.sh /home/marciopsa/interscity_dana_project_version2/pal/learner.sh
ENV DANA_HOME=/home/marciopsa/dana/
ENV PATH="${PATH}:/home/marciopsa/dana/"
WORKDIR /home/marciopsa/interscity_dana_project_version2/pal/

RUN ["chmod", "+x", "assembly.sh"]
RUN ["chmod", "+x", "start.sh"]
RUN ["chmod", "+x", "learner.sh"]

ENTRYPOINT ["/bin/bash", "./start.sh"]

