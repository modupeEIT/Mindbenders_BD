#!usr/bin/bash

cd
sudo apt update

#create opt dir
mkdir opt
cd opt

#Download Java
wget -O jdk-8u221-linux-x64.tar.gz \-c --content-disposition \
"https://javadl.oracle.com/webapps/download/AutoDL?BundleId=239835_230deb18db3e4014bb8e3e8324f81b43"

#Unzip
tar -zxvf jdk-8u221-linux-x64.tar.gz

#remove tar file
rm jdk-8u221-linux-x64.tar.gz

#home dir
cd

#set the path
echo "JAVA_HOME=/opt/jdk1.8.0_221" >> .bash_profile.sh
echo "export PATH=$PATH:$JAVA_HOME/bin" >> .bash_profile.sh
source .bash_profile.sh
  

#set up SSH
sudo apt-get install openssh-server openssh-client
ssh keygen -t rsa -P
cat $HOME/.ssh/id_rsa.pub>>$HOME/.ssh/authorized_keys

#download and install HADOOP
cd opt
wget https://archive.apache.org/dist/hadoop/common/hadoop-2.7.1/hadoop-2.7.1.tar.gz
tar hadoop-2.7.1.tar.gz

#set path 
echo "export HADOOP_PREFIX=/home/hdadmin/hadoop-2.7.1" >> .bash_profile.sh
echo "export PATH=$PATH:$HADOOP_PREFIX/bin" >> .bash_profile.sh
echo "export PATH=$PATH:$HADOOP_PREFIX/sbin" >> .bash_profile.sh
echo "export HADOOP_MAPRED_HOME=${HADOOP_PREFIX}" >> .bash_profile.sh
echo "export HADOOP_COMMON_HOME=${HADOOP_PREFIX}" >> .bash_profile.sh
echo "export HADOOP_HDFS_HOME=${HADOOP_PREFIX}" >> .bash_profile.sh
echo "export YARN_HOME=${HADOOP_PREFIX}" >> .bash_profile.sh
echo "export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_PREFIX/lib/native" >> .bash_profile.sh
echo "export HADOOP_OPTS=”-Djava.library.path=$HADOOP_PREFIX/lib" >> .bash_profile.sh
source .bash_profile.sh

cd opt/hadoop-2.7.3/etc/hadoop
sed 's+JAVA_HOME=${JAVA_HOME}+JAVA_HOME=~/opt/jdk1.8.0_221+' hadoop-env.sh
    
echo "<configuration>" >> core-site.xml
echo "<property> >>" core-site.xml
echo "<name>fs.defaultFS</name>" core-site.xml
echo "<value>hdfs://localhost:9000</value>" core-site.xml
echo "</property>" core-site.xml
echo "<property>" core-site.xml
echo "<name>hadoop.tmp.dir</name>" core-site.xml
echo "<value>/home/hdadmin/hdata</value>" core-site.xml
echo "</property>" core-site.xml
echo "</configuration>" core-site.xml

echo "<configuration>" >> mapred-site.xml
echo "<property>" >> mapred-site.xml
echo "<name>dfs.replication</name>" >> mapred-site.xml
echo "<value>1</value>" >> mapred-site.xml
echo "</property>" >> mapred-site.xml
echo "</configuration>" >> mapred-site.xml
cp mapred-site.xml.template mapred-site.xml

echo "<configuration>" >> yarn-site.xml
echo "<property>" >> yarn-site.xml
echo "<name>yarn.nodemanager.aux-services</name>" >> yarn-site.xml
echo "<value>mapreduce_shuffle</value>" >> yarn-site.xml
echo "</property>" >> yarn-site.xml
echo "<property>" >> yarn-site.xml
echo "<name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>" >> yarn-site.xml
echo "<value>org.apache.hadoop.mapred.ShuffleHandler</value>" >> yarn-site.xml
echo "</property>" >> yarn-site.xml
echo "</configuration>" >> yarn-site.xml
    
