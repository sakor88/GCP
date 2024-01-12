resource "google_cloudfunctions_function" "tfer--gcp-final-project-410222-backend-0" {
  name    = "backend"
  project = "gcp-final-project-410222"
  runtime = "python37"

  source_repository {
    url = "https://source.cloud.google.com/gcp-final-project-410222"
  }
}
