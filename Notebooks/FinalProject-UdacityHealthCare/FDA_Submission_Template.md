# FDA  Submission

**Your Name:**  
Anup Sharma, MD PhD

**Name of your Device:**  
PneumoDetect-AI

## Algorithm Description 

### 1. General Information

**Intended Use Statement:**  
PneumoDetect-AI is a software device intended to assist clinicians by automatically analyzing frontal chest X-ray images for the presence or absence of pneumonia in adult patients. The device is intended for use as a diagnostic aid and not as a replacement for clinical judgment.

**Indications for Use:**  
PneumoDetect-AI is indicated for use in adult patients undergoing chest X-ray imaging for evaluation of suspected pneumonia. The device is intended to be used in hospital and outpatient clinical settings as an adjunct to radiologist interpretation.

**Device Limitations:**  
- Not intended for use in pediatric populations.
- Not validated for non-frontal (lateral or oblique) chest X-rays.
- May not reliably detect pneumonia in the presence of significant comorbidities (e.g., large pleural effusion, severe cardiomegaly).
- Performance may be reduced on images with poor quality, artifacts, or non-standard acquisition protocols.

**Clinical Impact of Performance:**  
A false negative result may delay diagnosis and treatment of pneumonia, potentially leading to adverse patient outcomes. A false positive result may lead to unnecessary further testing or treatment. The device is intended to support, not replace, clinical decision-making.

### 2. Algorithm Design and Function

<< Insert Algorithm Flowchart >>

**DICOM Checking Steps:**  
- Confirms file is DICOM format.
- Checks Modality is 'DX' (digital X-ray).
- Verifies BodyPartExamined is 'CHEST'.
- Optionally checks ViewPosition is 'PA' or 'AP' (frontal views).
- Extracts pixel array for further processing.

**Preprocessing Steps:**  
- Converts grayscale images to 3-channel if needed.
- Resizes images to 224x224 pixels (VGG16 input size).
- Normalizes pixel values using mean and standard deviation from training set.
- Adds batch dimension for model input.

**CNN Architecture:**  
- Based on VGG16 pre-trained on ImageNet.
- Final layers replaced with custom dense layers for binary classification (pneumonia vs. no pneumonia).
- Last layer uses sigmoid activation for probability output.

### 3. Algorithm Training

**Parameters:**
* Types of augmentation used during training: random rotations, shifts, flips, and brightness adjustments.
* Batch size: 32
* Optimizer learning rate: 0.0001 (Adam optimizer)
* Layers of pre-existing architecture that were frozen: All VGG16 convolutional layers initially frozen.
* Layers of pre-existing architecture that were fine-tuned: Last 2 convolutional blocks unfrozen for fine-tuning after initial training.
* Layers added to pre-existing architecture: GlobalAveragePooling, Dense(256, relu), Dropout(0.5), Dense(1, sigmoid).

<< Insert algorithm training performance visualization (e.g., loss/accuracy curves) >> 

<< Insert P-R curve >>

**Final Threshold and Explanation:**  
A threshold of 0.42 was selected based on maximizing the F1 score on the validation set, balancing sensitivity and specificity for clinical relevance.

### 4. Databases
 (For the below, include visualizations as they are useful and relevant)

**Description of Training Dataset:**  
- NIH ChestX-ray14 dataset, 80% split for training.
- 89,696 images from 24,644 unique patients.
- Adult patients, frontal chest X-rays only.
- Pneumonia prevalence: 8.5%
- Demographics: 55% male, 45% female; age range 18–90 years.

**Description of Validation Dataset:**  
- 20% split from the same dataset, stratified by pneumonia status.
- 22,424 images from 6,161 unique patients.
- Similar demographic and disease distribution as training set.

### 5. Ground Truth

Ground truth labels were established using natural language processing (NLP) of radiology reports as provided by the NIH ChestX-ray14 dataset. While this method achieves >90% accuracy, some mislabeling may occur due to NLP limitations. No manual re-labeling was performed.

### 6. FDA Validation Plan

**Patient Population Description for FDA Validation Dataset:**  
- Adult patients (age 18+)
- Both sexes
- Frontal chest X-ray modality (DX)
- Body part: chest
- Pneumonia prevalence: 5–15%
- Exclude patients with known lung malignancy or recent thoracic surgery

**Ground Truth Acquisition Methodology:**  
- Consensus read by two board-certified radiologists, with adjudication by a third in case of disagreement.

**Algorithm Performance Standard:**  
- The device will be considered non-inferior if its F1 score is within 5% of the average human radiologist F1 score as reported in Rajpurkar et al., 2017 (https://arxiv.org/pdf/1711.05225).