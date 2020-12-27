## book online resources
org github:
https://github.com/fastai

it has 80+ repos!
* [ ] todo: review all repos to search for goodies


book git repo (this appears to be the most up2date repo)
https://github.com/fastai/fastbook

https://book.fast.ai

which points to

https://course.fast.ai/

On that page in section **the software you will be using** click on *fastai* link to arrive to 
https://docs.fast.ai/

This has the **Installing**  section

## software on fresh linux host
Assuming gpu is installed and configured, ssh key is generated

fastai has its own fastai channel on anaconda


### install pip for python3
```
sudo apt update
sudo apt install python3-pip python3-dev
sudo pip3 install --upgrade pip
sudo pip3 install virtualenv
```
### create a virtual env fai
```
mkdir ~/venv
cd ~/venv
/usr/bin/python3 -m virtualenv fai38
source ~/venv/fai38/bin/activate
pip install --upgrade pip
```

## install packages in virtual env
### jupyter notebook , jupyter lab
make sure the fai38 venv is activated
```
pip install jupyterlab
pip install notebook
pip install graphviz
sudo apt-get install graphviz #debian package needed for gv executable in path
```



Jupyter can be launched as

```
jupyter-lab
jupyter notebook
```

### pytorch
```
pip install numpy
```
on pytorch.org  select   a pytorch version with  cuda=none owr cuda


with cuda = none
```
pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
```

with cuda enabled
```
pip install torch torchvision
```

verify installation
```
ipython

: import torch
: x=torch.rand(5,3)
: print(x)
: torch.cuda.is_available()
: exit## register on forums.fast.ai

```


### fastai
for installing in editable mode refer to  section *fastai repo*


## fastai repo
1. in ~/repos fork the repo https://github.com/fastai/fastai
```
git clone git@github.com:slzdevsnp/fastai.git
```

set the upstream
```
cd fastai
git remote add upstream  git@github.com:fastai/fastai.git

git remote -v #to verify
```


2. clone the fastcore repo as well
  * fastcore repo are extensions to python language by fast. It is used by the fastai lib.
```
cd ~/repos/fai
git clone git@github.com:fastai/fastcore.git
```
3. fork the repo fastbook to do notebook from the book
Optionally switch to a branch `develop`   to make your commits in it, to perform `git fetch upstream` in a `master` branch  to keep them separate.

4. in the fai38 venv install fastai packages in editable mode
```
cd ~/repo
(fai38) pip install -e fai/fastcore
(fai38) pip install -e fastai
```
observe that the fastai.egg link in virtual environement's site-packages points to my fastai repo
```
(fai38) zimine@zub:~/repos$ cat  ~/venv/fai38/lib/python3.8/site-packages/fastai.egg-link 

/home/zimine/repos/fastai
```

## open code in pycharm
* create  a project from source on fastbook  repo
* let it index all symbols
* open a notebook, NB! pycharm will attemp to start a jupyter server of its own on 8888 (default port),  8889  if 8888 is busy




to run jupyterLab
```
jupyter-lab
#or
jupyter notebook
```

## register on forums.fast.ai
