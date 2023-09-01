import subprocess
import sys

def run_subprocess(campaign_id, identifier, session_vol):
    command_template = (
        "python3 agent_manager.py -c '{identifier}' -a send_campaign -i {campaign_id}"
    )

    for _ in range(session_vol):
        command = command_template.format(identifier=identifier, campaign_id=campaign_id)
        subprocess.Popen(command, shell=True)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python script.py <campaign_id> <identifier> <session_vol>")
        sys.exit(1)

    campaign_id = sys.argv[1]
    identifier = sys.argv[2]
    session_vol = int(sys.argv[3])

    run_subprocess(campaign_id, identifier, session_vol)
