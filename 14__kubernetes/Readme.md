# Kubernetes 
- also knows as k8s
- developed by google in 2014
- Now maintained by: Cloud Native Computing Foundation (CNCF)

## Origin
- Kubernetes  was inspired by Google’s internal cluster management system called Borg.
- Google had over a decade of experience running massive-scale systems and created Kubernetes
- to share that model with the world in an open-source form.

## Why Do We Need Kubernetes?
- In the era of microservices and cloud-native apps,
- applications are made of many loosely coupled components running in containers (like Docker).
- Managing these containers manually becomes very complex.

## Kubernetes helps to:
- Automate deployment, scaling, and operations of containers

- Orchestrate multiple containers across clusters

- Self-heal (restart crashed containers, replace failed ones)

- Load balance traffic across services

- Ensure zero downtime deployments (rolling updates, rollbacks)

- Keep infrastructure consistent, portable, and declarative

## How to Use Kubernetes (Basic Steps)
### 1. Set up Kubernetes Cluster
#### You can use:

- Minikube (local testing)

- Kind (Kubernetes in Docker)
- k3d  (Kubernetes in Docker)
- Cloud providers (e.g., Google Kubernetes Engine, Amazon EKS, Azure AKS)

### 2. Define Your Application
#### Use YAML files to declare:

- Pods (smallest unit)

- Deployments

- Services

- ConfigMaps / Secrets

- Ingress rules

# Difference Between Monolithic and Microservices

| Feature              | Monolithic Architecture                     | Microservices Architecture                    |
|----------------------|----------------------------------------------|-----------------------------------------------|
| Structure            | Single, unified codebase and application     | Multiple, small, independent services         |
| Deployment           | Entire app is deployed as one unit           | Each service is deployed separately           |
| Development          | One team usually works on the full system    | Different teams work on different services    |
| Scalability          | Scales the whole application                 | Scales individual services as needed          |
| Technology Stack     | Uses one language/framework throughout       | Each service can use different technologies   |
| Codebase             | Single large codebase                        | Multiple small codebases                      |
| Data Management      | Usually uses one shared database             | Each service can have its own database        |
| Fault Isolation      | One bug can crash the whole app              | Failure in one service doesn’t crash others   |
| Testing              | Easier unit testing, harder system testing   | Needs more setup for integration testing      |
| Deployment Speed     | Slower, full redeploy for small changes      | Faster, deploy only the changed service       |
| Maintenance          | Harder as the app grows                      | Easier due to isolation                       |
| Communication        | Internal method calls                        | Inter-service (e.g., HTTP, gRPC)              |




