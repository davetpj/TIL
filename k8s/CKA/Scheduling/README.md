# Scheduling

<br>

### Practice Test Manual Scheduling

<br>

1. A pod definition file nginx.yaml is given. Create a pod using the file.
Only create the POD for now. We will inspect its status next.

```
$ ls
$ kubectl apply -f nginx.yaml
```

<br>

2. What is the status of the created POD?

```
$ kubectl get po
```

3. Why is the POD in a pending state?
Inspect the environment for various kubernetes control plane components.

```
$ kubectl get pods --namespace kube-system
```
Solution : We have removed the scheduler from this Kubernetes cluster. As a result, as it stands, the pod will remain in a pending state forever.

<br>

4. Manually schedule the pod on node01.
Delete and recreate the POD if necessary.

```
$ vi nginx.yaml
```

```yaml
---
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  nodeName: node01
  containers:
  -  image: nginx
     name: nginx
```

```
$ kubectl delete -f nginx.yaml
$ kubectl apply -f nginx.yaml
```

<br>

5. Now schedule the same pod on the controlplane node.
Delete and recreate the POD if necessary.

```
$ vi nginx.yaml
```

```yaml
---
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  nodeName: controlplane
  containers:
  -  image: nginx
     name: nginx
```

```
$ kubectl delete -f nginx.yaml
$ kubectl apply -f nginx.yaml
```

<br>

### Practice Test Labels and Selectors

<br>

1. We have deployed a number of PODs. They are labelled with tier, env and bu. How many PODs exist in the dev environment?
Use selectors to filter the output

```
$ kubectl get pods --selector env=dev
or
$ kubectl get pods --selector env=dev --no-headers | wc -l
```

<br>

2. How many PODs are in the finance business unit (bu)?

```
$ kubectl get pods --show-labels | grep finance |grep wc -l
```

<br>

3. How many objects are in the prod environment including PODs, ReplicaSets and any other objects?

```
$ kubectl get all --show-labels |grep prod
```

<br>

4. Identify the POD which is part of the prod environment, the finance BU and of frontend tier?

```
$ kubectl get all --selector env=prod,bu=finance,tier=frontend
or
$ kubectl get pods --show-labels | grep prod
```

<br>

5. A ReplicaSet definition file is given replicaset-definition-1.yaml. Try to create the replicaset. There is an issue with the file. Try to fix it.

```
$ vi replicaset-definition.yaml
```

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
   name: replicaset-1
spec:
   replicas: 2
   selector:
      matchLabels:
        tier: front-end
   template:
     metadata:
       labels:
        tier: front-end
     spec:
       containers:
       - name: nginx
         image: nginx
```

```
$ kubectl apply -f ./
```

<br>

### Practice Test - Taints and Tolerations 

<br>

1. How many nodes exist on the system?
Including the controlplane node.

```
$ kubectl get node
```

<br>

2. Do any taints exist on node01 node?

```
kubectl describe node/node01 | grep -i taints
```

<br>

3. Create a taint on node01 with key of spray, value of mortein and effect of NoSchedule

```
$ kubectl taint nodes node01 spray=mortein:NoSchedule
```

<br>

4. Create a new pod with the nginx image and pod name as mosquito.

```
$ kubectl run mosquito --image=nginx
```

<br>

5. What is the state of the POD?

```
ans : Pending
```

<br>

6. Why do you think the pod is in a pending state?

```
ans : POD Mosquito cannot tolerate taint Mortein
```

7. Create another pod named bee with the nginx image, which has a toleration set to the taint mortein.

```
$ vi
```

```yaml

```

<br>

### Practice Test Resource Limits

<br>

1. A pod called rabbit is deployed. Identify the CPU requirements set on the Pod. in the current(default) namespace

```
$ kubectl get po/rabbit 
```

<br>

2. Delete the rabbit Pod.
Once deleted, wait for the pod to fully terminate.

```
$ kubectl delete po/rabbit
```

<br>

3. Another pod called elephant has been deployed in the default namespace. It fails to get to a running state. Inspect this pod and identify the Reason why it is not running.

```
$ kubectl get po
$ kubectl describe po/elephant
```

<br>

5. The elephant pod runs a process that consume 15Mi of memory. Increase the limit of the elephant pod to 20Mi.
Delete and recreate the pod if required. Do not modify anything other than the required fields.

```
$ kubectl get po/elephant -o yaml > elephant.yaml

$ kubectl delete po/elephant

$ vi elephant.yaml
```

```yaml
...
resources:
    limits:
        memory: 20Mi
    requests:
        memory: 5Mi
...
```

```
$ kubectl apply -f elephant.yaml
```

<br>

6. Inspect the status of POD. Make sure it's running

```
$ kubectl get po
```

7. Delete the elephant Pod.
Once deleted, wait for the pod to fully terminate.

```
$ kubectl delete po/elephant
```

<br>

### Practice Test DaemonSets

<br>

1. How many DaemonSets are created in the cluster in all namespaces?
Check all namespaces

```
$ kubectl get daemonsets -A
```

<br>

2. Which namespace are the DaemonSets created in?

```
$ kubectl get daemonsets -A
```

<br>

3. Which of the below is a DaemonSet?

```
$ kubectl get all -A
```

<br>

4. On how many nodes are the pods scheduled by the DaemonSet kube-proxy

```
$ kubectl describe daemonset kube-proxy -n=kube-system
```

<br>

5. What is the image used by the POD deployed by the kube-flannel-ds DaemonSet?

```
$ kubectl describe daemonset kube-flannel-ds -n=kube-system | grep -i image
```

<br>

6. Deploy a DaemonSet for FluentD Logging

```
$ kubectl create deployment elasticsearch --image=k8s.gcr.io/fluentd-elasticsearch:1.20 -n kube-system --dry-run=client -o yaml > fluentd.yaml
```

``` yaml
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  labels:
    app: elasticsearch
  name: elasticsearch
  namespace: kube-system
spec:
  selector:
    matchLabels:
      app: elasticsearch
  template:
    metadata:
      labels:
        app: elasticsearch
    spec:
      containers:
      - image: k8s.gcr.io/fluentd-elasticsearch:1.20
        name: fluentd-elasticsearch
```