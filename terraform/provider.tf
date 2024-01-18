provider "google" {
  credentials = file("account.json")
  project     = "gcp-final-project-410222"
  region      = "europe-west2" 
}