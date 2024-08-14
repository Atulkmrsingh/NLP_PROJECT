# Multimodal Machine Translation

This project was developed as part of the **CS 772: Deep Learning for Natural Language Processing** course, under the guidance of **Prof. Pushpak Bhattacharya** (Jan 2023 - April 2023). The goal was to design and implement a multimodal machine translation (NMT) model that leverages both text and image inputs to improve translation accuracy.

## Project Overview

In traditional neural machine translation (NMT), only text data is used for translating between languages. However, in real-world scenarios, additional context such as visual information from images can significantly enhance translation quality. This project explores the integration of both text and image data to improve translation performance.

### Key Achievements

- **Multimodal NMT Model**: Developed a translation model that combines both text and image inputs. The model was trained and evaluated on a dataset containing 30,000 instances of paired text and images.
- **BLEU Score Improvement**: The multimodal NMT model achieved a BLEU score of **40.51**, outperforming the text-only NMT model, which scored **38.84**.
- **Detectron2 for Feature Extraction**: Utilized Detectron2, a state-of-the-art object detection library, to extract visual features from images. These features were then integrated into the translation process.
- **Named Entity Recognition (NER)**: Incorporated masked named entities in the text using NER to retain key information during translation. The visual and textual features were combined using MBART, a transformer-based model, to produce more accurate translations.

## Technical Details

### Dataset

- **Size**: 30,000 instances
- **Content**: Each instance consists of a text (source language) and an associated image.

### Model Architecture

1. **Text Processing**: 
   - Used standard NMT techniques to process and translate text data.
   - Masked named entities were identified using a Named Entity Recognition (NER) model.

2. **Image Processing**: 
   - Extracted visual features from images using **Detectron2**.
   - The visual features were processed to capture relevant contextual information.

3. **Multimodal Fusion**:
   - Combined the textual and visual features to enhance the translation output.
   - Used **MBART** (Multilingual BART) as the core model for handling the multimodal input.

### Results

- **Multimodal NMT**:
  - BLEU Score: **40.51**
- **Text-only NMT**:
  - BLEU Score: **38.84**

The significant improvement in BLEU score demonstrates the efficacy of incorporating visual information into the translation process.

## How to Run

1. **Prerequisites**:
   - Python 3.x
   - PyTorch
   - Detectron2
   - MBART model and tokenizer
   - NLTK for BLEU score calculation

2. **Setup**:
   - Clone the repository.
   - Install the required dependencies using `pip install -r requirements.txt`.

3. **Training**:
   - Preprocess the dataset to extract text and image features.
   - Train the multimodal NMT model using the provided training script.

4. **Evaluation**:
   - Evaluate the model on the test set to calculate BLEU scores.

## Conclusion

This project demonstrates that integrating visual context into machine translation significantly improves the quality of translations. The multimodal NMT model outperformed the text-only model, indicating the potential of multimodal approaches in real-world translation tasks.

## Acknowledgments

- **Instructor**: Prof. Pushpak Bhattacharya
- **Course**: CS 772: Deep Learning for Natural Language Processing
- **Semester**: January 2023 - April 2023

---

For more information or to access the code, please refer to the repository or contact the author.
