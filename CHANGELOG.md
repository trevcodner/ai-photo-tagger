# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial development phase

## [3.0.0] - 2025-07-18

### Added
- **Quality Control System**: Comprehensive blur detection, histogram analysis, and exposure assessment
- **Concert Photography Mode**: Specialized features for concert and live music photography
- **Enhanced RAW Support**: Improved processing for .ARW, .CR2, .NEF, and other RAW formats
- **Cross-Platform Compatibility**: Full support for Windows, Linux, and macOS
- **Advanced Blur Detection**: Distinguishes between camera shake and intentional motion blur
- **Stage Lighting Detection**: Recognizes concert lighting patterns and dramatic lighting
- **Crowd Analysis**: Automatic detection of audience and venue atmosphere
- **Histogram Analysis**: Identifies under/overexposed and low contrast images
- **Configurable Thresholds**: Adjustable quality standards for different photography styles
- **Professional Output**: Clean, aligned status displays and progress tracking
- **Automated Setup Scripts**: One-click installation for all supported platforms
- **Enhanced Metadata**: Rich XMP sidecar files with quality and technical analysis
- **Resume Capability**: Interrupted processing can be safely resumed
- **Batch Processing**: Efficient handling of large photo collections
- **Quality Tags**: Automatic tagging based on technical analysis
- **Concert Tags**: Specialized tags for stage lighting, motion, and venue characteristics
- **Low Light Optimization**: Special handling for concert and challenging lighting conditions
- **Venue Analysis**: Automatic detection of venue size and atmosphere
- **Motion Analysis**: Differentiate between artistic motion blur and technical issues
- **Exposure Optimization**: Concert-specific exposure tolerance and analysis
- **Multi-Format Support**: Enhanced support for modern camera RAW formats
- **Progress Tracking**: Detailed processing statistics and quality metrics
- **Error Recovery**: Robust error handling and detailed logging
- **Memory Management**: Efficient processing of high-resolution images
- **Documentation**: Comprehensive setup guides and usage examples

### Technical Specifications
- **Python**: 3.9+ required
- **AI Model**: llava:7b (local processing)
- **RAW Processing**: rawpy library integration
- **Computer Vision**: OpenCV for advanced image analysis
- **Metadata**: ExifTool integration for comprehensive metadata handling
- **Cross-Platform**: Native support for Windows, Linux, and macOS
- **Performance**: ~400 photos/hour processing rate
- **Memory**: Optimized for large collections with efficient memory usage

### Quality Control Features
- **Blur Detection**: Laplacian variance method with configurable thresholds
- **Histogram Analysis**: Comprehensive exposure and contrast assessment
- **Quality Metrics**: Technical quality scoring and classification
- **Artistic Recognition**: Distinguishes artistic choices from technical issues
- **Concert Optimization**: Specialized analysis for live music photography
- **Threshold Configuration**: Adjustable quality standards for different workflows

### Concert Photography Features
- **Stage Lighting**: Automatic detection and classification
- **Motion Analysis**: Artistic motion blur vs. camera shake detection
- **Crowd Detection**: Audience and venue atmosphere analysis
- **Low Light**: Specialized processing for challenging lighting conditions
- **Venue Classification**: Automatic venue size and type detection
- **Performance Analysis**: Musical performance and energy detection

### Platform Support
- **Windows**: Full compatibility with automated setup and batch scripts
- **Linux**: Support for Ubuntu, Debian, CentOS, Fedora, and Arch Linux
- **macOS**: Native support with Homebrew integration and Apple Silicon optimization

### Dependencies
- **Core**: ollama, pillow, numpy, opencv-python, rawpy
- **Optional**: exifread for enhanced metadata parsing
- **Development**: pytest, black, flake8, isort for development workflow

### Known Issues
- **Large Collections**: Memory usage may increase with very large photo collections
- **Network**: Initial setup requires internet connection for AI model download
- **Storage**: XMP sidecar files increase storage requirements

### Migration
- **From v2.0**: Completely separate installation, no migration required
- **Configuration**: New configuration system with enhanced options
- **Compatibility**: XMP files compatible with Lightroom and other photo managers

## [2.0.0] - 2025-07-17

### Added
- Smart folder discovery and interactive selection
- Enhanced .ARW support with rawpy integration
- Progress tracking and resume capability
- Professional output formatting
- PIL warning suppression for large images
- Confirmation prompts and error handling

### Fixed
- Sony .ARW file processing issues
- Large image handling without warnings
- Progress file corruption issues
- Cross-platform path handling

## [1.0.0] - 2025-07-16

### Added
- Initial release with basic AI photo tagging
- Support for common image formats
- XMP sidecar file generation
- Basic progress tracking
- Ollama integration for local AI processing

---

## Contributors

### Core Development
- **@tca**: Project creator and lead developer
- **@claude-ai**: AI assistant for development and documentation

### Special Thanks
- **Concert Photography Community**: Feature testing and feedback
- **Sony A7C Users**: RAW processing optimization
- **Cross-Platform Testers**: Windows, Linux, and macOS validation

### Photography Expertise
- **Concert Photographers**: Stage lighting and motion blur analysis
- **Quality Control Specialists**: Image analysis and technical assessment
- **RAW Processing Experts**: Enhanced file format support

---

## Versioning

This project uses [Semantic Versioning](https://semver.org/):
- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality in a backwards compatible manner
- **PATCH**: Backwards compatible bug fixes

## Support

For questions, issues, or contributions:
- **Issues**: [GitHub Issues](https://github.com/your-username/ai-photo-tagger/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/ai-photo-tagger/discussions)
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)
