# 🤖 AI Photo Tagger v3.0 - Enhanced Quality Control & Concert Photography

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Cross-Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)](https://github.com/trevcodner/ai-photo-tagger)

Automatically tag thousands of photos using local AI with advanced quality control, concert photography features, and cross-platform support.

## ✨ Features

### 🎯 **Enhanced Quality Control**
- **Blur Detection**: Identifies sharp, blurry, and very blurry images
- **Histogram Analysis**: Detects under/overexposed and low contrast photos
- **Exposure Analysis**: Automatic exposure quality assessment
- **Configurable Thresholds**: Adjust quality standards for your workflow

### 🎵 **Concert Photography Mode**
- **Stage Lighting Detection**: Recognizes concert lighting patterns
- **Motion Blur Analysis**: Distinguishes artistic motion from camera shake
- **Crowd Detection**: Identifies audience and venue shots
- **Low Light Optimization**: Special handling for concert conditions
- **Venue Analysis**: Automatic venue size and atmosphere detection

### 📸 **Professional RAW Support**
- **Enhanced .ARW Processing**: Optimized for Sony cameras (A7C, A7R, etc.)
- **Universal RAW Support**: .CR2, .NEF, .ORF, .RW2, .DNG files
- **rawpy Integration**: High-quality RAW processing with proper color
- **Metadata Preservation**: Maintains original camera settings

### 🌍 **Cross-Platform Compatibility**
- **Windows**: Full support with automated setup
- **Linux**: Ubuntu, Debian, CentOS, Fedora, Arch Linux
- **macOS**: Native support with Homebrew integration

## 🚀 Quick Start

### Windows
```batch
# Download and run setup
setup_windows.bat

# For concert photography
Run_Concert_Mode.bat
```

### Linux/macOS
```bash
# Make executable and run setup
chmod +x setup_linux.sh
./setup_linux.sh

# For concert photography
./run_concert_mode.sh
```

## 📋 Requirements

- **Python 3.9+**
- **Ollama** (local AI service)
- **4GB+ free space** (for AI model)
- **8GB+ RAM** (16GB recommended for large collections)

## 🔧 Installation

### Automated Setup (Recommended)

Choose your platform:

- **Windows**: Run `setup_windows.bat`
- **Linux**: Run `./setup_linux.sh`
- **macOS**: Run `./setup_macos_enhanced.sh`

### Manual Installation

1. **Install Ollama**:
   ```bash
   # Windows: Download from https://ollama.ai/download
   # Linux/macOS:
   curl -fsSL https://ollama.ai/install.sh | sh
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download AI model**:
   ```bash
   ollama pull llava:7b
   ```

4. **Run the application**:
   ```bash
   python ai_photo_tagger_v3.py --help
   ```

## 🎵 Concert Photography Usage

### Basic Concert Mode
```bash
python ai_photo_tagger_v3.py \
    --folder /path/to/concert/photos \
    --concert-mode \
    --quality-check
```

### Advanced Concert Settings
```bash
python ai_photo_tagger_v3.py \
    --folder /path/to/concert/photos \
    --concert-mode \
    --quality-check \
    --blur-threshold 150 \
    --model llava:7b
```

### Quality Control Only
```bash
python ai_photo_tagger_v3.py \
    --folder /path/to/photos \
    --quality-check \
    --blur-threshold 100
```

## 📊 Generated Tags

### AI Content Tags
- **Subjects**: person, musician, guitar, crowd, stage
- **Actions**: playing, singing, dancing, performing
- **Settings**: concert, venue, outdoor, indoor
- **Mood**: energetic, dramatic, intimate, lively

### Quality Control Tags
- **Technical**: `quality:sharp`, `quality:blurry`, `quality:very_blurry`
- **Exposure**: `exposure:underexposed`, `exposure:overexposed`, `exposure:good`
- **Contrast**: `contrast:low_contrast`, `contrast:high_contrast`, `contrast:dramatic`

### Concert-Specific Tags
- **Lighting**: `stage_lighting`, `dramatic_lighting`, `colored_lights`, `spotlight`
- **Movement**: `motion_blur`, `camera_shake`, `intentional_movement`
- **Venue**: `crowd`, `audience`, `packed_venue`, `intimate_venue`
- **Conditions**: `low_light`, `high_iso`, `dark_venue`

## 🔍 Quality Analysis Examples

### Concert Photography Results
```
🎯 Processing: IMG_3847.jpg
✅ AI Tags: musician, guitar, stage, concert, performance
🔍 Quality: stage_lighting, motion_blur, dramatic_lighting
⚠️  Motion blur detected: intentional_movement
📊 Histogram: high_contrast (acceptable for concert)
🎵 Venue: packed_venue, low_light
```

### Quality Control Workflow
1. **Process photos** with quality analysis
2. **Filter by quality tags**:
   - `quality:sharp` → Portfolio candidates
   - `stage_lighting` → Apply stage presets
   - `motion_blur` → Review for artistic value
   - `quality:very_blurry` → Delete or review
3. **Use in Lightroom** via XMP sidecar files

## 🛠 Configuration

### Concert Mode Settings
```python
CONCERT_CONFIG = {
    "blur_threshold": 150,        # Higher tolerance for motion
    "exposure_threshold": 0.15,   # Accept dramatic exposure
    "contrast_threshold": 0.3,    # Accept high contrast
    "low_light_threshold": 30,    # Concert lighting levels
}
```

### Quality Control Settings
```python
QUALITY_CONFIG = {
    "check_blur": True,
    "check_histogram": True,
    "check_exposure": True,
    "blur_threshold": 100.0,
    "histogram_balance_threshold": 0.8,
    "exposure_threshold": 0.1,
}
```

## 📁 Output

### XMP Sidecar Files
- **Keywords**: AI-generated content tags + quality tags
- **Quality Metadata**: Technical analysis results
- **Lightroom Compatible**: Import with metadata
- **Searchable**: Filter by any tag combination

### Processing Reports
- **Statistics**: Processing rate, quality issues detected
- **Quality Summary**: Blur, exposure, contrast analysis
- **Concert Analysis**: Stage lighting, motion, crowd detection
- **Progress Tracking**: Resume interrupted sessions

## 🎯 Use Cases

### Concert Photographers
- **Rapid Quality Assessment**: Identify keepers vs. rejects
- **Artistic Motion Blur**: Distinguish from camera shake
- **Stage Lighting**: Automatic detection and tagging
- **Crowd Shots**: Venue atmosphere documentation
- **Portfolio Curation**: Quality-based filtering

### General Photography
- **Quality Control**: Blur and exposure analysis
- **Batch Processing**: Large photo collections
- **Metadata Enhancement**: Rich keyword generation
- **Workflow Integration**: Lightroom/photo manager support

## 🔧 Troubleshooting

### Common Issues

**Windows**:
- Run as Administrator if permission errors
- Install Visual Studio Build Tools for rawpy
- Use PowerShell instead of Command Prompt

**Linux**:
- Install build tools: `sudo apt-get install build-essential`
- For rawpy: `sudo apt-get install python3-dev`
- Check Python version: `python3 --version` (need 3.9+)

**macOS**:
- Install Xcode Command Line Tools: `xcode-select --install`
- Use Homebrew: `brew install python@3.11`
- For M1/M2 Macs: Check architecture compatibility

### Performance Tips
- **Large Collections**: Process in batches of 1000-5000 photos
- **Memory Usage**: Close other applications during processing
- **Storage**: Ensure adequate free space for XMP files
- **Interruption**: Processing can be safely resumed

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup
```bash
git clone https://github.com/trevcodner/ai-photo-tagger.git
cd ai-photo-tagger
pip install -r requirements-dev.txt
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Ollama** for local AI inference
- **rawpy** for RAW file processing
- **OpenCV** for image analysis
- **ExifTool** for metadata handling
- **Concert photographers** for feature testing and feedback

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/trevcodner/ai-photo-tagger/issues)
- **Discussions**: [GitHub Discussions](https://github.com/trevcodner/ai-photo-tagger/discussions)
- **Documentation**: [Wiki](https://github.com/trevcodner/ai-photo-tagger/wiki)

## 🚀 What's Next

- **Face Recognition**: Enhanced people detection
- **Venue Database**: Automatic venue identification
- **Batch Export**: Direct integration with photo managers
- **Cloud Processing**: Optional cloud AI processing
- **Mobile App**: Companion mobile application

---

**⭐ Star this repository if you find it useful!**

Made with ❤️ by photographers, for photographers.
