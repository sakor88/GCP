resource "google_cloud_run_service" "tfer--gcp-final-project-410222-europe-west2-frontend-0" {
  location = "europe-west2"
  name     = "frontend"
  project  = "gcp-final-project-410222"

  template {
    spec {
      containers {
        image = "gcr.io/cloudrun/final-frontend"

        ports {
          container_port = "3000"
        }
      }
    }
  }
}
