# 📋 Photo Tagger Pro - Requirements

## 💻 **System Requirements**

- **Hardware:** Apple Silicon (M1/M2/M3) is effectively required for LLaVA/Ollama speed.
  - Intel Macs will work but be very slow (30s+ per image).
- **RAM:** 16GB minimum recommended (AI models need ~4-8GB dedicated).
- **Storage:** Fast SSD for image reading.

---

## 🛠️ **Dev Environment**

- **Python:** 3.11+
- **Ollama:** Installed and running (`brew install ollama`).
- **ExifTool:** Required for XMP writing (`brew install exiftool`).

---

## 🔑 **Dependencies**

```text
ollama      # AI Vision
opencv-python # Blur detection
rawpy       # RAW file reading
Pillow      # Image resizing
numpy       # Math
```

---

## 🚀 **Setup Instructions**

1.  **Install System Tools:**
    ```bash
    brew install exiftool ollama
    ollama pull llava:7b
    ```

2.  **Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Run:**
    ```bash
    python ai_photo_tagger.py --folder ~/Pictures/MyShoot
    ```

---

## ⚠️ **Known Hurdles**

- **Ollama Service:** Must be running (`ollama serve`) before the script starts.
- **Model Download:** First run requires downloading ~4GB model file.

