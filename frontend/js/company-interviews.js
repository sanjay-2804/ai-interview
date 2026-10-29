/**
 * InterviewAI — Company-Specific Placement Drives Controller
 * Handles Multi-Round Recruitment Simulations for TCS, Infosys, Amazon, Accenture, Wipro, and Cognizant.
 */

let allCompanies = [];
let activeCompany = null;
let activeRound = null;
let activeQuestionIndex = 0;
let currentFilter = 'all';

document.addEventListener('DOMContentLoaded', async () => {
  const user = await auth.requireAuth();
  if (!user) return;

  loadCompanyDrives();
  bindCompanyEvents();
  bindCompanyFilterEvents();
});

async function loadCompanyDrives() {
  const grid = document.getElementById('companyCardsGrid');
  try {
    const data = await api.get('/interviews/companies');
    allCompanies = data || [];
    renderCompanyGrid(allCompanies);
  } catch (err) {
    console.error('Failed to load company drives:', err);
    grid.innerHTML = `<div style="text-align:center;padding:2rem;color:#ef4444;">Failed to load company specifications.</div>`;
  }
}

function renderCompanyGrid(companies) {
  const grid = document.getElementById('companyCardsGrid');
  if (!companies || companies.length === 0) {
    grid.innerHTML = `<div style="text-align:center;padding:3rem;color:var(--color-text-subtle);grid-column:1/-1;">No companies match your search criteria.</div>`;
    return;
  }

  let html = '';
  companies.forEach(c => {
    let roundsSummaryHtml = '';
    if (c.rounds_summary) {
      roundsSummaryHtml = c.rounds_summary.map(r => `<div style="font-size:0.75rem;color:var(--color-text-muted);display:flex;align-items:center;gap:0.35rem;"><i data-lucide="check" style="width:12px;height:12px;color:var(--color-success);"></i> ${escapeHtml(r)}</div>`).join('');
    }

    html += `
      <div class="card company-card" data-slug="${c.slug}" style="cursor:pointer; display:flex; flex-direction:column; justify-content:space-between; padding:1.75rem; transition:transform 0.2s, box-shadow 0.2s;">
        <div>
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.75rem;">
            <span class="badge badge-primary">${escapeHtml(c.badge || 'Campus Drive')}</span>
            <span style="font-weight:700; color:var(--color-primary); font-size:0.9375rem;">${escapeHtml(c.package)}</span>
          </div>

          <h3 style="font-size:1.3rem; margin-bottom:0.35rem; color:var(--color-text-main);">${escapeHtml(c.name)}</h3>
          <p style="font-size:0.875rem; color:var(--color-text-muted); line-height:1.5; margin-bottom:1rem;">
            ${escapeHtml(c.description)}
          </p>

          <div style="padding:0.75rem; background:var(--color-bg-page); border-radius:var(--radius-md); border:1px solid var(--color-border); margin-bottom:1.25rem;">
            <div style="font-size:0.75rem; font-weight:700; color:var(--color-text-subtle); text-transform:uppercase; margin-bottom:0.35rem;">Selection Rounds (${c.rounds_count} Rounds)</div>
            <div style="display:flex; flex-direction:column; gap:0.25rem;">
              ${roundsSummaryHtml}
            </div>
          </div>
        </div>

        <div>
          <button class="btn btn-primary btn-sm btn-full view-company-btn" data-slug="${c.slug}">
            <i data-lucide="play" style="width:14px;height:14px;"></i> Start Company Drive Simulator
          </button>
        </div>
      </div>
    `;
  });

  grid.innerHTML = html;
  if (window.lucide) lucide.createIcons();

  // Bind company clicks
  grid.querySelectorAll('.company-card').forEach(card => {
    card.addEventListener('click', () => {
      const slug = card.dataset.slug;
      openCompanyDetail(slug);
    });
  });

  grid.querySelectorAll('.view-company-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const slug = btn.dataset.slug;
      openCompanyDetail(slug);
    });
  });
}

function bindCompanyFilterEvents() {
  const searchInput = document.getElementById('companySearchInput');
  if (searchInput) {
    searchInput.addEventListener('input', () => filterCompanies());
  }

  document.querySelectorAll('.company-filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.company-filter-btn').forEach(b => {
        b.classList.remove('active', 'btn-primary');
        b.classList.add('btn-secondary');
      });
      btn.classList.add('active', 'btn-primary');
      btn.classList.remove('btn-secondary');
      currentFilter = btn.dataset.filter;
      filterCompanies();
    });
  });
}

