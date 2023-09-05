from glob import glob
import os
print(os.getcwd())

img_list = glob('./data/images/*.jpg')

print(len(img_list))


from sklearn.model_selection import train_test_split

train_img_list, val_img_list = train_test_split(img_list, test_size = 0.2, random_state = 2000)

print(len(train_img_list), len(val_img_list))

with open('data\\train.txt', 'w') as f:
    f.write('\n'.join(train_img_list) + '\n')

with open('data\\val.txt', 'w') as f:
    f.write('\n'.join(val_img_list) + '\n')