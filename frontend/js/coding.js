/**
 * InterviewAI — Coding Practice Controller
 * Connects problem browser to execution runner with multi-language starter templates.
 */

let allProblems = [];
let activeProblem = null;

const STARTER_TEMPLATES = {
  python: `def solution():\n    # Write your solution here\n    pass\n`,
  javascript: `function solution() {\n    // Write your solution here\n}\n`,
  java: `public class Solution {\n    public static void main(String[] args) {\n        // Write your solution here\n    }\n}\n`,
  cpp: `#include <iostream>\nusing namespace std;\n\nint main() {\n    // Write your solution here\n    return 0;\n}\n`
};

document.addEventListener('DOMContentLoaded', async () => {
  const user = await auth.requireAuth();
  if (!user) return;

  initFilters();
  bindEditorEvents();
  loadProblems();
});

function initFilters() {
  const catFilter = document.getElementById('categoryFilter');
  const diffFilter = document.getElementById('difficultyFilter');
  const searchInput = document.getElementById('searchProblemInput');

  if (catFilter) catFilter.addEventListener('change', renderProblemList);
  if (diffFilter) diffFilter.addEventListener('change', renderProblemList);
  if (searchInput) searchInput.addEventListener('input', renderProblemList);

  const langSelect = document.getElementById('languageSelect');
  if (langSelect) {
    langSelect.addEventListener('change', () => {
      const lang = langSelect.value;
      if (activeProblem && activeProblem.starter_code_json && activeProblem.starter_code_json[lang]) {
        document.getElementById('codeEditor').value = activeProblem.starter_code_json[lang];
      } else {
        document.getElementById('codeEditor').value = STARTER_TEMPLATES[lang] || '';
      }
    });
  }

  const hintsBtn = document.getElementById('viewHintsBtn');
  if (hintsBtn) {
    hintsBtn.addEventListener('click', () => {
      const container = document.getElementById('hintsContainer');
      container.style.display = container.style.display === 'none' ? 'block' : 'none';
    });
  }
}

async function loadProblems() {
  const listEl = document.getElementById('problemList');
  try {
    const data = await api.get('/coding/problems');
    allProblems = data || [];
    renderProblemList();

    // Automatically select first problem
    if (allProblems.length > 0) {
      selectProblem(allProblems[0].id);
    }
  } catch (err) {
    console.error('Failed to load problems:', err);
    if (listEl) {
      listEl.innerHTML = `<div style="text-align:center;padding:2rem 1rem;color:#ef4444;">Failed to load coding library.</div>`;
    }
  }
}

function renderProblemList() {
  const listEl = document.getElementById('problemList');
  if (!listEl) return;

  const cat = document.getElementById('categoryFilter').value.toLowerCase();
  const diff = document.getElementById('difficultyFilter').value.toLowerCase();
  const q = document.getElementById('searchProblemInput').value.toLowerCase();

  const filtered = allProblems.filter(p => {
    const matchCat = cat === 'all' || (p.category && p.category.toLowerCase().includes(cat));
    const matchDiff = diff === 'all' || (p.difficulty && p.difficulty.toLowerCase() === diff);
    const matchQ = !q || p.title.toLowerCase().includes(q);
    return matchCat && matchDiff && matchQ;
  });

  if (filtered.length === 0) {
    listEl.innerHTML = `<div style="text-align:center;padding:2rem 1rem;color:var(--color-text-subtle);font-size:0.875rem;">No matching problems found.</div>`;
    return;
  }

  let html = '';
  filtered.forEach(p => {
    const isActive = activeProblem && activeProblem.id === p.id;
    let badgeClass = 'badge-primary';
    if (p.difficulty === 'Easy') badgeClass = 'badge-success';
    else if (p.difficulty === 'Hard') badgeClass = 'badge-danger';
    else if (p.difficulty === 'Medium') badgeClass = 'badge-warning';

    html += `
      <div class="problem-item card" data-id="${p.id}" style="padding:0.75rem; cursor:pointer; border-color:${isActive ? 'var(--color-primary)' : 'var(--color-border)'}; background:${isActive ? 'var(--color-primary-light)' : '#ffffff'};">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.25rem;">
          <span style="font-weight:600; font-size:0.875rem; color:var(--color-text-main);">${escapeHtml(p.title)}</span>
          <span class="badge ${badgeClass}" style="font-size:0.7rem; padding:0.15rem 0.45rem;">${p.difficulty}</span>
        </div>
        <div style="font-size:0.75rem; color:var(--color-text-subtle); display:flex; justify-content:space-between;">
          <span>${escapeHtml(p.category || 'Algorithms')}</span>
          ${p.is_solved ? '<span style="color:#059669;font-weight:600;">✓ Solved</span>' : ''}
        </div>
      </div>
    `;
  });

  listEl.innerHTML = html;

  // Bind click
  listEl.querySelectorAll('.problem-item').forEach(el => {
    el.addEventListener('click', () => {
      const id = parseInt(el.dataset.id, 10);
      selectProblem(id);
    });
  });
}

