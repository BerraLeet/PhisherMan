def clean_response_blocks(filepath="proxy_output.txt"):
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        cleaned_lines = []
        i = 0

        while i < len(lines):
            current_line = lines[i].strip()
            next_line = lines[i + 1].strip() if i + 1 < len(lines) else ""

            # Clean "=== RESPONSE ===" if next row is "=== REQUEST ==="
            if current_line == "=== RESPONSE ===" and next_line == "=== REQUEST ===":
                i += 1  # Skip response row
            else:
                cleaned_lines.append(lines[i])
                i += 1 # Add cleaned Line

        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(cleaned_lines)

    except Exception as e:
        print(f"Error: {e}")
