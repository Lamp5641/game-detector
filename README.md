"cd ~/jetson-inference/
./docker/run.sh" starts the training for the ai.
"cd python/training/classification" moves to the classification folder.
"python3 train.py --model-dir=models/gameplay_model data/gameplay_data" checks for the data set
"python3 onnx_export.py --model-dir=models/gameplay_model" converts PyTorch to ONNX
"NET=models/gameplay_model
DATASET=data/gameplay_data" saves the current model paths
"imagenet.py
--model=$NET/resnet18.onnx
--labels=$DATASET/labels.txt
--input_blob=input_0
--output_blob=output_0
$DATASET/test/[image]/[image name].png output.jpg" loads the image and the ai tries to figure out what game it is.
Data set came from https://www.kaggle.com/datasets/aditmagotra/gameplay-images 
