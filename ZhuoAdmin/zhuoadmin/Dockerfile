FROM nginx:latest

ENV TimeZone=Asia/Shanghai

COPY ./dist/  /usr/share/nginx/html/
# 用本地的nginx配置文件覆盖镜像的Nginx配置
COPY default.conf /etc/nginx/conf.d/


