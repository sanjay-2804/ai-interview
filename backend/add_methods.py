path = 'e:/MINI 2.0/backend/app/services/company_interview_service.py'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

target = 'company_service = CompanyInterviewService()'
addition = '''    def add_company(self, data: dict) -> dict:
        slug = data.get("slug") or data.get("name", "").lower().replace(" ", "-")
        data["slug"] = slug
        data["id"] = data.get("id") or slug
        if "rounds" not in data:
            data["rounds"] = []
        COMPANIES_DATA.append(data)
        return data

    def update_company(self, slug: str, data: dict):
        for idx, c in enumerate(COMPANIES_DATA):
            if c["slug"].lower() == slug.lower() or c["id"].lower() == slug.lower():
                COMPANIES_DATA[idx].update(data)
                return COMPANIES_DATA[idx]
        return None

    def delete_company(self, slug: str) -> bool:
        for idx, c in enumerate(COMPANIES_DATA):
            if c["slug"].lower() == slug.lower() or c["id"].lower() == slug.lower():
                COMPANIES_DATA.pop(idx)
                return True
        return False

'''

if 'def add_company' not in text:
    new_text = text.replace(target, addition + target)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Methods appended successfully")
else:
    print("Methods already exist")
