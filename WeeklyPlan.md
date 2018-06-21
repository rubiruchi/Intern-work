Weekly Explanation

# 11-17 June
### Meeting 21 June 2018
  About try to  training model
  - preprocess the data  into 2 set
    - 1.  P1 Grouping dataset
    - 2.  P2 not Grouping using all be one-hot attrubutes
  - Training model with Preprocess set1
    - SVM : 100000 packets | 0.47025 | using train1.csv | 4-5 hours
    - Deep learning : 100000 packets | 0.49052 | using train1.csv | 1 minute
  
##### Note (conclusion)
  Try use sklearn with :
  - GPU or use other library because take a long times
  Status is much overfit :
  - using weight from in each attributes to get then  in continuous value.
   —> may be in %, may be depend on window size
  - use another attribute that will attack or  not  in weight
 
  Next plan
  - do dataset2 
  - find lib or tools to work with GPU
  
  

 
