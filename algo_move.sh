cd /mnt/c/Users/kmkwo/Downloads
mv exercise.zip /home/kangmin/baekjoon-onlineJudge
cd /home/kangmin/baekjoon-onlineJudge && unzip exercise.zip -d exercise
cd exercise && rm main.py && cp -r . ../String
cd .. && rm -rf exercise*
