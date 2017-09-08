# JSTMB_O185_Pipeline

This is the source code for our JSTMB primitive on the seed data O185.

Once you clone this folder into your local repo, you can directly build the Docker image by:

docker build -t jstmb185 ./

Then, you can run the pipeline script in the following way:

docker run jstmb185 python O185_JSTMB_wrapper.py "trainData.csv" "trainTargets.csv"

The output is the selected features stored in a csv file
