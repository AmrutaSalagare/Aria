"""
Configuration and Profile
Contains Amruta's profile and job portal configurations
"""

# AMRUTA'S PROFILE (Extracted from USER.md)
AMRUTA_PROFILE = {
    'name': 'Amruta Salagare',
    'email': 'amrutasalagare2609@gmail.com',
    'phone': '9008008973',
    'location': 'Mysore / Bengaluru, Karnataka, India',
    'timezone': 'Asia/Kolkata',
    
    # Education
    'degree': 'B.E. Computer Science & Engineering (AI & ML)',
    'college': 'ATME College of Engineering, Mysore',
    'cgpa': 8.9,
    'graduating': 2026,
    'batch': '2022-2026',
    
    # Current Role
    'current_role': 'Prompt Engineer (Freelance) at Soul AI',
    'current_duration': 'November 2024 - Present',
    
    # Skills
    'languages': [
        'Python', 'C', 'SQL', 'HTML', 'CSS'
    ],
    'tools': [
        'VS Code', 'Git', 'GitHub', 'Jupyter Notebook', 'Google Colab',
        'Tableau', 'Power BI'
    ],
    'frameworks': [
        'NumPy', 'Pandas', 'TensorFlow', 'Keras', 'PyTorch',
        'Scikit-learn', 'Streamlit', 'OpenCV', 'FastAPI', 'Flask'
    ],
    'specializations': [
        'Computer Vision', 'Deep Learning', 'Machine Learning',
        'YOLO', 'ONNX Runtime', 'MediaPipe', 'MobileNetV2', 'VGG19',
        'Transfer Learning', 'IoT', 'Edge AI', 'Raspberry Pi',
        'LLM Evaluation', 'Prompt Engineering'
    ],
    
    # Projects
    'projects': [
        {
            'name': 'Intelligent Traffic Management System',
            'tech': ['YOLOv11', 'ONNX Runtime', 'Raspberry Pi', 'Python'],
            'highlight': 'Real-time edge-AI, >93% counting accuracy'
        },
        {
            'name': 'StreetRaksha - Women Safety Platform',
            'tech': ['YOLO', 'MediaPipe', 'MobileNetV2', 'FastAPI', 'IoT'],
            'highlight': 'Real-time CCTV threat detection'
        },
        {
            'name': 'AgroBalance - Smart Farming System',
            'tech': ['Random Forest', 'Neural Networks', 'Flask', 'IoT'],
            'highlight': 'Precision farming, crop recommendations'
        },
        {
            'name': 'Lung Disease Classifier',
            'tech': ['VGG19', 'CNN', 'Streamlit', 'TensorFlow'],
            'highlight': '96% accuracy, chest X-ray diagnosis'
        }
    ],
    
    # Leadership
    'leadership': [
        'Program Head - IEEE Student Branch Chapter, ATMECE',
        'Stage Committee Head - IET On Campus, ATMECE',
        'Runner-up - Code Battle 2K24',
        'Hackathon Organizer - Tech Avishkar 2.0 (200+ participants)',
    ],
    
    # Certifications
    'certifications': [
        'Building LLM Applications with Prompt Engineering',
        'Explore Machine Learning with TensorFlow',
        'Introduction to Oracle SQL',
        'Analytics using Tableau',
        'Database and SQL',
        'Web Development',
        'Python for Data Science'
    ],
    
    # Job Preferences
    'target_roles': [
        'Software Development Engineer (SDE)',
        'Software Engineer (SWE)',
        'Backend Developer',
        'Full Stack Developer',
        'Frontend Developer',
        'Data Analyst',
        'Data Engineer',
        'Business Analyst (Tech)',
        'AI Engineer',
        'ML Engineer',
        'Applied AI Engineer',
        'NLP Engineer',
        'Prompt Engineer',
        'Computer Vision Engineer',
        'Graduate Engineer Trainee (GET)',
        'Associate Engineer',
        'Junior Developer',
        'Product Analyst',
        'Research Associate'
    ],
    
    'preferred_locations': [
        'Bengaluru',
        'Hyderabad',
        'Pune',
        'Mumbai',
        'Chennai',
        'Delhi NCR',
        'Noida',
        'Gurugram',
        'Remote India',
        'Remote Global'
    ],
    
    'salary_range': {
        'min_lpa': 10,        # Increased from 8
        'max_lpa': 50,
        'currency': 'INR',
        'preferred_min': 15,  # Prefer above 15 LPA
    },
    
    'job_type': 'Full-time',
    
    # Experience Filters
    'min_experience': 0,
    'max_experience': 2,
    
    # STRICT QUALITY FILTERS
    'quality_filters': {
        'required_keywords_in_title': [
            'software',
            'engineer',
            'developer',
            'ai',
            'ml',
            'data',
            'backend',
            'frontend',
            'full stack',
            'associate',
            'graduate',
            'sde',
            'swe',
            'fresher',
            'trainee',
        ],
        'reject_keywords': [
            'consultant',
            'sales',
            'marketing',
            'support',
            'hr',
            'bcd',
            'bpo',
            'call center',
            'accountant',
            'finance',
            'customer service',
            'operations',
        ],
        'reject_companies': [
            'TCS',
            'Infosys',
            'Wipro',
            'HCL',
            'Cognizant',
            'Accenture',
            'Deloitte',
            'EY',
            'KPMG',
            'PwC',
        ],  # Typically service-based with low fresher salaries
        
        'min_job_quality_score': 7,  # Only show jobs scoring 7+ out of 10
        
        'prefer_company_types': [
            'Product',
            'Startup',
            'Tech Company',
            'FAANG',
            'Indian Tech',
        ],
    },
    
    # LinkedIn specific preferences
    'linkedin_preferences': {
        'filter_by': [
            'recruiter_posts',
            'employee_referrals',
            'company_careers',
        ],
        'must_have_salary_info': True,
        'must_state_fresher_eligible': True,
    }

}

