# Security Policy

## Supported Versions

We actively support the following versions of AI Photo Tagger:

| Version | Supported          |
| ------- | ------------------ |
| 3.0.x   | :white_check_mark: |
| 2.0.x   | :white_check_mark: |
| 1.0.x   | :x:                |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability, please follow these steps:

### 1. Do Not Create Public Issues

**DO NOT** create public GitHub issues for security vulnerabilities. This could put users at risk.

### 2. Contact Us Privately

Email security concerns to: **security@[your-domain]** (replace with your actual email)

Include:
- Detailed description of the vulnerability
- Steps to reproduce the issue
- Potential impact assessment
- Suggested fixes (if any)

### 3. Response Timeline

- **24 hours**: Initial response acknowledging receipt
- **7 days**: Preliminary assessment of the issue
- **30 days**: Security patch or mitigation plan
- **Public disclosure**: After fix is released and users have time to update

### 4. Responsible Disclosure

We follow responsible disclosure practices:
- We will work with you to verify and address the issue
- We will credit you (if desired) when the issue is resolved
- We ask that you do not publicly disclose the issue until we have had a chance to address it

## Security Considerations

### Local Processing
- **AI Processing**: All AI analysis happens locally on your machine
- **No Cloud Data**: Photos never leave your computer
- **Privacy**: No personal data is transmitted to external services

### Dependencies
- **Ollama**: Local AI service, no external API calls
- **rawpy**: Local RAW file processing
- **OpenCV**: Local image analysis
- **Pillow**: Local image manipulation

### File System Access
- **Read Access**: Application reads photos from specified directories
- **Write Access**: Creates XMP sidecar files and log files
- **No Network**: No network access required after initial setup

### Potential Risks
- **File System**: Application has access to photo directories
- **Metadata**: XMP files contain keywords and analysis data
- **Log Files**: Processing logs may contain file paths

### Mitigation Strategies
- **Sandboxing**: Run in isolated environment if concerned
- **Permissions**: Limit file system access to photo directories only
- **Review**: Inspect XMP files before sharing
- **Logs**: Review log files for sensitive information

## Security Best Practices

### For Users
- **Backup**: Always backup photos before processing
- **Permissions**: Run with minimal required permissions
- **Updates**: Keep application and dependencies updated
- **Review**: Check generated XMP files before sharing

### For Developers
- **Input Validation**: Validate all file paths and inputs
- **Error Handling**: Avoid exposing sensitive information in errors
- **Dependencies**: Keep all dependencies updated
- **Testing**: Regular security testing and code review

## Known Security Considerations

### File Path Handling
- **Directory Traversal**: Application validates file paths to prevent directory traversal attacks
- **Symbolic Links**: Handles symbolic links safely
- **Permissions**: Respects file system permissions

### Memory Management
- **Large Files**: Handles large image files without memory exhaustion
- **Cleanup**: Properly cleans up temporary files and memory
- **Limits**: Implements reasonable limits on file sizes and processing

### External Dependencies
- **Ollama**: Local AI service with no external network access
- **ExifTool**: Trusted metadata manipulation tool
- **Python Libraries**: Well-maintained libraries with security track record

## Vulnerability Categories

### High Priority
- **Remote Code Execution**: Any ability to execute arbitrary code
- **Path Traversal**: Accessing files outside intended directories
- **Data Exfiltration**: Unintended transmission of user data
- **Privilege Escalation**: Gaining higher system privileges

### Medium Priority
- **Denial of Service**: Causing application crashes or system instability
- **Information Disclosure**: Leaking sensitive information in logs or metadata
- **Input Validation**: Improper handling of malformed files

### Low Priority
- **Documentation Issues**: Missing or incorrect security documentation
- **Configuration**: Insecure default configurations
- **Logging**: Overly verbose logging that might expose information

## Security Updates

### Distribution
- **GitHub Releases**: Security updates distributed through GitHub releases
- **Notifications**: Security advisories posted to GitHub Security tab
- **Changelog**: All security fixes documented in CHANGELOG.md

### Installation
- **Update Script**: Automated update scripts for all platforms
- **Manual Update**: Manual update instructions for each platform
- **Verification**: Checksums and signatures for release verification

## Contact Information

For security-related questions or concerns:
- **Email**: security@[your-domain]
- **PGP Key**: [Public key for encrypted communications]
- **Response Time**: 24 hours for initial response

For general questions:
- **GitHub Issues**: Public issues for non-security questions
- **GitHub Discussions**: Community discussions and feature requests

---

**Note**: This security policy is a living document and may be updated as the project evolves. Please check back regularly for updates.
