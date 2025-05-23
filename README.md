🚀 EKS Sample Application Deployment (Flask Backend + Python Frontend)
This project contains a simple full-stack application deployed on AWS EKS using Kubernetes.
The backend is a Flask API, and the frontend is a lightweight static HTML page served by Python.

It covers:

Kubernetes Deployments and Services

Liveness and Readiness Probes

ConfigMaps and Secrets

Horizontal Pod Autoscaler (HPA)

Logging via Fluent Bit to CloudWatch

Monitoring and alerting

🗂️ Project Structure
bash
Copy
Edit
.
├── backend/         # Flask REST API
├── frontend/        # Static HTML frontend
├── k8s/             # Kubernetes manifests
├── monitoring/      # Logging & monitoring setup
└── README.md
📦 Prerequisites
Before you begin, ensure the following:

AWS CLI configured (aws configure)

EKS cluster is created and kubectl is configured

Docker installed and logged into your container registry (e.g., Docker Hub or ECR)

kubectl and eksctl installed and working

IAM roles and CloudWatch log group (if needed) are set up

🔨 Step 1: Build & Push Docker Images
📁 Backend

cd backend
docker build -t <your-dockerhub-username>/eks-backend:latest .
docker push <your-dockerhub-username>/eks-backend:latest
🌐 Frontend

cd ../frontend
docker build -t <your-dockerhub-username>/eks-frontend:latest .
docker push <your-dockerhub-username>/eks-frontend:latest
🔁 Replace <your-dockerhub-username> with your Docker Hub or ECR username.

🧠 Step 2: Update Image References in YAML
In the following files, replace the image placeholders:

k8s/backend-deployment.yaml → image: <your-backend-image>

k8s/frontend-deployment.yaml → image: <your-frontend-image>

🚀 Step 3: Deploy to EKS
Apply all Kubernetes manifests:


kubectl apply -f k8s/
This will:

Create ConfigMap and Secret

Deploy frontend and backend apps

Expose frontend via LoadBalancer

Set up internal ClusterIP service for backend

Deploy HPA for backend

✅ Step 4: Validate Deployment
Services

kubectl get svc
Look for the external IP of the frontend service under EXTERNAL-IP. Open it in a browser.

Pods & Logs

kubectl get pods
kubectl logs <pod-name>
HPA (Auto-scaling)

kubectl get hpa
To test HPA, generate load on the backend using a tool like hey, ab, or a looped curl.

📊 Step 5: Enable Logging with Fluent Bit (CloudWatch)
Apply Fluent Bit Config and DaemonSet

kubectl apply -f monitoring/fluent-bit-configmap.yaml
kubectl apply -f monitoring/fluent-bit-daemonset.yaml
Ensure the Fluent Bit pods are running:

kubectl -n kube-system get pods | grep fluent-bit
Your container logs will now be forwarded to CloudWatch Logs under the group eks-app-logs.

🔔 Step 6: CloudWatch Monitoring & Alerts
Set up the following in AWS Console:

Create CloudWatch Alarm for backend CPU usage > 70%

Attach SNS Topic with your email

Confirm email subscription from your inbox

Optional:

Create dashboards for CPU, memory, replica count

Monitor logs using CloudWatch Logs Insights

📌 Clean Up
To remove all deployed resources:


kubectl delete -f k8s/
kubectl delete -f monitoring/
✅ Deliverables Summary
 Backend & frontend deployments

 ConfigMap and Secret integration

 Liveness and readiness probes

 Auto-scaling with HPA

 Fluent Bit logging to CloudWatch

 SNS Alert (documented in monitoring/sns-alert-policy.md)

