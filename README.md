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
   
- Problem 
 - Attack dataset is mixing between attack packets and not attack packets.
 - Have to remodel and new preprocess
 - Define is DDoS Attack or not
 - [TRY] preprocess3 using window
Try to find the relation of each attributes with R language (Multiple regression)
```
 Call:
lm(formula = Status ~ Ether_or_Dot3 + MAC_src + MAC_dst + Ether_type + 
    LLC + LLC_ssap + LLC_dsap + IP_ttl + IP_version + TCP + UDP + 
    ARP + ICMP + pLen + Num_ip_pair + Ratio_ip + Num_ip_src + 
    Num_ip_dst + Ratio_port + Num_port_dst + Weight_ip + Weight_port + 
    Num_port_src + Weight_ip + Weight_port + Num_all_packets)

Residuals:
     Min       1Q   Median       3Q      Max 
-1.01651 -0.00034 -0.00013  0.00001  0.99941 

Coefficients: (16 not defined because of singularities)
                           Estimate Std. Error  t value Pr(>|t|)    
(Intercept)              -5.509e-04  4.744e-03   -0.116 0.907549    
Ether_or_Dot3            -3.153e-01  5.108e-03  -61.725  < 2e-16 ***
MAC_src00:13:80:5c:32:c0 -1.195e-03  1.893e-03   -0.631 0.527962    
MAC_src00:17:3f:9c:23:76 -7.205e-02  2.097e-03  -34.366  < 2e-16 ***
MAC_src00:1a:70:14:d6:4a -4.591e-02  1.743e-03  -26.344  < 2e-16 ***
MAC_src00:1b:21:23:b9:90  4.041e-03  4.792e-04    8.434  < 2e-16 ***
MAC_src00:1b:21:3a:79:d5 -1.111e-03  3.090e-04   -3.596 0.000323 ***
MAC_src00:1b:78:1f:49:78 -4.094e-02  5.412e-03   -7.565 3.89e-14 ***
MAC_src00:1e:4f:3e:1a:ae -2.505e-01  1.910e-03 -131.132  < 2e-16 ***
MAC_src00:1e:4f:3e:43:19 -3.185e-01  2.219e-03 -143.549  < 2e-16 ***
MAC_src00:1e:4f:3e:45:1f -3.185e-01  6.033e-04 -528.046  < 2e-16 ***
MAC_src00:1f:ca:9e:7e:d8 -7.315e-05  4.819e-03   -0.015 0.987890    
MAC_src00:1f:ca:9e:7e:d9 -7.315e-05  4.819e-03   -0.015 0.987890    
MAC_src00:1f:ca:9e:7e:df -7.315e-05  4.819e-03   -0.015 0.987890    
MAC_src00:1f:ca:9e:7e:e0 -7.315e-05  4.819e-03   -0.015 0.987890    
MAC_src00:1f:ca:9e:7e:e1 -7.315e-05  4.819e-03   -0.015 0.987890    
MAC_src00:1f:ca:9e:7e:e3 -7.315e-05  4.819e-03   -0.015 0.987890    
MAC_src00:1f:ca:9e:7e:e4 -7.315e-05  4.819e-03   -0.015 0.987890    
MAC_src00:1f:ca:9e:7e:e6 -7.315e-05  4.819e-03   -0.015 0.987890    
MAC_src00:1f:ca:9e:7e:e8 -7.315e-05  4.819e-03   -0.015 0.987890    
MAC_src00:1f:ca:9e:7e:ef -7.315e-05  4.819e-03   -0.015 0.987890    
MAC_src00:21:56:ef:bc:00 -1.175e-02  1.893e-03   -6.207 5.40e-10 ***
MAC_src00:21:9b:fc:19:68         NA         NA       NA       NA    
MAC_dst00:17:3f:9c:23:76 -9.814e-02  2.790e-03  -35.177  < 2e-16 ***
MAC_dst00:1a:70:14:d6:4a -9.215e-02  2.573e-03  -35.813  < 2e-16 ***
MAC_dst00:1b:21:23:b9:90 -1.767e-02  1.891e-03   -9.347  < 2e-16 ***
MAC_dst00:1b:21:3a:79:d5 -2.214e-02  1.907e-03  -11.610  < 2e-16 ***
MAC_dst00:1e:4f:3e:1a:ae  2.488e-02  1.839e-03   13.526  < 2e-16 ***
MAC_dst00:1e:4f:3e:43:19 -1.472e-03  4.029e-03   -0.365 0.714932    
MAC_dst00:1e:4f:3e:45:1f -2.256e-02  1.909e-03  -11.822  < 2e-16 ***
MAC_dst00:21:56:ef:bc:00         NA         NA       NA       NA    
MAC_dst00:21:9b:fc:19:68 -2.649e-02  1.904e-03  -13.912  < 2e-16 ***
MAC_dst01:00:0c:cc:cc:cc         NA         NA       NA       NA    
MAC_dst01:00:5e:00:00:fb -9.776e-01  2.924e-03 -334.314  < 2e-16 ***
MAC_dst01:00:5e:00:00:fc  6.286e-01  2.843e-03  221.082  < 2e-16 ***
MAC_dst01:80:c2:00:00:00         NA         NA       NA       NA    
MAC_dst33:33:00:01:00:03  6.338e-01  2.843e-03  222.918  < 2e-16 ***
MAC_dstff:ff:ff:ff:ff:ff         NA         NA       NA       NA    
Ether_type2054            4.664e-01  9.549e-04  488.400  < 2e-16 ***
Ether_type34525                  NA         NA       NA       NA    
Ether_typeN                      NA         NA       NA       NA    
LLC                              NA         NA       NA       NA    
LLC_ssap66                       NA         NA       NA       NA    
LLC_ssapN                        NA         NA       NA       NA    
LLC_dsap66                       NA         NA       NA       NA    
LLC_dsapN                        NA         NA       NA       NA    
IP_ttl                    5.231e-03  9.457e-07 5531.226  < 2e-16 ***
IP_version6                      NA         NA       NA       NA    
IP_versionN                      NA         NA       NA       NA    
TCP                      -1.385e-03  7.589e-05  -18.251  < 2e-16 ***
UDP                              NA         NA       NA       NA    
ARP                              NA         NA       NA       NA    
ICMP                      9.984e-01  5.824e-04 1714.249  < 2e-16 ***
pLen                     -8.928e-08  1.794e-08   -4.977 6.46e-07 ***
Num_ip_pair              -2.092e-06  2.828e-07   -7.399 1.38e-13 ***
Ratio_ip                 -1.311e-02  1.945e-03   -6.744 1.54e-11 ***
Num_ip_src               -1.349e-06  2.409e-07   -5.599 2.15e-08 ***
Num_ip_dst                3.384e-06  1.376e-07   24.586  < 2e-16 ***
Ratio_port                6.702e-03  1.898e-03    3.530 0.000416 ***
Num_port_dst             -2.107e-07  9.975e-09  -21.127  < 2e-16 ***
Weight_ip                 2.633e-05  3.086e-06    8.530  < 2e-16 ***
Weight_port               3.780e-05  5.383e-06    7.023 2.18e-12 ***
Num_port_src             -1.907e-07  7.215e-09  -26.434  < 2e-16 ***
Num_all_packets           6.578e-08  3.584e-09   18.354  < 2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.006708 on 1217321 degrees of freedom
Multiple R-squared:  0.9978,	Adjusted R-squared:  0.9978 
F-statistic: 1.187e+07 on 47 and 1217321 DF,  p-value: < 2.2e-16
```
but in this dataset is define the status value by known destination attack (problem)

   
###### Training Data
- Prepare dataset (csv)
ref: https://medium.com/click-bait/splitting-csv-into-train-and-test-data-1407a063dd74
- Random value
ref: https://stackoverflow.com/questions/43062613/how-to-randomly-select-rows-from-a-data-set-using-pandas
# Dataset1
- Training data && Test data with grouping IP, MAC, Port

## SVM in Jupyter-lab 
- SVM.ipynb in path /home/panin/Desktop/workspace/Intern-work/Data-csv/SVM.ipynb
- in localhost:12345

# Try case 1
- Dataset1
  - eval = 0.4998~0.5008

## Deep learning in Jupyter-lab  
- Deep learning.ipynb in path /srv/workspace/Intern-work/Data-csv/Deep learning.ipynb
- in localhost:8888

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
