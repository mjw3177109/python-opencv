start:
	docker stop zhuoadmin && docker rm zhuoadmin
	docker rmi django
	docker build -t django .
	docker run -itd -p 80:80 --name zhuoadmin --restart=always django
