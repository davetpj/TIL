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