# NVIDIA-NIM-GenAI

## Create NVIDIA_API_KEY on Nvidia site

1) Create a free account with NVIDIA, which hosts NVIDIA AI Foundation models.  
https://build.nvidia.com/explore/discover  

2) Select the Retrieval tab, then select your model of choice.  

3) Under Input select the Python tab, and click Get API Key. Then click Generate Key.  

4) Copy and save the generated key as NVIDIA_API_KEY. From there, you should have access to the endpoints.

## Create Tavily Key
Create Tavily Key on this site -> https://tavily.com/

## Run below command to set NVIDIA_API_KEY into Environment Variables

### On Linux
export NVIDIA_API_KEY="Your NVIDIA_API_KEY"

### On Windows

setx NVIDIA_API_KEY "Your NVIDIA_API_KEY"

## Run App
Python/Python3 app.py
