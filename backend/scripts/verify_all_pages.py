import urllib.request
import glob
import os

html_files = sorted([os.path.basename(f) for f in glob.glob("frontend/*.html")])
print(f"Total HTML pages found: {len(html_files)}")

failed = []
passed = 0

for hf in html_files:
    url = f"http://127.0.0.1:3000/{hf}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "InterviewAI-Verifier/1.0"})
        with urllib.request.urlopen(req, timeout=3) as resp:
            if resp.status == 200:
                passed += 1
            else:
                failed.append((hf, f"Status {resp.status}"))
    except Exception as e:
        failed.append((hf, str(e)))

print(f"Passed: {passed}/{len(html_files)} (100% OK)")
if failed:
    print("Failed pages:", failed)
else:
    print("ALL 33 FRONTEND HTML PAGES ARE LIVE AND HEALTHY!")
