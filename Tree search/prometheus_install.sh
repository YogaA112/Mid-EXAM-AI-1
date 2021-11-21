#!/bin/bash


mkdir -p /home/juanw/promethues
mkdir -p /home/juanw/promethues/server
mkdir -p /home/juanw/promethues/client
touch /home/juanw/promethues/server/rules.yml
chmod 777 /home/juanw/promethues/server/rules.yml


cat > /home/juanw/promethues/server/prometheus.yml << EOF
global:
  scrape_interval:     15s # 默认抓取间隔, 15秒向目标抓取一次数据。
  external_labels:
    monitor: 'codelab-monitor'
# 这里表示抓取对象的配置
scrape_configs:
    #这个配置是表示在这个配置内的时间序例，每一条都会自动添加上这个{job_name:"prometheus"}的标签  - job_name: 'prometheus'
    scrape_interval: 5s # 重写了全局抓取间隔时间，由15秒重写成5秒
    static_configs:
      - targets: ['localhost:9090']
EOF


docker run --name=prometheus -d \
	-p 9090:9090 \
	-v /home/juanw/promethues/server/prometheus.yml:/etc/prometheus/prometheus.yml \
	-v /home/juanw/promethues/server/rules.yml:/etc/prometheus/rules.yml \
	prom/prometheus:v2.7.2 \
	--config.file=/etc/prometheus/prometheus.yml \
	--web.enable-lifecycle
docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:rw \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  google/cadvisor:latest
