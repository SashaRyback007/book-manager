from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int
    pages: int

    @property
    def short_info(self) -> str:
        return f"'{self.title}' by {self.author} ({self.year})"