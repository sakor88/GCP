resource "google_storage_bucket" "tfer--image-storage" {
  force_destroy = "false"
  location      = "europe-west2"
  name          = "image-storage"
  project       = "gcp-final-project-410222"
}
