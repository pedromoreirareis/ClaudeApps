/* Esforço Vence — Alfabetização · v123 (versão final do novo cadastro da família)
   (escola-familia.js 1.2 · nuvem-sync.js 4.1 · tela sempre acesa · convite para instalar) */
const C='esforco-vence-v123';
const FILES=['./','./index.html','./manifest.webmanifest','./icon-192.png','./icon-512.png','./nuvem-sync.js','./escola-pwa.js','./escola-familia.js'];
/* nuvem-config.js é buscado sempre na internet primeiro (se o Pedro
   trocar a configuração, os celulares pegam a nova na hora) */
const REDE_PRIMEIRO=['nuvem-config.js'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>
  c.addAll(FILES).then(()=>c.add('./nuvem-config.js').catch(()=>{}))
).then(()=>self.skipWaiting()));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==C).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',e=>{
  if(e.request.method!=='GET') return;
  const url=new URL(e.request.url);
  /* conversa com o Firebase (outro endereço): nunca guardar, sempre direto na internet */
  if(url.origin!==self.location.origin) return;
  if(REDE_PRIMEIRO.some(n=>url.pathname.endsWith('/'+n))){
    e.respondWith(fetch(e.request).then(n=>{
      if(n&&n.ok){const cl=n.clone(); caches.open(C).then(c=>c.put(e.request,cl));}
      return n;
    }).catch(()=>caches.match(e.request,{ignoreSearch:true})));
    return;
  }
  e.respondWith(caches.match(e.request,{ignoreSearch:true}).then(r=>r||fetch(e.request).then(n=>{
    if(n&&n.ok){const cl=n.clone(); caches.open(C).then(c=>c.put(e.request,cl));}
    return n;
  }).catch(()=>caches.match('./index.html'))));
});
