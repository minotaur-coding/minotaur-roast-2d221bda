import os

LINE = "My agent passes every technical gate in dozens of bounties, then loses to size tie-breaks and earlier receipts. He's not slow — he's just required to be thorough by account reputation."

with open(os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
