"""
Telegram Bot Integration
Sends job reports to Telegram
"""

import requests
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class TelegramSender:
    """Sends messages to Telegram"""
    
    def __init__(self, bot_token: str, chat_id: str):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.base_url = f"https://api.telegram.org/bot{bot_token}"
    
    def send_message(self, text: str, parse_mode: str = 'Markdown') -> bool:
        """
        Send a message to Telegram
        
        Args:
            text: Message text
            parse_mode: 'Markdown' or 'HTML'
        
        Returns:
            True if successful, False otherwise
        """
        if not self.bot_token or not self.chat_id:
            logger.warning("Telegram credentials not configured. Skipping send.")
            return False
        
        try:
            url = f"{self.base_url}/sendMessage"
            payload = {
                'chat_id': self.chat_id,
                'text': text,
                'parse_mode': parse_mode,
                'disable_web_page_preview': True
            }
            
            response = requests.post(url, json=payload, timeout=10)
            
            if response.status_code == 200:
                logger.info("Message sent to Telegram successfully")
                return True
            else:
                logger.error(f"Telegram API error: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            logger.error(f"Failed to send Telegram message: {e}")
            return False
    
    def send_document(self, document_path: str, caption: str = '') -> bool:
        """
        Send a document (file) to Telegram
        
        Args:
            document_path: Path to the file
            caption: Optional caption
        
        Returns:
            True if successful, False otherwise
        """
        if not self.bot_token or not self.chat_id:
            logger.warning("Telegram credentials not configured.")
            return False
        
        try:
            url = f"{self.base_url}/sendDocument"
            
            with open(document_path, 'rb') as f:
                files = {'document': f}
                data = {
                    'chat_id': self.chat_id,
                    'caption': caption,
                    'parse_mode': 'Markdown'
                }
                
                response = requests.post(url, files=files, data=data, timeout=30)
            
            if response.status_code == 200:
                logger.info(f"Document {document_path} sent to Telegram")
                return True
            else:
                logger.error(f"Telegram API error: {response.status_code}")
                return False
                
        except Exception as e:
            logger.error(f"Failed to send Telegram document: {e}")
            return False
    
    def test_connection(self) -> bool:
        """
        Test if Telegram connection is working
        
        Returns:
            True if bot token and chat ID are valid
        """
        if not self.bot_token or not self.chat_id:
            logger.error("Telegram credentials missing")
            return False
        
        try:
            url = f"{self.base_url}/getMe"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                logger.info(f"Telegram connection OK. Bot: {data['result']['username']}")
                return True
            else:
                logger.error(f"Telegram connection failed: {response.status_code}")
                return False
                
        except Exception as e:
            logger.error(f"Telegram connection error: {e}")
            return False


def format_job_card(job: dict, index: int = 0) -> str:
    """
    Format a job as a nice Telegram message card
    
    Args:
        job: Job dictionary
        index: Job number (1-indexed)
    
    Returns:
        Formatted markdown string
    """
    title = job.get('title', 'Unknown')
    company = job.get('company', 'Unknown')
    location = job.get('location', 'Not specified')
    score = job.get('score', 0)
    url = job.get('url', '')
    posted_date = job.get('posted_date', 'Unknown')
    
    card = f"**{index}. {title}**\n"
    card += f"📍 {company} • {location}\n"
    card += f"⭐ Score: {score}/10\n"
    card += f"📅 Posted: {posted_date}\n"
    
    if url:
        card += f"🔗 [View Job]({url})\n"
    
    card += "\n"
    
    return card


def format_report_summary(total_jobs: int, top_job: Optional[dict] = None) -> str:
    """
    Format report summary message
    
    Args:
        total_jobs: Total number of jobs in report
        top_job: Top job match
    
    Returns:
        Formatted markdown string
    """
    summary = "🎯 **Good morning Amruta!**\n\n"
    summary += f"Your job report is ready.\n"
    summary += f"**{total_jobs} fresh opportunities found today.**\n\n"
    
    if top_job:
        summary += f"🏆 **Top Match:**\n"
        summary += f"*{top_job.get('title')}* @ {top_job.get('company')}\n"
        summary += f"Score: **{top_job.get('score')}/10**\n\n"
    
    summary += "Sending full list now...\n"
    
    return summary


def format_action_plan() -> str:
    """Format daily action plan message"""
    plan = "📋 **Your Action Plan Today:**\n\n"
    plan += "1️⃣ Review top 3 matches above\n"
    plan += "2️⃣ Check for bond clauses or service agreements\n"
    plan += "3️⃣ Prepare customized cover letter\n"
    plan += "4️⃣ Set LinkedIn referral reminders\n"
    plan += "5️⃣ Apply to 3-5 best matches\n\n"
    plan += "_That is today's full list. Go get it!_ 🚀"
    
    return plan
