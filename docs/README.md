# 📖 Documentation

Welcome to the AI Photo Tagger v3.0 documentation!

## 📚 Table of Contents

### Getting Started
- [Installation Guide](installation.md) - Complete setup instructions for all platforms
- [Quick Start](quick-start.md) - Get up and running in 5 minutes
- [Configuration](configuration.md) - Customize settings for your workflow

### Features
- [Quality Control](quality-control.md) - Blur detection, histogram analysis, exposure assessment
- [Concert Photography](concert-photography.md) - Stage lighting, motion blur, crowd detection
- [RAW Processing](raw-processing.md) - Enhanced support for .ARW, .CR2, .NEF files
- [Cross-Platform](cross-platform.md) - Windows, Linux, macOS compatibility

### Usage Guides
- [Basic Usage](basic-usage.md) - Standard photo tagging workflow
- [Concert Mode](concert-mode.md) - Specialized concert photography features
- [Quality Analysis](quality-analysis.md) - Understanding quality metrics and tags
- [Batch Processing](batch-processing.md) - Handling large photo collections

### Integration
- [Lightroom](lightroom-integration.md) - Using XMP files with Adobe Lightroom
- [Photo Managers](photo-managers.md) - Integration with other photo management software
- [Workflow](workflow-integration.md) - Integrating into your existing photography workflow

### Technical Reference
- [API Reference](api-reference.md) - Function and class documentation
- [Configuration Options](config-reference.md) - Complete configuration reference
- [Quality Metrics](quality-metrics.md) - Understanding quality analysis results
- [Troubleshooting](troubleshooting.md) - Common issues and solutions

### Development
- [Contributing](../CONTRIBUTING.md) - How to contribute to the project
- [Architecture](architecture.md) - Technical architecture overview
- [Testing](testing.md) - Testing guidelines and procedures
- [Building](building.md) - Building from source

### Examples
- [Concert Photography](examples/concert-photography.md) - Real-world concert photography examples
- [Quality Control](examples/quality-control.md) - Quality analysis examples
- [Batch Processing](examples/batch-processing.md) - Large collection processing examples
- [Custom Configuration](examples/custom-config.md) - Custom configuration examples

## 🎯 Quick Links

### For Concert Photographers
- [Concert Mode Setup](concert-photography.md#setup)
- [Stage Lighting Detection](concert-photography.md#stage-lighting)
- [Motion Blur Analysis](concert-photography.md#motion-blur)
- [Quality Thresholds](concert-photography.md#quality-thresholds)

### For General Photography
- [Quality Control Setup](quality-control.md#setup)
- [Blur Detection](quality-control.md#blur-detection)
- [Exposure Analysis](quality-control.md#exposure-analysis)
- [Batch Processing](batch-processing.md)

### For Developers
- [API Documentation](api-reference.md)
- [Contributing Guidelines](../CONTRIBUTING.md)
- [Architecture Overview](architecture.md)
- [Testing Framework](testing.md)

## 🛠 Platform-Specific Guides

### Windows
- [Windows Installation](installation.md#windows)
- [Windows Troubleshooting](troubleshooting.md#windows)
- [Windows Performance](performance.md#windows)

### Linux
- [Linux Installation](installation.md#linux)
- [Distribution-Specific Notes](installation.md#linux-distributions)
- [Linux Troubleshooting](troubleshooting.md#linux)

### macOS
- [macOS Installation](installation.md#macos)
- [Homebrew Setup](installation.md#homebrew)
- [Apple Silicon Notes](installation.md#apple-silicon)

## 📊 Features Overview

### Quality Control
- **Blur Detection**: Laplacian variance method with configurable thresholds
- **Histogram Analysis**: Exposure and contrast assessment
- **Quality Classification**: Technical quality scoring and categorization
- **Artistic Recognition**: Distinguishes artistic choices from technical issues

### Concert Photography
- **Stage Lighting**: Automatic detection and classification
- **Motion Analysis**: Artistic motion blur vs. camera shake detection
- **Crowd Detection**: Audience and venue atmosphere analysis
- **Low Light**: Specialized processing for challenging conditions

### RAW Processing
- **Enhanced Support**: .ARW, .CR2, .NEF, .ORF, .RW2, .DNG files
- **Color Accuracy**: Proper color space and white balance handling
- **Performance**: Optimized processing for large RAW files
- **Compatibility**: Works with modern camera RAW formats

## 🎵 Concert Photography Examples

### Stage Lighting Detection
```
🎯 Processing: concert_001.jpg
✅ AI Tags: musician, guitar, stage, concert, performance
🔍 Quality: stage_lighting, dramatic_lighting, colored_lights
📊 Analysis: High contrast (acceptable for concert)
🎵 Venue: main_stage, large_venue
```

### Motion Blur Analysis
```
🎯 Processing: drummer_action.jpg
✅ AI Tags: drummer, drums, action, performance, energy
🔍 Quality: motion_blur, intentional_movement
⚠️  Motion detected: artistic (keep for portfolio)
🎵 Analysis: Performance energy captured
```

## 🔧 Configuration Examples

### Concert Photography Config
```python
CONCERT_CONFIG = {
    "blur_threshold": 150,      # Higher tolerance for motion
    "exposure_threshold": 0.15, # Accept dramatic exposure
    "contrast_threshold": 0.3,  # Accept high contrast
    "stage_lighting": True,     # Enable stage lighting detection
    "crowd_detection": True,    # Enable crowd analysis
}
```

### Quality Control Config
```python
QUALITY_CONFIG = {
    "check_blur": True,
    "check_histogram": True,
    "check_exposure": True,
    "blur_threshold": 100.0,
    "histogram_balance": 0.8,
    "exposure_threshold": 0.1,
}
```

## 📞 Getting Help

### Community Support
- [GitHub Discussions](https://github.com/your-username/ai-photo-tagger/discussions) - Community Q&A
- [GitHub Issues](https://github.com/your-username/ai-photo-tagger/issues) - Bug reports and feature requests

### Documentation Feedback
If you find any issues with this documentation or have suggestions for improvement:
1. [Create an issue](https://github.com/your-username/ai-photo-tagger/issues/new) with the "documentation" label
2. [Start a discussion](https://github.com/your-username/ai-photo-tagger/discussions) in the "Q&A" category
3. Submit a pull request with improvements

## 🏆 Contributing to Documentation

We welcome contributions to improve this documentation:
- Fix typos and improve clarity
- Add examples and use cases
- Create tutorials for specific workflows
- Translate documentation to other languages

See our [Contributing Guide](../CONTRIBUTING.md) for more information.

---

**Happy photo tagging!** 📸✨