function filterCompanies() {
  const query = (document.getElementById('companySearchInput')?.value || '').toLowerCase().trim();
  const productSlugs = ['amazon', 'microsoft', 'google', 'oracle', 'adobe', 'zoho', 'cisco', 'walmart', 'freshworks', 'flipkart', 'paypal'];
  const itSlugs = ['tcs', 'infosys', 'wipro', 'cognizant', 'hcltech', 'techmahindra', 'ltimindtree', 'ibm'];
  const consultingSlugs = ['accenture', 'deloitte', 'capgemini'];

  const filtered = allCompanies.filter(c => {
    const matchesQuery = !query || c.name.toLowerCase().includes(query) || (c.description || '').toLowerCase().includes(query) || (c.badge || '').toLowerCase().includes(query) || (c.package || '').toLowerCase().includes(query);
    if (!matchesQuery) return false;

    if (currentFilter === 'product') return productSlugs.includes(c.slug);
    if (currentFilter === 'it') return itSlugs.includes(c.slug);
    if (currentFilter === 'consulting') return consultingSlugs.includes(c.slug);
    return true;
  });

  renderCompanyGrid(filtered);
}

async function openCompanyDetail(slug) {
  try {
    const comp = await api.get(`/interviews/companies/${slug}`);
    if (!comp) return;

    activeCompany = comp;

    document.getElementById('detailCompanyName').textContent = comp.name;
    document.getElementById('detailBadge').textContent = comp.badge;
    document.getElementById('detailDescription').textContent = comp.description;
    document.getElementById('detailPackage').textContent = comp.package;
    document.getElementById('detailEligibility').textContent = `Eligibility: ${comp.eligibility}`;

    const roundsContainer = document.getElementById('roundsListContainer');
    let rHtml = '';

    comp.rounds.forEach(r => {
      let sectionsHtml = '';
      if (r.sections) {
        sectionsHtml = r.sections.map(s => `<span class="badge badge-neutral" style="font-size:0.75rem;">${escapeHtml(s)}</span>`).join(' ');
      }

      rHtml += `
        <div class="card" style="padding:1.5rem; border-left:4px solid var(--color-primary); display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
          <div style="max-width:650px;">
            <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.25rem;">
              <span class="badge badge-primary">Round ${r.round_number}</span>
              <h4 style="font-size:1.15rem; margin:0;">${escapeHtml(r.name)}</h4>
              <span class="badge badge-warning" style="font-size:0.7rem;">Cutoff: ${r.cutoff_percentage}%</span>
            </div>
            <div style="font-size:0.8125rem; color:var(--color-text-subtle); margin-bottom:0.5rem;">
              Duration: ${r.duration_minutes} mins • Format: ${escapeHtml(r.type)}
            </div>
            <div style="display:flex; flex-wrap:wrap; gap:0.35rem; margin-bottom:0.5rem;">
              ${sectionsHtml}
            </div>
            <div style="font-size:0.8125rem; color:var(--color-text-muted);">
              <strong>Recruiter Tip:</strong> ${escapeHtml(r.tips)}
            </div>
          </div>

          <div>
            <button class="btn btn-outline btn-sm launch-round-btn" data-round="${r.round_number}">
              Practice Round ${r.round_number}
            </button>
          </div>
        </div>
      `;
    });

    roundsContainer.innerHTML = rHtml;

    // Bind round launch
    roundsContainer.querySelectorAll('.launch-round-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const roundNum = parseInt(btn.dataset.round, 10);
        launchRoundSimulator(roundNum);
      });
    });

    showView('companyDetailView');

  } catch (err) {
    showToast('Failed to load company detail.', 'error');
  }
}

function launchRoundSimulator(roundNum) {
  if (!activeCompany) return;
  const round = activeCompany.rounds.find(r => r.round_number === roundNum);
  if (!round) return;

  activeRound = round;
  activeQuestionIndex = 0;

  document.getElementById('activeRoundCompanyBadge').textContent = activeCompany.name;
  document.getElementById('activeRoundTitle').textContent = `Round ${round.round_number}: ${round.name}`;
  document.getElementById('activeRoundCutoffBadge').textContent = `Cutoff: ${round.cutoff_percentage}% Required`;
  document.getElementById('activeRoundTip').textContent = round.tips;

  renderActiveQuestion();
  showView('activeRoundView');
}

