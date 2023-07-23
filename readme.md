# PDF RESIZE APP

## About

The app is a full stack web application hosted on aws ec2 instance as a docker container.

The app is meant to resize a pdf and split into multiple pages when the height of a pdf page is greater than 3480pixels.

Whenever there is a change in the souce code of the app, the CI/CD pipeline will take care of the deployments automatically. Additionaly, there is a custom domain name (radixploreassignment.online) mapped to the public ip of the ec2 instance. 
To make the app more user-friendly, the nginx server takes care of reverse proxy'ing the port 8000 to the custom domain name. ( We can just type in the URL instead of URL:8000 in the browser )

## Setup

To run the app, you can visit http://radixploreassignment.online or run locally using a docker container.