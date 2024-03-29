const staticCacheName = 'site-static-v3';
const dynamicCacheName = 'site-dynamic-v3'
const assets = [
    '/',
    '/index.html',
    '/js/app.js',
    'https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css',
    'https://code.jquery.com/jquery-3.5.1.slim.min.js',
    'https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js',
    'https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js',
]

// Cache limit function
const limitCacheSize = (name, size) => {
    caches.open(name).then(cache => {
        cache.keys().then(keys => {
            if (keys.length > size) {
                cache.delete(keys[0]).then(limitCacheSize(name, size))
            }
        })
    })
}

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
    evt.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(keys
                .filter(key => key !== staticCacheName)
                .map(key => caches.delete(key))    
            )
        })
    )
})

// fetch event
self.addEventListener('fetch', evt => {
    console.log('fetch event', evt);
    if(evt.request.url.indexOf('firestore.googleapis.com') === -1){
        evt.respondWith(
            caches.match(evt.request).then(res => {
                return res || fetch(evt.request).then(fetchRes => {
                    return caches.open(dynamicCacheName).then(cache => {
                        cache.put(evt.request.url, fetchRes.clone())
                        limitCacheSize(dynamicCacheName, 15)
                        return fetchRes
                    })
                });
            })
        )
    }
})