(function(){
var o=document.getElementById('out'),i=document.getElementById('cmd');if(!o||!i)return;
var R={about:'about.html',projects:'projects.html',stack:'stack.html',principles:'principles.html',faq:'faq.html',contact:'contact.html',handles:'handles.html'};
var H={whoami:'djunekz — Tooling Architect & Automation Engineer',help:'commands: '+Object.keys(R).join(', ')+', whoami, github, clear',github:'opening github.com/djunekz ...'};
function p(t,c){var d=document.createElement('div');d.className=c||'';d.textContent=t;o.appendChild(d);o.scrollTop=o.scrollHeight}
p('type "help" to see commands.','o');
i.addEventListener('keydown',function(e){if(e.key!=='Enter')return;var v=i.value.trim().toLowerCase();i.value='';if(!v)return;p('$ '+v);
if(v==='clear'){o.textContent='';return}
if(v==='github'){p(H.github,'o');setTimeout(function(){location.href='https://github.com/djunekz'},500);return}
if(R[v]){p('opening '+R[v]+' ...','o');setTimeout(function(){location.href=R[v]},350);return}
if(H[v]){p(H[v],'o');return}
p('command not found: '+v+'. try "help".','e')})
})();
