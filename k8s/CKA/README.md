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

### Practice Test Image Security

### Practice Test Network Policies