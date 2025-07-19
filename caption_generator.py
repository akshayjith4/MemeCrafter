def extract_captions(text):
    import re
    pattern = r'\*\*Option\s+\d+\s*\([^)]+\)\s*:\*\*\s*["“](.*?)["”]'
    matches = re.findall(pattern, text, re.DOTALL)

    if not matches:
        print("⚠️ No captions matched regex, trying fallback pattern.")
        fallback = re.findall(r'"(.*?)"', text)
        return [f.strip() for f in fallback if len(f.strip()) > 10]  # filter noise

    return [m.strip() for m in matches]
