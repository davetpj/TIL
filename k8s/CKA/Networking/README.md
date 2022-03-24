# Networking

### Preactice Test - Explore Environment

<br>

1. How many nodes are part of this cluster?

```
$ kubectl get node
```

<br>

2. What is the Internal IP address of the controlplane node in this cluster?

```
$ kubectl get node -o wide
```

<br>

3. What is the network interface configured for cluster connectivity on the master node?

```
$ kubectl get node -o wide

$ ip a | grep <Interneal-IP>
```

<br>

4. What is the MAC address of the interface on the master node?

```
$ ip link show eth0
```

<br>

5. What is the IP address assigned to node01?

```
$ kubectl get node -o wide
```

<br>

6. What is the MAC address assigned to node01?

```
$ arp node01
```

<br>

7. We use Docker as our container runtime. What is the interface/bridge created by Docker on this host?

```
$ ip link | grep docker
```

<br>

8. What is the state of the interface docker0?

```
$ ip link show docker0
```

<br>

9. If you were to ping google from the master node, which route does it take?
What is the IP address of the Default Gateway?

```
$ ip route show default
```

<br>

10. What is the port the kube-scheduler is listening on in the controlplane node?

```
$ netstat -nplt | grep kube-scheduler
```

<br>

11. Notice that ETCD is listening on two ports. Which of these have more client connections established?

```
$ netstat -anp | grep etcd
```

<br>

### Practice Test CNI Weave

<br>

1. Inspect the kubelet service and identify the network plugin configured for Kubernetes.

```
$ ps -aux | grep kubelet | grep --color network
```
명령어 잘 모르겠음 (aux, multiple grep)

<br>

2. What is the path configured with all binaries of CNI supported plugins?

```
ans : /opt/cni/bin
```

<br>

3. Identify which of the below plugins is not available in the list of available CNI plugins on this host?

```
$ ls /opt/cni/bin
```

<br>

4. What is the CNI plugin configured to be used on this kubernetes cluster?

```
$ ls /etc/cni/net.d/

```

<br>

5. What binary executable file will be run by kubelet after a container and its associated namespace are created.

```
$ cat /etc/cni/net.d/ grep | type
```

### Practice Test - Deploy Network Solution

1. In this practice test we will install weave-net POD networking solution to the cluster. Let us first inspect the setup.
We have deployed an application called app in the default namespace. What is the state of the pod?

```
$ kubectl get po
```

2. Inspect why the POD is not running.

```
$ kubectl describe po/ap
```

3. Deploy weave-net networking solution to the cluster.
Replace the default IP address and subnet of weave-net to the 10.50.0.0/16. Please check the official weave installation and configuration guide which is available at the top right panel.

```
$ ???
```

### Deploy Network Solution

<br>

1. In this practice test we will install weave-net POD networking solution to the cluster. Let us first inspect the setup. We have deployed an application called app in the default namespace. What is the state of the pod?

```
$ kubectl get po
```

<br>

2. Inspect why the POD is not running.

```
$ kubectl describe po/app
```

3. Deploy weave-net networking solution to the cluster.
Replace the default IP address and subnet of weave-net to the 10.50.0.0/16. Please check the official weave installation and configuration guide which is available at the top right panel.

```
$ ???
```
