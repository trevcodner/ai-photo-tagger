#!/usr/bin/env python3
"""
AI Photo Tagger v3.0 - Enhanced Quality Control & Cross-Platform
NEW VERSION - Does not modify existing v2.0 script

Features:
- Quality Control: Blur detection, histogram analysis, exposure issues
- Cross-platform: Windows/Linux/macOS support
- Concert Photography: Stage lighting, motion blur, crowd detection
- Enhanced .ARW support with rawpy
- Professional output formatting
- Configurable quality thresholds

Author: Created with Claude AI assistance
License: MIT
"""

import os
import sys
import json
import time
import logging
import argparse
import subprocess
import platform
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageStat
import numpy as np
import cv2

# Configure PIL for large photo processing
import warnings
from PIL import ImageFile

Image.MAX_IMAGE_PIXELS = 200000000
ImageFile.LOAD_TRUNCATED_IMAGES = True
warnings.filterwarnings("ignore", category=Image.DecompressionBombWarning)

import ollama
from typing import List, Dict, Optional, Tuple

# Enhanced RAW support
try:
    import rawpy
    HAS_RAWPY = True
    print("✅ rawpy available - Enhanced .ARW support enabled")
except ImportError:
    HAS_RAWPY = False
    print("⚠️  rawpy not available - install with: pip install rawpy")

# Quality analysis support
try:
    import cv2
    HAS_CV2 = True
    print("✅ OpenCV available - Quality analysis enabled")
except ImportError:
    HAS_CV2 = False
    print("⚠️  OpenCV not available - install with: pip install opencv-python")

# Configuration
DEFAULT_CONFIG = {
    "pictures_folder": Path.home() / "Pictures",
    "ollama_model": "llava:7b",
    "supported_formats": {".jpg", ".jpeg", ".png", ".tiff", ".tif", ".dng", ".cr2", ".nef", ".arw", ".orf", ".rw2"},
    "max_image_size": 1024,
    "batch_size": 5,
    "max_tags": 8,
    "delay_between_batches": 3,
    "embed_in_dng": True,
    "quality_control": {
        "check_blur": True,
        "check_histogram": True,
        "check_exposure": True,
        "blur_threshold": 100.0,  # Lower = more blurry
        "histogram_balance_threshold": 0.8,  # Histogram balance
        "exposure_threshold": 0.1,  # Under/over exposure
    },
    "concert_mode": {
        "enabled": False,
        "detect_stage_lighting": True,
        "detect_motion_blur": True,
        "detect_crowd": True,
        "low_light_threshold": 50,
    },
    "ai_prompt": "Analyze this image and provide exactly 6-8 essential keywords only. Focus on the most important elements: main subject, key action, setting, mood. Use single words or simple phrases. Separate with commas. Be concise and avoid overly specific details. Example: 'woman, portrait, smiling, indoor, casual, natural'.",
}

