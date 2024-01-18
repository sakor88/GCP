resource "google_cloud_run_service" "tfer--gcp-final-project-410222-europe-west2-frontend-0" {
  location = "europe-west2"
  name     = "frontend"
  project  = "gcp-final-project-410222"

  template {
    spec {
      containers {
        image = "europe-west2-docker.pkg.dev/gcp-final-project-410222/final-project/front"

        ports {
          container_port = "3000"
        }
      }
    }
  }
}


resource "google_cloud_run_service_iam_binding" "default" {
  location = google_cloud_run_service.tfer--gcp-final-project-410222-europe-west2-frontend-0.location
  service  = google_cloud_run_service.tfer--gcp-final-project-410222-europe-west2-frontend-0.name
  role     = "roles/cloudfunctions.invoker"
  members = [
    "allUsers"
  ]
}