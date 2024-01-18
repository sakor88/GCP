resource "google_storage_bucket" "tfer--image-storage" {
  force_destroy = "true"
  location      = "europe-west2"
  name          = "image-storage-gcp-final-project-410222"
  project       = "gcp-final-project-410222"
  uniform_bucket_level_access = true
}