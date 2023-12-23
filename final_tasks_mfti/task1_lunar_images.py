from PIL import Image # считаем картинку в numpy array
import numpy as np #подключаем библиотеку numpy

def update_img(f_name): #создаем функцию для обработки изображения
    img = Image.open(f_name) #открываем износальный файл
    data = np.array(img) #создание массивов
    updated_data = [(i - np.min(data)) * (255 // ((np.max(data)) - (np.min(data)))) for i in data] #переинтерполирование и улучшение контраста
    updated_data = np.array(updated_data ) #запсиь обнавленного массива
    res_img = Image.fromarray(updated_data) #преобразование массива
    res_img.save(f'lunar_images/new_lunar{f_name[-10:-8]}_raw.jpg')#сохраняем файл
    res_img.show()#выводим(открываем) на экран

update_img('lunar_images/lunar01_raw.jpg') #вызываем функцию с первым изображением
update_img('lunar_images/lunar02_raw.jpg') #вызываем функцию со вторым изображением
update_img('lunar_images/lunar03_raw.jpg') #вызываем функцию с третим изображением


