# DataDrivenAgent Package
# Import main components for easy access

from .data_loader import DataLoader
from .database import Database
from .ai_agent import AIAgent
from .matcher import Matcher
from .proposal_generator import ProposalGenerator

__version__ = "0.1.0"
__all__ = [
    "DataLoader",
    "Database",
    "AIAgent",
    "Matcher",
    "ProposalGenerator",
]
