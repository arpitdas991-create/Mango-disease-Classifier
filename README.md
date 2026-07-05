Mango disease classifier, using pretrained model (resnet18).

**DATASET** : downloaded from kaggle at (https://www.kaggle.com/datasets/warcoder/mango-leaf-disease-dataset)

**METRIC**:
                  precision    recall  f1-score   support

Anthracnose       1.00      1.00      1.00        67

Bacterial Canker       0.99      1.00      0.99        72
  
  Cutting Weevil       1.00      1.00      1.00        76
  
  Die Back       0.99      1.00      0.99        79
  
  Gall Midge       1.00      0.97      0.99        77
  
  Healthy       1.00      1.00      1.00        67
  
  Powdery Mildew       1.00      1.00      1.00        94
  
  Sooty Mould       1.00      1.00      1.00        68

  
  accuracy                           1.00       600
  
  macro avg       1.00      1.00      1.00       600
  
  weighted avg       1.00      1.00      1.00       600

**Test Accuracy** : 99.83% (599/600 correct predictions)

**Model Training (Google Colab)**:
1. Split the dataset into training, validation, and test sets.
2. Apply data augmentation and preprocessing.
3. Train the final classification layer of a pretrained ResNet18.
4. Fine-tune the entire network.
5. Save the model with the best validation accuracy.
6. Evaluate the model on the test set.
7. Generate the confusion matrix and classification report.

**Deployment** :
1. Create a Hugging Face Space.
2. Build the interface using Gradio.
3. Implement app.py and model.py using PyTorch, Torchvision, Pillow, and Gradio.
4. Test the application locally.
5. Deploy the application on Hugging Face Spaces.

**HUGGING FACE SPACE** : https://huggingface.co/spaces/dasArpit111/MANGO_DISEASE_CLASSIFIER

**Technologies Used** :
1. Python
2. PyTorch
3. Torchvision
4. ResNet18 (Transfer Learning)
5. Gradio
6. Pillow
7. Scikit-learn
8. Google Colab
9. Hugging Face Spaces
