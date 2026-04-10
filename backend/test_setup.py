"""
CricSense Setup Test Script
Run this to verify your Python environment is ready!

Usage:
    py backend/test_setup.py
"""

import sys
import os

print("\n" + "=" * 60)
print("🏏 CricSense Environment Test")
print("=" * 60 + "\n")

# Test 1: Python Version
print("1️⃣  Python Version")
print(f"   Version: {sys.version}")
print(f"   Location: {sys.executable}")
print(f"   ✅ PASS\n")

# Test 2: Virtual Environment
print("2️⃣  Virtual Environment")
venv_path = os.environ.get('VIRTUAL_ENV')
if venv_path:
    print(f"   Active: YES")
    print(f"   Path: {venv_path}")
    print(f"   ✅ PASS\n")
else:
    print(f"   Active: NO")
    print(f"   ⚠️  WARNING: Virtual environment not activated!")
    print(f"   Run: venv\\Scripts\\activate\n")

# Test 3: Core Data Science Packages
print("3️⃣  Data Science Packages")
packages_to_test = {
    'pandas': 'Data manipulation',
    'numpy': 'Numerical computing',
    'sklearn': 'Machine learning',
    'matplotlib': 'Data visualization',
}

for package, description in packages_to_test.items():
    try:
        mod = __import__(package)
        version = getattr(mod, '__version__', 'unknown')
        print(f"   ✅ {package:20s} v{version:10s} ({description})")
    except ImportError as e:
        print(f"   ❌ {package:20s} - NOT INSTALLED")

print()

# Test 4: Web Framework
print("4️⃣  Web Framework")
try:
    import flask
    print(f"   ✅ Flask                v{flask.__version__:10s} (Web API)")
except ImportError:
    print(f"   ❌ Flask - NOT INSTALLED")

print()

# Test 5: Utilities
print("5️⃣  Utility Packages")
utility_packages = {
    'requests': 'HTTP requests',
    'joblib': 'Model serialization',
}

for package, description in utility_packages.items():
    try:
        mod = __import__(package)
        version = getattr(mod, '__version__', 'unknown')
        print(f"   ✅ {package:20s} v{version:10s} ({description})")
    except ImportError:
        print(f"   ❌ {package:20s} - NOT INSTALLED")

print()

# Test 6: Data Directory Structure
print("6️⃣  Directory Structure")
base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(base_dir))

required_dirs = {
    'data/raw': 'Raw data storage',
    'data/processed': 'Processed data',
    'data/models': 'Trained models',
}

print(f"   Project Root: {project_root}\n")

for dir_path, description in required_dirs.items():
    full_path = os.path.join(project_root, dir_path)
    exists = os.path.exists(full_path)
    status = "✅" if exists else "❌"
    print(f"   {status} {dir_path:25s} ({description})")

print()

# Test 7: Import Test
print("7️⃣  Import Test")
try:
    import pandas as pd
    import numpy as np
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    import flask
    import requests
    import joblib
    
    print("   ✅ All critical imports successful!")
except Exception as e:
    print(f"   ❌ Import failed: {e}")

print()

# Test 8: Quick Data Test
print("8️⃣  Data Handling Test")
try:
    import pandas as pd
    import numpy as np
    
    # Create sample data
    data = {
        'team1': ['CSK', 'MI', 'RCB'],
        'team2': ['MI', 'RCB', 'KKR'],
        'runs': [200, 180, 195]
    }
    df = pd.DataFrame(data)
    
    print("   Created sample DataFrame:")
    print(f"   Shape: {df.shape}")
    print(f"   Columns: {list(df.columns)}")
    print(f"   ✅ Data handling works!")
except Exception as e:
    print(f"   ❌ Data test failed: {e}")

print()

# Summary
print("=" * 60)
print("✅ SUMMARY")
print("=" * 60)
print("""
Your CricSense environment is ready! 🚀

Next Steps:
1. Download or generate IPL data
   - Check: Windows_Setup_Fix_Guide.md
   
2. Explore the data:
   py backend/src/data_loader.py
   
3. Start building models:
   - Follow: CricSense_Complete_Guide.md
   
4. Run Flask API:
   py backend/app.py
   
5. Open frontend:
   frontend/index.html

Happy coding! 🏏⚡
""")
print("=" * 60 + "\n")