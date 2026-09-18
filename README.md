## DevOps test tasks

### Terraform GCP

`terraform-test/`
Contains the Terraform configuration for GCP, provisioning the following resources (all within the Always Free Tier):
- 1 Google Cloud Storage bucket
- 1 BigQuery dataset
- 1 Compute Engine VM

`logs/`
Contains the full execution log trail, in order:
1. init.log
2. plan.log
3. apply_1.log - first terraform apply. The bucket and the BigQuery dataset were created successfully, but VM creation failed because the Compute Engine API was not yet enabled on the project.
4. apply_2.log - second terraform apply, run after enabling the Compute Engine API. Terraform detected the existing bucket and dataset in the state file and only created the missing VM.
5. migrate_to_gcs.log - terraform init -migrate-state after uncommenting the GCS backend, migrating the local state file to the newly created bucket.
6. migrate_to_local.log - terraform init -migrate-state after commenting the GCS backend out again, migrating the state back to the local machine before destroying the bucket that held it.
7. destroy.log
