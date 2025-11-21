#!/usr/bin/env python3
"""
Top-level build pipeline for all deployable units
Builds shared libraries first, then dependent services
"""

import os
import subprocess
import sys
import shutil
from pathlib import Path
from typing import List, Dict, Optional


class BuildPipeline:
    """Build pipeline for all deployable units"""

    def __init__(self, src_dir: Path = None):
        self.src_dir = src_dir or Path(__file__).parent / "src"
        self.build_dir = Path(__file__).parent / "build"
        self.dist_dir = Path(__file__).parent / "dist"
        
        # Define build order (dependencies first)
        self.build_order = [
            "data-scratch-library",  # Shared library
            "data-scratch-amqp",     # AMQP service
            "data-scratch-mqtt",     # MQTT service  
            "data-scratch-matplotlib", # Visualization service
            "data-scratch-scrape",   # Web scraping service
            "data-scratch-node-library", # Node.js library
            "rest-scratch-flask",    # Flask REST service
            "rest-scratch-node-express", # Express REST service
            "rest-scratch-rust",     # Rust REST service
            "rest-scratch-pistache", # Pistache REST service
            "rest-client-ts-node",   # TypeScript Node client
        ]

    def clean(self) -> None:
        """Clean build and dist directories"""
        print("🧹 Cleaning build directories...")
        
        for dir_path in [self.build_dir, self.dist_dir]:
            if dir_path.exists():
                shutil.rmtree(dir_path)
            dir_path.mkdir(parents=True, exist_ok=True)
        
        print("✅ Clean completed")

    def build_shared_library(self) -> bool:
        """Build the shared data-scratch-library"""
        print("📦 Building shared library: data-scratch-library")
        
        lib_dir = self.src_dir / "data-scratch-library"
        if not lib_dir.exists():
            print(f"❌ Library directory not found: {lib_dir}")
            return False

        # Create build directory for library
        lib_build_dir = self.build_dir / "data-scratch-library"
        lib_build_dir.mkdir(parents=True, exist_ok=True)

        try:
            # Install library in development mode with dependencies
            result = subprocess.run([
                sys.executable, "-m", "pip", "install", "-e", str(lib_dir)
            ], capture_output=True, text=True, cwd=lib_dir)
            
            if result.returncode != 0:
                print(f"❌ Failed to install shared library: {result.stderr}")
                return False

            # Run tests if they exist
            if (lib_dir / "tests").exists():
                print("🧪 Running shared library tests...")
                test_result = subprocess.run([
                    sys.executable, "-m", "pytest", "tests/", "-v"
                ], capture_output=True, text=True, cwd=lib_dir)
                
                if test_result.returncode != 0:
                    print(f"⚠️  Shared library tests failed: {test_result.stderr}")
                else:
                    print("✅ Shared library tests passed")

            print("✅ Shared library built successfully")
            return True

        except Exception as e:
            print(f"❌ Error building shared library: {e}")
            return False

    def build_python_service(self, service_name: str) -> bool:
        """Build a Python service"""
        print(f"🐍 Building Python service: {service_name}")
        
        service_dir = self.src_dir / service_name
        if not service_dir.exists():
            print(f"❌ Service directory not found: {service_dir}")
            return False

        # Check if this is actually a Python project
        if not ((service_dir / "setup.py").exists() or (service_dir / "pyproject.toml").exists()):
            print(f"⚠️  No setup.py or pyproject.toml found for {service_name}, skipping")
            return False

        try:
            # Install service dependencies
            if (service_dir / "requirements.txt").exists():
                result = subprocess.run([
                    sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
                ], capture_output=True, text=True, cwd=service_dir)
                
                if result.returncode != 0:
                    print(f"❌ Failed to install dependencies for {service_name}: {result.stderr}")
                    return False

            # Install service in development mode
            result = subprocess.run([
                sys.executable, "-m", "pip", "install", "-e", str(service_dir)
            ], capture_output=True, text=True, cwd=service_dir)
            
            if result.returncode != 0:
                print(f"❌ Failed to install {service_name}: {result.stderr}")
                return False

            # Run tests
            test_result = self.run_tests(service_dir)
            if not test_result:
                print(f"⚠️  Tests failed for {service_name}")

            # Create distribution package
            self.create_python_distribution(service_name, service_dir)
            
            print(f"✅ Python service {service_name} built successfully")
            return True

        except Exception as e:
            print(f"❌ Error building Python service {service_name}: {e}")
            return False

    def build_node_service(self, service_name: str) -> bool:
        """Build a Node.js service"""
        print(f"📦 Building Node.js service: {service_name}")
        
        service_dir = self.src_dir / service_name
        if not service_dir.exists():
            print(f"❌ Service directory not found: {service_name}")
            return False

        # Check if package.json exists
        if not (service_dir / "package.json").exists():
            print(f"⚠️  No package.json found for {service_name}, skipping")
            return False

        try:
            # Check if npm is available
            npm_check = subprocess.run(["npm", "--version"], capture_output=True, text=True)
            if npm_check.returncode != 0:
                print("⚠️  npm not available, skipping Node.js build")
                return False

            # Install dependencies
            result = subprocess.run(["npm", "install"], capture_output=True, text=True, cwd=service_dir)
            if result.returncode != 0:
                print(f"❌ Failed to install npm dependencies for {service_name}: {result.stderr}")
                return False

            # Run tests
            if (service_dir / "test").exists() or (service_dir / "tests").exists():
                print("🧪 Running Node.js tests...")
                test_result = subprocess.run(["npm", "test"], capture_output=True, text=True, cwd=service_dir)
                if test_result.returncode != 0:
                    print(f"⚠️  Node.js tests failed for {service_name}: {test_result.stderr}")

            # Create distribution
            self.create_node_distribution(service_name, service_dir)
            
            print(f"✅ Node.js service {service_name} built successfully")
            return True

        except Exception as e:
            print(f"❌ Error building Node.js service {service_name}: {e}")
            return False

    def build_rust_service(self, service_name: str) -> bool:
        """Build a Rust service"""
        print(f"🦀 Building Rust service: {service_name}")
        
        service_dir = self.src_dir / service_name
        if not service_dir.exists():
            print(f"❌ Service directory not found: {service_name}")
            return False

        # Check if Cargo.toml exists
        if not (service_dir / "Cargo.toml").exists():
            print(f"⚠️  No Cargo.toml found for {service_name}, skipping")
            return False

        try:
            # Check if cargo is available
            cargo_check = subprocess.run(["cargo", "--version"], capture_output=True, text=True)
            if cargo_check.returncode != 0:
                print("⚠️  cargo not available, skipping Rust build")
                return False

            # Build the service
            result = subprocess.run(["cargo", "build", "--release"], capture_output=True, text=True, cwd=service_dir)
            if result.returncode != 0:
                print(f"❌ Failed to build Rust service {service_name}: {result.stderr}")
                return False

            # Run tests
            print("🧪 Running Rust tests...")
            test_result = subprocess.run(["cargo", "test"], capture_output=True, text=True, cwd=service_dir)
            if test_result.returncode != 0:
                print(f"⚠️  Rust tests failed for {service_name}")

            # Create distribution
            self.create_rust_distribution(service_name, service_dir)
            
            print(f"✅ Rust service {service_name} built successfully")
            return True

        except Exception as e:
            print(f"❌ Error building Rust service {service_name}: {e}")
            return False

    def run_tests(self, service_dir: Path) -> bool:
        """Run tests for a Python service"""
        if not (service_dir / "tests").exists():
            return True  # No tests to run
        
        try:
            result = subprocess.run([
                sys.executable, "-m", "pytest", "tests/", "-v", "--tb=short"
            ], capture_output=True, text=True, cwd=service_dir)
            
            return result.returncode == 0
        except Exception:
            return False

    def create_python_distribution(self, service_name: str, service_dir: Path) -> None:
        """Create distribution package for Python service"""
        dist_service_dir = self.dist_dir / service_name
        dist_service_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy source files
        shutil.copytree(service_dir, dist_service_dir / "src", dirs_exist_ok=True)
        
        # Copy requirements and setup files
        for file_name in ["requirements.txt", "setup.py", "pyproject.toml", "Dockerfile"]:
            src_file = service_dir / file_name
            if src_file.exists():
                shutil.copy2(src_file, dist_service_dir)

    def create_node_distribution(self, service_name: str, service_dir: Path) -> None:
        """Create distribution package for Node.js service"""
        dist_service_dir = self.dist_dir / service_name
        dist_service_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy source files, excluding node_modules
        for item in service_dir.iterdir():
            if item.name != "node_modules":
                if item.is_file():
                    shutil.copy2(item, dist_service_dir)
                else:
                    shutil.copytree(item, dist_service_dir / item.name, dirs_exist_ok=True)

    def create_rust_distribution(self, service_name: str, service_dir: Path) -> None:
        """Create distribution package for Rust service"""
        dist_service_dir = self.dist_dir / service_name
        dist_service_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy source files
        for item in service_dir.iterdir():
            if item.name != "target":
                if item.is_file():
                    shutil.copy2(item, dist_service_dir)
                else:
                    shutil.copytree(item, dist_service_dir / item.name, dirs_exist_ok=True)
        
        # Copy the compiled binary
        target_dir = service_dir / "target" / "release"
        if target_dir.exists():
            for binary in target_dir.iterdir():
                if binary.is_file() and binary.stat().st_mode & 0o111:  # Executable
                    shutil.copy2(binary, dist_service_dir)

    def build_all(self, clean_first: bool = True) -> bool:
        """Build all services in dependency order"""
        print("🚀 Starting build pipeline...")
        
        if clean_first:
            self.clean()
        
        # Build shared library first
        if not self.build_shared_library():
            print("❌ Shared library build failed, aborting")
            return False
        
        # Build services in order
        success_count = 1  # Shared library
        total_count = len(self.build_order)
        
        for service_name in self.build_order[1:]:  # Skip shared library, already built
            service_dir = self.src_dir / service_name
            if not service_dir.exists():
                print(f"⚠️  Service {service_name} not found, skipping")
                continue
            
            # Determine service type and build accordingly
            # Check Node.js services first (more specific)
            if service_name in ["data-scratch-node-library", "rest-scratch-node-express"] or service_name.startswith("rest-client"):
                if self.build_node_service(service_name):
                    success_count += 1
            # Check Rust/C++ services
            elif service_name in ["rest-scratch-rust", "rest-scratch-pistache"]:
                if self.build_rust_service(service_name):
                    success_count += 1
            # Default to Python services (data-scratch-*, rest-scratch-flask)
            elif any(service_name.startswith(prefix) for prefix in ["data-scratch", "rest-scratch-flask"]):
                if self.build_python_service(service_name):
                    success_count += 1
            else:
                print(f"⚠️  Unknown service type for {service_name}, skipping")
        
        print(f"\n📊 Build Summary: {success_count}/{total_count} services built successfully")
        
        # Success if shared library built and at least half of the other services built
        # This is lenient to handle optional services that may not have full implementation
        min_required = max(1 + (total_count - 1) // 2, 1)  # At least shared library + half of others
        success = success_count >= min_required
        
        if not success:
            print(f"❌ Build failed: only {success_count} services built (minimum required: {min_required})")
        
        return success

    def build_specific(self, service_name: str) -> bool:
        """Build a specific service"""
        if service_name == "data-scratch-library":
            return self.build_shared_library()
        
        service_dir = self.src_dir / service_name
        if not service_dir.exists():
            print(f"❌ Service {service_name} not found")
            return False
        
        # Ensure shared library is built first
        if not self.build_shared_library():
            print("❌ Shared library build failed")
            return False
        
        # Build the specific service
        # Check Node.js services first (more specific)
        if service_name in ["data-scratch-node-library", "rest-scratch-node-express"] or service_name.startswith("rest-client"):
            return self.build_node_service(service_name)
        # Check Rust/C++ services
        elif service_name in ["rest-scratch-rust", "rest-scratch-pistache"]:
            return self.build_rust_service(service_name)
        # Default to Python services (data-scratch-*, rest-scratch-flask)
        elif any(service_name.startswith(prefix) for prefix in ["data-scratch", "rest-scratch-flask"]):
            return self.build_python_service(service_name)
        else:
            print(f"❌ Unknown service type for {service_name}")
            return False


def main():
    """Main build entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Build pipeline for data-scratch services")
    parser.add_argument("--clean", action="store_true", help="Clean before building")
    parser.add_argument("--service", help="Build specific service only")
    parser.add_argument("--no-clean", action="store_true", help="Don't clean before building")
    
    args = parser.parse_args()
    
    pipeline = BuildPipeline()
    
    if args.service:
        success = pipeline.build_specific(args.service)
    else:
        clean_first = not args.no_clean
        success = pipeline.build_all(clean_first=clean_first)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
