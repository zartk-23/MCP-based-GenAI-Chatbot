# animator.py - Makes cool live steps
from rich.console import Console
from rich.panel import Panel
from rich import box
import time

console = Console()

def show_step(title, content, color="cyan"):
    panel = Panel(
        f"[bold {color}]{content}[/]",
        title=f"[{color}]{title}[/{color}]",
        border_style=color,
        box=box.ROUNDED
    )
    console.print(panel)
    time.sleep(1.2)  # Pause so you can read