sudo docker run --rm -it -v $(pwd):/source -p 50070-50080:50070-50080 sequenceiq/hadoop-docker /etc/bootstrap.sh -bash
crea MapReducer
cp /source/Article\ 6/*.java /source/Article\ 6/*.csv MapReducer
export HADOOP_HOME=/usr/local/hadoop


https://code.tutsplus.com/es/tutorials/how-to-download-files-in-python--cms-30099
https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html


python3 -m pip install wikipedia
https://www.delftstack.com/es/howto/python/write-string-to-a-file-in-python/
https://shortcut.com/developer-how-to/how-to-set-up-a-hadoop-cluster-in-docker


https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/

cat ./carpeta2/Argentina.txt | python3 mapper.py

cat ./carpeta2/Argentina.txt | python3 mapper.py | python3 reducer.py


sudo docker-compose up -d

sudo docker exec -it namenode bash

mkdir input

sudo docker cp ./carpeta1 56bf1519146d:/input/.
sudo docker cp ./carpeta2 56bf1519146d:/input/.
sudo docker cp mapper.py 56bf1519146d:.
sudo docker cp reducer.py 56bf1519146d:.

hadoop fs -mkdir -p input

hdfs dfs -put ./input/* input

hadoop jar /hadoop-streaming-2.7.3.jar \

> -input /input/carpeta1/Chile.txt\

> -output /word_count_in_python/output \

> -mapper /mapper.py \

> -reducer /reducer.py

hadoop jar mapper.py mapper.py input output

hdfs dfs -cat output/part-r-00000

docker-compose down

hdfs dfs -copyFromLocal /path 1 /path 2 .... /path n /destination

hdfs dfs -copyFromLocal /home/dikshant/Documents/word_count_data.txt /word_count_in_python

sudo docker cp ./hadoop-mapreduce-examples-2.7.1-sources.jar ID_CONTAINER_NAMENODE:hadoop-mapreduce-examples-2.7.1-sources.jar

sudo docker-compose down