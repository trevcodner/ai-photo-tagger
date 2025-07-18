#!/bin/bash
# AI Photo Tagger v3.0 - Linux Setup Script
# Supports Ubuntu, Debian, CentOS, RHEL, Fedora, Arch Linux

set -e  # Exit on any error

echo "================================================"
echo "   AI Photo Tagger v3.0 - Linux Setup Script"
echo "================================================"
echo

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Helper functions
print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Detect Linux distribution
detect_distro() {
    if [[ -f /etc/os-release ]]; then
        . /etc/os-release
        DISTRO=$ID
        VERSION=$VERSION_ID
    elif [[ -f /etc/redhat-release ]]; then
        DISTRO="rhel"
    elif [[ -f /etc/debian_version ]]; then
        DISTRO="debian"
    else
        DISTRO="unknown"
    fi
    
    echo "Detected distribution: $DISTRO"
}

# Install system dependencies
install_system_deps() {
    echo "[1/6] Installing system dependencies..."
    
    case $DISTRO in
        ubuntu|debian)
            sudo apt-get update
            sudo apt-get install -y python3 python3-pip python3-venv curl wget exiftool
            print_success "System dependencies installed (apt)"
            ;;
        fedora)
            sudo dnf install -y python3 python3-pip curl wget perl-Image-ExifTool
            print_success "System dependencies installed (dnf)"
            ;;
        centos|rhel)
            sudo yum install -y python3 python3-pip curl wget
            # ExifTool might need EPEL repository
            sudo yum install -y epel-release
            sudo yum install -y perl-Image-ExifTool
            print_success "System dependencies installed (yum)"
            ;;
        arch|manjaro)
            sudo pacman -S --noconfirm python python-pip curl wget perl-image-exiftool
            print_success "System dependencies installed (pacman)"
            ;;
        *)
            print_warning "Unknown distribution. Please install manually:"
            echo "  - Python 3.9+"
            echo "  - pip3"
            echo "  - curl"
            echo "  - exiftool"
            read -p "Continue anyway? (y/n): " -n 1 -r
            echo
            if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                exit 1
            fi
            ;;
    esac
}

# Check Python version
check_python() {
    echo "[2/6] Checking Python version..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
        echo "Python version: $PYTHON_VERSION"
        
        if python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3,9) else 1)'; then
            print_success "Python 3.9+ is installed"
        else
            print_error "Python 3.9+ required, found $PYTHON_VERSION"
            exit 1
        fi
    else
        print_error "Python 3 not found"
        exit 1
    fi
}

# Install Python dependencies
install_python_deps() {
    echo "[3/6] Installing Python dependencies..."
    echo "This may take several minutes..."
    
    # Create virtual environment (optional but recommended)
    if [[ "$1" == "--venv" ]]; then
        python3 -m venv ai_photo_tagger_env
        source ai_photo_tagger_env/bin/activate
        echo "Created virtual environment"
    fi
    
    # Install dependencies
    pip3 install --upgrade pip
    pip3 install ollama pillow opencv-python rawpy numpy
    
    if [[ $? -eq 0 ]]; then
        print_success "Python dependencies installed"
    else
        print_error "Failed to install Python dependencies"
        print_warning "Try installing individually:"
        echo "  pip3 install ollama"
        echo "  pip3 install pillow"
        echo "  pip3 install opencv-python"
        echo "  pip3 install rawpy"
        echo "  pip3 install numpy"
        exit 1
    fi
}

# Install Ollama
install_ollama() {
    echo "[4/6] Installing Ollama..."
    
    if command -v ollama &> /dev/null; then
        print_success "Ollama already installed"
    else
        echo "Downloading and installing Ollama..."
        curl -fsSL https://ollama.ai/install.sh | sh
        
        if [[ $? -eq 0 ]]; then
            print_success "Ollama installed"
        else
            print_error "Failed to install Ollama"
            echo "Please install manually from: https://ollama.ai/download"
            exit 1
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
        print_warning "ExifTool not found"
        echo "ExifTool is optional but recommended for DNG embedding"
        echo "Install with your package manager:"
        echo "  Ubuntu/Debian: sudo apt-get install exiftool"
        echo "  Fedora: sudo dnf install perl-Image-ExifTool"
        echo "  CentOS/RHEL: sudo yum install perl-Image-ExifTool"
        echo "  Arch: sudo pacman -S perl-image-exiftool"
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
# AI Photo Tagger v3.0 - Concert Mode
echo "Starting AI Photo Tagger v3.0 in Concert Mode..."
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

echo "Concert mode processing complete!"
EOF
    
    chmod +x run_concert_mode.sh
    
    # Regular mode script
    cat > run_regular_mode.sh << 'EOF'
#!/bin/bash
# AI Photo Tagger v3.0 - Regular Mode
echo "Starting AI Photo Tagger v3.0..."
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
    --quality-check

echo "Processing complete!"
EOF
    
    chmod +x run_regular_mode.sh
    
    print_success "Created example scripts"
}

# Main setup function
main() {
    echo "This script will install AI Photo Tagger v3.0 and its dependencies."
    echo "You may be prompted for your password (sudo) during installation."
    echo
    read -p "Continue? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Setup cancelled."
        exit 1
    fi
    
    # Run setup steps
    detect_distro
    install_system_deps
    check_python
    install_python_deps $1
    install_ollama
    check_exiftool
    setup_ai_model
    create_examples
    
    echo
    echo "================================================"
    echo "   🎉 SETUP COMPLETE!"
    echo "================================================"
    echo
    echo "Next steps:"
    echo "1. Download AI_Photo_Tagger_v3_Enhanced.py to this directory"
    echo "2. For concert photography: ./run_concert_mode.sh"
    echo "3. For regular use: ./run_regular_mode.sh"
    echo "4. Or run manually: python3 AI_Photo_Tagger_v3_Enhanced.py --help"
    echo
    echo "Examples:"
    echo "  Concert mode: ./run_concert_mode.sh"
    echo "  Regular mode: ./run_regular_mode.sh"
    echo "  Custom folder: python3 AI_Photo_Tagger_v3_Enhanced.py --folder /path/to/photos"
    echo
    print_success "Setup successful! Happy photo tagging!"
}

# Handle command line arguments
if [[ "$1" == "--help" ]]; then
    echo "AI Photo Tagger v3.0 - Linux Setup Script"
    echo
    echo "Usage: $0 [OPTIONS]"
    echo
    echo "Options:"
    echo "  --venv     Create a Python virtual environment"
    echo "  --help     Show this help message"
    echo
    echo "This script will install:"
    echo "  - System dependencies (Python, pip, ExifTool)"
    echo "  - Ollama AI service"
    echo "  - Python packages (ollama, pillow, opencv-python, rawpy, numpy)"
    echo "  - AI model (llava:7b)"
    echo
    exit 0
fi

# Run main setup
main $1
