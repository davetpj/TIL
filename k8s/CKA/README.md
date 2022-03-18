## Security
### Practice Test View Certificate Details

<br>

### Practice Certificates API
<br>

### Practice Test KubeConfig

<br>

### Practice Test Role Based Access Controls

<br>

1. How many roles exist in the default namespace?
```
$ kubectl get po -A
$ kubectl describe po/kube-apiserver-controlplane -n kube-system |grep authorization
```

<br>

2. How many roles exist in the default namespace?
```
$ kubectl get roles
```

<br>

3. How many roles exist in all namespaces together?
```
$ kubectl get roles -A
```

<br>

4. What are the resources the kube-proxy role in the kube-system namespace is given access to?
```
$ kubectl describe roles/kube-proxy -n kube-system
```

<br>

5. What actions can the kube-proxy role perform on configmaps?
```
$ kubectl describe roles/kube-proxy -n kube-system
```

<br>

6. Which of the following statements are true?
```
a. kube-proxy role can delete the configmap it created 
b. kube-proy role can get details of configmap object by the name kube-proxy
c. kube-proy role can only view and update configmap object by the name kube-proxy

ans : b
```

<br>

7. Which account is the kube-proxy role assigned to it?
```
$ kubectl describe rolebinding kube-proxy -n kube-system
```

<br>

8. A user dev-suer is created. User's details have been added to kubeconfig file. Inspect the permissions granted to the user. Check if the user can list pods in the default namespace
```
$ kubectl get po --as dev-user
```

<br>

9. Create the necessary roles and role bindings required for the dev-user to create, list and delete pods in the default namespace.
```
$ kubectl create role developer --namespace=default --verb=list,create,delete --resource=pods

$ kubectl create rolebinding dev-user-binding --namespace=default --role=developer --user=dev-user
```

<br>

10. The dev-user is trying to get details about the dark-blue-app pod in the blue namespace. Investigate and fix the issue.
```
$ kubectl get ns
$ kubectl get po -n blue
$ kubectl get role -n blue
$ kubectl edit role developer -n blue

resourceName: blue-app to dark-blue-app
```

<br>

11. Grant the dev-user permissions to create deployments in the blue namespace.
```yaml
---
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  namespace: blue
  name: deploy-role
rules:
- apiGroups: ["apps", "extensions"]
  resources: ["deployments"]
  verbs: ["create"]

---
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: dev-user-deploy-binding
  namespace: blue
subjects:
- kind: User
  name: dev-user
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: deploy-role
  apiGroup: rbac.authorization.k8s.io
```
keywords : rbac

<br>

### Practice Test Cluster Roles

1. How many ClusterRoles do you see defined in the cluster?
```
$ kubectl get clusterroles --no-headers | wc -l

or

$ kubectl get clusterroles --no-headers -o json |jq '.items | length'
```

<br>

2. How man ClusterRoleBindings exist on the cluster?
```
$ kubectl get clusterolebindings --no-headers | wc -l
```

<br>

3. What namespace is the cluster-admin clusterrole part of?
```
a. Cluster Roles are cluster wide and not part of any namespace
b. kube-public
c. kube-system
d. default

ans : a
```

<br>

4. What user/group are the cluster-admin role bound to?
```
$ kubectl describe clusterrolebinding cluster-admin
```

<br>

5. WHat level of permission does the cluster-admin role grant?
```
$ kubectl describe clusterrole cluster-admin
```

<br>

6. A new user michelle joined the team. She will be focusing on the nodes in the cluster. Create the required ClusterRoles and ClusterRoleBindings so she gets access to the nodes.

```
$ kubectl auth can-i list nodes --as michelle
```


```yaml
---
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: node-admin
rules:
- apiGroups: [""]
  resources: ["nodes"]
  verbs: ["get", "watch", "list", "create", "delete"]

---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: michelle-binding
subjects:
- kind: User
  name: michelle
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: node-admin
  apiGroup: rbac.authorization.k8s.io

```
```
$ kubectl apply -f <file-name>.yaml

or

$ kubectl create -f <file-name>.yaml
```
```
$ ubectl auth can-i list nodes --as michelle
```
7. michelle's responsibilites are growing and now she will be responsible for storage as well. Create the required ClusterRoles and ClusterRoleBindings to allow her access to Storage.
```yaml
---
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: storage-admin
rules:
- apiGroups: [""]
  resources: ["persistentvolumes"]
  verbs: ["get", "watch", "list", "create", "delete"]
- apiGroups: ["storage.k8s.io"]
  resources: ["storageclasses"]
  verbs: ["get", "watch", "list", "create", "delete"]

---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: michelle-storage-admin
subjects:
- kind: User
  name: michelle
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: storage-admin
  apiGroup: rbac.authorization.k8s.io
```


### Practice Test Service Accounts
1. How many Service Accounts exist in the default namespace?
```
$ kubectl get serviceaccounts
```

<br>

2. What is the secret token used by the default service account?
```
$ kubectl describe serviceaccounts/default
```

<br>

3. We just deployed the Dashboard application. Inspect the deployment. What is the image used by the deployment?
```
$ kubectl describe deploy/web-dashboard |grep Image
```

<br>

5. What is the state of the dashboard? Have the pod details loaded successfully?
```
ans : Failed
``` 

<br>

6. What type of account does the Dashboard application use to query the Kubernetes API?
```
ans : Service Account
```

<br>

7. Which account does the Dashboard application use to query the Kubernetes API?
```
ans : Default
```

<br>

