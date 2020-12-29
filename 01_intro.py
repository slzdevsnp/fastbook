from fastbook import *
from fastai.vision.all import *


def is_cat(x): return x[0].isupper()


def model_cats_dogs():
    path = untar_data(URLs.PETS) / 'images'
    dls = ImageDataLoaders.from_name_func(path, get_image_files(path),
                                          valid_pct=0.2, seed=42,
                                          label_func=is_cat,
                                          item_tfms=Resize(224))
    learn = cnn_learner(dls, resnet34, metrics=error_rate)
    return learn


def model_cats_dogs_train(model, nepochs):
    model.fine_tune(1)

def predict_image(model, img):
    is_cat, _, probs = model.predict(img)
    print(f"Is this a cat?: {is_cat}.")
    print(f"Probability it's a cat: {probs[1].item():.6f}")

def test_on_catsdogs_data(model):
    print("Testing on cats and dogs data from the internet..")

    uploader = SimpleNamespace(data=['/home/zimine/images/fai/ch1/cats/cat1.jpg',
              '/home/zimine/images/fai/ch1/dogs/puppy1.jpg'])

    img = PILImage.create(uploader.data[0])
    predict_image(model,img)

    img = PILImage.create(uploader.data[1])
    predict_image(model,img)


if __name__ == '__main__':
    learn = model_cats_dogs()
    model_cats_dogs_train(learn, 1)
    test_on_catsdogs_data(learn)
