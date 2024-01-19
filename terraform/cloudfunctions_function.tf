resource "google_cloudfunctions_function" "tfer--gcp-final-project-410222-backend-0" {
  name    = "backend"
  region = "${var.region}"
  project = "${var.project_id}"
  runtime     = "python310"
  entry_point = "analyze_image"

  environment_variables = {
    BUCKET_NAME = "image-storage-gcp-final-project-410222"
  }
    
  source_archive_bucket = google_storage_bucket.bucket.name
  source_archive_object = google_storage_bucket_object.object.name

  trigger_http = true
}


resource "google_storage_bucket" "bucket" {
  name                        = "${random_id.bucket_prefix.hex}-gcp-final-project-410222" 
  location                    = "US"
  uniform_bucket_level_access = true
}

resource "google_storage_bucket_object" "object" {
  name   = "function.zip"
  bucket = google_storage_bucket.bucket.name
  source = "function.zip" 
}

resource "random_id" "bucket_prefix" {
  byte_length = 8
}

resource "google_cloudfunctions_function_iam_member" "invoker" {
  project        = google_cloudfunctions_function.tfer--gcp-final-project-410222-backend-0.project
  region         = google_cloudfunctions_function.tfer--gcp-final-project-410222-backend-0.region
  cloud_function = google_cloudfunctions_function.tfer--gcp-final-project-410222-backend-0.name

  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"
}