import re, subprocess, pathlib

src = pathlib.Path("index.html").read_text(encoding="utf-8")
n = 0
for i, (attrs, body) in enumerate(re.findall(r"<script([^>]*)>(.*?)</script>", src, re.S)):
    if body.strip() and "json" not in attrs and "importmap" not in attrs:
        ext = "mjs" if "module" in attrs else "js"
        p = pathlib.Path(f"/tmp/s{i}.{ext}")
        p.write_text(body, encoding="utf-8")
        subprocess.run(["node", "--check", str(p)], check=True)
        n += 1
print(f"script syntax OK ({n} scripts)")
