# Breast-Cancer-Detection

# Creating an AI app for Breast Cancer Detection
![Cancer Prognosis using AI](https://cms.qz.com/wp-content/uploads/2018/08/breast-cancer-animated-final.gif?w=1400&strip=all&quality=75)

Breast cancer has the second highest mortality rate in women next to lung cancer. As per clinical statistics, 1 in every 8 women is diagnosed with breast cancer in their lifetime. However, periodic clinical checkups and self-tests help in early detection and thereby significantly increase the chances of survival. Invasive detection techniques cause rupture of the tumor, accelerating the spread of cancer to adjoining areas. Hence, there arises the need for a more robust, fast, accurate, and efficient noninvasive cancer detection system (Selvathi, D & Aarthy Poornila, A. (2018). Deep Learning Techniques for Breast Cancer Detection Using Medical Image Analysis).

Early detection can give patients more treatment options. In order to detect signs of cancer, breast tissue from biopsies is stained to enhance the nuclei and cytoplasm for microscopic examination. Then, pathologists evaluate the extent of any abnormal structural variation to determine whether there are tumors.

Architectural Distortion (AD) is a very subtle contraction of the breast tissue and may represent the earliest sign of cancer. Since it is very likely to be unnoticed by radiologists, several approaches have been proposed over the years but none using deep learning techniques. 

AI will become a transformational force in healthcare and soon, computer vision models will be able to get a higher accuracy when researchers have the access to more medical imaging datasets.

##### We will develop a computer vision model to detect breast cancer in histopathological images. Two classes will be used in this project:
<ol> 
    <li> Benign </li>
    <li> and Malignant. </li>
    </ol>

# Breast Cancer Histopathological Database (BreakHis)

From https://www.kaggle.com/ambarish/breakhis description:

The Breast Cancer Histopathological Image Classification (BreakHis) is composed of 7,909 microscopic images of breast tumor tissue collected from 82 patients using different magnifying factors (40X, 100X, 200X, and 400X). To date, it contains 2,480 benign and 5,429 malignant samples (700X460 pixels, 3-channel RGB, 8-bit depth in each channel, PNG format). This database has been built in collaboration with the P&D Laboratory - Pathological Anatomy and Cytopathology, Parana, Brazil.

The dataset BreaKHis is divided into two main groups: benign tumors and malignant tumors. Histologically benign is a term referring to a lesion that does not match any criteria of malignancy - e.g., marked cellular atypia, mitosis, disruption of basement membranes, metastasize, etc. Normally, benign tumors are relatively "innocents", presents slow growing and remains localized. Malignant tumor is a synonym for cancer: lesion can invade and destroy adjacent structures (locally invasive) and spread to distant sites (metastasize) to cause death.

The dataset currently contains four histological distinct types of benign breast tumors: adenosis (A), fibroadenoma (F), phyllodes tumor (PT), and tubular adenona (TA); and four malignant tumors (breast cancer): carcinoma (DC), lobular carcinoma (LC), mucinous carcinoma (MC) and papillary carcinoma (PC).

We are going to determine if there exists cancer or not.

<img src="images/mal_ben.png"/>


# Getting Started

The project is broken down into the following steps:
<ol>
    <li>  Load and preprocess the image dataset</li>
    <li> Train the image classifier on your dataset </li>
    <li> Use the trained classifier to predict image content </li> </ol>

### Dependencies

To set up your python environment to run the code in this repository, follow the instructions below.

1. Create (and activate) a new environment with Python 3.6.

	- __Linux__ or __Mac__: 
	```bash
	conda create --name bcdp python=3.6
	conda activate bcdp
	```
	- __Windows__: 
	```bash
	conda create --name bcdp python=3.6 
	activate bcdp
	```

2. Clone the repository (if you haven't already!), and navigate to the `breast-cancer-detection` folder.  Then, install several dependencies.
```bash
git clone https://github.com/Droid021/breast-cancer-detection.git
cd breast-cancer-detection
pip install -r requirements.txt
```

4. Create a `data` in the root of the project

- Download the dataset from [kaggle](https://www.kaggle.com/ambarish/breakhis)
- Extract the downloaded zip file to the data folder

5. Run `python train.py --config config.json` on the cli with the the environment activated.

6. Config (optional)

- Modify the config json file to experiemnt with different parameters
- `Note: ` Check out this repository for a better understanding on how the folders and files are structured https://github.com/victoresque/pytorch-template

- **_Visiualization_**
        - By default tensorboard is set to `true` in the config file. 
        - Once training is done visit run `tensorboard --logdir saved/log/` on the cli and visit `http://localhost:6006` on the browser.

## Training log metrics
Model used is a densent 121 model(pretrained) and is included in the current repo in the saved folder
Can be used directly or train a different by defining a different model in the models folder and updating it the config file.

#### Training and validation accuracies (logged on tensorboard)
<img src="images/train_val_acc.png" width="280"/>

#### Training and validation loss (logged on tensorboard)
<img src="images/train_val_loss.png" width="280"/>