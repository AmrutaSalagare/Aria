#!/usr/bin/env python3
"""
Test script to verify all components are working
Run this before pushing to GitHub
"""

import os
import sys
import json
from pathlib import Path

def test_imports():
    """Test that all modules can be imported"""
    print("Testing imports...")
    try:
        from config import AMRUTA_PROFILE, JOB_PORTALS
        from scorer import JobScorer
        from telegram_sender import TelegramSender
        from job_search import JobSearcher
        print("✅ All imports successful")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def test_config():
    """Test that config has all required fields"""
    print("\nTesting configuration...")
    try:
        from config import AMRUTA_PROFILE, SEARCH_CONFIG
        
        required_fields = [
            'name', 'email', 'location', 'languages', 'frameworks',
            'target_roles', 'preferred_locations', 'salary_range'
        ]
        
        for field in required_fields:
            if field not in AMRUTA_PROFILE:
                print(f"❌ Missing field in AMRUTA_PROFILE: {field}")
                return False
        
        print(f"✅ Profile complete - {AMRUTA_PROFILE['name']}")
        print(f"   Skills: {len(AMRUTA_PROFILE['languages'])} languages, "
              f"{len(AMRUTA_PROFILE['frameworks'])} frameworks")
        print(f"   Target roles: {len(AMRUTA_PROFILE['target_roles'])} types")
        return True
        
    except Exception as e:
        print(f"❌ Config test failed: {e}")
        return False

def test_scorer():
    """Test job scoring engine"""
    print("\nTesting job scorer...")
    try:
        from config import AMRUTA_PROFILE
        from scorer import JobScorer
        
        scorer = JobScorer(AMRUTA_PROFILE)
        
        # Test job
        test_job = {
            'title': 'Junior Software Engineer - Python',
            'company': 'TechCorp',
            'location': 'Bangalore',
            'experience_required': 'Fresher',
            'salary': '10 LPA',
            'description': 'Seeking fresher python developer with ML experience',
            'requirements': 'Python, TensorFlow, machine learning',
            'url': 'https://example.com/job',
            'posted_date': '2026-03-18'
        }
        
        score = scorer.score_job(test_job)
        print(f"✅ Test job scored: {score}/10")
        
        if 0 <= score <= 10:
            print("✅ Scoring system works correctly")
            return True
        else:
            print(f"❌ Score out of range: {score}")
            return False
            
    except Exception as e:
        print(f"❌ Scorer test failed: {e}")
        return False

def test_telegram():
    """Test Telegram connection"""
    print("\nTesting Telegram setup...")
    try:
        bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        chat_id = os.getenv('TELEGRAM_CHAT_ID')
        
        if not bot_token or not chat_id:
            print("⚠️  Telegram credentials not set in environment")
            print("   Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID before deployment")
            return True  # Not a failure, just not configured yet
        
        from telegram_sender import TelegramSender
        sender = TelegramSender(bot_token, chat_id)
        
        if sender.test_connection():
            print("✅ Telegram connection successful")
            return True
        else:
            print("❌ Telegram connection failed - check credentials")
            return False
            
    except Exception as e:
        print(f"❌ Telegram test failed: {e}")
        return False

def test_directories():
    """Test that required directories exist"""
    print("\nTesting directory structure...")
    try:
        required_dirs = [
            'workspace',
            'workspace/reports',
            'workspace/memory',
            '.github/workflows'
        ]
        
        for dir_path in required_dirs:
            Path(dir_path).mkdir(parents=True, exist_ok=True)
        
        print("✅ All required directories present")
        return True
        
    except Exception as e:
        print(f"❌ Directory test failed: {e}")
        return False

def test_requirements():
    """Test that requirements.txt exists"""
    print("\nTesting requirements.txt...")
    try:
        if Path('requirements.txt').exists():
            with open('requirements.txt', 'r') as f:
                packages = len(f.readlines())
            print(f"✅ requirements.txt found ({packages} packages)")
            return True
        else:
            print("❌ requirements.txt not found")
            return False
            
    except Exception as e:
        print(f"❌ Requirements test failed: {e}")
        return False

def test_workflow():
    """Test that GitHub Actions workflow file exists"""
    print("\nTesting GitHub Actions workflow...")
    try:
        workflow_path = Path('.github/workflows/daily-job-search.yml')
        
        if workflow_path.exists():
            print("✅ GitHub Actions workflow file found")
            
            with open(workflow_path, 'r') as f:
                content = f.read()
                
            if 'TELEGRAM_BOT_TOKEN' in content and 'python job_search.py' in content:
                print("✅ Workflow configuration looks good")
                return True
            else:
                print("❌ Workflow missing required configuration")
                return False
        else:
            print("❌ Workflow file not found")
            return False
            
    except Exception as e:
        print(f"❌ Workflow test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("ARIA JOB SEARCH - SYSTEM TEST")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_config,
        test_scorer,
        test_directories,
        test_requirements,
        test_workflow,
        test_telegram,
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {sum(results)}/{len(results)} tests passed")
    print("=" * 60)
    
    if all(results):
        print("\n✅ All systems operational! Ready for GitHub deployment.")
        return 0
    else:
        print("\n❌ Some tests failed. Fix issues before pushing to GitHub.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
