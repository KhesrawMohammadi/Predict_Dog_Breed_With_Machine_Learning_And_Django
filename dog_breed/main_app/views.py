from django.shortcuts import render
import os
import numpy as np
import cv2
from keras.models import load_model
from django.core.files.storage import default_storage
from django.conf import settings


model_path = os.path.join(settings.BASE_DIR, 'main_app/dog_breed.h5')
model = load_model(model_path)

CLASS_NAMES = ["Afghan Hound",'Scottish Deerhound','Maltese Dog','Bernese Mountain Dog']


def predict_breed(request):
    if request.method == 'POST':
        if 'dog_image' in request.FILES:
            file = request.FILES.get('dog_image',None)

            file_name = default_storage.save(file.name, file)
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)

            img = cv2.imread(file_path)
            img = cv2.resize(img,(224,224))
            img = np.expand_dims(img, axis=0)

            prediction = model.predict(img)
            breed = CLASS_NAMES[np.argmax(prediction)]

            return render(request, 'result.html',{'breed': breed, 'image_url': file_name})
        
    return render(request,'upload.html')
    





