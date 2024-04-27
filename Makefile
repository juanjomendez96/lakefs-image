up:
	docker compose up -d

stop:
	docker stop lakefs minio

rm:
	docker rm lakefs minio