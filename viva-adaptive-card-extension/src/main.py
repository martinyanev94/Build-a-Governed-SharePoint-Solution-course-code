from dataclasses import dataclass
from typing import Optional


@dataclass
class NorthstarCard:
    days_without_accidents: int
    acknowledged_by: Optional[str] = None

    def render(self) -> dict[str, object]:
        return {
            "title": "Safety",
            "summary": f"{self.days_without_accidents} days without an accident",
            "action": "Acknowledged" if self.acknowledged_by else "Acknowledge",
            "status": self.acknowledged_by or "Action required",
        }

    def acknowledge(self, actor: str) -> dict[str, object]:
        if not actor.strip():
            raise ValueError("actor is required")
        self.acknowledged_by = actor.strip()
        return self.render()


def demo() -> None:
    card = NorthstarCard(days_without_accidents=12)
    print(card.render())
    print(card.acknowledge("Jordan Lee"))


if __name__ == "__main__":
    demo()
