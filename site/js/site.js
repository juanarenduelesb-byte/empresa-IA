// Navegación compartida, tema y controles segmentados
(function(){
  var pages=[
    ['index.html','Inicio'],['negocio.html','La idea'],['metodo.html','Método'],
    ['cerebro.html','El cerebro'],['flujos.html','Flujos'],['simulacion.html','Simulación'],['atlas.html','Atlas'],
    ['procesos.html','Procesos'],['conocimiento.html','Conocimiento'],['seguridad.html','Seguridad'],['legal.html','Leyes'],
    ['claude.html','Construir en Claude'],['planning.html','Plan 12 semanas'],['decisiones.html','Decisiones'],['glosario.html','Glosario']
  ];
  var here=(location.pathname.split('/').pop()||'index.html');
  if(here.indexOf('.html')<0) here='index.html';
  var mark='<span class="mk" aria-hidden="true"><i></i><i></i><i></i></span>';
  var links=pages.map(function(p){return '<a href="'+p[0]+'"'+(p[0]===here?' aria-current="page"':'')+'>'+p[1]+'</a>'}).join('');
  var nav=document.createElement('nav');nav.className='nav';nav.setAttribute('aria-label','Páginas');
  nav.innerHTML='<div class="nav-in"><a class="logo" href="index.html">'+mark+'varios</a><div class="nav-links">'+links+'</div><button class="theme-btn" type="button" aria-label="Cambiar tema claro u oscuro"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6l1.4 1.4M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg></button></div>';
  document.body.insertBefore(nav,document.body.firstChild);
  var w=document.createElement('div');w.className='water';w.innerHTML='<i></i><i></i><i></i>';document.body.insertBefore(w,document.body.firstChild);
  var cur=nav.querySelector('[aria-current]');if(cur&&cur.scrollIntoView){try{cur.scrollIntoView({block:'nearest',inline:'center'})}catch(e){}}
  try{var t=localStorage.getItem('varios-theme');if(t)document.documentElement.setAttribute('data-theme',t)}catch(e){}
  nav.querySelector('.theme-btn').addEventListener('click',function(){
    var d=document.documentElement,c=d.getAttribute('data-theme');
    var dark=c?c==='dark':matchMedia('(prefers-color-scheme: dark)').matches;
    var n=dark?'light':'dark';d.setAttribute('data-theme',n);try{localStorage.setItem('varios-theme',n)}catch(e){}
  });
  // Página anterior y siguiente
  var i=pages.findIndex(function(p){return p[0]===here});
  var slot=document.getElementById('next');
  if(slot&&i>-1){
    var h='';
    if(i>0)h+='<a href="'+pages[i-1][0]+'"><div class="card"><span class="dir">Anterior</span><b>'+pages[i-1][1]+'</b></div></a>';
    if(i<pages.length-1)h+='<a href="'+pages[i+1][0]+'"><div class="card" style="text-align:right"><span class="dir">Siguiente</span><b>'+pages[i+1][1]+'</b></div></a>';
    slot.innerHTML=h;
  }
  var f=document.createElement('footer');
  f.innerHTML='<span>varios · nombre provisional</span><span>Documento interno de los socios · actualizado el 17/11/2026</span>';
  document.body.appendChild(f);
  // Controles segmentados: data-seg="grupo", botones con data-show="id"
  document.querySelectorAll('[data-seg]').forEach(function(seg){
    var btns=seg.querySelectorAll('button');
    btns.forEach(function(b){b.addEventListener('click',function(){
      btns.forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false');var el=document.getElementById(x.dataset.show);if(el)el.hidden=x!==b});
    })});
  });
})();
