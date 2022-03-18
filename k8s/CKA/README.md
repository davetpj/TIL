## Security
### Practice Test View Certificate Details

### Practice Certificates API

### Practice Test KubeConfig

### Practice Test Role Based Access Controls

1. How many roles exist in the default namespace?
```
$ kubectl get po -A
$ kubectl describe po/kube-apiserver-controlplane -n kube-system |grep authorization
```
2. How many roles exist in the default namespace?
```
$ kubectl get roles
```

3. How many roles exist in all namespaces together?
```
$ kubectl get roles -A
```

4. What are the resources the kube-proxy role in the kube-system namespace is given access to?
```
$ kubectl describe roles/kube-proxy -n kube-system
```
5. What actions can the kube-proxy role perform on configmaps?
```
$ kubectl describe roles/kube-proxy -n kube-system
```
6. Which of the following statements are true?
```
a. kube-proxy role can delete the configmap it created 
b. kube-proy role can get details of configmap object by the name kube-proxy
c. kube-proy role can only view and update configmap object by the name kube-proxy

ans : b
```
7. Which account is the kube-proxy role assigned to it?
```
$ kubectl describe rolebinding kube-proxy -n kube-system
```
8. A user dev-suer is created. User's details have been added to kubeconfig file. Inspect the permissions granted to the user. Check if the user can list pods in the default namespace
```
$ kubectl get po --as dev-user
```

9. Create the necessary roles and role bindings required for the dev-user to create, list and delete pods in the default namespace.
```
$ kubectl create role developer --namespace=default --verb=list,create,delete --resource=pods

$ kubectl create rolebinding dev-user-binding --namespace=default --role=developer --user=dev-user
```

10. The dev-user is trying to get details about the dark-blue-app pod in the blue namespace. Investigate and fix the issue.
```
$ kubectl get ns
$ kubectl get po -n blue
$ kubectl get role -n blue
$ kubectl edit role developer -n blue

resourceName: blue-app to dark-blue-app
```
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

### Practice Test Cluster Roles

### Practice Test Service Accounts

### Practice Test Image Security

### Practice Test Network Policies