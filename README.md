# Intern-work
compare the performance of the model in deep learning and svm to find the best way to use with sdn classify DDoS attack

## Our system
 - cuda 9.1
 - CudNN 7.0
 - openmpi 3
 - python 2
 - ubuntu 18.04 x86_64
 - GTX 1080
 
 **_Data format_** 
 DARPA 2009 DDoS attack dataset [1 GB (zip) :3 GB (unzip)] 
 ref : https://drive.google.com/open?id=10j4394CgkgKK920ey7ay41xTuNuA2Xka
  - use for Attack packets dataset
 DARPA 2009 Scalable Network Monitoring [1.64 TB : 6.54 TB ?]
 ref : in email 
  - use for Normal packets dataset
 - pcap file that is ascii file that contain the header and raw in packets
 - convert file pass this programs (order)
 Choice 1 (using scapy + scapy-http libary)
 prepare by 
 ```
 "pip install scapy"
 "pip install scapy-httpscapy-http"
 ```
 1. Fullyfile.ipynb (MAC) : pcap --> txt | use command "p.show()" get a lot of detail in package, example
 
 2. summay.py (MAC) : pcap --> txt | use command "p.summary()" get a little detail in package, example
 
 3. Preprocess-intoDataFame.ipynb (Ubuntu) : txt --> csv | convert in logic part in this program to use with training model
 
 **_Example some difference in dataset (not Ether)_**
 > 1.
 ```
 ###[ 802.3 ]### 
  dst       = 01:80:c2:00:00:00
  src       = 00:1f:ca:9e:7e:df
  len       = 38
 ###[ LLC ]### 
      dsap      = 0x42
      ssap      = 0x42
      ctrl      = 3
 ###[ Spanning Tree Protocol ]### 
         proto     = 0
         version   = 0
         bpdutype  = 0
         bpduflags = 0
         rootid    = 32768
         rootmac   = 00:21:56:ef:bc:01
         pathcost  = 0
         bridgeid  = 32768
         bridgemac = 00:21:56:ef:bc:01
         portid    = 32800
         age       = 0.0
         maxage    = 20.0
         hellotime = 2.0
         fwddelay  = 15.0
 ###[ Padding ]### 
            load      = '\x00\x00\x00\x00\x00\x00\x00\x00'
 ```
 
 > 2.
 ```
 ###[ Ethernet ]### 
  dst       = 00:1e:4f:3e:45:1f
  src       = 00:1b:21:3a:79:d5
  type      = 0x806
 ###[ ARP ]### 
      hwtype    = 0x1
      ptype     = 0x800
      hwlen     = 6
      plen      = 4
      op        = is-at
      hwsrc     = 00:1b:21:3a:79:d5
      psrc      = 192.168.61.196
      hwdst     = 00:1e:4f:3e:45:1f
      pdst      = 192.168.61.208
 ###[ Padding ]### 
         load      = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
 ```
         
 > 3.
 ```
 ###[ Ethernet ]### 
  dst       = ab:00:00:02:00:00
  src       = 00:21:56:ef:bc:00
  type      = 0x6002
 ###[ Raw ]### 
       load      = '=\x00\x07\x00\x00\x00\x01\x00\x03\x03\x00\x00\x02\x00\x02!\x00\x03\x00\x06\x00\x00\x00\x00\x00\x00\x04\x00\x02<\x00\x05\x00\x02\xd8\x05\x06\x00\x02\x00\x01\x07\x00\x06\x00!V\xef\xbc\x00d\x00\x01y\x90\x01\x01\x01\x91\x01\x02\xee\x05'
```

  > 4.
  ```
  ###[ Ethernet ]### 
   dst       = 33:33:00:01:00:03
   src       = 00:1e:4f:3e:43:19
   type      = 0x86dd
  ###[ IPv6 ]### 
       version   = 6
       tc        = 0
       fl        = 0
       plen      = 37
       nh        = UDP
       hlim      = 1
       src       = fe80::b6:a9b:e37d:95f3
       dst       = ff02::1:3
  ###[ UDP ]### 
          sport     = 55902
          dport     = hostmon
          len       = 37
          chksum    = 0x9fa2
  ###[ Link Local Multicast Node Resolution - Query ]### 
             id        = 54023
             qr        = 0
             opcode    = QUERY
             c         = 0
             tc        = 0
             z         = 0
             rcode     = ok
             qdcount   = 1
             ancount   = 0
             nscount   = 0
             arcount   = 0
             \qd        \
              |###[ DNS Question Record ]### 
              |  qname     = 'Unspecified.'
              |  qtype     = A
              |  qclass    = IN
             an        = None
             ns        = None
             ar        = None
```

**_Dataset (collect  in the same day 20091105 )_**
- for training
  - Attack packets:
   - 4856 = 1217369 packets
   - 5102 = 1470285 packets

  - Nomal packets:
   - 0448 = 1219540 packets
   - 1052 = 1216464 packets
 [may be select packets by random]

- for test
  - Attack packets:
   - 5253 = 1267616 packets
  - Nomal packets:
   - 2823 = 1217463 packets
  
###### MAC - Groups

- 0X:80:C2:00:00:00 to 0X:80:C2:FF:FF:FF
    - X = 0  individual addresses
    - X = 1  group addresses
    - Ref https://en.wikipedia.org/wiki/Multicast_address
    - Ref https://stats.stackexchange.com/questions/82923/mixing-continuous-and-binary-data-with-linear-svm
    
###### Assign port
- Ref https://en.wikipedia.org/wiki/Registered_port
 
 Meaning in each field
 Ref : https://thepacketgeek.com/scapy-p-05-sending-our-first-packet-arp-response/  
 
###### LLC ssap/dsap
- Ref https://en.wikipedia.org/wiki/IEEE_802.2

###### Ether type
- Ref https://en.wikipedia.org/wiki/EtherType

###### Feature : 
  ref - https://github.com/invernizzi/scapy-http with scapy-http
 - Physical [Ethernet, 802.3, others (0x6002 protocol)]
 - IP, ARP [Vesion, Len, protocol, src, dest]
 - TCP, UDP, ICMP [sport, dport]
 ... HTTP, Raw 
 using Ether [one-hot] , 802.3 [one-hot], Version [one-hot : IPv4, IPv6 ...], Len, protocol [one-hot : TCP, UDP, ...], src [one-hot : with class] , dest [one-hot with class], sport [real-value] , dport [real-value]
 feild "other" is out because it is too low packets.

[now working]
- Add field "MAC address : src & dest" - from PcapReader 
- Add field "port by not using dict" - use PcapReader lib from scapy to read P[IP].sport, P[IP].dport 
[problem]
- field is not completely, sometime occur that IndexError, but  it write a little part  in  file ?
May be some part not have Ether field


**_Requirement [Ubuntu 18.04]_**

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

**_[Error check]_**
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
  
  **_try:_**
   - [ ] install by using docker hub 
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
    - [ ] install from dockerfile
    below this web : https://github.com/gw0/docker-keras/blob/master/Dockerfile.py3-tf-gpu  
    but It get (core dump)
    - [x] install with https://github.com/gw0/docker-keras-full
    and using command "sudo nvidia-docker run -d -p 8888:8888 -v $(pwd):/srv gw000/keras-full"
    access web in "http://<ip>:8888" with password "keras" <ip> can use localhost
 
Ref: guide write git https://help.github.com/articles/basic-writing-and-formatting-syntax/
