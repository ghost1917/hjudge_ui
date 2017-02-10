FROM centos:6

# ==================================================
# Install java
ENV \
  JAVA_VERSION=8u111 \
  BUILD_VERSION=b14

RUN \
  curl -s -L -H "Cookie: oraclelicense=accept-securebackup-cookie" -o /tmp/java.rpm \
    "http://download.oracle.com/otn-pub/java/jdk/$JAVA_VERSION-$BUILD_VERSION/jdk-$JAVA_VERSION-linux-x64.rpm" && \
  yum -y install /tmp/java.rpm && \
  yum clean all && \
  rm -f /tmp/java.rpm

ENV JAVA_HOME=/usr/java/default

# ==================================================
# Install hadoop client
COPY ./files/cloudera-cdh5.repo /etc/yum.repos.d/cloudera-cdh5.repo

RUN \
  rpm --rebuilddb && \
  yum install -y \
    hadoop-client \
    hive \
    openssl-devel \
    spark-core \
  yum clean all

ENV LD_LIBRARY_PATH=/usr/lib/hadoop/lib/native

# ==================================================
# Install python and miniconda
RUN \
  yum --disablerepo="*" --enablerep="base" install -y tar bzip2 && \
  yum clean all && \
  curl -s -L https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh -o /tmp/miniconda.sh && \
  bash /tmp/miniconda.sh -b -p /opt/conda && \
  /opt/conda/bin/conda update -y conda && \
  rm -f /tmp/miniconda.sh
ENV PATH /opt/conda/bin:$PATH


# ==================================================
