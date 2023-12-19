# import tensorflow as tf
# from tensorflow import keras
# from keras.preprocessing import image
# import numpy as np
# import matplotlib.pyplot as plt

# class_names = ['Banana', 'Unknown','Lemon']
# # load the CNN model
# model = tf.keras.models.load_model('my_model.h5')

# # feed the image into the CNN
# img = image.load_img("test-lemon.jpg", target_size=(180, 180))
# img_array = image.img_to_array(img)
# img_array = np.expand_dims(img_array, axis=0)
# # img_array /= 255.0  # Normalize pixel values to [0, 1]

# predictions = model.predict(img_array)
# score = tf.nn.softmax(predictions[0])

# print(
#     "This image most likely belongs to {} with a {:.2f} percent confidence."
#     .format(class_names[np.argmax(score)], 100 * np.max(score))
# )

# plt.imshow(img_array[0])
# plt.show()