resource "google_storage_bucket" "stas_demo_bucket" {
  name                     = "${var.project_id}-demo-data-bucket"
  location                 = var.region
  force_destroy            = true
  public_access_prevention = "enforced"
  uniform_bucket_level_access = true
}

resource "google_bigquery_dataset" "stas_demo_dataset" {
  dataset_id                 = "stas_demo_dataset"
  friendly_name              = "Test Demo Dataset"
  description                = "My test BigQuery dataset created via Terraform"
  location                   = "US"
  delete_contents_on_destroy = true
}

resource "google_compute_instance" "demo_vm" {
  name         = "demo-vm-instance"
  machine_type = "e2-micro"
  zone         = var.zone
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-12"
      size  = 10
      type  = "pd-standard"
    }
  }
  network_interface {
    network = "default"
    access_config {}
  }
}
