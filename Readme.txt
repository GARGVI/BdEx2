#ejecucion cluster hadoop

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-*.jar
-input Input/data.csv
-output Output/monthlyConsumption
-file mapreduce/monthlyConsumption/mapper.py
-file mapreduce/monthlyConsumption/reducer.py
-mapper mapreduce/monthlyConsumption/mapper.py
-combiner mapreduce/monthlyConsumption/reducer.py
-reducer mapreduce/monthlyConsumption/reducer.py

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-*.jar
-input Output/monthlyConsumption/mapper_output.txt
-output Output/avgMonthlyConsumption
-file mapreduce/avgMonthlyConsumption/mapper.py
-file mapreduce/avgMonthlyConsumption/reducer.py
-mapper mapreduce/avgMonthlyConsumption/mapper.py
-reducer mapreduce/avgMonthlyConsumption/reducer.py




#ejecucion local en windows

cd C:\Users\Gemma\ProyectosPython\Beedata

python ./mapreduce/monthlyConsumption/mapper.py < ./Input/data.csv > ./Output/monthlyConsumption/mapper_output.txt

python ./mapreduce/monthlyConsumption/reducer.py < ./Output/monthlyConsumption/mapper_output.txt > ./Output/monthlyConsumption/reducer_output.txt

python ./mapreduce/avgMonthlyConsumption/mapper.py < ./Output/monthlyConsumption/reducer_output.txt > ./Output/avgMonthlyConsumption/mapper_output.txt

python ./mapreduce/avgMonthlyConsumption/reducer.py < ./Output/avgMonthlyConsumption/mapper_output.txt > ./Output/avgMonthlyConsumption/reducer_output.txt