### Summary

This repo is two subtasks involved in training a neural network for image segmentation.
Task 1 is to pair up the annotated contour with the raw image. The module ./libs/match_dic_2_contour.py is for this.

In the version, the manually annotated contour is compared with contour genereated by cv2. 

Task 2 is to create a cyclic data generator. The module ./libs/train_generator.py is  for this task


### Dependencies
python: 3.6
cv2: 3.2.0
dicom: 0.9.9
numpy: 1.11.3



### How to run?

```
 ./libs/match_dic_2_contour.py and ./libs/train_generator.py can be tested by run
cd ./libs
python match_dic_2_contour.py # Its output is saved at out_data/tmp/tmp.jpg
python train_generator.py   #
```

```
Another way to run is run the scirpt in ./src/test/run_test.sh for unit test.
```
```
The last way to test multiple tests is to run the script in ./script/test_match_dic_2_contour.sh 
```
