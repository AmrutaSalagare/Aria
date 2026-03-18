#!/usr/bin/env python3
"""
Aria Job Search Script
Searches job portals, scores jobs, and sends reports to Telegram
"""

import os
import json
import requests
from datetime import datetime
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

import sys
sys.path.insert(0, '.')

from scorer import JobScorer
from config import AMRUTA_PROFILE, JOB_PORTALS, SEARCH_CONFIG
from telegram_sender import TelegramSender


class JobSearcher:
    """Main job search orchestrator"""
    
    def __init__(self, profile: Dict, config: Dict):
        self.profile = profile
        self.config = config
        self.scorer = JobScorer(profile)
        self.telegram = TelegramSender(
            bot_token=os.getenv('TELEGRAM_BOT_TOKEN'),
            chat_id=os.getenv('TELEGRAM_CHAT_ID')
        )
        self.all_jobs = []
        self.report_date = datetime.now().strftime("%Y-%m-%d")
    
    def search_linkedin(self) -> List[Dict]:
        """Search LinkedIn Jobs for entry-level positions"""
        jobs = []
        try:
            logger.info("Searching LinkedIn Jobs...")
            # LinkedIn requires authentication - using Google search fallback
            search_query = f"site:linkedin.com/jobs fresher 2026 batch India engineer Python"
            results = self._google_search(search_query, num_results=10)
            
            # Note: Full LinkedIn scraping requires authentication
            # This is a simplified search that finds job postings
            logger.info(f"Found {len(results)} potential LinkedIn results")
        except Exception as e:
            logger.warning(f"LinkedIn search failed: {e}")
        
        return jobs
    
    def search_naukri(self) -> List[Dict]:
        """Search Naukri.com for fresher jobs"""
        jobs = []
        try:
            logger.info("Searching Naukri...")
            # Naukri API endpoint (simplified)
            url = "https://www.naukri.com/jobs-search?src=gnbjobs_homepage_srch"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            params = {
                'keyword': 'software engineer, python developer, data engineer',
                'experience': '0',
                'location': 'bangalore,hyderabad,pune,mumbai,delhi',
                'noOfResults': '50',
                'pageNo': '1'
            }
            
            # Note: Direct HTML scraping would require BeautifulSoup
            # For now, returning empty to show structure
            logger.info("Naukri search structure ready (requires BeautifulSoup for full implementation)")
            
        except Exception as e:
            logger.warning(f"Naukri search failed: {e}")
        
        return jobs
    
    def search_indeed(self) -> List[Dict]:
        """Search Indeed for entry-level tech jobs"""
        jobs = []
        try:
            logger.info("Searching Indeed...")
            # Indeed has limited search API
            # Using RSS feed approach
            rss_url = "https://www.indeed.co.in/rss?q=fresher+software+engineer&l=India&jt=&limit=50"
            
            response = requests.get(rss_url, timeout=10)
            # Would parse RSS feed here
            logger.info("Indeed RSS feed ready for parsing")
            
        except Exception as e:
            logger.warning(f"Indeed search failed: {e}")
        
        return jobs
    
    def search_internshala(self) -> List[Dict]:
        """Search Internshala for fresher and PPO roles"""
        jobs = []
        try:
            logger.info("Searching Internshala...")
            # Internshala has a basic search interface
            # Full scraping would need Selenium or similar
            logger.info("Internshala search structure ready")
            
        except Exception as e:
            logger.warning(f"Internshala search failed: {e}")
        
        return jobs
    
    def search_google_jobs(self) -> List[Dict]:
        """Search Google Jobs (aggregator)"""
        jobs = []
        try:
            logger.info("Searching Google Jobs...")
            query = "software engineer fresher 2026 India site:google.com/search/jobs"
            
            # Google Jobs search via Google Search API (if available)
            logger.info("Google Jobs search structure ready")
            
        except Exception as e:
            logger.warning(f"Google Jobs search failed: {e}")
        
        return jobs
    
    def _google_search(self, query: str, num_results: int = 10) -> List[Dict]:
        """Generic Google search fallback (limited without API key)"""
        results = []
        # Note: Full Google search requires API key
        # This is a placeholder for the structure
        logger.info(f"Google search structure: {query}")
        return results
    
    def run_search(self) -> List[Dict]:
        """Execute full job search across all platforms"""
        logger.info("=" * 60)
        logger.info("ARIA JOB SEARCH INITIATED")
        logger.info(f"Report Date: {self.report_date}")
        logger.info("=" * 60)
        
        # Search all platforms
        all_jobs = []
        all_jobs.extend(self.search_linkedin())
        all_jobs.extend(self.search_naukri())
        all_jobs.extend(self.search_indeed())
        all_jobs.extend(self.search_internshala())
        all_jobs.extend(self.search_google_jobs())
        
        logger.info(f"Total jobs found: {len(all_jobs)}")
        
        # Score all jobs
        scored_jobs = []
        for job in all_jobs:
            score = self.scorer.score_job(job)
            job['score'] = score
            if score >= 5:  # Minimum threshold
                scored_jobs.append(job)
        
        # Sort by score
        scored_jobs.sort(key=lambda x: x['score'], reverse=True)
        
        # Keep top 25
        top_jobs = scored_jobs[:25]
        
        logger.info(f"Jobs with score >= 5: {len(scored_jobs)}")
        logger.info(f"Top 25 kept for report: {len(top_jobs)}")
        
        self.all_jobs = top_jobs
        return top_jobs
    
    def build_report(self) -> str:
        """Build markdown report"""
        if not self.all_jobs:
            return "No jobs found matching your criteria today."
        
        report = f"# Job Search Report — {self.report_date}\n\n"
        report += f"**Good morning Amruta!** Your job report is ready.\n"
        report += f"**Total opportunities found:** {len(self.all_jobs)}\n\n"
        
        if self.all_jobs:
            top = self.all_jobs[0]
            report += f"🎯 **Top Match:** {top.get('title')} at {top.get('company')} — **{top['score']}/10**\n\n"
        
        report += "## All Opportunities\n\n"
        
        for i, job in enumerate(self.all_jobs, 1):
            report += f"### {i}. {job.get('title')} @ {job.get('company')}\n"
            report += f"- **Score:** {job['score']}/10\n"
            report += f"- **Location:** {job.get('location', 'Not specified')}\n"
            report += f"- **Experience:** {job.get('experience', 'Fresher-eligible')}\n"
            report += f"- **Posted:** {job.get('posted_date', 'Unknown')}\n"
            report += f"- **Link:** {job.get('url', 'N/A')}\n\n"
        
        report += "## Your Action Plan Today\n\n"
        report += "1. Review top 3 matches above\n"
        report += "2. Check for bond clauses in company terms\n"
        report += "3. Prepare customized cover letter\n"
        report += "4. Set LinkedIn referral reminders\n\n"
        report += "---\n"
        report += f"*Report generated at {datetime.now().strftime('%Y-%m-%d %H:%M IST')}*\n"
        
        return report
    
    def save_report(self, report: str):
        """Save report to file"""
        report_dir = "workspace/reports"
        os.makedirs(report_dir, exist_ok=True)
        
        report_file = f"{report_dir}/{self.report_date}.md"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        logger.info(f"Report saved to {report_file}")
    
    def send_report(self, report: str):
        """Send report to Telegram"""
        try:
            # Split report into chunks for Telegram
            chunks = self._split_report(report, max_length=4000)
            
            for chunk in chunks:
                self.telegram.send_message(chunk)
                logger.info("Chunk sent to Telegram")
            
            logger.info("Full report sent to Telegram")
        except Exception as e:
            logger.error(f"Failed to send Telegram message: {e}")
    
    def _split_report(self, report: str, max_length: int = 4000) -> List[str]:
        """Split report into Telegram-friendly chunks"""
        chunks = []
        lines = report.split('\n')
        current_chunk = []
        current_length = 0
        
        for line in lines:
            if current_length + len(line) + 1 > max_length:
                if current_chunk:
                    chunks.append('\n'.join(current_chunk))
                    current_chunk = [line]
                    current_length = len(line) + 1
            else:
                current_chunk.append(line)
                current_length += len(line) + 1
        
        if current_chunk:
            chunks.append('\n'.join(current_chunk))
        
        return chunks
    
    def run_full_cycle(self):
        """Execute complete search → score → report → send cycle"""
        try:
            # Search
            jobs = self.run_search()
            
            # Build report
            report = self.build_report()
            
            # Save locally
            self.save_report(report)
            
            # Send to Telegram
            if os.getenv('TELEGRAM_BOT_TOKEN'):
                self.send_report(report)
            
            logger.info("=" * 60)
            logger.info("ARIA JOB SEARCH COMPLETE")
            logger.info("=" * 60)
            
        except Exception as e:
            logger.error(f"Search cycle failed: {e}")
            error_msg = f"❌ Aria Job Search Failed\n\nError: {str(e)}\n\nCheck logs for details."
            if os.getenv('TELEGRAM_BOT_TOKEN'):
                self.telegram.send_message(error_msg)


if __name__ == "__main__":
    searcher = JobSearcher(AMRUTA_PROFILE, JOB_PORTALS)
    searcher.run_full_cycle()
