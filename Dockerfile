FROM amazonlinux:latest as base

WORKDIR usr/src/binpack

# Make able to install Node 6.x from upstream
# Install GCC, Make, NodeJS, and libyaml for parsing .yml (serverless) via Python
# Clean-up after ourselves
RUN curl --silent --location https://rpm.nodesource.com/setup_10.x | bash - && \
  yum install -y python3-pip python3-devel gcc-c++ make nodejs libyaml libyaml-devel && \
  yum clean all && rm -rf /var/cache/yum

# Install the serverless framework globally
RUN npm install -g serverless

# Install/upgrade pip, awscli, mysqlclient for Python
RUN ls -la /usr/local/bin
RUN find / -iname "pip*"

RUN pip-3 install --no-cache-dir --upgrade pip awscli pyyaml


COPY package.json package.json
RUN npm i

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY scripts ./scripts
COPY serverless.yml .
COPY src .

FROM base as deploy

CMD cd scripts && ./deploy.sh