# 🤟 AI Powered Sign Language Converter

An AI-powered real-time Sign Language Converter that recognizes hand gestures using **MediaPipe Holistic**, classifies them with a **Machine Learning model**, converts the recognized words into natural language using an **LLM**, and finally speaks the generated sentence using **Text-to-Speech**.

---

# 📌 Project Overview

The project works in four major stages:

1. **Collect Sign Language Data**
2. **Train a Machine Learning Model**
3. **Predict Signs in Real Time**
4. **Convert Predicted Words into Natural Sentences using an LLM**

---

# 🏗️ Complete Workflow

```text
          Webcam
             │
             ▼
      MediaPipe Holistic
             │
             ▼
 Landmark Extraction (Face + Pose + Hands)
             │
             ▼
      coords.csv Dataset
             │
             ▼
 Random Forest Model Training
             │
             ▼
    body_language.pkl
             │
             ▼
 Real-Time Prediction
             │
             ▼
 List of Predicted Words
             │
             ▼
        Large Language Model
             │
             ▼
     Natural Sentence
             │
             ▼
      Text-to-Speech
```

---

# 📂 Project Files

| File                | Purpose                                               |
| ------------------- | ----------------------------------------------------- |
| `main.py`           | Main application                                      |
| `llm.py`            | Converts detected words into proper English sentences |
| `tts_service.py`    | Speaks the generated sentence                         |
| `coords.csv`        | Dataset generated from landmarks                      |
| `body_language.pkl` | Trained Machine Learning model                        |
| `.env`              | Stores API keys securely                              |
| `requirements.txt`  | Project dependencies                                  |

---

# 🧠 Stage 1 — Dataset Creation

The first step is teaching the computer what each sign looks like.

Example words:

* hello
* thank_you
* sorry
* please
* yes
* no
* i
* you
* need
* food
* water

For every word, the application records approximately **200 samples**.

Each frame captured from the webcam is processed by **MediaPipe Holistic**, which extracts body landmarks instead of saving raw images.

---

# 🎯 Landmark Extraction

Instead of learning from pixels, the model learns from landmark coordinates.

For every frame the application extracts:

### Pose

* 33 Body Landmarks

Each landmark contains:

* X
* Y
* Z
* Visibility

---

### Face

* 468 Face Landmarks

Each landmark contains:

* X
* Y
* Z

---

### Left Hand

* 21 Landmarks

Each landmark contains:

* X
* Y
* Z

---

### Right Hand

* 21 Landmarks

Each landmark contains:

* X
* Y
* Z

---

# 📄 coords.csv

Every captured frame becomes one row inside `coords.csv`.

Example:

```text
class,
pose_x0,pose_y0,...
face_x0,...
lh_x0,...
rh_x0,...
```

Example row:

```text
hello,0.41,0.73,0.02,...
```

The CSV becomes the complete training dataset for the Machine Learning model.

---

# 🤖 Stage 2 — Model Training

After collecting enough samples, the dataset is loaded using Pandas.

The project separates:

* Features (Landmarks)
* Labels (Gesture Name)

The data is then split into training and testing datasets.

Current classifier:

* Random Forest Classifier

After training, the model is saved as

```text
body_language.pkl
```

This allows the project to make predictions instantly without retraining every time.

---

# 🎥 Stage 3 — Real-Time Prediction

During prediction:

1. Webcam captures live frames.
2. MediaPipe extracts landmarks.
3. Landmark coordinates are converted into feature vectors.
4. The trained model predicts the gesture.
5. Confidence score is calculated.
6. Only stable predictions are accepted.

To reduce false positives, the same prediction must appear multiple consecutive times before it is accepted.

Example:

```text
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
```

Only then is the word added to the sentence.

---

# 🧠 Stage 4 — Sentence Generation using LLM

The Machine Learning model only predicts individual words.

Example:

```text
["i", "need", "water"]
```

These words are passed to the Large Language Model.

The LLM understands context and generates a natural sentence.

Example:

Input

```text
["i", "need", "water"]
```

Output

```text
I need some water.
```

Another example

Input

```text
["you", "food"]
```

Output

```text
Do you need food?
```

The LLM makes communication much more natural than simply displaying isolated words.

---

# 🔊 Text-to-Speech

After sentence generation, the final sentence is spoken aloud.

Example

```text
I need some water.
```

↓

Speaker Output

```text
"I need some water."
```

---

# ➕ How to Teach the Model New Words

Adding new vocabulary is simple.

### Step 1

Open the `actions` list.

Example:

```python
actions = [
    "hello",
    "thank_you",
    "sorry",
    "please",
    "yes",
    "no",
    "i",
    "you",
    "need",
    "food",
    "water"
]
```

Add new words.

Example:

```python
actions = [
    ...
    "hospital",
    "medicine",
    "help",
    "doctor",
    "family"
]
```

---

### Step 2

Run the data collection script.

The application will automatically:

* Detect landmarks
* Record approximately 200 samples
* Append them into `coords.csv`

No manual labeling is required.

---

### Step 3

Train the model again.

A new

```text
body_language.pkl
```

will be generated containing knowledge of the new signs.

---

### Step 4

Run the prediction program.

The newly added gestures can now be recognized automatically.

---

# 💡 Why Landmarks Instead of Images?

Using landmarks makes the system:

* Faster
* Smaller
* More robust
* Less affected by lighting
* Easier to train
* Requires much less storage

Instead of storing thousands of images, the project only stores numerical coordinates.

---

# 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe Holistic
* NumPy
* Pandas
* Scikit-learn
* Pickle
* Google Gemini / Hugging Face (LLM)
* pyttsx3
* python-dotenv

---

# 🚀 Future Improvements

* Support 100+ sign language words
* Deep Learning (LSTM / Transformer)
* Sentence correction
* Continuous sign recognition
* Hindi language support
* Mobile application
* Cloud deployment
* User-specific training
* Multi-language translation

---

# 👨‍💻 Author

**Sarthak Bansal**

Computer Science Engineering Student

AI • Machine Learning • Computer Vision • MERN Stack
