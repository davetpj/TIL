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