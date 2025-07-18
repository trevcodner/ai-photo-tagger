# Contributing to AI Photo Tagger v3.0

We welcome contributions from the photography and developer communities! This document provides guidelines for contributing to the project.

## 🤝 How to Contribute

### Reporting Issues
- Use the [GitHub Issues](https://github.com/trevcodner/ai-photo-tagger/issues) page
- Search existing issues before creating new ones
- Include detailed reproduction steps
- Provide system information (OS, Python version, etc.)
- Include sample photos if relevant (without personal content)

### Suggesting Features
- Use [GitHub Discussions](https://github.com/trevcodner/ai-photo-tagger/discussions) for feature requests
- Describe the photography workflow problem you're solving
- Provide examples of how the feature would be used
- Consider cross-platform compatibility

### Submitting Code
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 🔧 Development Setup

### Prerequisites
- Python 3.9+
- Git
- A photo collection for testing

### Setup Steps
```bash
# Clone your fork
git clone https://github.com/trevcodner/ai-photo-tagger.git
cd ai-photo-tagger

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Install Ollama and model
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull llava:7b

# Run tests
pytest tests/
```

## 📝 Coding Standards

### Python Code Style
- Follow PEP 8
- Use type hints where appropriate
- Maximum line length: 88 characters (Black formatter)
- Use descriptive variable names
- Add docstrings for all public functions and classes

### Code Formatting
```bash
# Format code with Black
black ai_photo_tagger_v3.py

# Sort imports
isort ai_photo_tagger_v3.py

# Check with flake8
flake8 ai_photo_tagger_v3.py
```

### Testing
- Write tests for new features
- Ensure existing tests pass
- Test on multiple platforms if possible
- Include edge cases and error handling

## 🎯 Focus Areas

### High Priority
- **Performance Optimization**: Faster processing for large collections
- **Memory Management**: Efficient handling of high-resolution images
- **Error Handling**: Robust error recovery and reporting
- **Cross-Platform**: Windows, Linux, macOS compatibility

### Concert Photography Features
- **Venue Recognition**: Automatic venue identification
- **Instrument Detection**: Specific musical instrument tagging
- **Lighting Analysis**: Advanced stage lighting classification
- **Crowd Dynamics**: Audience energy and size analysis

### Quality Control Enhancement
- **Noise Analysis**: High ISO noise detection and rating
- **Composition Analysis**: Rule of thirds, leading lines, etc.
- **Color Analysis**: Color temperature and saturation assessment
- **Artistic Filters**: Distinguish artistic choices from technical issues

## 🧪 Testing Guidelines

### Test Categories
- **Unit Tests**: Individual function testing
- **Integration Tests**: Component interaction testing
- **End-to-End Tests**: Complete workflow testing
- **Performance Tests**: Speed and memory usage testing

### Test Data
- Use synthetic test images when possible
- Include various formats: JPG, PNG, RAW files
- Test with different image sizes and qualities
- Respect privacy - no personal photos in test data

### Platform Testing
- Test on Windows, Linux, and macOS
- Verify setup scripts work correctly
- Test with different Python versions (3.9, 3.10, 3.11)
- Validate cross-platform path handling

## 📋 Pull Request Guidelines

### Before Submitting
- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] Documentation updated if needed
- [ ] Commit messages are clear and descriptive
- [ ] No merge conflicts with main branch

### Pull Request Description
Include:
- **Purpose**: What problem does this solve?
- **Changes**: What was modified?
- **Testing**: How was it tested?
- **Screenshots**: For UI changes
- **Breaking Changes**: Any compatibility issues?

### Review Process
- Maintainers will review within 48 hours
- Address feedback promptly
- Keep discussions constructive and respectful
- Be open to suggestions and improvements

## 🎯 Photography Expertise Welcome

We especially welcome contributions from photographers who understand:
- **Concert Photography**: Stage lighting, motion, crowd dynamics
- **Wedding Photography**: Event flow, lighting challenges
- **Street Photography**: Candid moments, urban environments
- **Wildlife Photography**: Motion blur, tracking, telephoto challenges
- **Portrait Photography**: Lighting, composition, expression analysis

## 🌟 Recognition

Contributors are recognized in:
- **README.md**: Contributor section
- **CHANGELOG.md**: Feature attribution
- **GitHub**: Contributor graph and statistics
- **Documentation**: Author credits where appropriate

## 💡 Ideas for Contributions

### Easy First Issues
- **Documentation**: Improve setup guides
- **Translations**: Multi-language support
- **Bug Fixes**: Address reported issues
- **Examples**: Add usage examples

### Medium Complexity
- **New Quality Metrics**: Add analysis features
- **Performance**: Optimize processing speed
- **UI Improvements**: Better status displays
- **Configuration**: More user options

### Advanced Projects
- **Machine Learning**: Custom model training
- **Database Integration**: Photo management systems
- **Cloud Processing**: Remote AI processing
- **Mobile App**: Companion mobile application

## 🔒 Security

### Reporting Security Issues
- **DO NOT** create public issues for security problems
- Email security concerns to: security@[domain]
- Include detailed reproduction steps
- We'll respond within 24 hours

### Privacy Considerations
- Never commit personal photos to the repository
- Respect user privacy in data collection
- Document data handling practices
- Ensure secure local processing

## 📚 Resources

### Photography Resources
- [Digital Photography School](https://digital-photography-school.com/)
- [PetaPixel](https://petapixel.com/)
- [Concert Photography Community](https://www.facebook.com/groups/concertphotography/)

### Development Resources
- [Python Photography Libraries](https://github.com/topics/photography)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Pillow Documentation](https://pillow.readthedocs.io/)

### AI/ML Resources
- [Ollama Documentation](https://ollama.ai/docs)
- [Computer Vision Tutorials](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
- [rawpy Documentation](https://rawpy.readthedocs.io/)

## 🏆 Hall of Fame

Special thanks to contributors who have made significant impacts:

- **Concert Photographers**: Feature testing and feedback
- **RAW Processing Experts**: Enhanced file format support
- **Cross-Platform Developers**: Windows, Linux, macOS compatibility
- **Quality Control Specialists**: Advanced image analysis

## 📞 Contact

- **General Questions**: [GitHub Discussions](https://github.com/your-username/ai-photo-tagger/discussions)
- **Bug Reports**: [GitHub Issues](https://github.com/your-username/ai-photo-tagger/issues)
- **Feature Requests**: [GitHub Discussions](https://github.com/your-username/ai-photo-tagger/discussions)
- **Security Issues**: security@[domain]

---

Thank you for contributing to AI Photo Tagger v3.0! Together, we're building the future of automated photo management for photographers worldwide. 📸✨
