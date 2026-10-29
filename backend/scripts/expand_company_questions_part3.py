import sys
import json

sys.path.insert(0, r'e:\MINI 2.0\backend')
from app.services.company_interview_service import COMPANIES_DATA

PART3_QUESTIONS = {
    "tech-mahindra": {
        1: [
            {
                "question": "In a communication network with packet loss, if 4 packets are transmitted with an independent failure probability of 0.1 for each packet, what is the probability that at least 3 packets arrive successfully?",
                "options": ["0.9477", "0.8523", "0.6561", "0.9855"],
                "answer": "0.9477",
                "explanation": "Binomial distribution: n=4, p=0.9 (success), q=0.1 (failure). P(X >= 3) = P(X=3) + P(X=4) = 4*(0.9)^3*(0.1) + (0.9)^4 = 4*(0.729)*(0.1) + 0.6561 = 0.2916 + 0.6561 = 0.9477."
            }
        ],
        2: [
            {
                "question": "Given an array of strings words, group the anagrams together in any order.\nInput: ['eat','tea','tan','ate','nat','bat']\nOutput: [['bat'],['nat','tan'],['ate','eat','tea']]",
                "expected": ["Hash Map with sorted string as key or 26-char frequency tuple as key", "Group matching anagram words into list values", "O(N * K log K) or O(N * K) time where K is max word length"],
                "model_answer": "Use a dictionary mapping a canonical key to a list of anagrams. For each word, sort its characters (e.g. sorted('eat') -> 'aet') and use it as dictionary key. Append the original word to dict['aet']. Return list of dict values in O(N * K log K) time."
            }
        ],
        3: [
            {
                "question": "What is Network Slicing in 5G telecommunication networks, and how does software-defined networking (SDN) enable it?",
                "expected": ["Virtual multiplexed logical networks on shared physical infrastructure", "SDN separates control plane from data plane", "Customized slices for low latency (URLLC), high bandwidth (eMBB), and IoT (mMTC)"]
            }
        ]
    },
    "ltimindtree": {
        1: [
            {
                "question": "What is the output of the following Java snippet?\npublic class Test {\n  public static void main(String[] args) {\n    String s1 = 'LTI';\n    String s2 = new String('LTI');\n    System.out.println((s1 == s2) + ' ' + s1.equals(s2));\n  }\n}",
                "options": ["false true", "true true", "false false", "true false"],
                "answer": "false true",
                "explanation": "'==' compares object memory references: s1 is in String Constant Pool, s2 is a new heap object (different addresses => false). '.equals()' compares string content character by character ('LTI' == 'LTI' => true)."
            }
        ],
        2: [
            {
                "question": "Given a singly linked list, reverse the nodes of the list in-place and return the reversed list.\nInput: 1 -> 2 -> 3 -> 4 -> 5\nOutput: 5 -> 4 -> 3 -> 2 -> 1",
                "expected": ["Three pointers (prev, curr, next)", "Iterative pointer reversal in O(N) time and O(1) space", "Null termination of former head node"],
                "model_answer": "Initialize prev = None, curr = head. While curr is not None: next_node = curr.next, curr.next = prev, prev = curr, curr = next_node. Returns prev as the new head in O(N) time and O(1) space."
            }
        ],
        3: [
            {
                "question": "Explain the difference between Optimistic Concurrency Control and Pessimistic Locking in enterprise relational databases. When is optimistic locking preferred?",
                "expected": ["Pessimistic locking uses SELECT FOR UPDATE and blocks other transactions", "Optimistic concurrency uses version column / timestamp and checks on commit", "Optimistic is preferred when read contention is high and write conflicts are rare"]
            }
        ]
    },
    "hcl": {
        1: [
            {
                "question": "A complete binary tree has 250 leaf nodes. How many total nodes does the tree have if every non-leaf node has exactly two children?",
                "options": ["499", "500", "501", "251"],
                "answer": "499",
                "explanation": "In any strictly binary tree where every internal node has 2 children: Total Leaves L = Internal Nodes I + 1 => I = L - 1 = 250 - 1 = 249. Total Nodes = L + I = 250 + 249 = 499."
            }
        ],
        2: [
            {
                "question": "Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i], without using the division operator in O(N) time.",
                "expected": ["Prefix products pass from left", "Suffix products pass from right", "O(N) time and O(1) auxiliary space (excluding output array)"],
                "model_answer": "Initialize output array with 1s. Compute prefix products: answer[i] = answer[i-1] * nums[i-1]. Then maintain a running suffix product from right to left: multiply answer[i] by suffix, then update suffix *= nums[i]. Runs in O(N) time with no division."
            }
        ]
    },
    "ibm": {
        1: [
            {
                "question": "In Linux systems engineering, what is the role of an Inode in the Ext4 filesystem?",
                "options": ["An Inode stores file metadata (size, permissions, owner, timestamps, and data block pointers) but not file content or filename", "An Inode stores the file's name and user password", "An Inode is an encrypted zip compression algorithm", "An Inode runs the Linux bootloader"],
                "answer": "An Inode stores file metadata (size, permissions, owner, timestamps, and data block pointers) but not file content or filename",
                "explanation": "Inodes store all filesystem metadata and disk block pointers for a file. Directory entries map filenames to their corresponding inode numbers."
            }
        ],
        2: [
            {
                "question": "Design an algorithm to find the diameter of a Binary Tree (the longest path between any two nodes in a tree, which may or may not pass through the root).",
                "expected": ["Post-order DFS traversal", "Calculate max_depth of left and right subtrees", "Diameter at node = left_depth + right_depth", "Update global max diameter in O(N) time"],
                "model_answer": "Maintain a global variable max_diameter = 0. Helper function depth(node): if node is None return 0. Recursively calculate L = depth(node.left), R = depth(node.right). max_diameter = max(max_diameter, L + R). Return max(L, R) + 1. Returns max_diameter in O(N) time."
            }
        ]
    },
    "deloitte": {
        1: [
            {
                "question": "What is the fundamental difference between Symmetric Encryption (e.g. AES) and Asymmetric Encryption (e.g. RSA) in enterprise security architectures?",
                "options": ["Symmetric uses a single shared secret key for both encryption and decryption; Asymmetric uses a public-private key pair", "Symmetric encryption only works on numbers; Asymmetric only on text", "Asymmetric encryption runs 1000x faster than Symmetric", "Symmetric encryption does not require keys"],
                "answer": "Symmetric uses a single shared secret key for both encryption and decryption; Asymmetric uses a public-private key pair",
                "explanation": "AES symmetric encryption is fast and encrypts bulk data. Asymmetric RSA/ECC uses public key for encryption and private key for decryption, solving secure key exchange."
            }
        ],
        2: [
            {
                "question": "Describe how you would design an audit trail and role-based access control (RBAC) mechanism for an enterprise financial analytics dashboard.",
                "expected": ["Immutable append-only audit event log table", "RBAC with Users, Roles, and Permissions", "JWT claims containing role permissions checked in API gateway middleware", "Cryptographic hashing of sensitive financial records"]
            }
        ]
    }
}

