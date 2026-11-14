(function(){
  const toggle=document.querySelector('.menu-toggle');
  const nav=document.querySelector('.primary-nav');
  if(toggle&&nav){
    const close=()=>{nav.classList.remove('is-open');toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label','Open navigation')};
    toggle.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';nav.classList.toggle('is-open',open);toggle.setAttribute('aria-expanded',String(open));toggle.setAttribute('aria-label',open?'Close navigation':'Open navigation')});
    nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',close));
    document.addEventListener('keydown',e=>{if(e.key==='Escape')close()});
    document.addEventListener('click',e=>{if(!nav.contains(e.target)&&!toggle.contains(e.target))close()});
    window.addEventListener('resize',()=>{if(window.innerWidth>700)close()});
  }
  document.querySelectorAll('a[href^="http"]:not([rel])').forEach(a=>{if(a.hostname!==location.hostname){a.rel='noopener noreferrer';a.target='_blank'}});
})();
