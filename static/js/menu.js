(function(){
  const root = document.querySelector('.menubar');
  if(!root) return;
  let open;
  root.addEventListener('click', (e)=>{
    const btn = e.target.closest('.mi-btn');
    if(!btn) return;
    const item = btn.parentElement;
    if(open && open!==item){ open.classList.remove('open'); }
    item.classList.toggle('open');
    open = item.classList.contains('open') ? item : null;
  });
  document.addEventListener('click',(e)=>{
    if(!e.target.closest('.menubar')){ if(open){open.classList.remove('open'); open=null;} }
  });
  // клавиатура
  root.querySelectorAll('.mi-btn').forEach(b=>{
    b.setAttribute('aria-haspopup','true');
    b.setAttribute('aria-expanded','false');
    b.addEventListener('keydown', (e)=>{
      if(e.key==='Escape' && open){ open.classList.remove('open'); open=null; b.focus(); }
    });
  });
})();
