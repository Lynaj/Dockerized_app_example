# Stage 0 - installing stress test software
RUN apt-get update && apt-get install siege 
# Stage 1 - nginx & frontend dist
FROM nginx:alpine

COPY nginx/prod.conf /etc/nginx/nginx.conf
COPY --from=build-deps /app/dist/ /dist/

CMD ["nginx", "-g", "daemon off;"]
