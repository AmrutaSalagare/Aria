"""
Job Scoring Engine
Scores jobs against Amruta's profile
"""

from typing import Dict, List
import re


class JobScorer:
    """Scores jobs against a candidate profile"""
    
    def __init__(self, profile: Dict):
        self.profile = profile
        self.skills = self._extract_skills()
        self.target_roles = profile.get('target_roles', [])
        self.preferred_locations = profile.get('preferred_locations', [])
    
    def _extract_skills(self) -> Dict[str, List[str]]:
        """Extract skills from profile"""
        return {
            'languages': self.profile.get('languages', []),
            'tools': self.profile.get('tools', []),
            'frameworks': self.profile.get('frameworks', []),
            'specializations': self.profile.get('specializations', []),
        }
    
    def score_job(self, job: Dict) -> float:
        """Score a job out of 10"""
        score = 0.0
        
        # Role match (0-3 points)
        score += self._score_role_match(job)
        
        # Skills match (0-4 points)
        score += self._score_skills_match(job)
        
        # Experience level (0-2 points)
        score += self._score_experience_level(job)
        
        # Location bonus (0-1 point)
        score += self._score_location(job)
        
        # Salary bonus (0-0.5 points)
        score += self._score_salary(job)
        
        # Red flags (negative points)
        score += self._check_red_flags(job)
        
        # Clamp to 0-10
        return max(0, min(10, round(score, 1)))
    
    def _score_role_match(self, job: Dict) -> float:
        """Score based on role match (0-3 points)"""
        title = job.get('title', '').lower()
        score = 0
        
        target_keywords = {
            'software engineer': 1.5,
            'developer': 1.0,
            'data engineer': 1.5,
            'ml engineer': 1.5,
            'ai engineer': 1.5,
            'backend': 1.0,
            'frontend': 1.0,
            'full stack': 1.0,
            'sde': 1.5,
            'swe': 1.5,
            'analyst': 0.5,
            'graduate engineer': 1.5,
            'trainee': 1.5,
        }
        
        for keyword, points in target_keywords.items():
            if keyword in title:
                score += min(points, 3)  # Cap at 3
        
        return min(score, 3)
    
    def _score_skills_match(self, job: Dict) -> float:
        """Score based on skills match (0-4 points)"""
        job_description = (
            job.get('description', '') + ' ' + 
            job.get('requirements', '')
        ).lower()
        
        score = 0
        matched_skills = set()
        
        # Check all skills
        for skill_category, skills in self.skills.items():
            for skill in skills:
                if skill.lower() in job_description:
                    matched_skills.add(skill)
                    score += 0.5  # 0.5 points per skill
        
        return min(score, 4)  # Cap at 4 points
    
    def _score_experience_level(self, job: Dict) -> float:
        """Score based on experience requirement (0-2 points)"""
        exp_req = job.get('experience_required', 'fresher').lower()
        
        if any(word in exp_req for word in ['fresher', '0 year', 'entry level', 'no experience']):
            return 2.0
        elif any(word in exp_req for word in ['1 year', '2 year']):
            return 1.0
        elif any(word in exp_req for word in ['3 year', '4 year', '5 year']):
            return -2.0  # Exclude senior roles
        else:
            return 0.5  # Neutral
    
    def _score_location(self, job: Dict) -> float:
        """Score based on location (0-1 point)"""
        location = job.get('location', '').lower()
        
        preferred = {
            'bangalore': 1.0,
            'bengaluru': 1.0,
            'hyderabad': 1.0,
            'pune': 1.0,
            'mumbai': 1.0,
            'delhi': 0.8,
            'remote': 1.0,
        }
        
        for city, points in preferred.items():
            if city in location:
                return points
        
        return 0  # Non-preferred location
    
    def _score_salary(self, job: Dict) -> float:
        """Score based on salary (0-0.5 points)"""
        salary = job.get('salary', '')
        
        # Look for salary in LPA range
        if salary:
            if any(str(i) in salary for i in range(8, 50)):  # 8 LPA to 50 LPA
                return 0.5
        
        return 0
    
    def _check_red_flags(self, job: Dict) -> float:
        """Check for red flags (-0.5 to -2 points)"""
        description = (
            job.get('description', '') + ' ' + 
            job.get('requirements', '')
        ).lower()
        
        penalties = 0
        
        # Bond clauses
        if any(word in description for word in ['bond', 'service agreement']):
            penalties -= 0.5
        
        # Mass hiring
        if any(word in description for word in ['mass recruitment', 'bulk hiring', 'thousands']):
            penalties -= 0.5
        
        # Suspicious platforms
        if job.get('source', '').lower() in ['unknown', 'spam', 'suspicious']:
            penalties -= 1.0
        
        return penalties
    
    def get_score_explanation(self, job: Dict, score: float) -> str:
        """Get human-readable explanation of score"""
        explanations = []
        
        if score >= 8:
            explanations.append("🎯 Strong match — high probability of fit")
        elif score >= 6:
            explanations.append("✅ Good match — worth applying")
        elif score >= 5:
            explanations.append("👍 Moderate match — consider applying")
        else:
            explanations.append("❌ Low match — not a priority")
        
        if 'bond' in job.get('description', '').lower():
            explanations.append("⚠️ Has bond clause — read carefully")
        
        return " | ".join(explanations)


# Sample profiles for testing
SAMPLE_JOB = {
    'title': 'Software Engineer (Entry Level)',
    'company': 'TechCorp India',
    'location': 'Bangalore',
    'experience_required': '0-2 years or fresher',
    'salary': '8-12 LPA',
    'description': 'Looking for fresher engineers with Python, machine learning background',
    'requirements': 'Python, TensorFlow, PyTorch, strong fundamentals',
    'source': 'LinkedIn',
    'posted_date': '2026-03-18',
    'url': 'https://example.com/job'
}