function renderActiveQuestion() {
  if (!activeRound) return;
  const questions = activeRound.sample_questions || [];
  const total = Math.max(1, questions.length);
  const sampleQObj = questions[activeQuestionIndex] || {
    question: "Describe your solution approach and walk through the algorithm step by step."
  };

  // Update badge and pagination buttons
  const badge = document.getElementById('activeRoundQuestionBadge');
  if (badge) badge.textContent = `Question ${activeQuestionIndex + 1} of ${total}`;

  const prevBtn = document.getElementById('prevQuestionBtn');
  if (prevBtn) prevBtn.disabled = activeQuestionIndex <= 0;

  const nextBtn = document.getElementById('nextQuestionBtn');
  if (nextBtn) nextBtn.disabled = activeQuestionIndex >= questions.length - 1;

  document.getElementById('activeRoundQuestion').textContent = sampleQObj.question;
  const responseInput = document.getElementById('activeRoundResponse');
  responseInput.value = '';
  responseInput.disabled = false;
  document.getElementById('roundVerdictCard').style.display = 'none';

  const submitBtn = document.getElementById('submitRoundResponseBtn');
  if (submitBtn) {
    submitBtn.disabled = false;
    submitBtn.style.display = 'inline-flex';
  }

  const progBtn = document.getElementById('roundNextProgressionBtn');
  if (progBtn) progBtn.style.display = 'none';

  const optionsGrid = document.getElementById('activeRoundOptionsGrid');
  const textareaGroup = document.getElementById('activeRoundTextareaGroup');

  if (sampleQObj.options && Array.isArray(sampleQObj.options)) {
    optionsGrid.style.display = 'flex';
    optionsGrid.innerHTML = '';
    sampleQObj.options.forEach((optText, i) => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'option-btn';
      btn.innerHTML = `<span class="option-key-badge">${String.fromCharCode(65 + i)}</span> <span>${escapeHtml(optText)}</span>`;
      btn.addEventListener('click', () => {
        if (btn.disabled) return;
        optionsGrid.querySelectorAll('.option-btn').forEach(b => b.classList.remove('selected'));
        btn.classList.add('selected');
        document.getElementById('activeRoundResponse').value = optText;
      });
      optionsGrid.appendChild(btn);
    });
    textareaGroup.style.display = 'none';
  } else {
    optionsGrid.style.display = 'none';
    textareaGroup.style.display = 'block';
  }

  if (window.lucide) lucide.createIcons();
}

function bindCompanyEvents() {
  const backToCompaniesBtn = document.getElementById('backToCompaniesBtn');
  if (backToCompaniesBtn) {
    backToCompaniesBtn.addEventListener('click', () => showView('companiesView'));
  }

  const backToDetailBtn = document.getElementById('backToDetailBtn');
  if (backToDetailBtn) {
    backToDetailBtn.addEventListener('click', () => showView('companyDetailView'));
  }

  const prevQuestionBtn = document.getElementById('prevQuestionBtn');
  if (prevQuestionBtn) {
    prevQuestionBtn.addEventListener('click', () => {
      if (activeQuestionIndex > 0) {
        activeQuestionIndex--;
        renderActiveQuestion();
      }
    });
  }

  const nextQuestionBtn = document.getElementById('nextQuestionBtn');
  if (nextQuestionBtn) {
    nextQuestionBtn.addEventListener('click', () => {
      if (activeRound && activeRound.sample_questions && activeQuestionIndex < activeRound.sample_questions.length - 1) {
        activeQuestionIndex++;
        renderActiveQuestion();
      }
    });
  }

  const submitBtn = document.getElementById('submitRoundResponseBtn');
  if (submitBtn) {
    submitBtn.addEventListener('click', submitRoundResponse);
  }
}

