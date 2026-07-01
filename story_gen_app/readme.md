## AI Story Generator

An AI-powered Story Generator built using **Streamlit**, **LangChain**, and **Google Gemini AI**. Users can generate unique stories by selecting genre, tone, length, language, character name, setting, and a custom prompt. The generated story can also be downloaded as a PDF.

---

##  Features

* Generate stories using Generative AI

* Multiple genres:

  * Fantasy
  * Mystery
  * Horror
  * Sci-Fi
  * Adventure

* Multiple story tones:

  * Funny
  * Serious
  * Dark
  * Emotional
  * Suspenseful

* Adjustable story length:

  * Short
  * Medium
  * Long

* Multi-language support:

  * English
  * Hindi
  * Hinglish
  * Spanish
  * French

* Character customization

* Story setting customization

* Custom story prompts

* Download generated stories as PDF files

* Simple and interactive Streamlit UI

---

##  Tech Stack

### Frontend

* Streamlit

### AI Framework

* LangChain

### LLM

* Google Gemini (Google Generative AI)

### PDF Generation

* ReportLab / Custom PDF Utility

### Language

* Python

---

## 📂 Project Structure

```bash
AI-Story-Generator/
│
├── app.py
│
├── chains/
│   └── story_chains.py
│
├── utils/
│   └── story_pdf.py
│
├── .env
├── requirements.txt
└── README.md
```

---

##  Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/AI-Story-Generator.git

cd AI-Story-Generator
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Get your API key from Google AI Studio.

---

##  Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📋 How It Works

### Step 1

Select story settings from the sidebar:

* Genre
* Tone
* Story Length
* Language

### Step 2

Provide:

* Character Name
* Story Setting
* Story Prompt

### Step 3

Click:

```text
 Generate Story
```

### Step 4

LangChain sends the structured prompt to Google Gemini AI.

### Step 5

Gemini generates a unique story based on the selected inputs.

### Step 6

The story is converted into a PDF and can be downloaded.

---

##  Example Prompt

```text
Character: Aryan

Setting: Ancient Magical Kingdom

Prompt:
A young warrior discovers a hidden dragon egg that can change the fate of the kingdom.
```

---

##  AI Workflow

```text
User Input
     ↓
Streamlit UI
     ↓
LangChain Prompt Template
     ↓
Google Gemini AI
     ↓
Generated Story
     ↓
PDF Generator
     ↓
Download PDF
```

---

##  Required Libraries

```txt
streamlit
langchain
langchain-google-genai
python-dotenv
reportlab
```

---

## Future Improvements

* Story illustrations using AI
* Story history storage
* User authentication
* Story sharing feature
* Voice narration
* More language support
* Multiple AI model selection

---

## Author

Developed by Sarthak Bansal

A Generative AI project demonstrating the integration of Streamlit, LangChain, and Google Gemini for dynamic story generation.