class QualityAnalyzer:
    """Advanced quality analysis for photos"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.quality_config = config.get("quality_control", {})
        self.concert_config = config.get("concert_mode", {})
        
    def analyze_blur(self, image_path: Path) -> Tuple[float, str]:
        """Analyze image blur using Laplacian variance"""
        if not HAS_CV2:
            return 0.0, "unknown"
            
        try:
            # Read image
            img = cv2.imread(str(image_path))
            if img is None:
                return 0.0, "error"
                
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Calculate Laplacian variance
            laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
            
            # Determine blur level
            threshold = self.quality_config.get("blur_threshold", 100.0)
            if laplacian_var < threshold / 4:
                return laplacian_var, "very_blurry"
            elif laplacian_var < threshold / 2:
                return laplacian_var, "blurry"
            elif laplacian_var < threshold:
                return laplacian_var, "slightly_blurry"
            else:
                return laplacian_var, "sharp"
                
        except Exception as e:
            return 0.0, "error"
    
    def analyze_histogram(self, image_path: Path) -> Tuple[Dict, str]:
        """Analyze histogram for exposure and color balance"""
        try:
            with Image.open(image_path) as img:
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Calculate histogram
                hist_r = img.histogram()[0:256]
                hist_g = img.histogram()[256:512]
                hist_b = img.histogram()[512:768]
                
                # Calculate statistics
                total_pixels = sum(hist_r)
                
                # Check for clipping (under/over exposure)
                underexposed = (hist_r[0] + hist_g[0] + hist_b[0]) / (total_pixels * 3)
                overexposed = (hist_r[255] + hist_g[255] + hist_b[255]) / (total_pixels * 3)
                
                # Calculate histogram spread
                def calculate_spread(hist):
                    first_nonzero = next((i for i, x in enumerate(hist) if x > 0), 0)
                    last_nonzero = next((i for i, x in enumerate(reversed(hist)) if x > 0), 0)
                    return (255 - last_nonzero - first_nonzero) / 255
                
                spread_r = calculate_spread(hist_r)
                spread_g = calculate_spread(hist_g)
                spread_b = calculate_spread(hist_b)
                avg_spread = (spread_r + spread_g + spread_b) / 3
                
                # Determine quality
                exposure_threshold = self.quality_config.get("exposure_threshold", 0.1)
                quality = "good"
                
                if underexposed > exposure_threshold:
                    quality = "underexposed"
                elif overexposed > exposure_threshold:
                    quality = "overexposed"
                elif avg_spread < 0.5:
                    quality = "low_contrast"
                
                return {
                    "underexposed": underexposed,
                    "overexposed": overexposed,
                    "spread": avg_spread,
                    "quality": quality
                }, quality
                
        except Exception as e:
            return {}, "error"
    
    def analyze_concert_specific(self, image_path: Path) -> Dict:
        """Concert photography specific analysis"""
        if not self.concert_config.get("enabled", False):
            return {}
            
        try:
            with Image.open(image_path) as img:
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Convert to array for analysis
                img_array = np.array(img)
                
                # Stage lighting detection (high contrast, colored lights)
                stage_lighting = self.detect_stage_lighting(img_array)
                
                # Motion blur detection (specific patterns)
                motion_blur = self.detect_motion_blur(img_array)
                
                # Crowd detection (lots of faces/people)
                crowd_detected = self.detect_crowd_elements(img_array)
                
                return {
                    "stage_lighting": stage_lighting,
                    "motion_blur": motion_blur,
                    "crowd_detected": crowd_detected,
                    "low_light": np.mean(img_array) < self.concert_config.get("low_light_threshold", 50)
                }
                
        except Exception as e:
            return {"error": str(e)}
    
    def detect_stage_lighting(self, img_array: np.ndarray) -> bool:
        """Detect stage lighting patterns"""
        # Look for high contrast and color saturation typical of stage lights
        brightness = np.mean(img_array)
        contrast = np.std(img_array)
        
        # Stage lighting typically has high contrast and moderate brightness
        return contrast > 60 and 30 < brightness < 200
    
    def detect_motion_blur(self, img_array: np.ndarray) -> str:
        """Detect motion blur patterns"""
        if not HAS_CV2:
            return "unknown"
            
        # Convert to grayscale
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        
        # Use different blur detection for motion vs camera shake
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        
        # Motion blur tends to be directional
        x_var = np.var(sobelx)
        y_var = np.var(sobely)
        
        if max(x_var, y_var) / min(x_var, y_var) > 2:
            return "motion_blur"
        elif x_var < 100 and y_var < 100:
            return "camera_shake"
        else:
            return "sharp"
    
    def detect_crowd_elements(self, img_array: np.ndarray) -> bool:
        """Detect crowd/audience elements"""
        # Simple crowd detection based on texture and patterns
        # This is a simplified version - could be enhanced with face detection
        
        # Look for repetitive patterns typical of crowds
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY) if HAS_CV2 else img_array.mean(axis=2)
        
        # High texture variance often indicates crowds
        texture_variance = np.var(gray)
        return texture_variance > 1000  # Threshold for crowd-like texture

class EnhancedPhotoTagger:
    """Enhanced photo tagger with quality control"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.quality_analyzer = QualityAnalyzer(config)
        self.setup_logging()
        self.setup_progress_tracking()
        self.check_dependencies()
        
    def setup_logging(self):
        """Setup logging configuration"""
        log_file = self.config["pictures_folder"] / "ai_photo_tagger_v3.log"
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def setup_progress_tracking(self):
        """Initialize progress tracking"""
        self.progress_file = self.config["pictures_folder"] / "ai_photo_tagger_v3_progress.json"
        self.processed_count = 0
        self.skipped_count = 0
        self.error_count = 0
        self.quality_issues = 0
        self.start_time = datetime.now()
        self.progress = self.load_progress()
        
    def load_progress(self) -> Dict:
        """Load progress from previous sessions"""
        if self.progress_file.exists():
            try:
                with open(self.progress_file, 'r') as f:
                    progress = json.load(f)
                    progress["processed_files"] = set(progress.get("processed_files", []))
                    return progress
            except:
                pass
        return {"processed_files": set(), "last_processed": None}
        
    def save_progress(self):
        """Save current progress"""
        progress_data = {
            "processed_files": list(self.progress["processed_files"]),
            "last_processed": self.progress["last_processed"],
            "session_stats": {
                "processed": self.processed_count,
                "skipped": self.skipped_count,
                "errors": self.error_count,
                "quality_issues": self.quality_issues,
                "session_start": self.start_time.isoformat()
            }
        }
        with open(self.progress_file, 'w') as f:
            json.dump(progress_data, f, indent=2)
            
    def check_dependencies(self):
        """Check if required dependencies are available"""
        print()
        print("=" * 70)
        print("  🔍 ENHANCED PHOTO TAGGER v3.0 - SYSTEM CHECK  ".center(70))
        print("=" * 70)
        
        # Platform info
        print(f"🖥️  Platform ................................ {platform.system()} {platform.release()}")
        
        # Check Ollama
        try:
            ollama.list()
            print("✅ Ollama Service .......................... RUNNING")
        except Exception as e:
            print("❌ Ollama Service .......................... NOT RUNNING")
            print("   Please install Ollama and run: ollama serve")
            sys.exit(1)
            
        # Check model
        try:
            models = ollama.list()
            available_models = [m['model'] for m in models['models']]
            if self.config["ollama_model"] not in available_models:
                print(f"❌ AI Model ({self.config['ollama_model']}) ............... NOT FOUND")
                print(f"   Install with: ollama pull {self.config['ollama_model']}")
                sys.exit(1)
            print(f"✅ AI Model ({self.config['ollama_model']}) ................... AVAILABLE")
        except Exception as e:
            print(f"❌ Error checking models: {e}")
            sys.exit(1)
            
        # Check ExifTool
        exiftool_cmd = "exiftool.exe" if platform.system() == "Windows" else "exiftool"
        try:
            result = subprocess.run([exiftool_cmd, '-ver'], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ ExifTool (v{result.stdout.strip()}) ...................... INSTALLED")
            else:
                print("⚠️  ExifTool ............................... NOT FOUND")
                self.config["embed_in_dng"] = False
        except FileNotFoundError:
            print("⚠️  ExifTool ............................... NOT FOUND")
            self.config["embed_in_dng"] = False
            
        # Check quality analysis capabilities
        if HAS_CV2:
            print("✅ Quality Analysis (OpenCV) ............... ENABLED")
        else:
            print("⚠️  Quality Analysis ....................... DISABLED")
            print("   Install with: pip install opencv-python")
            
        # Check concert mode
        if self.config.get("concert_mode", {}).get("enabled", False):
            print("🎵 Concert Mode ............................ ENABLED")
        else:
            print("🎵 Concert Mode ............................ DISABLED")
            
        print("=" * 70)
        
    def open_image_enhanced(self, image_path: Path) -> Optional[Image.Image]:
        """Open image with enhanced RAW support"""
        try:
            # RAW file handling
            if (image_path.suffix.lower() in {'.arw', '.cr2', '.nef', '.orf', '.rw2'} and HAS_RAWPY):
                with rawpy.imread(str(image_path)) as raw:
                    rgb = raw.postprocess(
                        demosaic_algorithm=rawpy.DemosaicAlgorithm.AHD,
                        half_size=False,
                        use_camera_wb=True,
                        output_color=rawpy.ColorSpace.sRGB,
                        gamma=(2.2, 4.5),
                        bright=1.0,
                    )
                    return Image.fromarray(rgb)
            
            # Standard image handling
            with Image.open(image_path) as img:
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                return img.copy()
                
        except Exception as e:
            self.logger.error(f"Error opening {image_path}: {e}")
            return None
            
    def analyze_photo_quality(self, image_path: Path) -> Dict:
        """Perform comprehensive quality analysis"""
        quality_results = {}
        
        if self.config.get("quality_control", {}).get("check_blur", False):
            blur_score, blur_level = self.quality_analyzer.analyze_blur(image_path)
            quality_results["blur"] = {"score": blur_score, "level": blur_level}
            
        if self.config.get("quality_control", {}).get("check_histogram", False):
            hist_data, hist_quality = self.quality_analyzer.analyze_histogram(image_path)
            quality_results["histogram"] = hist_data
            quality_results["histogram"]["quality"] = hist_quality
            
        # Concert-specific analysis
        if self.config.get("concert_mode", {}).get("enabled", False):
            concert_analysis = self.quality_analyzer.analyze_concert_specific(image_path)
            quality_results["concert"] = concert_analysis
            
        return quality_results
        
    def generate_quality_tags(self, quality_results: Dict) -> List[str]:
        """Generate quality-related tags"""
        tags = []
        
        # Blur tags
        if "blur" in quality_results:
            blur_level = quality_results["blur"]["level"]
            if blur_level in ["very_blurry", "blurry"]:
                tags.append(f"quality:{blur_level}")
                
        # Histogram tags
        if "histogram" in quality_results:
            hist_quality = quality_results["histogram"]["quality"]
            if hist_quality != "good":
                tags.append(f"exposure:{hist_quality}")
                
        # Concert tags
        if "concert" in quality_results:
            concert_data = quality_results["concert"]
            if concert_data.get("stage_lighting", False):
                tags.append("stage_lighting")
            if concert_data.get("motion_blur", "") == "motion_blur":
                tags.append("motion_blur")
            if concert_data.get("crowd_detected", False):
                tags.append("crowd")
            if concert_data.get("low_light", False):
                tags.append("low_light")
                
        return tags
        
    def get_enhanced_keywords(self, image_path: Path) -> List[str]:
        """Get AI keywords with quality analysis"""
        try:
            # Open image
            img = self.open_image_enhanced(image_path)
            if not img:
                return []
            
            # Perform quality analysis
            quality_results = self.analyze_photo_quality(image_path)
            quality_tags = self.generate_quality_tags(quality_results)
            
            # Check if we should skip due to quality issues
            if quality_results.get("blur", {}).get("level") == "very_blurry":
                self.quality_issues += 1
                print(f"⚠️  Very blurry image detected")
                
            # Resize for AI processing
            if max(img.size) > self.config["max_image_size"]:
                img.thumbnail((self.config["max_image_size"], self.config["max_image_size"]))
                
            # Convert to base64
            from io import BytesIO
            import base64
            buffer = BytesIO()
            img.save(buffer, format="JPEG", quality=85)
            base64_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
            
            # Get AI keywords
            response = ollama.chat(
                model=self.config["ollama_model"],
                messages=[{
                    'role': 'user',
                    'content': self.config["ai_prompt"],
                    'images': [base64_image]
                }],
                options={"temperature": 0.3, "num_predict": 50}
            )
            
            # Parse keywords
            keywords_raw = response['message']['content']
            keywords = []
            for keyword in keywords_raw.split(','):
                cleaned = keyword.strip().lower()
                if cleaned and len(cleaned) > 1 and len(cleaned) < 25:
                    keywords.append(cleaned)
            
            # Combine AI keywords with quality tags
            all_keywords = keywords[:self.config["max_tags"]] + quality_tags
            return all_keywords[:self.config["max_tags"]]
            
        except Exception as e:
            self.logger.error(f"Enhanced keyword processing error for {image_path}: {e}")
            return []
            
    def write_enhanced_xmp(self, image_path: Path, keywords: List[str], quality_data: Dict = None) -> bool:
        """Write enhanced XMP file with quality metadata"""
        xmp_path = image_path.with_suffix(image_path.suffix + '.xmp')
        
        # Build quality metadata
        quality_metadata = ""
        if quality_data:
            quality_metadata = f'''
            <photoshop:Instructions>Quality Analysis: {json.dumps(quality_data)}</photoshop:Instructions>'''
        
        xmp_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Enhanced AI Photo Tagger v3.0">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">
            <dc:subject>
                <rdf:Bag>
{chr(10).join(f'                    <rdf:li>{keyword}</rdf:li>' for keyword in keywords)}
                </rdf:Bag>
            </dc:subject>
            <xmp:CreatorTool>Enhanced AI Photo Tagger v3.0</xmp:CreatorTool>
            <xmp:ModifyDate>{datetime.now().isoformat()}</xmp:ModifyDate>{quality_metadata}
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>'''
        
        try:
            with open(xmp_path, 'w', encoding='utf-8') as f:
                f.write(xmp_content)
            return True
        except Exception as e:
            self.logger.error(f"Error writing enhanced XMP for {image_path}: {e}")
            return False
            
    def process_photo_enhanced(self, photo_path: Path) -> bool:
        """Process photo with enhanced quality analysis"""
        print(f"🎯 Processing: {photo_path.name}")
        
        # Quality analysis
        quality_results = self.analyze_photo_quality(photo_path)
        
        # Get enhanced keywords
        keywords = self.get_enhanced_keywords(photo_path)
        if not keywords:
            print("⚠️  No keywords generated")
            self.skipped_count += 1
            return False
        
        # Write enhanced XMP
        if not self.write_enhanced_xmp(photo_path, keywords, quality_results):
            print("❌ Failed to write enhanced XMP")
            self.error_count += 1
            return False
        
        # Display results
        ai_keywords = [k for k in keywords if not k.startswith(('quality:', 'exposure:'))]
        quality_tags = [k for k in keywords if k.startswith(('quality:', 'exposure:', 'stage_', 'motion_', 'crowd', 'low_light'))]
        
        print(f"✅ AI Tags: {', '.join(ai_keywords[:3])}{'...' if len(ai_keywords) > 3 else ''}")
        if quality_tags:
            print(f"🔍 Quality: {', '.join(quality_tags)}")
        
        # Quality warnings
        if quality_results.get("blur", {}).get("level") in ["very_blurry", "blurry"]:
            print(f"⚠️  Blur detected: {quality_results['blur']['level']}")
        if quality_results.get("histogram", {}).get("quality") != "good":
            print(f"⚠️  Exposure: {quality_results['histogram']['quality']}")
        
        self.processed_count += 1
        self.progress["processed_files"].add(str(photo_path))
        return True
        
    def print_enhanced_status(self):
        """Print enhanced processing status"""
        elapsed = datetime.now() - self.start_time
        hours = elapsed.total_seconds() / 3600
        rate = self.processed_count / hours if hours > 0 else 0
        
        print()
        print("=" * 70)
        print("  📈 ENHANCED PROCESSING STATUS  ".center(70))
        print("=" * 70)
        print(f"✅ Photos Processed ........................ {self.processed_count:,}")
        print(f"🔍 Quality Issues Detected ................. {self.quality_issues:,}")
        print(f"⚠️  Files Skipped .......................... {self.skipped_count:,}")
        print(f"❌ Processing Errors ....................... {self.error_count:,}")
        print(f"⚡ Current Rate ............................ {rate:.1f} photos/hour")
        print(f"🕒 Elapsed Time ............................ {str(elapsed).split('.')[0]}")
        print("=" * 70)

def main():
    """Main function for Enhanced Photo Tagger v3.0"""
    parser = argparse.ArgumentParser(
        description='Enhanced AI Photo Tagger v3.0 with Quality Control',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--folder', type=str, help='Photos folder to process')
    parser.add_argument('--model', type=str, default='llava:7b', help='Ollama model')
    parser.add_argument('--concert-mode', action='store_true', help='Enable concert photography mode')
    parser.add_argument('--quality-check', action='store_true', help='Enable quality analysis')
    parser.add_argument('--blur-threshold', type=float, default=100.0, help='Blur detection threshold')
    
    args = parser.parse_args()
    
    # Configure
    config = DEFAULT_CONFIG.copy()
    if args.folder:
        config["pictures_folder"] = Path(args.folder).expanduser()
    if args.model:
        config["ollama_model"] = args.model
    if args.concert_mode:
        config["concert_mode"]["enabled"] = True
    if args.quality_check:
        config["quality_control"]["check_blur"] = True
        config["quality_control"]["check_histogram"] = True
    if args.blur_threshold:
        config["quality_control"]["blur_threshold"] = args.blur_threshold
    
    # Create and run enhanced tagger
    tagger = EnhancedPhotoTagger(config)
    
    print()
    print("🚀 Enhanced AI Photo Tagger v3.0 ready!")
    print("   New features: Quality control, concert mode, cross-platform support")
    print()
    
    # This is a demo version - full implementation would continue here
    print("✅ Enhanced Photo Tagger v3.0 initialized successfully!")
    print("📝 This is the foundation for the enhanced version with quality control")

if __name__ == "__main__":
    main()