8. Inspect the Dashboard Application POD and identify the Service Account mounted on it.
```
ans : Default
```

<br>

9. At what location is the ServiceAccount credentials available within the pod?
```
$ kubectl describe po/<web-dashboard-pod-name>
```

<br>

10. The application needs a ServiceAccount with the Right permissions to be created to authenticate to Kubernetes. The 'default' ServiceAccount has limited access. Create a new ServiceAccount named 'dashboard-sa'.

```
$ kubectl create sa dashboard-sa
```

<br>

12. You shouldn't have to copy and paste the token each time. The Dashboard application is programmed to read token from the secret mount location. However currently, the 'default' service account is mounted. Update the deployment to use the newly created ServiceAccount
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-dashboard
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      name: web-dashboard
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
  template:
    metadata:
      creationTimestamp: null
      labels:
        name: web-dashboard
    spec:
      serviceAccountName: dashboard-sa
      containers:
      - image: gcr.io/kodekloud/customimage/my-kubernetes-dashboard
        imagePullPolicy: Always
        name: web-dashboard
        ports:
        - containerPort: 8080
          protocol: TCP
```

<br>

### Practice Test Image Security
1. What is the secret type we choose for the docker registry?
```
$ kubectl create secret --help
```

<br>

2. We have an application running on our cluster. Let us explore it first. What image is the application using? 
```
$ kubectl get deploy
$ kubectl describe deploy/web | grep Image
```

<br>

3. We decided to use a modified version of the application from an internal private registry. Update the image of the deployment to use a new image from myprivateregistry.com:5000
```
$ kubectl edit deploy/web
```
```
nginx:alpine -> myprivateregistry.com:5000/nginx:alpine
```

4. Are the new PODs created with the new images successfully running?
```
$ kubectl get po
```

<br>

5. Create a secret object with the credentials required to access the registry
```
$ kubectl create secret docker-registry private-reg-cred  --docker-username=dock_user --docker-password=dock_password --docker-server=myprivateregistry.com:5000 --docker-email=dock_user@myprivateregistry.com
```

<br>

6. Configure the deployment to use credentials from the new secret to pull images from the private registry
```
$ kubectl get deploy
$ kubectl edit deploy/web
```
```yaml
... # deploy/web
imagePullSecrets:
- name: private-reg-cred
...
```
[Reference](https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod)

<br>

### Practice Test Security Contexts
1. What is the user used to execute the sleep process within the ubuntu0sleeper
```
$ kubectl get po
$ kubectl exec ubuntu-sleeper -- whoami
```

<br>

2. Edit the pod ubuntu-sleeper to run the sleep process with user ID 1010.
```
$ kubectl delete po/ubuntu-sleeper
$ vi ubuntu-sleeper.yaml
```
```yaml
---
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-sleeper
spec:
  securityContext:
    runAsUser: 1010
  containers:
  - name: ubuntu-sleeper
    image: ubuntu
    command: [ "sleep", "4800" ]  
```
```bash
$ kubectl apply -f ubuntu-sleeper.yaml
```

<br>

3. A Pod definition file named multi-pod.yaml is given. With what user are the processes in the web container started?
<br>
<br>
The pod is created with multiple containers and security contexts defined at the Pod and Container level.

```
$ ls
$ cat multi-pod.yaml
```
```yaml
... # output
containers:
- image: ubuntu
  name: web
  command: ["sleep", "5000"]
  securityContext:
   runAsUser: 1002
...
```

<br>

4. With what user are the processes in the sidecar container started?
<br>
<br>
The pod is created with multiple containers and security contexts defined at the Pod and Container level.
```bash
$ ls
$ cat multi-pod.yaml
```
```yaml
... # output
spec:
  securityContext:
    runAsUser: 1001
...
```

<br>

5. Update pod ubuntu-sleeper to run as Root user and with the SYS_TIME capability.

<br>

Note: Only make the necessary changes. Do not modify the name of the pod.
```
$ kubectl delete po/ubuntu-sleeper
$ vi ubuntu-sleeper.yaml 
```
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-sleeper
spec:
  containers:
  - name: ubuntu-sleeper
    image: ubuntu
    securityContext:
      capabilities:
        add: ["SYS_TIME"] 
```
```
$ kubectl apply -f ubuntu-sleeper.yaml
```
[Reference](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#:~:text=apiVersion%3A%20v1%0Akind%3A%20Pod%0Ametadata%3A%0A%20%20name%3A%20security%2Dcontext%2Ddemo%2D4%0Aspec%3A%0A%20%20containers%3A%0A%20%20%2D%20name%3A%20sec%2Dctx%2D4%0A%20%20%20%20image%3A%20gcr.io/google%2Dsamples/node%2Dhello%3A1.0%0A%20%20%20%20securityContext%3A%0A%20%20%20%20%20%20capabilities%3A%0A%20%20%20%20%20%20%20%20add%3A%20%5B%22NET_ADMIN%22%2C%20%22SYS_TIME%22%5D)

<br>

6. Now update the pod to also make use of the NET_ADMIN capability.
<br>
<br>
Note: Only make the necessary changes. Do not modify the name of the pod.
```
$ kubectl delete po/ubuntu-sleeper
$ vi ubuntu-sleeper.yaml
```
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-sleeper
spec:
  containers:
  - name: ubuntu-sleeper
    image: ubuntu
    securityContext:
      capabilities:
        add: ["SYS_TIME","NET_ADMIN"] 
```

<br>

### Practice Test Network Policies