# 🎯 AI Photo Tagger - Current State

**Last Updated:** December 22, 2024
**Version:** 3.0 (Script)
**Status:** Functional CLI Tool

---

## ✅ **What Works:**

### **Vision Analysis (100%)**
- ✅ Detects objects, people, scenes.
- ✅ Understands context (e.g., "concert", "crowd").
- ✅ Generates relevant keywords via LLaVA model.

### **Quality Analysis (100%)**
- ✅ **Blur:** Calculates Laplacian variance to score sharpness.
- ✅ **Exposure:** Analyzes histogram for over/under exposure.
- ✅ **Color:** Checks dynamic range.

### **File Operations (100%)**
- ✅ recursive directory scanning.
- ✅ RAW file support (`.ARW`, `.CR2`, etc.) using `rawpy` and `exiftool`.
- ✅ XMP Sidecar generation (Industry standard).

### **Workflow (CLI)**
- ✅ Progress bars.
- ✅ Resume capability (skips already processed files).
- ✅ Logging.

---

## 🚧 **The "User Friction" Gap:**

1.  **Terminal Only:** You have to remember command line arguments.
    - `python ai_photo_tagger.py --folder /Photos/Concert --model llava:7b`
2.  **Installation:** Requires `pip install` of complex libraries (`opencv`, `rawpy`). Hard to give to a friend.
3.  **Visual Feedback:** You can't see the photo while it's being analyzed.

---

## 🛠️ **Tech Stack Details:**

- **Python:** 3.11
- **AI:** Local Ollama instance (Zero cost, privacy focused).
- **Processing:** Multi-threaded (can be improved).

---

## 🔧 **Known Issues:**

- **Speed:** Local vision models are heavy. 5-10 seconds per image on M3 Max. High volume shoots take time.
- **Hallucinations:** Sometimes AI sees things that aren't there (standard AI issue).

---

## 🚀 **Deployment:**

**Current:** Python Script.
**Target:** Native Mac App ("Photo Tagger Pro").

---

**Confidence:** Core algorithm is excellent. UX needs overhaul.
