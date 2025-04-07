
import argparse
from src.ai_recon import recon
from src.stealth_mode import stealth
from src.role_access import access

def main():
    parser = argparse.ArgumentParser(description="Secure Training Simulation CLI")
    parser.add_argument("--mode", choices=["recon", "stealth", "auth"], help="Choose CLI mode")
    args = parser.parse_args()

    if args.mode == "recon":
        recon.generate_report()
    elif args.mode == "stealth":
        stealth.launch_stealth_dashboard()
    elif args.mode == "auth":
        access.authenticate_user()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
