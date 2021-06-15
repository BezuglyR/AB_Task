FROM bezuglyr/python3-chrome

RUN mkdir /usr/src/test
ADD . /usr/src/test/
WORKDIR /usr/src/test

VOLUME /dev/shm:/dev/shm

EXPOSE 4444:4444

RUN pip3 install --no-cache-dir -r requirements.txt
RUN python3 test_suit.py

#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
#    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
#RUN apt-get update && apt-get -y install google-chrome-stable

#ENTRYPOINT ["python", "test_suit.py"]