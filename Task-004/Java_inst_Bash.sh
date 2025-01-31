#!usr/bin/bash


#check for update
sudo apt update

#create opt dir
cd
mkdir opt
cd opt

#Download Java
wget -O jdk-8u221-linux-x64.tar.gz \
-c --content-disposition \
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
