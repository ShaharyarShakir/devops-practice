FROM docker.io/ubuntu:latest

LABEL Author="Shaharyar"
LABEL Project="waso"

ENV DEBIAN_FRONTEND=noninteractive

# Install Apache and tools
RUN apt update && \
	apt install -y apache2 git wget unzip && \
	wget -O waso.zip https://www.tooplate.com/zip-templates/2130_waso_strategy.zip && \
	unzip waso.zip && \
	rm waso.zip && \
	mv 2130_waso_strategy/* /var/www/html/ && \
	rm -rf 2130_waso_strategy && \
	apt clean && \
	rm -rf /var/lib/apt/lists/*

# Set working directory and permissions
WORKDIR /var/www/html

# Expose Apache HTTP port
EXPOSE 80

# Apache log volume
VOLUME /var/log/apache2

# Start Apache in the foreground
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

