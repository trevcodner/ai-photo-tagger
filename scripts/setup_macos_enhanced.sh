#!/bin/bash
# AI Photo Tagger v3.0 - macOS Enhanced Setup Script
# For users who want the enhanced version with concert features

set -e  # Exit on any error

echo "================================================"
echo "   AI Photo Tagger v3.0 - macOS Enhanced Setup"
echo "================================================"
echo

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check if Homebrew is installed
check_homebrew() {
    echo "[1/6] Checking Homebrew..."
    if command -v brew &> /dev/null; then
        print_success "Homebrew is installed"
    else
        print_warning "Homebrew not found"
        echo "Installing Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        
        # Add Homebrew to PATH for Apple Silicon Macs
        if [[ $(uname -m) == "arm64" ]]; then
            echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
            eval "$(/opt/homebrew/bin/brew shellenv)"
        else
            echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zshrc
            eval "$(/usr/local/bin/brew shellenv)"
        fi
        
        print_success "Homebrew installed"
    fi
}

# Install system dependencies
install_system_deps() {
    echo "[2/6] Installing system dependencies..."
    brew install python@3.11 exiftool
    print_success "System dependencies installed"
}

# Install Python dependencies
install_python_deps() {
    echo "[3/6] Installing Python dependencies..."
    echo "This may take several minutes..."
    
    # Use Homebrew Python
    pip3 install --upgrade pip
    pip3 install ollama pillow opencv-python rawpy numpy
    
    if [[ $? -eq 0 ]]; then
        print_success "Python dependencies installed"
    else
        print_error "Failed to install Python dependencies"
        echo "Try installing individually if needed"
        exit 1
    fi
}

# Install Ollama
install_ollama() {
    echo "[4/6] Installing Ollama..."
    
    if command -v ollama &> /dev/null; then
        print_success "Ollama already installed"
    else
        # Try Homebrew first
        if brew install ollama 2>/dev/null; then
            print_success "Ollama installed via Homebrew"
        else
            # Fallback to official installer
            curl -fsSL https://ollama.ai/install.sh | sh
            print_success "Ollama installed"
        fi
    fi
}

# Check ExifTool
check_exiftool() {
    echo "[5/6] Checking ExifTool..."
    
    if command -v exiftool &> /dev/null; then
        EXIFTOOL_VERSION=$(exiftool -ver)
        print_success "ExifTool installed (version $EXIFTOOL_VERSION)"
    else
        print_warning "ExifTool not found - installing..."
        brew install exiftool
        print_success "ExifTool installed"
    fi
}

# Download AI model
setup_ai_model() {
    echo "[6/6] Setting up AI model..."
    
    # Start Ollama service
    echo "Starting Ollama service..."
    ollama serve &
    OLLAMA_PID=$!
    
    # Wait for service to start
    echo "Waiting for Ollama to start..."
    sleep 5
    
    # Download model
    echo "Downloading AI model (this may take 10-15 minutes)..."
    ollama pull llava:7b
    
    if [[ $? -eq 0 ]]; then
        print_success "AI model downloaded"
    else
        print_error "Failed to download AI model"
        echo "You can try manually later: ollama pull llava:7b"
    fi
    
    # Stop Ollama service
    kill $OLLAMA_PID 2>/dev/null || true
}

