# Running the App in a local Kubernetes cluster with Minikube

## Prerequisites

- Install [Kubectl](https://kubernetes.io/docs/tasks/tools/).
- Install [Minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Farm64%2Fstable%2Fbinary+download).
- Follow the steps [here](shared-steps#mongo-db) to make sure you have a database available.
- Copy the [secrets.template.yaml](../../k8s/secrets.template.yaml) file and populate the missing secret values.

## Deploy to Minikube Cluster

- Run `minikube start` to start your local Minikube cluster.
- Run `docker compose -f docker/docker-compose-dev.yaml up --build` to build your Docker image.
- Run `cd k8s && kubectl apply -f secrets.yaml -f deployment.yaml -f service.yaml` to deploy to your local Minikube cluster.
- Run `kubectl port-forward service/module-14 7080:80` to forward the Service port to `localhost:7080`.