"""
Job Scoring Engine - QUALITY FOCUSED
Scores jobs for perfect matches only (quality over quantity)
Filters out unsuitable roles aggressively
"""

from typing import Dict, List
import re


class JobScorer:
    """Scores jobs against Amruta's profile - STRICT QUALITY FILTER"""
    
    def __init__(self, profile: Dict):
        self.profile = profile
        self.skills = self._extract_skills()
        self.target_roles = profile.get('target_roles', [])
        self.preferred_locations = profile.get('preferred_locations', [])
        self.quality_filters = profile.get('quality_filters', {})
        self.salary_range = profile.get('salary_range', {})
        self.linkedin_prefs = profile.get('linkedin_preferences', {})
    
    def _extract_skills(self) -> Dict[str, List[str]]:
        """Extract skills from profile"""
        return {
            'languages': self.profile.get('languages', []),
            'tools': self.profile.get('tools', []),
            'frameworks': self.profile.get('frameworks', []),
            'specializations': self.profile.get('specializations', []),
        }
    
    def should_reject_job(self, job: Dict) -> tuple[bool, str]:
        """
        QUALITY GATE: Reject unsuitable jobs before scoring
        Returns: (reject: bool, reason: str)
        """
        title = job.get('title', '').lower()
        company = job.get('company', '').lower()
        description = (job.get('description', '') + ' ' + job.get('requirements', '')).lower()
        location = job.get('location', '').lower()
        
        # ❌ GATE 1: Check for rejected keywords in title
        reject_keywords = self.quality_filters.get('reject_keywords', [])
        for keyword in reject_keywords:
            if keyword.lower() in title:
                return True, f"Rejected: '{keyword}' in title"
        
        # ❌ GATE 2: Check for non-tech roles
        required_keywords = self.quality_filters.get('required_keywords_in_title', [])
        has_required = any(kw.lower() in title for kw in required_keywords)
        if not has_required:
            return True, "Rejected: Not a software/tech role"
        
        # ❌ GATE 3: Reject service-based companies
        reject_companies = self.quality_filters.get('reject_companies', [])
        for reject_co in reject_companies:
            if reject_co.lower() in company:
                return True, f"Rejected: Service-based company (TCS/Infosys/etc)"
        
        # ❌ GATE 4: Experience filter - must be fresher-eligible
        exp_req = job.get('experience_required', 'fresher').lower()
        if any(year in exp_req for year in ['3 year', '4 year', '5 year', '6 year', '7 year', '8 year']):
            return True, "Rejected: Requires 3+ years experience"
        
        # ❌ GATE 5: Location must be in preferred list
        if not any(loc.lower() in location for loc in self.preferred_locations):
            if 'remote' not in location:
                return True, f"Rejected: Location {location} not preferred"
        
        # ❌ GATE 6: Salary must be specified and in range
        salary_range = self.quality_filters.get('min_job_quality_score', 7)
        if self.linkedin_prefs.get('must_have_salary_info', False):
            salary_str = job.get('salary', '').lower()
            if not salary_str or 'salary' not in salary_str:
                return True, "Rejected: Salary not specified"
        
        # ❌ GATE 7: Must explicitly mention fresher-eligible
        if self.linkedin_prefs.get('must_state_fresher_eligible', False):
            if not any(word in description for word in ['fresher', 'entry level', '0 year', '1 year']):
                return True, "Rejected: Doesn't explicitly mention fresher eligibility"
        
        # ❌ GATE 8: Reject if has problematic clauses
        if any(word in description for word in ['bond', 'service agreement', '1-2 year commitment']):
            return True, "Rejected: Has bond/commitment clause"
        
        return False, "Passed all gates"
    
    def score_job(self, job: Dict) -> float:
        """
        Score a job out of 10 (ONLY if it passes quality gates)
        Returns 0 if rejected
        """
        # First check quality gates
        should_reject, reason = self.should_reject_job(job)
        if should_reject:
            return 0.0  # Rejected jobs score 0
        
        score = 0.0
        
        # NOW score high-quality jobs aggressively
        
        # Role match (0-3.5 points) - STRICT
        score += self._score_role_match(job)
        
        # Skills match (0-3 points)
        score += self._score_skills_match(job)
        
        # Experience level (0-1.5 points)
        score += self._score_experience_level(job)
        
        # Location bonus (0-1 point)
        score += self._score_location(job)
        
        # Company type (0-1 point) - prefer product/startup
        score += self._score_company_type(job)
        
        # Salary bonus (0-0.5)
        score += self._score_salary(job)
        
        # Clamp to 0-10
        return max(0, min(10, round(score, 1)))
    
    def _score_role_match(self, job: Dict) -> float:
        """Score role match (0-3.5 points) - VERY STRICT"""
        title = job.get('title', '').lower()
        score = 0
        
        # Key roles for Amruta (with high scores)
        high_priority_roles = {
            'software engineer': 3.5,
            'software development engineer': 3.5,
            'sde': 3.5,
            'swe': 3.5,
            'backend engineer': 3.0,
            'backend developer': 3.0,
            'full stack engineer': 3.0,
            'full stack developer': 3.0,
            'ml engineer': 3.5,
            'ai engineer': 3.5,
            'machine learning engineer': 3.5,
            'data engineer': 3.0,
            'computer vision engineer': 3.5,
            'nlp engineer': 3.5,
        }
        
        # Medium priority roles
        medium_priority_roles = {
            'developer': 2.0,
            'frontend engineer': 2.0,
            'data scientist': 2.0,
            'research engineer': 2.0,
            'graduate engineer': 2.5,
            'associate engineer': 2.5,
        }
        
        # Check high priority first
        for role, points in high_priority_roles.items():
            if role in title:
                return points
        
        # Then medium priority
        for role, points in medium_priority_roles.items():
            if role in title:
                return points
        
        return 0.5  # Very low score if no match
    
    def _score_skills_match(self, job: Dict) -> float:
        """Score skills match (0-3 points) - SPECIALIZED TECH"""
        job_text = (
            job.get('description', '') + ' ' + 
            job.get('requirements', '')
        ).lower()
        
        score = 0
        
        # High-value skill matches for Amruta
        high_value_skills = {
            'python': 1.5,
            'tensorflow': 1.5,
            'pytorch': 1.5,
            'machine learning': 1.5,
            'deep learning': 1.5,
            'computer vision': 1.5,
            'yolo': 1.5,
            'opencv': 1.0,
            'pandas': 0.8,
            'numpy': 0.8,
            'fastapi': 1.0,
            'flask': 0.8,
        }
        
        for skill, points in high_value_skills.items():
            if skill in job_text:
                score += min(points, 3)
        
        return min(score, 3)
    
    def _score_experience_level(self, job: Dict) -> float:
        """Score experience requirement (0-1.5 points)"""
        exp_req = job.get('experience_required', 'fresher').lower()
        
        if any(word in exp_req for word in ['fresher', '0 year', 'entry level', 'no experience', 'batch of']):
            return 1.5
        elif any(word in exp_req for word in ['0-1 year', '0-2 year', '1 year']):
            return 1.0
        else:
            return 0.5
    
    def _score_location(self, job: Dict) -> float:
        """Score location preference (0-1 point)"""
        location = job.get('location', '').lower()
        
        top_locations = {
            'bengaluru': 1.0,
            'bangalore': 1.0,
            'hyderabad': 0.9,
            'pune': 0.8,
            'remote': 1.0,
        }
        
        for city, points in top_locations.items():
            if city in location:
                return points
        
        return 0.3  # Other locations get minimal score
    
    def _score_company_type(self, job: Dict) -> float:
        """Score company type (0-1 point) - prefer product/startup"""
        company = job.get('company', '').lower()
        description = job.get('description', '').lower()
        
        # Prefer product/startup companies
        prefer_companies = [
            'google', 'microsoft', 'amazon', 'meta', 'apple',
            'startup', 'product', 'tech', 'ai', 'ml',
            'flipkart', 'myntra', 'paytm', 'razorpay', 'unacademy',
        ]
        
        for company_type in prefer_companies:
            if company_type in company or company_type in description:
                return 1.0
        
        return 0.3  # Generic company gets low score
    
    def _score_salary(self, job: Dict) -> float:
        """Score salary (0-0.5 points)"""
        salary_str = job.get('salary', '').lower()
        
        # Bonus for salary >= 15 LPA
        if any(str(i) in salary_str for i in range(15, 50)):
            return 0.5
        
        # Base salary in range
        if any(str(i) in salary_str for i in range(8, 15)):
            return 0.2
        
        return 0
    
    def get_score_explanation(self, job: Dict, score: float) -> str:
        """Get human-readable explanation of score"""
        
        if score == 0:
            should_reject, reason = self.should_reject_job(job)
            return f"❌ Filtered out: {reason}"
        
        if score >= 8:
            return "🎯 EXCELLENT - Highly recommended"
        elif score >= 7:
            return "✅ VERY GOOD - Strong match"
        elif score >= 6:
            return "👍 GOOD - Worth considering"
        else:
            return "⚠️ OK - Lower priority"
    
    def get_top_jobs(self, jobs: List[Dict], min_score: int = 7) -> List[Dict]:
        """Get only high-quality jobs (score >= 7)"""
        scored_jobs = []
        
        for job in jobs:
            score = self.score_job(job)
            job['score'] = score
            job['explanation'] = self.get_score_explanation(job, score)
            
            if score >= min_score:  # Only keep 7+ scores
                scored_jobs.append(job)
        
        # Sort by score descending
        scored_jobs.sort(key=lambda x: x['score'], reverse=True)
        
        return scored_jobs


# Sample profile for testing
SAMPLE_JOB = {
    'title': 'Software Engineer - Fresher (Python/AI)',
    'company': 'Google India',
    'location': 'Bangalore',
    'experience_required': 'Fresher / 0 years',
    'salary': '25-35 LPA',
    'description': 'Join Google as a Software Engineer Fresher. Work on AI/ML using Python, TensorFlow.',
    'requirements': 'Python, TensorFlow, strong problem solving',
    'source': 'LinkedIn',
    'posted_date': '2026-03-18',
    'url': 'https://example.com/job'
}