for company in COMPANIES_DATA:
    slug = company["slug"].lower()
    if slug in PART3_QUESTIONS:
        rounds_dict = PART3_QUESTIONS[slug]
        for round_item in company["rounds"]:
            r_num = round_item["round_number"]
            if r_num in rounds_dict:
                existing_qs = round_item.setdefault("sample_questions", [])
                for new_q in rounds_dict[r_num]:
                    if not any(eq.get("question") == new_q["question"] for eq in existing_qs):
                        existing_qs.append(new_q)

total_after = sum(len(r.get("sample_questions", [])) for c in COMPANIES_DATA for r in c["rounds"])
print(f"Total company sample questions is now: {total_after}")

service_file_path = r'e:\MINI 2.0\backend\app\services\company_interview_service.py'

header = '''from typing import List, Dict, Any, Optional

COMPANIES_DATA = '''

footer = '''

class CompanyInterviewService:
    def list_companies(self) -> List[Dict[str, Any]]:
        return [
            {
                "id": c["id"],
                "name": c["name"],
                "slug": c["slug"],
                "badge": c["badge"],
                "package": c["package"],
                "hiring_season": c["hiring_season"],
                "eligibility": c["eligibility"],
                "description": c["description"],
                "rounds_count": len(c["rounds"]),
                "rounds_summary": [f"Round {r['round_number']}: {r['name']}" for r in c["rounds"]]
            }
            for c in COMPANIES_DATA
        ]

    def get_company(self, slug: str) -> Optional[Dict[str, Any]]:
        for c in COMPANIES_DATA:
            if c["slug"].lower() == slug.lower() or c["id"].lower() == slug.lower():
                return c
        return None

    def add_question(self, slug: str, round_number: int, question_data: Dict[str, Any]) -> bool:
        comp = self.get_company(slug)
        if not comp:
            return False
        for r in comp["rounds"]:
            if r["round_number"] == round_number:
                r.setdefault("sample_questions", []).append(question_data)
                return True
        return False

company_service = CompanyInterviewService()
'''

with open(service_file_path, 'w', encoding='utf-8') as f:
    f.write(header)
    json.dump(COMPANIES_DATA, f, indent=4, ensure_ascii=False)
    f.write(footer)

print(f"Successfully updated {service_file_path} with Part 3 expanded questions!")