async function selectProblem(id) {
  try {
    const detail = await api.get(`/coding/problems/${id}`);
    if (!detail) return;

    activeProblem = detail;
    renderProblemList(); // updates highlight

    // Update Header
    document.getElementById('currentProblemTitle').textContent = detail.title;
    const diffBadge = document.getElementById('currentProblemDifficulty');
    diffBadge.textContent = detail.difficulty;
    diffBadge.className = `badge ${detail.difficulty === 'Easy' ? 'badge-success' : detail.difficulty === 'Hard' ? 'badge-danger' : 'badge-warning'}`;
    document.getElementById('currentProblemCategory').textContent = detail.category || 'Algorithms';

    document.getElementById('timeComplexityVal').textContent = detail.time_complexity || 'O(N)';
    document.getElementById('spaceComplexityVal').textContent = detail.space_complexity || 'O(1)';

    // Description & Examples
    document.getElementById('problemDescription').textContent = detail.description;

    const examplesEl = document.getElementById('problemExamples');
    if (detail.examples_json && detail.examples_json.length > 0) {
      let exHtml = '<strong>Examples:</strong><div style="display:flex;flex-direction:column;gap:0.5rem;margin-top:0.35rem;">';
      detail.examples_json.forEach((ex, idx) => {
        exHtml += `
          <div style="background:var(--color-bg-page);border:1px solid var(--color-border);padding:0.6rem;border-radius:var(--radius-sm);font-family:var(--font-mono);font-size:0.8125rem;">
            <div><strong>Input:</strong> ${escapeHtml(ex.input)}</div>
            <div><strong>Output:</strong> ${escapeHtml(ex.output)}</div>
            ${ex.explanation ? `<div style="color:var(--color-text-muted);font-size:0.75rem;margin-top:0.25rem;">${escapeHtml(ex.explanation)}</div>` : ''}
          </div>
        `;
      });
      exHtml += '</div>';
      examplesEl.innerHTML = exHtml;
    } else {
      examplesEl.innerHTML = '';
    }

    // Constraints
    const constraintsEl = document.getElementById('problemConstraints');
    if (detail.constraints) {
      constraintsEl.innerHTML = `<strong>Constraints:</strong> ${escapeHtml(detail.constraints)}`;
    } else {
      constraintsEl.innerHTML = '';
    }

    // Hints
    const hintContent = document.getElementById('hintContent');
    if (detail.hints_json && detail.hints_json.length > 0) {
      hintContent.textContent = detail.hints_json.join(' ');
      document.getElementById('viewHintsBtn').style.display = 'inline-flex';
    } else {
      hintContent.textContent = 'Consider breaking down the problem into sub-problems or using two pointers.';
    }
    document.getElementById('hintsContainer').style.display = 'none';

    // Populate Starter Code
    const lang = document.getElementById('languageSelect').value;
    if (detail.starter_code_json && detail.starter_code_json[lang]) {
      document.getElementById('codeEditor').value = detail.starter_code_json[lang];
    } else {
      document.getElementById('codeEditor').value = STARTER_TEMPLATES[lang] || '';
    }

    // Reset console
    document.getElementById('consoleOutput').textContent = 'Ready for execution.';
    const statusBadge = document.getElementById('testStatusBadge');
    statusBadge.className = 'badge badge-neutral';
    statusBadge.textContent = 'Ready';

  } catch (err) {
    console.error('Failed to select problem:', err);
  }
}

function bindEditorEvents() {
  const runBtn = document.getElementById('runCodeBtn');
  const submitBtn = document.getElementById('submitCodeBtn');

  if (runBtn) {
    runBtn.addEventListener('click', () => executeCode(false));
  }
  if (submitBtn) {
    submitBtn.addEventListener('click', () => executeCode(true));
  }
}

async function executeCode(isSubmission = false) {
  if (!activeProblem) {
    showToast('Please select a problem first.', 'info');
    return;
  }

  const code = document.getElementById('codeEditor').value;
  const lang = document.getElementById('languageSelect').value;
  const consoleEl = document.getElementById('consoleOutput');
  const statusBadge = document.getElementById('testStatusBadge');

  statusBadge.className = 'badge badge-warning';
  statusBadge.textContent = isSubmission ? 'Evaluating...' : 'Running...';
  consoleEl.textContent = 'Submitting code to sandboxed execution runner...';

  try {
    const res = await api.post('/coding/submissions', {
      problem_id: activeProblem.id,
      language: lang,
      code: code
    });

    if (res.status === 'accepted') {
      statusBadge.className = 'badge badge-success';
      statusBadge.textContent = 'Accepted';
      showToast('All test cases passed! Solution Accepted.', 'success');
      activeProblem.is_solved = true;
      renderProblemList();
    } else if (res.status === 'wrong_answer') {
      statusBadge.className = 'badge badge-danger';
      statusBadge.textContent = 'Wrong Answer';
    } else {
      statusBadge.className = 'badge badge-neutral';
      statusBadge.textContent = res.status || 'Evaluated';
    }

    let outText = `Verdict: ${res.status.toUpperCase()}\n`;
    if (res.message) outText += `${res.message}\n\n`;
    if (res.passed_tests !== undefined && res.total_tests !== undefined) {
      outText += `Passed: ${res.passed_tests} / ${res.total_tests} test cases\n`;
    }
    if (res.test_results && res.test_results.length > 0) {
      res.test_results.forEach((t, i) => {
        outText += `Test #${i+1}: ${t.passed ? 'PASSED' : 'FAILED'} (Input: ${t.input} | Expected: ${t.expected} | Got: ${t.got || 'N/A'})\n`;
      });
    }

    consoleEl.textContent = outText;

  } catch (err) {
    statusBadge.className = 'badge badge-danger';
    statusBadge.textContent = 'Execution Error';
    consoleEl.textContent = `Execution failed: ${err.message || 'Execution runner unavailable.'}`;
  }
}
