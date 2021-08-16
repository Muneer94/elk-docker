# FROM jenkins/jenkins:latest
# ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
# ENV CASC_JENKINS_CONFIG /var/jenkins_home/casc.yaml
# COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
# RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
# COPY casc.yaml /var/jenkins_home/casc.yaml

FROM jenkins/jenkins:2.289.3
USER root

RUN apt-get update && apt-get install python3-pip python3 ansible-lint -y && \
    pip3 install ansible --upgrade &&\
    apt-get upgrade -y && apt-get update

USER jenkins