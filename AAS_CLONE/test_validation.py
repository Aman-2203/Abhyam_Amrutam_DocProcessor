"""
Test script to verify document validation logic
"""
import os
import sys

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils import calculate_page_usage, validate_trial_limits, TRIAL_PAGE_LIMIT, TRIAL_CHAR_LIMIT

def test_validation_logic():
    """Test the document validation logic"""
    print("=" * 60)
    print("Testing Document Validation Logic")
    print("=" * 60)
    
    # Test scenarios
    test_cases = [
        {
            'name': 'PDF - 2 pages (should pass with 3 page limit)',
            'page_usage_info': {
                'page_usage': 2.0,
                'actual_pages': 2,
                'char_count': None,
                'file_type': 'pdf'
            },
            'remaining_pages': 3.0,
            'expected_valid': True
        },
        {
            'name': 'PDF - 5 pages (should fail - exceeds absolute limit)',
            'page_usage_info': {
                'page_usage': 5.0,
                'actual_pages': 5,
                'char_count': None,
                'file_type': 'pdf'
            },
            'remaining_pages': 3.0,
            'expected_valid': False
        },
        {
            'name': 'DOCX - 8000 chars (should pass)',
            'page_usage_info': {
                'page_usage': 2.4,  # 8000 / 3333 ≈ 2.4
                'actual_pages': None,
                'char_count': 8000,
                'file_type': 'docx'
            },
            'remaining_pages': 3.0,
            'expected_valid': True
        },
        {
            'name': 'DOCX - 15000 chars (should fail - exceeds 10k limit)',
            'page_usage_info': {
                'page_usage': 4.5,  # 15000 / 3333 ≈ 4.5
                'actual_pages': None,
                'char_count': 15000,
                'file_type': 'docx'
            },
            'remaining_pages': 3.0,
            'expected_valid': False
        },
        {
            'name': 'PDF - 2 pages but only 1.5 remaining (should fail)',
            'page_usage_info': {
                'page_usage': 2.0,
                'actual_pages': 2,
                'char_count': None,
                'file_type': 'pdf'
            },
            'remaining_pages': 1.5,
            'expected_valid': False
        },
    ]
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test['name']}")
        print(f"  Page usage: {test['page_usage_info']['page_usage']}")
        print(f"  Remaining: {test['remaining_pages']}")
        
        result = validate_trial_limits(test['page_usage_info'], test['remaining_pages'])
        
        if result['valid'] == test['expected_valid']:
            print(f"  [PASS]")
            passed += 1
        else:
            print(f"  [FAIL]")
            print(f"    Expected valid={test['expected_valid']}, got valid={result['valid']}")
            print(f"    Message: {result['message']}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    # Display limits
    print(f"\nConfigured Limits:")
    print(f"  - PDF: {TRIAL_PAGE_LIMIT} pages")
    print(f"  - DOCX: {TRIAL_CHAR_LIMIT:,} characters (~{TRIAL_PAGE_LIMIT} pages)")
    print(f"  - Character to page ratio: 1 page ~ 3,333 chars")
    
    return failed == 0

if __name__ == '__main__':
    success = test_validation_logic()
    sys.exit(0 if success else 1)
