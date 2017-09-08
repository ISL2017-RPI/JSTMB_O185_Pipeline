FROM keyi/python2-mcr2017a-rpi-isl


COPY JSTMB_O185/ ./JSTMB_O185
COPY setup.py ./
COPY O185_JSTMB_wrapper.py ./
COPY trainData.csv ./
COPY trainTargets.csv ./

