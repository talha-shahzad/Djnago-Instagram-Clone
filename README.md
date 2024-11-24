
# Instagram Clone

This project is a simple **Instagram clone** built with Django, designed to mimic the core features of Instagram, including posting images, viewing stories, liking and commenting on posts, and following other users.

## Features

- **User Authentication**: Users can register, log in, and log out securely.
- **Profile Management**: Each user has a profile with an avatar and bio.
- **Posts**: Users can upload images, with a maximum of 10 images per post.
- **Stories**: Users can add temporary stories that are available for 24 hours.
- **Likes and Comments**: Users can like and comment on each other's posts.
- **Follow System**: Users can follow and unfollow each other.

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: Django Templates, HTML, CSS, JavaScript (optional for interactivity)
- **Database**: SQLite (default for Django) or PostgreSQL (recommended for production)
- **Other**: Pillow (for image handling)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/instagram-clone.git
    cd instagram-clone
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    - Apply migrations:
      ```bash
      python manage.py migrate
      ```

    - Create a superuser:
      ```bash
      python manage.py createsuperuser
      ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Access the application:**
    - Open [http://localhost:8000](http://localhost:8000) in your browser.

## Usage

1. **Register**: Create a new user account.
2. **Set Up Profile**: Customize your profile with an avatar and bio.
3. **Create a Post**: Upload images (max 10) and create a new post.
4. **View and Add Stories**: Share stories that will disappear after 24 hours.
5. **Like and Comment**: Engage with posts by liking and leaving comments.
6. **Follow Users**: Follow other users to see their posts and stories.

## Project Structure

- **templates/**: HTML templates for rendering pages with Django's template system.
  - **base.html**: Main template with navigation.
  - **post_list.html**: Shows the feed of posts.
  - **profile.html**: User profile page.
  - **story.html**: Page for viewing stories.
- **static/**: CSS, JavaScript, and images.
- **accounts/**: User authentication and profile management.
- **posts/**: Core functionality for posts, including images, comments, and likes.
- **stories/**: Temporary story functionality.
- **follows/**: Follow system to connect users.
- **media/**: Directory where uploaded images are stored.
<br>

Now we will start the process of applying the DEVOPS concepts to deploy the project.

## Prerequisites

- **Docker Desktop** installed and running
- **Minikube** installed
- Kubernetes CLI (`kubectl`) configured

---

## Step 1: Install Docker Desktop

1. Download Docker Desktop from the [official website](https://www.docker.com/products/docker-desktop/).
2. Install Docker Desktop and follow the setup instructions to enable the Docker Engine.
3. Verify Docker installation by running the following command:
   ```bash
   docker ps
   ```
   This should display the list of running containers.

---

## Step 2: Install Minikube

1. Download Minikube from the [official website](https://minikube.sigs.k8s.io/docs/start/).
2. **Windows users** can use PowerShell to install Minikube:
   ```powershell
   New-Item -Path 'c:\' -Name 'minikube' -ItemType Directory -Force
   Invoke-WebRequest -OutFile 'c:\minikube\minikube.exe' -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' -UseBasicParsing
   ```
3. Add Minikube to your system's `PATH` environment variable:
   ```powershell
   $oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
   if ($oldPath.Split(';') -inotcontains 'C:\minikube'){
     [Environment]::SetEnvironmentVariable('Path', $('{0};C:\minikube' -f $oldPath), [EnvironmentVariableTarget]::Machine)
   }
   ```

---

## Step 3: Start Minikube

1. Ensure Docker Engine is running.
2. Start Minikube:
   ```bash
   minikube start
   ```
3. Verify Minikube status:
   ```bash
   minikube status
   ```

---

## Step 4: Deploying a Django Pod

1. Create a `pod.yaml` file with the following configuration:
   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: django-pod
     labels:
       app: django-app 
   spec:
     containers:
       - name: django
         image: talhashahzad0/instaclone:v1.0
         imagePullPolicy: IfNotPresent  # Use local image if available
         ports:
           - containerPort: 8000
         env:
           - name: DJANGO_SECRET_KEY
             value: "django-insecure--319s9_g4+q4_lzgcvhcsr2x20_tw+%06-ro64ulpabk=6s^9)"
           - name: DJANGO_DEBUG
             value: "True"
         volumeMounts:
           - name: static-volume
             mountPath: /app/staticfiles
           - name: media-volume
             mountPath: /app/media
     volumes:
       - name: static-volume
         emptyDir: {}
       - name: media-volume
         emptyDir: {}
   ```

2. Apply the pod configuration:
   ```bash
   kubectl apply -f pod.yaml
   ```

3. Verify that the pod is running:
   ```bash
   kubectl get pods
   ```

4. Check logs for troubleshooting or confirmation:
   ```bash
   kubectl logs django-pod
   ```

---

## Step 5: Add a Kubernetes Service

To expose the Django application, define a `service.yaml` file:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: django-service
spec:
  selector:
    app: django-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
  type: NodePort
```

1. Apply the service configuration:
   ```bash
   kubectl apply -f service.yaml
   ```

2. Get the service details:
   ```bash
   kubectl get svc
   ```

3. Access the application:
   - Use the `NodePort` value displayed in the output of `kubectl get svc`.
   - Run the following command to forward a local port to the service:
     ```bash
     kubectl port-forward service/django-service 8080:80
     ```
   - Access the application at `http://localhost:8080`.

---

## Step 6: Verify Kubernetes Setup

1. Check Kubernetes pods:
   ```bash
   kubectl get po -A
   ```

2. Verify the deployed application:
   ```bash
   kubectl get pods
   kubectl logs django-pod
   ```

---

## Conclusion

You have successfully set up Docker, Minikube, and Kubernetes, and deployed a Django application using a pod and a service. You can now scale and manage your application efficiently in the Kubernetes environment.
