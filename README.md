# Vaccine Misinformation Detector

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](#license)  
[Try the demo on Hugging Face Spaces]([https://huggingface.co/spaces/Heishigan/vaccine-misinfo-detector](https://huggingface.co/spaces/heishi99/vaccine-misinfo-detector))

---

## Overview

A Natural Language Processing (NLP) tool to **detect and rebut vaccine-related misinformation** using a fine-tuned BERT model with OCR support. Future enhancements will include a Retrieval-Augmented Generation (RAG) pipeline that provides real-time, evidence-based rebuttals.

---

## Features

- **Text Classification**: BERT-based binary classifier (`misinfo` vs. `factual`)
- **OCR Detection**: Extract and classify text from images (e.g., memes)
- **Future RAG Pipeline**:
  - Semantic search over a curated vaccine knowledge base
  - Contextual rebuttal generation with citations

---

##  Demo

Check out the live demo hosted on Hugging Face Spaces:

 [https://huggingface.co/spaces/Heishigan/vaccine-misinfo-detector](https://huggingface.co/spaces/Heishigan/vaccine-misinfo-detector)

---

## 🛠️ Quick Start

### 1. Clone the repository
```git clone https://github.com/Heishigan/vaccine-misinfo-detector.git```
```cd vaccine-misinfo-detector```


### 2. Setup Environment
```python3 -m venv venv```
```source venv/bin/activate```
```pip install -r requirements.txt```


### 3. Run the Demo Locally
```python app.py```

Or use Gradio:
```gradio app.py```

---

## How It Works

1. **Input**: Text or image containing a vaccine-related claim
2. **Classification**: BERT model outputs 0 (misinfo) or 1 (factual)
3. *(Upcoming)*: If flagged as misinformation, the RAG pipeline will launch a knowledge retrieval + LLM-generated rebuttal

---

## Team & Acknowledgements

**Developed by**:
- Heishigan
- Xinrui Wan
- Kaif Ahmed
- Siqi Xiang

**Built with**:
- Hugging Face Transformers
- EasyOCR
- Gradio
- SciVerify
- World Health Organization (WHO)
- Centers for Disease Control and Prevention (CDC)

---

## Roadmap

- ✅ Deploy to Hugging Face Spaces
- ⬜ Add OCR image support
- ⬜ Implement RAG pipeline (retriever + generator)
- ⬜ Add citation metadata to rebuttals
- ⬜ Evaluate on external datasets

---

