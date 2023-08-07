# LLMs for Isotope Production
Author: Logan Endes (github.com/Log45)

## Getting Started
To reproduce my work this summer, enter these commands in a terminal of a linux machine (I used Ubuntu):

### Install Wget 

If you don't have wget on your machine, run these commands:
```sudo apt-get update```
```cd /tmp```
```apt-get install wget```
```sudo apt-get update```

### Setup Conda

To install anaconda, use these commands:
```wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh sha256sum Anaconda3-2023.03-1-Linux-x86_64.sh```
Navigate through the Anaconda setup, choose an install directory, and then test the connection with the following commands
```source ~/.bashrc```
```conda info```
Once conda is working, create a new conda environment using:
```conda create -n env_name```

### Configure Environment

Once your environment is created, activate it with:
```conda activate env_name```
For this project, I used Python 3.8 to be compatible with `galai`.
```conda install python=3.8```
Before installing dependencies, find out which version of cuda your graphics card is running using:
```nvidia-smi```
Now, install the following dependencies (change pytorch-cuda=11.7 to whatever version of cuda you are running):
```conda install torchvision torchaudio pytorch-cuda=11.7 git -c pytorch -c nvidia```
```pip install -r requirements.txt```
```pip install git+https://github.com/huggingface/transformers```

### Run the demo
Currently, the only demo that can be ran is in functions.py (as of writing it checks galactica-standard using a single filter with some html files)
```python3 functions.py```
If you are afraid of accidentally killing your connection, run:
```nohup python3 functions.py```