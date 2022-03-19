# Core Concepts

### PRACTICE TEST – PODS

1. How many pods exist on the system?
In the current(default) namespace.

```
$ kubectl get pods
```

<br>

2. Create a new pod with the nginx image.

```
$ kubectl run nginx --image=nginx
```

<br>

3. How many pods are created now?
Note: We have created a few more pods. So please check again.

```
$ kubectl get pods
```

<br>

4. What is the image used to create the new pods?
You must look at one of the new pods in detail to figure this out.

```
$ kubectl describe po/<pod-name> |grep Image
```

<br>

5. Which nodes are these pods placed on?
You must look at all the pods in detail to figure this out.

```
$ kubectl get po -o wide
```

<br>

6. How many containers are part of the pod webapp?
Note: We just created a new POD. Ignore the state of the POD for now.

```
$ kubectl get po
```

<br>

7. What images are used in the new webapp pod?
You must look at all the pods in detail to figure this out.

```
$ kubectl describe po/webapp |grep Image
```

<br>

8. What is the state of the container agentx in the pod webapp?
Wait for it to finish the ContainerCreating state

```
$ kubectl describe po/webapp
```

<br>

9. Why do you think the container agentx in pod webapp is in error?
Try to figure it out from the events section of the pod.

```
ans : A Docker image with this name doesn't exist on Docker Hub
```

<br>

10. What does the READY column in the output of the kubectl get pods command indicate?

```
ans : Running Containers in POD/Total Containers in POD
```

<br>

11. Delete the webapp Pod.
Once deleted, wait for the pod to fully terminate.

```
$ kubectl delete po/webapp
```

<br>

12. Create a new pod with the name redis and with the image redis123.
Use a pod-definition YAML file. And yes the image name is wrong! 

```
$ kubectl run redis --image=redis123
```

<br>

13. Now change the image on this pod to redis.
Once done, the pod should be in a running state. 

```
$ kubectl edit po/redis
```

```yaml
spec:
  containers:
  - image: redis # redis123 -> redis
```

<br>

