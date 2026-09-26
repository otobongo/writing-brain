(function () {
  const V = window.VIDEOS || [];
  const C = window.CONCEPTS || [];
  const app = document.getElementById('app');
  const tabs = document.getElementById('tabs');
  const navSearch = document.getElementById('navSearch');

  const $ = (s, el) => (el || document).querySelector(s);
  const esc = s => s.replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
  const fmtT = t => {
    t = Math.max(0, Math.floor(t));
    const h = Math.floor(t / 3600), m = Math.floor(t % 3600 / 60), s = t % 60;
    return (h ? h + ':' + String(m).padStart(2, '0') : m) + ':' + String(s).padStart(2, '0');
  };
  const fmtViews = n => n >= 1000 ? (n / 1000).toFixed(n >= 10000 ? 0 : 1).replace(/\.0$/, '') + 'K' : String(n);
  const fmtDate = d => { const [y, m, day] = d.split('-'); const M = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']; return `${M[+m-1]} ${+day}, ${y}`; };
  const fmtMonth = d => { const [y, m] = d.split('-'); const M = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']; return `${M[+m-1]} ${y}`; };

  const byId = {}; V.forEach(v => byId[v.id] = v);
  const totalWords = V.reduce((s, v) => s + v.words, 0);
  const totalHits = C.reduce((s, c) => s + c.hits.length, 0);

  // ---------------- router ----------------
  function parseHash() {
    const h = location.hash.slice(1); // '', '/', '/v/ID/T', '/concepts'
    const parts = h.split('/').filter(Boolean);
    if (parts[0] === 'v' && parts[1]) return { view: 'player', id: parts[1], t: +parts[2] || 0 };
    if (parts[0] === 'concepts') return { view: 'concepts', q: decodeURIComponent(parts[1] || '') };
    return { view: 'library' };
  }
  function go(hash) { location.hash = hash; }
  window.addEventListener('hashchange', render);

  // ---------------- library ----------------
  let libSort = 'asc', libQuery = '';
  function renderLibrary() {
    tabs.querySelectorAll('a').forEach(a => a.classList.toggle('active', a.dataset.tab === 'library'));
    navSearch.style.display = 'none';

    const q = libQuery.toLowerCase();
    let list = V.filter(v => !q || v.title.toLowerCase().includes(q));
    list = list.slice().sort((a, b) => libSort === 'asc' ? a.date.localeCompare(b.date) : b.date.localeCompare(a.date));

    let groups = [];
    let lastKey = null;
    list.forEach(v => {
      const key = v.date.slice(0, 4);
      if (key !== lastKey) { groups.push({ key, items: [] }); lastKey = key; }
      groups[groups.length - 1].items.push(v);
    });

    const cardHtml = v => `
      <a class="card" href="#/v/${v.id}/0">
        <div class="thumb">
          <img loading="lazy" src="https://i.ytimg.com/vi/${v.id}/mqdefault.jpg" alt="">
          ${v.dur ? `<span class="dur">${fmtT(v.dur)}</span>` : ''}
        </div>
        <div class="body">
          <h3>${esc(v.title)}</h3>
          <div class="cmeta">
            <span>${fmtMonth(v.date)}</span>
            <span class="dot">·</span>
            <span>${v.words.toLocaleString()} words</span>
            ${v.views ? `<span class="dot">·</span><span>${fmtViews(v.views)} views</span>` : ''}
          </div>
        </div>
      </a>`;

    app.innerHTML = `
      <div class="library">
        <div class="hero">
          <h1>The Writer Science <em>study library</em></h1>
          <p class="lede">Every long-form video from William Fitzpatrick's Writer Science channel, transcribed and synced word-for-word to the recording — read along as you watch, or jump straight to any of 113 named concepts.</p>
          <div class="stats">
            <div class="stat"><div class="n">${V.length}</div><div class="l">Videos</div></div>
            <div class="stat"><div class="n">${Math.round(totalWords / 1000)}K</div><div class="l">Words</div></div>
            <div class="stat"><div class="n">${C.length}</div><div class="l">Concepts</div></div>
            <div class="stat"><div class="n">${totalHits}</div><div class="l">Taught moments</div></div>
          </div>
        </div>
        <div class="toolbar">
          <input class="lib-search" id="libSearch" placeholder="Filter by title…" value="${esc(libQuery)}">
          <select id="libSort">
            <option value="asc"${libSort === 'asc' ? ' selected' : ''}>Oldest first</option>
            <option value="desc"${libSort === 'desc' ? ' selected' : ''}>Newest first</option>
          </select>
          <span class="count">${list.length} video${list.length === 1 ? '' : 's'}</span>
        </div>
        ${groups.map(g => `<div class="year-head">${g.key}</div><div class="grid">${g.items.map(cardHtml).join('')}</div>`).join('')}
      </div>`;

    $('#libSearch').oninput = e => { libQuery = e.target.value; renderLibrary(); };
    $('#libSort').onchange = e => { libSort = e.target.value; renderLibrary(); };
  }

  // ---------------- player ----------------
  let player = null, ytReady = false, cur = null, pendingSeek = 0, tSearch = '';

  function renderPlayer(id, t) {
    tabs.querySelectorAll('a').forEach(a => a.classList.toggle('active', a.dataset.tab === 'library'));
    navSearch.style.display = 'none';
    cur = byId[id];
    if (!cur) { go('/'); return; }
    tSearch = '';

    app.innerHTML = `
      <div class="player-shell">
        <section class="pl-left">
          <div class="back-row">
            <a class="back-link" href="#/">&larr; Library</a>
            <select class="jump-select" id="jumpSelect"></select>
          </div>
          <div class="player-frame"><div id="yt"></div></div>
          <div class="vmeta">
            <h2>${esc(cur.title)}</h2>
            <div class="sub">
              <span>${fmtDate(cur.date)}</span>
              <span>·</span>
              <span>${cur.words.toLocaleString()} words</span>
              <span>·</span>
              <a href="https://youtu.be/${cur.id}" target="_blank" rel="noopener">watch on YouTube ↗</a>
            </div>
          </div>
        </section>
        <section class="pl-right">
          <div class="pl-tools">
            <input class="transcript-search" id="tq" placeholder="Search this transcript…">
            <label class="follow-chk"><input type="checkbox" id="follow" checked> follow video</label>
          </div>
          <div id="paras"></div>
        </section>
      </div>`;

    const sel = $('#jumpSelect');
    V.forEach(v => { const o = document.createElement('option'); o.value = v.id; o.textContent = `${v.date}  ${v.title}`; if (v.id === id) o.selected = true; sel.appendChild(o); });
    sel.onchange = e => go(`/v/${e.target.value}/0`);

    renderParas();
    $('#tq').oninput = e => { tSearch = e.target.value; renderParas(); };
    $('#paras').addEventListener('click', e => { const a = e.target.closest('a.t'); if (a) { e.preventDefault(); seekTo(+a.dataset.t); } });

    // the DOM node the old player was attached to is gone (innerHTML rebuilt above) — always start fresh
    if (player && player.destroy) { try { player.destroy(); } catch (e) {} }
    player = null; ytReady = false;
    loadPlayer(id, t);
  }

  function renderParas() {
    const q = tSearch.trim().toLowerCase();
    const rx = q ? new RegExp(q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi') : null;
    $('#paras').innerHTML = cur.p.map((p, i) => {
      if (rx && !rx.test(p.x)) return '';
      const x = rx ? esc(p.x).replace(rx, m => `<mark>${m}</mark>`) : esc(p.x);
      return `<div class="para" data-i="${i}" data-t="${p.t}"><a class="t" href="#" data-t="${p.t}">${fmtT(p.t)}</a><div>${x}</div></div>`;
    }).join('');
  }

  function loadPlayer(id, t) {
    pendingSeek = t || 0;
    if (!window.YT || !window.YT.Player) return; // API script still loading; onYouTubeIframeAPIReady will create it
    if (!$('#yt')) return; // view navigated away before the API finished loading
    player = new YT.Player('yt', {
      videoId: id,
      playerVars: { start: t || 0, rel: 0, modestbranding: 1 },
      events: {
        onReady: () => { ytReady = true; },
        onStateChange: e => { if (e.data === 1) tick(); }
      }
    });
  }
  function seekTo(t) { if (player && ytReady) { player.seekTo(t, true); player.playVideo(); } }

  function tick() {
    if (!ytReady || !cur || !player.getCurrentTime) return;
    const t = player.getCurrentTime();
    let idx = -1;
    cur.p.forEach((p, i) => { if (p.t <= t + 0.3) idx = i; });
    const prev = $('.para.cur');
    const el = $(`.para[data-i="${idx}"]`);
    if (prev && prev !== el) prev.classList.remove('cur');
    if (el && !el.classList.contains('cur')) {
      el.classList.add('cur');
      const followEl = $('#follow');
      if (followEl && followEl.checked) el.scrollIntoView({ block: 'center', behavior: 'smooth' });
    }
  }

  // ---------------- concepts ----------------
  function renderConcepts(initialQ) {
    tabs.querySelectorAll('a').forEach(a => a.classList.toggle('active', a.dataset.tab === 'concepts'));
    navSearch.style.display = '';
    navSearch.value = initialQ || '';
    navSearch.placeholder = 'Filter concepts…';

    app.innerHTML = `<div class="concepts-page">
      <p class="lede">Every place across the channel a concept is taught, in order. <b>Bold</b> timestamps are the fullest explanation — start there.</p>
      <div id="clist"></div>
    </div>`;
    paintConcepts(initialQ || '');
  }
  function paintConcepts(q) {
    q = (q || '').toLowerCase();
    let g = '';
    const html = C.filter(c => !q || (c.name + ' ' + c.group + ' ' + c.hits.map(h => h.note || '').join(' ')).toLowerCase().includes(q))
      .map(c => {
        const gh = c.group !== g ? `<div class="group-head">${esc(g = c.group)}</div>` : '';
        const hits = c.hits.length
          ? c.hits.map(h => {
              const v = byId[h.vid];
              return `<div class="hit${h.primary ? ' primary' : ''}"><a href="#/v/${h.vid}/${h.t}">${fmtT(h.t)}</a> <span class="v">${v ? esc(v.title) + ' (' + v.date.slice(0, 4) + ')' : h.vid}</span>${h.note ? ' — <span class="note">' + esc(h.note) + '</span>' : ''}</div>`;
            }).join('')
          : `<div class="hit empty">no passage found</div>`;
        return `${gh}<div class="concept-name">${esc(c.name)}</div>${hits}`;
      }).join('');
    $('#clist').innerHTML = html || '<p style="color:var(--muted)">No matches.</p>';
  }

  // ---------------- render dispatch ----------------
  function render() {
    const r = parseHash();
    if (r.view === 'player') renderPlayer(r.id, r.t);
    else if (r.view === 'concepts') renderConcepts(r.q);
    else renderLibrary();
    window.scrollTo(0, 0);
  }

  navSearch.oninput = e => {
    if (parseHash().view === 'concepts') paintConcepts(e.target.value);
  };
  tabs.addEventListener('click', e => {
    const a = e.target.closest('a'); if (!a) return;
  });

  window.onYouTubeIframeAPIReady = () => {
    if (cur) loadPlayer(cur.id, pendingSeek);
  };
  setInterval(tick, 500);
  const ytTag = document.createElement('script');
  ytTag.src = 'https://www.youtube.com/iframe_api';
  document.head.appendChild(ytTag);

  render();
})();