async function submitRoundResponse() {
  if (!activeCompany || !activeRound) return;
  const responseText = document.getElementById('activeRoundResponse').value.trim();
  if (!responseText) {
    showToast('Please select or type your response before submitting.', 'info');
    return;
  }

  const submitBtn = document.getElementById('submitRoundResponseBtn');
  setButtonLoading(submitBtn, true, 'Evaluating against company rubric...');

  try {
    const payload = {
      round_number: activeRound.round_number,
      question: document.getElementById('activeRoundQuestion').textContent.trim(),
      student_response: responseText
    };

    const res = await api.post(`/interviews/companies/${activeCompany.slug}/evaluate-round`, payload);

    // 1. Lock answer inputs immediately (zero redo, zero change answer)
    document.getElementById('activeRoundResponse').disabled = true;
    submitBtn.disabled = true;
    submitBtn.style.display = 'none';

    // 2. Lock option buttons and highlight correct / incorrect
    const optionsGrid = document.getElementById('activeRoundOptionsGrid');
    const optionBtns = optionsGrid.querySelectorAll('.option-btn');
    const questions = activeRound.sample_questions || [];
    const sampleQObj = questions[activeQuestionIndex];
    const correctAns = (sampleQObj && sampleQObj.answer) ? sampleQObj.answer.trim().toLowerCase() : '';

    optionBtns.forEach(btn => {
      btn.disabled = true;
      btn.style.cursor = 'default';
      const text = btn.querySelector('span:last-child')?.textContent?.trim()?.toLowerCase() || '';
      if (correctAns && (text === correctAns || text.includes(correctAns) || correctAns.includes(text))) {
        btn.classList.add('correct');
      } else if (btn.classList.contains('selected')) {
        btn.classList.add('incorrect');
      }
    });

    // 3. Render verdict card with explanation and tips
    const card = document.getElementById('roundVerdictCard');
    card.style.display = 'block';

    const verdictBadge = document.getElementById('verdictBadge');
    if (res.cleared_round) {
      verdictBadge.className = 'badge badge-success';
      verdictBadge.textContent = 'Cleared: ' + res.verdict;
      card.style.borderColor = 'var(--color-success-border)';
      card.style.backgroundColor = '#f0fdf4';
    } else {
      verdictBadge.className = 'badge badge-warning';
      verdictBadge.textContent = 'Review: ' + res.verdict;
      card.style.borderColor = '#fde68a';
      card.style.backgroundColor = '#fffbeb';
    }

    document.getElementById('verdictScore').textContent = `${res.score}/100`;
    document.getElementById('verdictFeedback').textContent = res.feedback;
    document.getElementById('verdictTips').innerHTML = `<strong>Recruiter Recommendation:</strong> ${escapeHtml(res.improvement_tips)}`;

    // 4. Show explicit Next Question progression button
    const hasNext = activeQuestionIndex < (activeRound.sample_questions?.length || 0) - 1;
    let nextProgressionBtn = document.getElementById('roundNextProgressionBtn');
    if (!nextProgressionBtn) {
      nextProgressionBtn = document.createElement('button');
      nextProgressionBtn.id = 'roundNextProgressionBtn';
      card.appendChild(nextProgressionBtn);
    }
    nextProgressionBtn.className = 'btn btn-primary btn-full btn-lg';
    nextProgressionBtn.style.marginTop = '1.25rem';
    nextProgressionBtn.style.display = 'inline-flex';
    nextProgressionBtn.innerHTML = hasNext 
      ? `<span>Next Question (${activeQuestionIndex + 2} of ${activeRound.sample_questions.length})</span> <i data-lucide="arrow-right" style="width:18px;height:18px;margin-left:0.5rem;"></i>`
      : `<span>Complete Round & Return to Company Rounds</span> <i data-lucide="check-circle" style="width:18px;height:18px;margin-left:0.5rem;"></i>`;
    
    nextProgressionBtn.onclick = () => {
      if (hasNext) {
        activeQuestionIndex++;
        renderActiveQuestion();
      } else {
        showView('companyDetailView');
      }
    };

    if (window.lucide) lucide.createIcons();
    card.scrollIntoView({ behavior: 'smooth' });
    showToast('Hiring evaluation complete!', 'success');

  } catch (err) {
    showToast(err.message || 'Failed to evaluate response.', 'error');
    submitBtn.disabled = false;
    submitBtn.style.display = 'inline-flex';
  } finally {
    setButtonLoading(submitBtn, false);
  }
}

function showView(viewId) {
  document.getElementById('companiesView').style.display = viewId === 'companiesView' ? 'block' : 'none';
  document.getElementById('companyDetailView').style.display = viewId === 'companyDetailView' ? 'block' : 'none';
  document.getElementById('activeRoundView').style.display = viewId === 'activeRoundView' ? 'block' : 'none';
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