# JOB PORTALS TO SEARCH
JOB_PORTALS = {
    'linkedin': {
        'name': 'LinkedIn Jobs',
        'url': 'https://www.linkedin.com/jobs/',
        'enabled': True,
        'priority': 1
    },
    'naukri': {
        'name': 'Naukri.com',
        'url': 'https://www.naukri.com/',
        'enabled': True,
        'priority': 1
    },
    'indeed': {
        'name': 'Indeed India',
        'url': 'https://www.indeed.co.in/',
        'enabled': True,
        'priority': 1
    },
    'internshala': {
        'name': 'Internshala',
        'url': 'https://internshala.com/',
        'enabled': True,
        'priority': 2
    },
    'glassdoor': {
        'name': 'Glassdoor India',
        'url': 'https://www.glassdoor.co.in/',
        'enabled': True,
        'priority': 2
    },
    'wellfound': {
        'name': 'Wellfound (AngelList)',
        'url': 'https://wellfound.com/jobs',
        'enabled': True,
        'priority': 2
    },
    'remotive': {
        'name': 'Remotive',
        'url': 'https://remotive.io/',
        'enabled': True,
        'priority': 2
    },
    'we_work_remotely': {
        'name': 'WeWorkRemotely',
        'url': 'https://weworkremotely.com/',
        'enabled': True,
        'priority': 2
    },
    'unstop': {
        'name': 'Unstop (formerly Dare2Compete)',
        'url': 'https://unstop.com/',
        'enabled': True,
        'priority': 3
    },
    'apna': {
        'name': 'Apna',
        'url': 'https://www.apna.co/',
        'enabled': True,
        'priority': 3
    },
}

# SEARCH CONFIGURATION
SEARCH_CONFIG = {
    'max_jobs_per_report': 25,
    'min_score_threshold': 5.0,
    'hours_back': 48,  # Search jobs posted in last 48 hours
    'deduplication': True,  # Remove duplicate job titles at same company
    'timeout_seconds': 30,
    'retry_count': 2
}

# SCORING THRESHOLDS
SCORING_THRESHOLDS = {
    'high_match': 8,     # 8-10: Strong match
    'good_match': 6,     # 6-8: Good match
    'moderate_match': 5, # 5-6: Moderate match
    'low_match': 0       # 0-5: Low match (excluded)
}

# TELEGRAM CONFIGURATION
TELEGRAM_CONFIG = {
    'enabled': True,
    'message_chunks': 4000,  # Max chars per message
    'schedule_time': '06:00'  # 6 AM IST
}

# REPORT CONFIGURATION
REPORT_CONFIG = {
    'save_locally': True,
    'local_dir': 'workspace/reports',
    'include_score_breakdown': True,
    'include_action_plan': True,
    'include_failed_portals': True
}
