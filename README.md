# Breast-Cancer-Detection

# Creating an AI app for Breast Cancer Detection
![alt text](http://www.innovationandtech.ae/wp-content/uploads/2018/01/Cancer-Prognosis-Prediction-using-AI-810x324.jpg)

Breast cancer has the second highest mortality rate in women next to lung cancer. As per clinical statistics, 1 in every 8 women is diagnosed with breast cancer in their lifetime. However, periodic clinical checkups and self-tests help in early detection and thereby significantly increase the chances of survival. Invasive detection techniques cause rupture of the tumor, accelerating the spread of cancer to adjoining areas. Hence, there arises the need for a more robust, fast, accurate, and efficient noninvasive cancer detection system (Selvathi, D & Aarthy Poornila, A. (2018). Deep Learning Techniques for Breast Cancer Detection Using Medical Image Analysis).

Early detection can give patients more treatment options. In order to detect signs of cancer, breast tissue from biopsies is stained to enhance the nuclei and cytoplasm for microscopic examination. Then, pathologists evaluate the extent of any abnormal structural variation to determine whether there are tumors.

Architectural Distortion (AD) is a very subtle contraction of the breast tissue and may represent the earliest sign of cancer. Since it is very likely to be unnoticed by radiologists, several approaches have been proposed over the years but none using deep learning techniques. 

AI will become a transformational force in healthcare and soon, computer vision models will be able to get a higher accuracy when researchers have the access to more medical imaging datasets.

We will develop a computer vision model to detect breast cancer in histopathological images. Two classes will be used in this project: **Benign and Malignant.**

# Breast Cancer Histopathological Database (BreakHis)

The Breast Cancer Histopathological Image Classification (BreakHis) is composed of 7,909 microscopic images of breast tumor tissue collected from 82 patients using different magnifying factors (40X, 100X, 200X, and 400X). To date, it contains 2,480 benign and 5,429 malignant samples (700X460 pixels, 3-channel RGB, 8-bit depth in each channel, PNG format). This database has been built in collaboration with the P&D Laboratory - Pathological Anatomy and Cytopathology, Parana, Brazil.

The dataset BreaKHis is divided into two main groups: benign tumors and malignant tumors. Histologically benign is a term referring to a lesion that does not match any criteria of malignancy - e.g., marked cellular atypia, mitosis, disruption of basement membranes, metastasize, etc. Normally, benign tumors are relatively "innocents", presents slow growing and remains localized. Malignant tumor is a synonym for cancer: lesion can invade and destroy adjacent structures (locally invasive) and spread to distant sites (metastasize) to cause death.

The dataset currently contains four histological distinct types of benign breast tumors: adenosis (A), fibroadenoma (F), phyllodes tumor (PT), and tubular adenona (TA); and four malignant tumors (breast cancer): carcinoma (DC), lobular carcinoma (LC), mucinous carcinoma (MC) and papillary carcinoma (PC).

We are going to determine if there exists cancer or not.

![alt text](https://www.researchgate.net/publication/319974998/figure/fig2/AS:541235083309056@1506051907719/a-c-Indicative-cases-of-H-E-breast-cancer-histological-images-from-our-dataset-image.png)


# Instructions

The project is broken down into multiple steps:

    Load and preprocess the image dataset
    Train the image classifier on your dataset
    Use the trained classifier to predict image content

Everything you need to recreate this project is on the jupyter notebook. Everything was coded in Google Colab, because of its GPU. The dataset was uploaded to Google Drive, so you can download it directly (the code to download it is in the notebook). For more details, the notebook includes the instructions to follow.

If you want to load the trained model, the code to download it, is in the notebook, in the "Load the checkpoint" section. The model was also uploaded to Google drive, so you can download it.

This project is updated to be compatible with PyTorch 0.4.0

Read more about this project here: https://medium.com/datadriveninvestor/detecting-breast-cancer-in-histopathological-images-using-deep-learning-a66552aef98
