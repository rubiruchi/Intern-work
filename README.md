# Intern-work
compare the performance of the model in deep learning and svm to find the best way to use with sdn classify DDoS attack

Our system
 - cuda 9.1
 - CudNN 7.0
 - openmpi 3
 - python 2
 - ubuntu 18.04 x86_64
 - GTX 1080

Requirement [Ubuntu 18.04]

- Check that package install
"dpkg -l | grep -i nvidia"
"dkms status" if you see nvidia, that means you already installed drivers 

  ref cuda + driver
  - cuda 9.2 : https://developer.nvidia.com/cuda-downloads
  - cuda 9.1 : https://developer.nvidia.com/cuda-91-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1704&target_type=deblocal
  - cuda 9.0 : https://developer.nvidia.com/cuda-90-download-archive

- nvidia driver for GPU
Check driver kernel that support for your GPU version here
http://www.nvidia.com/download/driverResults.aspx/134859/en-us
Download them 
use "sudo sh ___.run" --> GUI mode

[Error check]
  - gcc version 
  gcc vesion 4.8.5 can't use with the nvidia driver installation 
  remove them by "sudo apt remove gcc"
  and try "sudo apt-get install gcc"
  that will get both g++, gcc vesion upper 7
  - remove older driver in dkms : that means the module that was added
  check by  "dkms status"
  using "dkms remove nvidia/331.49 --all"
  - remove old cuda 
  "sudo apt-get --purge remove nvidia-*"
  "./uninstall_nvi*" in /usr/local/cuda/bin if had
  - when install with .deb file in local or network
  if error occurs that they can't found the url for install
  you have to change the url path in there "sudo nano /etc/apt/sources.list"
  and change url "tw.ubuntu..." --> "ubuntu..."
  - add repo
  ref: https://askubuntu.com/questions/307/how-can-ppas-be-removed?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
  - disable iPv6
  ref: https://www.techrepublic.com/article/how-to-disable-ipv6-on-linux/

  - install Tensorflow & Keras
  ref: https://medium.com/@asmello/how-to-install-tensorflow-cuda-9-1-into-ubuntu-18-04-b645e769f01d
  [Error] with version of gcc is not match (below than 6 , but we use 7)
  
  try:
   - install by using docker hub 
   req. nvidia-docker --> run with gpu 
   [Error] when download docker images from https://hub.docker.com/r/ermaker/keras-jupyter/ 
   and  try to 
   run the code in jupyter
   "from keras.models import Sequential"
   error occus, like np_utils can't import
   I tried use, by  ref : https://stackoverflow.com/questions/43027379/keras-importerror-cannot-import-name-ctc-ops/43145681?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    "pip install keras tensoflow --upgrade"
    and restart  kernel
    but It get (core dump)
    - install from dockerfile
    below this web : https://github.com/gw0/docker-keras/blob/master/Dockerfile.py3-tf-gpu
    [...]
