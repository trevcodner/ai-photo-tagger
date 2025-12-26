# 🗺️ Photo Tagger Pro - Mac App Roadmap

**Goal:** Turn "the script" into the ultimate Photographer's utility.

---

## 📅 **Phase 1: The UI Wrapper (Weeks 1-4)**

**Goal:** Drag & Drop simplicity.

1.  **SwiftUI App:**
    - Main Window: "Drop Folder Here".
    - Settings: "Choose Ollama Model", "Quality Thresholds".
2.  **Process Runner:** Swift executes the Python script in the background.
3.  **Live Log:** Show the script output in a nice scrolling window.

---

## 📅 **Phase 2: Visual Feedback (Weeks 5-8)**

**Goal:** See what the AI sees.

1.  **Grid View:** Show thumbnails of photos as they process.
2.  **Status Badges:** Green check for "Good", Red X for "Blurry".
3.  **Tag Inspector:** Click a photo to see the generated tags immediately.

---

## 📅 **Phase 3: Deep Integration (Weeks 9-12)**

**Goal:** Seamless Lightroom Workflow.

1.  **Watched Folders:** App sits in menu bar and watches your "Import" folder. Auto-tags new files.
2.  **Automations:** "If Quality = Blurry, move to /Rejects folder".
3.  **Notifications:** "Finished processing 500 photos. 42 rejects found."

---

## 📅 **Phase 4: Optimization (Future)**

1.  **Core ML:** Replace Ollama/LLaVA with Apple's Native CoreML Vision models (faster, no external dependencies).
2.  **Metal:** Use Metal for OpenCV operations (insane speedup).

---

**Status:** Ready to start Phase 1.
