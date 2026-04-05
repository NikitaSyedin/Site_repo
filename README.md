Команды для запуска:
```
docker build --network=host -t my-flask-app .
minikube start --driver=docker
minikube image load my-flask-app:latest
kubectl apply -f k8s/kuber.yaml
kubectl get pods
minikube service flask-service
```
