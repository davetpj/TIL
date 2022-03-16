# Daemonset


데몬셋은 클러스터 전체에 pod를 띄울때 사용하는 컨트롤러.

- replicaset 과 비슷하지만 replicas 를 지정하지 않음. (모든 노드에 하나씩 배치)
- 노드가 추가되면 자동으로 하나의 pod를 배치.
- 노드가 제거되면 삭제된 pod를 다른 노드에 배치하지 않음.
- 각각의 노드마다 배치해야하는 특성이 있는 성능 수집이나 로그수집이나 스토리지 서비스가 필요할 때 사용.

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd-elasticsearch
  namespace: kube-system
  labels:
    k8s-app: fluentd-logging
spec:
  selector:
    matchLabels:
      name: fluentd-elasticsearch
  template:
    metadata:
      labels:
        name: fluentd-elasticsearch
    spec:
      tolerations:
      # this toleration is to have the daemonset runnable on master nodes
      # remove it if your masters can't run pods
      - key: node-role.kubernetes.io/master
        operator: Exists
        effect: NoSchedule
      containers:
      - name: fluentd-elasticsearch
        image: quay.io/fluentd_elasticsearch/fluentd:v2.5.2
        resources:
          limits:
            memory: 200Mi
          requests:
            cpu: 100m
            memory: 200Mi
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: varlibdockercontainers
          mountPath: /var/lib/docker/containers
          readOnly: true
      terminationGracePeriodSeconds: 30
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: varlibdockercontainers
        hostPath:
          path: /var/lib/docker/containers

```

## taints

특정 노드에 taint를 지정할 수 있다.
taint를 설정한 노드에는 pod이 스케쥴링 되지 않음. 


## tolerations

taint 설정된 노드에 pod를 스케쥴링 하려면 toleration을 이용해서 지정해 주어야함.

