FROM nginx:mainline-alpine
RUN rm /etc/nginx/conf.d/*
RUN mkdir /etc/ssl/certs/
RUN mkdir /etc/ssl/private/
RUN chmod -R 775 /etc/ssl/
RUN chown -R nginx:nginx /etc/ssl/
ADD https.conf /etc/nginx/conf.d/
ADD index.html /usr/share/nginx/html/
ADD snug.blog.internal.crt /etc/ssl/certs/
ADD snug.blog.internal.key /etc/ssl/private/
EXPOSE 80 443