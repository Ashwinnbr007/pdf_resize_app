# PDF RESIZE APP

## About

The app is a full stack web application hosted on aws ec2 instance.

The app is meant to resize a pdf and split into multiple pages when the height of a pdf page is greater than 3480pixels.

Whenever there is a change in the souce code of the app, the CI/CD pipeline will take care of the deployments automatically. Additionaly, there is a custom domain name (radixploreassignment.online) mapped to the public ip of the ec2 instance. 
To make the app more user-friendly, the nginx server takes care of reverse proxy'ing the port 8000 to the custom domain name. ( We can just type in the URL instead of URL:8000 in the browser )

## Setup

To run the app, you can visit https://radixploreassignment.online or run locally using a docker container. ( SSL secured )

### To run locally using docker container

1. Clone the repo
2. cd into the repo `cd pdf_resize_app`
3. Build using `docker build -t pdf_resize_app .` (Ensure you have docker installed before this step)
4. Run the container `docker run pdf_resize_app`

## To create an image with NXM dimensions

I had run into an issue where i could not find any custom nxm for testing the logic, hence image_gen.py was created. 
Simply add in your width and height and run `python3 image_gen.py` and a blank NxM image will be generated.
