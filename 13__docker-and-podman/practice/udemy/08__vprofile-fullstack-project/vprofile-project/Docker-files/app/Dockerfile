FROM openjdk:11 AS builder
RUN apt update && apt install -y maven
RUN git clone https://github.com/devopshydclub/vprofile-project.git
RUN cd vprofile-project && git switch docker && mvn install

FROM tomcat:8-jre11
LABEL Project="Vprofile"
LABEL Author="Shaharyar"
RUN rm -rf /usr/local/tomcat/webapps/*
COPY --from=builder  vprofile-project/target/vprofile-v2.war  /usr/local/tomcat/webapps/ROOT.war
EXPOSE 8080
CMD [ "catalina.sh", "run" ]