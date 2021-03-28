const staticCacheName = 'site-static';
const assets = [
    '/',
    '/index.html',
    '/js/app.js',
    'https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css',
    'https://code.jquery.com/jquery-3.5.1.slim.min.js',
    'https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js',
    'https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js',
]

self.addEventListener('install', evt => {
    console.log('sw installed');
    evt.waitUntil(
        caches.open(staticCacheName).then(cache => {
            console.log('caching shell assets')
            cache.addAll(assets);
        })
    );
});

// activate event
self.addEventListener('activate', evt => {
    console.log('sw activated');
})

// fetch event
self.addEventListener('fetch', evt => {
    console.log('fetch event', evt);
    evt.respondWith(
        caches.match(evt.request).then(res => {
            return res || fetch(evt.request);
        })
    )
})