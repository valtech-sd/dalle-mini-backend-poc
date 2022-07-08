## High-Level Technical Overview 

The application utilizes an open source implementation of Dall-E mini, which uses an existing model to generate images. The github page provides a link to a Google Colab notebook, where developers can play around with image generations and run the code in a managed hosting environment. 

We needed to move the python script from Google Colab to AWS where we could have more control, and customization options, along with cheaper hosting costs. 

We ended up putting spinning up an EC2 instance and wrapping the python scripts into a Flask App. The Flask app exposes a generate-image API route which is requested hourly via a cron task on the server. 


On the front end, we fetch the latest image from the Cloudinary folder where the images are stored. Thus, the most recent image is shown whenever the user refreshes the browser. We also built an autorefresh meta tag into the html which refreshes the browser every ten minutes if the browser is left open. 

## Technical Architecture Overview 

**Flask App** - Backend API wrapper around open source Jupyter Notebook scripts. - Hosted on AWS EC2 instance, processes managed with tmux.
**AWS** – The instance is named, Dalle-Mini and hosted on a t2.large on the Valtech-SD AWS acct. 

**Next.JS App (separate repo)** - Front end - API routes - Assets hosted on Cloudinary  (https://github.com/valtech-sd/dalle-mini-viewer)
