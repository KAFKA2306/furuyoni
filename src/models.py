from dataclass import dataclass
from typing import Dict, List

@dataclass(frozen=True)
class Config:
    model: str
    paths: Dict[str, str]
    urls: Dict[str, str]
    term_mapping: Dict[str, str]

@dataclass(frozen=True)
class CardData:
    megami: str
    card_urls: List[str]
