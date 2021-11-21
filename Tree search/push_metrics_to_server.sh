#!/bin/bash

for i in `seq 1 100`; do
cat << EOF | curl --data-binary @- http://192.168.17.55:9091/metrics/job/cqh/instance/test
# 锻炼场所价格
muscle_metric{label="gym"} $(($RANDOM%500))
# 三大项数据 kg
bench_press $(($RANDOM%200))
dead_lift 160
deep_squal{label="testlabel"} 160
EOF

sleep $(($RANDOM%10))


cat << EOF | curl --data-binary @- http://192.168.17.55:9091/metrics/job/cqh/instance/test
# 锻炼场所价格
muscle_metric{label="gym"} $(($RANDOM%500))
# 三大项数据 kg
bench_press $(($RANDOM%300))
dead_lift 260
deep_squal{label="testlabel"} 260
EOF

sleep $(($RANDOM%10))
done
