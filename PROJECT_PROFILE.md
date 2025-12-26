# 📝 AI Photo Tagger (Photo Tagger Pro) - Project Profile

**Type:** Python Command-Line Tool -> Planned Mac App  
**Status:** Advanced Prototype (CLI working)  
**Purpose:** Automate professional photo metadata tagging using Local Vision AI.  
**Created:** 2024  
**Last Updated:** December 22, 2024

---

## 🎯 **What It Is:**

A powerful script that "looks" at your photos using AI (LLaVA), understands what's in them, analyzes their technical quality (blur, exposure), and writes keywords directly into the file metadata (XMP) so Lightroom can read them.

**The Problem It Solves:**
- "Culling" and tagging photos takes forever.
- Finding "that one shot of the guitarist jumping" is impossible without tags.
- Manual tagging is boring and ADHD-hostile.
- **This tool does it while you sleep.**

---

## 💡 **Origin Story:**

**The Spark:** You wanted a Lightroom plugin to auto-tag photos.
**The Failure:** Lua (LR's language) was obscure, and AI couldn't help write it well.
**The Pivot:** "Screw the plugin, I'll build a standalone tool."
**The Result:** A vastly superior external tool that uses powerful computer vision libraries (OpenCV, PyTorch) that a plugin never could.
**Lesson:** The constraint led to a better product.

---

## ✨ **Current Features:**

### **AI Vision:**
- Uses **Ollama / LLaVA** (Local Large Vision Model).
- "Sees" the image (Subject, Action, Mood, Lighting).
- Generates descriptive tags.

### **Quality Control (The "Pro" features):**
- **Blur Detection:** Identifies camera shake vs. motion blur.
- **Exposure Analysis:** Flags blown highlights or crushed shadows.
- **Histogram Analysis:** Checks contrast balance.

### **Special Modes:**
- **Concert Mode:** Special logic for stage lights, crowds, and low light situations. (Your passion!)

### **Output:**
- Writes sidecar `.xmp` files.
- Lightroom reads these automatically.
- Zero destructive changes to original RAW files.

---

## 🛠️ **Tech Stack:**

**Language:** Python 3.11  
**Core Libraries:**
- `ollama` (AI vision)
- `opencv-python` (cv2 - for blur/quality)
- `Pillow` (PIL - image handling)
- `numpy` (maths)
- `rawpy` (RAW file support)

---

## 📊 **Current Status:**

**Completion:** 80% (Core script is solid).  
**What Works:**
- All analysis features.
- XMP generation.
- Batch processing.

**What's Left:**
- **The Interface:** Currently runs in Terminal. Needs a drag-and-drop Mac UI to be "Photo Tagger Pro".
- **Installer:** Python environment setup is tricky for non-techies.

---

## 👤 **Who It's For:**

**Primary:** You (Concert Photographer).  
**Secondary:** Wedding/Event photographers who hate culling.  
**Potential:** Stock photographers (auto-keywording is money).

---

## 🎯 **Success Metrics:**

- **Time Saved:** Reduces 4 hours of culling to 20 mins of review.
- **Organization:** "Show me all photos of 'smiling' + 'stage light'" actually works in Lightroom.

---

**Status:** The engine is built. It needs a Ferrari body (Mac App).
