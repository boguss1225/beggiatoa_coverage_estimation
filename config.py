# some training parameters
EPOCHS = 200
BATCH_SIZE = 64
NUM_CLASSES = 11
image_height = 128
image_width = 128
channels = 3

model_save_name = "DenseNet121_11cls_v2"
model_dir = "trained_models/IMAS_Salmon/"+model_save_name+"/" # = save_dir

dir_base = "/home/mirap/0_DATABASE/IMAS_Salmon/7_detailed_11cls/"
train_dir = dir_base + "set1"
valid_dir = dir_base + "5_folds/1fold"
test_dir = dir_base + "test"

test_image_path = dir_base + "test/3_thick/untitled-214_2309_2087_3.jpg"
