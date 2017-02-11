FROM lwieske/java-8:jre-8u121

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
