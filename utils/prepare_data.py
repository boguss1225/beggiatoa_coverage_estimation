import tensorflow as tf
import config
import cv2
import numpy as np
from PIL import Image

def lab_preprocessing(image):
    image = np.array(image)
    lab_image = cv2.cvtColor(image,cv2.COLOR_RGB2Lab)
    lab_image = (lab_image * 255).astype(np.uint8)
    return Image.fromarray(lab_image)


def get_datasets():
    # Preprocess the dataset
    train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        # zoom_range=0.5,
        horizontal_flip=True,
        vertical_flip=True,
        brightness_range = (0.7,1.3),
        # rotation_range = 90
        # rescale=1.0 / 255.0
#         preprocessing_function = lab_preprocessing,
    )

    train_generator = train_datagen.flow_from_directory(config.train_dir,
                                                        target_size=(config.image_height, config.image_width),
                                                        color_mode="rgb",
                                                        batch_size=config.BATCH_SIZE,
                                                        seed=1,
                                                        shuffle=True,
                                                        class_mode="categorical")

    valid_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        horizontal_flip=True,
        vertical_flip=True,
        # rescale=1.0 /255.0
    )
    valid_generator = valid_datagen.flow_from_directory(config.valid_dir,
                                                        target_size=(config.image_height, config.image_width),
                                                        color_mode="rgb",
                                                        batch_size=config.BATCH_SIZE,
                                                        seed=7,
                                                        shuffle=True,
                                                        class_mode="categorical"
                                                        )
    
    test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        # rescale=1.0 /255.0
    )
    test_generator = test_datagen.flow_from_directory(config.test_dir,
                                                      target_size=(config.image_height, config.image_width),
                                                      color_mode="rgb",
                                                      batch_size=config.BATCH_SIZE,
                                                      seed=1,
                                                      shuffle=False,
                                                      class_mode="categorical"
                                                      )


    train_num = train_generator.samples
    valid_num = valid_generator.samples
    test_num = test_generator.samples


    return train_generator, \
           valid_generator, \
           test_generator, \
           train_num, valid_num, test_num




def get_datasets_autosplit():
    # Preprocess the dataset
    train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        # zoom_range=0.5,
        horizontal_flip=True,
        vertical_flip=True,
        brightness_range = (0.7,1.3),
        validation_split=0.2
        # rotation_range = 90
        # rescale=1.0 / 255.0
#         preprocessing_function = lab_preprocessing,
    )

    train_generator = train_datagen.flow_from_directory(config.train_dir,
                                                        target_size=(config.image_height, config.image_width),
                                                        color_mode="rgb",
                                                        batch_size=config.BATCH_SIZE,
                                                        seed=1,
                                                        shuffle=True,
                                                        class_mode="categorical",
                                                        subset='training')

    valid_generator = train_datagen.flow_from_directory(config.train_dir,
                                                        target_size=(config.image_height, config.image_width),
                                                        color_mode="rgb",
                                                        batch_size=config.BATCH_SIZE,
                                                        seed=7,
                                                        shuffle=True,
                                                        class_mode="categorical",
                                                        subset='validation'
                                                        )
    
    test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        # rescale=1.0 /255.0
    )
    test_generator = test_datagen.flow_from_directory(config.test_dir,
                                                      target_size=(config.image_height, config.image_width),
                                                      color_mode="rgb",
                                                      batch_size=config.BATCH_SIZE,
                                                      seed=1,
                                                      shuffle=False,
                                                      class_mode="categorical"
                                                      )


    train_num = train_generator.samples
    valid_num = valid_generator.samples
    test_num = test_generator.samples


    return train_generator, \
           valid_generator, \
           test_generator, \
           train_num, valid_num, test_num
