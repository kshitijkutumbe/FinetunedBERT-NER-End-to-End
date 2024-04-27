from ner.configuration.gcloud import GCloud
import os

obj = GCloud()

obj.sync_folder_from_gcloud(gcp_bucket_url='ner-bert-kk24',filename='archive.zip',destination="gcloud_bucket_test")