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

