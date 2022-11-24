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

https://dev.to/boyu1997/run-python-mapreduce-on-local-docker-hadoop-cluster-1g46

cat ./carpeta2/Argentina.txt | python3 mapper.py

cat ./carpeta2/Argentina.txt | python3 mapper.py | sort -k1,1 | python3 reducer.py


docker-compose up -d

docker exec -it namenode bash

mkdir input

docker cp ./carpeta1/Chile.txt 4689fe3d5015:/input/.
docker cp ./carpeta1/Bolivia.txt 4689fe3d5015:/input/.
docker cp ./carpeta2 4689fe3d5015:/input/.
docker cp mapper.py 4689fe3d5015:.
docker cp reducer.py 4689fe3d5015:.

mkdir input
echo "Hello World" >input/f1.txt
echo "Hello Docker" >input/f2.txt
echo "Hello Hadoop" >input/f3.txt
echo "Hello MapReduce" >input/f4.txt

hdfs dfs -rm -r /user/root/input
hdfs dfs -rm -r /user/root/output

hadoop fs -mkdir -p input

hdfs dfs -put ./input/* input

hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
-file mapper.py    -mapper mapper.py \
-file reducer.py   -reducer reducer.py \
-input input -output output


hadoop jar mapper.py mapper.py input output

hdfs dfs -cat output/part-r-00000

docker-compose down

hdfs dfs -copyFromLocal /path 1 /path 2 .... /path n /destination

hdfs dfs -copyFromLocal /home/dikshant/Documents/word_count_data.txt /word_count_in_python

sudo docker cp ./hadoop-mapreduce-examples-2.7.1-sources.jar ID_CONTAINER_NAMENODE:hadoop-mapreduce-examples-2.7.1-sources.jar

sudo docker-compose down


#############################################

cat ./jobs/data/carpeta1/Chile.txt ./jobs/data/carpeta1/Bolivia.txt | python3 ./jobs/jars/mapper.py | sort -k1,1 | python3 ./jobs/jars/reducer.py
cat ./jobs/data/carpeta2/Perú.txt ./jobs/data/carpeta2/Argentina.txt | python3 ./jobs/jars/mapper.py | sort -k1,1 | python3 ./jobs/jars/reducer.py
cat ./jobs/data/input/test.txt ./jobs/data/input/test2.txt | python3 ./jobs/jars/mapperfinal.py | sort -k1,1 | python3 ./jobs/jars/reducerfinal.py
hadoop fs -rm -r -f /test/outcarpeta1 /test/outcarpeta2 /test/inputresultados /test/inputresultado

docker-compose up --build -d

http://localhost:9870/

docker exec -it namenode bash

cd jars

hadoop fs -rm -r -f /test

hadoop fs -mkdir -p /test/
hadoop fs -mkdir -p /test/inputresultados
hadoop fs -copyFromLocal -f /app/data/carpeta1 /test/
hadoop fs -copyFromLocal -f /app/data/carpeta2 /test/

mapred streaming -files mapper.py,reducer.py \
-input /test/carpeta1 \
-output /test/outcarpeta1 \
-mapper "python mapper.py" \
-reducer "python reducer.py"

mapred streaming -files mapper.py,reducer.py \
-input /test/carpeta2 \
-output /test/outcarpeta2/ \
-mapper "python mapper.py" \
-reducer "python reducer.py"

hadoop fs -mv /test/outcarpeta1/part-00000 /test/outcarpeta1/r1.txt
hadoop fs -mv /test/outcarpeta2/part-00000 /test/outcarpeta2/r2.txt
hadoop fs -mv /test/outcarpeta1/r1.txt /test/inputresultados/
hadoop fs -mv /test/outcarpeta2/r2.txt /test/inputresultados/
hadoop fs -ls /test/inputresultados

hadoop fs -cat /test/inputresultados/r1.txt

mapred streaming -files mapperfinal.py,reducerfinal.py \
-input /test/inputresultados \
-output /test/final \
-mapper "python mapperfinal.py" \
-reducer "python reducerfinal.py"

hadoop fs -cat /test/final/part-00000
hadoop fs -mv /test/final/part-00000 /test/final/final.txt

hadoop fs -ls /test/outcarpeta1
hadoop fs -ls /test/outcarpeta2
hadoop fs -cat /test/output/part-00000