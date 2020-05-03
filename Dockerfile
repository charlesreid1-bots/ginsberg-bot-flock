FROM rainbowmindmachine/rainbowmindmachine:v23
MAINTAINER charles@charlesreid1.com

RUN git clone https://git.charlesreid1.com/bots/b-ginsberg.git /ginsberg
WORKDIR "/ginsberg/bot"
CMD ["/usr/bin/env","python","GinsbergBotFlock.py"]

