from rich.console import Console
from rich.panel import Panel
import argparse
import os

console = Console()

def simulate():
    console.print("[bold cyan]Simulating scenario...[/bold cyan]")
    # Placeholder logic
    console.print("Simulation complete.")

def replay(file):
    console.print(f"[bold yellow]Replaying from log: {file}[/bold yellow]")
    # Placeholder logic
    console.print("Replay finished.")

def logview():
    console.print("[bold green]Viewing logs...[/bold green]")
    logs_path = os.path.expanduser("~/.simulation/logs/")
    if not os.path.exists(logs_path):
        console.print("[red]No logs found.[/red]")
        return
    for root, _, files in os.walk(logs_path):
        for file in files:
            console.print(f"[white]- {file}[/white]")

def main():
    parser = argparse.ArgumentParser(description="Training Simulation System CLI")
    parser.add_argument("--simulate", action="store_true", help="Run simulation scenario")
    parser.add_argument("--replay", type=str, help="Replay a specific log file")
    parser.add_argument("--logview", action="store_true", help="View available logs")

    args = parser.parse_args()

    if args.simulate:
        simulate()
    elif args.replay:
        replay(args.replay)
    elif args.logview:
        logview()
    else:
        console.print(Panel("[bold]Training Simulation CLI[/bold]\nUse --simulate | --replay <file> | --logview", title="Welcome"))

if __name__ == "__main__":
    main()