import torch
import gradio as gr

from PIL import Image

from torchvision import transforms

from model import get_model

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = get_model(8)  

model.load_state_dict(
    torch.load(
        "best_disease_model.pth",
        map_location=device
    )
)

model.to(device)

model.eval()

train_mean = [0.7796, 0.7145, 0.6107]
train_std = [0.2099, 0.2098, 0.2097]

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.ToTensor(),
    transforms.Normalize(
        train_mean,
        train_std
    )
])

def predict(image):
    image = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        output = model(image)
        probabilities = torch.nn.functional.softmax(output, dim=1)
        confidence, predicted = torch.max(probabilities, 1)
        
    classes = ['Anthracnose', 'Bacterial Canker', 'Cutting Weevil', 'Dieback', 'Gall Midge', 'Healthy', 'Powdery Mildew', 'Sooty Mold']
    predicted_class = classes[predicted.item()]
    return f"{predicted_class} ({confidence.item()*100:.2f}%)"

app = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Text(label="Prediction"),
    title=" Mango Disease Classifier",
    description="Upload an image of a mango leaf to classify its disease."
)


app.launch()
