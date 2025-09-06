const CACHE = "duocpoint-v1";
const ASSETS = ["/", "/styles.css", "/main.js", "/manifest.webmanifest"]; // agrega lo que necesites

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS)));
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    )
  );
});

self.addEventListener("fetch", (e) => {
  e.respondWith(
    fetch(e.request).then(res => {
      const copy = res.clone();
      caches.open(CACHE).then(c => c.put(e.request, copy));
      return res;
    }).catch(() => caches.match(e.request))
  );
});

// (opcional) handler para push
self.addEventListener("push", (e) => {
  const data = e.data?.json() || { title: "Duoc-Point", body: "Notificación" };
  e.waitUntil(self.registration.showNotification(data.title, { body: data.body }));
});