# Create example scripts
create_examples() {
    echo "[BONUS] Creating example scripts..."
    
    # Concert mode script
    cat > run_concert_mode.sh << 'EOF'
#!/bin/bash
# AI Photo Tagger v3.0 - Concert Mode for macOS
echo "🎵 Starting AI Photo Tagger v3.0 in Concert Mode..."
echo

# Start Ollama if not running
if ! pgrep -f "ollama serve" > /dev/null; then
    echo "Starting Ollama service..."
    ollama serve &
    sleep 3
fi

# Run the enhanced tagger
python3 AI_Photo_Tagger_v3_Enhanced.py \
    --folder ~/Pictures \
    --concert-mode \
    --quality-check \
    --blur-threshold 150

echo "🎉 Concert mode processing complete!"
EOF
    
    chmod +x run_concert_mode.sh
    
    # Regular enhanced mode script
    cat > run_enhanced_mode.sh << 'EOF'
#!/bin/bash
# AI Photo Tagger v3.0 - Enhanced Mode for macOS
echo "🎯 Starting AI Photo Tagger v3.0 Enhanced Mode..."
echo

# Start Ollama if not running
if ! pgrep -f "ollama serve" > /dev/null; then
    echo "Starting Ollama service..."
    ollama serve &
    sleep 3
fi

# Run the enhanced tagger with quality control
python3 AI_Photo_Tagger_v3_Enhanced.py \
    --folder ~/Pictures \
    --quality-check \
    --blur-threshold 100

echo "🎉 Enhanced processing complete!"
EOF
    
    chmod +x run_enhanced_mode.sh
    
    # Sony A7C specific script
    cat > run_sony_a7c_mode.sh << 'EOF'
#!/bin/bash
# AI Photo Tagger v3.0 - Sony A7C Optimized Mode
echo "📸 Starting AI Photo Tagger v3.0 for Sony A7C..."
echo "   Enhanced .ARW processing with quality control"
echo

# Start Ollama if not running
if ! pgrep -f "ollama serve" > /dev/null; then
    echo "Starting Ollama service..."
    ollama serve &
    sleep 3
fi

# Run with Sony A7C optimized settings
python3 AI_Photo_Tagger_v3_Enhanced.py \
    --folder ~/Pictures \
    --quality-check \
    --blur-threshold 120

echo "🎉 Sony A7C processing complete!"
EOF
    
    chmod +x run_sony_a7c_mode.sh
    
    print_success "Created example scripts"
}

# Main setup function
main() {
    echo "This script will install AI Photo Tagger v3.0 Enhanced with:"
    echo "  - Quality control (blur detection, histogram analysis)"
    echo "  - Concert photography features"
    echo "  - Enhanced .ARW support"
    echo "  - Cross-platform compatibility"
    echo
    echo "This is separate from your existing v2.0 script."
    echo
    read -p "Continue? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Setup cancelled."
        exit 1
    fi
    
    # Run setup steps
    check_homebrew
    install_system_deps
    install_python_deps
    install_ollama
    check_exiftool
    setup_ai_model
    create_examples
    
    echo
    echo "================================================"
    echo "   🎉 ENHANCED SETUP COMPLETE!"
    echo "================================================"
    echo
    echo "Next steps:"
    echo "1. Download AI_Photo_Tagger_v3_Enhanced.py to this directory"
    echo "2. Choose your mode:"
    echo "   🎵 Concert photography: ./run_concert_mode.sh"
    echo "   📸 Sony A7C optimized: ./run_sony_a7c_mode.sh"
    echo "   🎯 Enhanced general: ./run_enhanced_mode.sh"
    echo
    echo "Features available:"
    echo "  ✅ Blur detection and quality analysis"
    echo "  ✅ Histogram analysis for exposure issues"
    echo "  ✅ Enhanced .ARW support with rawpy"
    echo "  ✅ Concert photography mode"
    echo "  ✅ Cross-platform compatibility"
    echo
    echo "Your existing v2.0 script continues to work unchanged!"
    echo
    print_success "Enhanced setup successful! Happy photo tagging!"
}

# Handle command line arguments
if [[ "$1" == "--help" ]]; then
    echo "AI Photo Tagger v3.0 - macOS Enhanced Setup Script"
    echo
    echo "This script installs the enhanced version with:"
    echo "  - Quality control features"
    echo "  - Concert photography mode"
    echo "  - Enhanced .ARW support"
    echo "  - Cross-platform compatibility"
    echo
    echo "Your existing v2.0 script will continue to work unchanged."
    echo
    exit 0
fi

# Run main setup
main
