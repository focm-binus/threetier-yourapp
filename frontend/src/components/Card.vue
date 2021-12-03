<template>
<div>
    <div class="js-thumbnail-base shot-thumbnail-base disabled-shot-section dribbble-shot dribbble  multi-shot">
        <figure style="background-color: #A1A0A2" class="js-thumbnail-placeholder shot-thumbnail-placeholder">
            <noscript>
                <img v-bind:src="'data:image/png;base64, '+ image" :alt="tagline">
            </noscript>
            <img :alt="tagline" width="330" height="247" data-sizes="auto" class="lazyautosizes lazyloaded" v-bind:src="'data:image/png;base64, '+ image" sizes="350px">
        </figure>
        <a class="shot-thumbnail-link dribbble-link js-thumbnail-link" :href="'/'+title">
            <span class="accessibility-text">See {{title}}</span>
        </a>
        <div class="shot-thumbnail-overlay">
            <div class="shot-thumbnail-overlay-content">
                <div class="shot-title">{{title}}</div>
                <ul class="js-dribbble-shot-actions shot-actions-container">
                    <li data-bucket-container="true" class="shot-action">
                        <a class="bucket-shot form-btn" title="Save this" data-signup-trigger="true" data-href="/signup/new" data-context="bucket-shot" href="/signup/new">
                            <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" viewBox="0 0 24 24" role="img" class="icon ">
                                <path
                                    d="m22 5h-11l-2-3h-7c-1.104 0-2 .896-2 2v16c0 1.104.896 2 2 2h20c1.104 0 2-.896 2-2v-13c0-1.104-.896-2-2-2zm-6 10h-3v3c0 .55-.45 1-1 1s-1-.45-1-1v-3h-3c-.55 0-1-.45-1-1s.45-1 1-1h3v-3c0-.55.45-1 1-1s1 .45 1 1v3h3c.55 0 1 .45 1 1s-.45 1-1 1z" />
                            </svg>
                        </a>
                    </li>
                    <div class="like-action-16644417   shot-action">
                        <a class="form-btn tipsy-mobile-disabled stats-action like-shot" rel="no-follow" title="Like this" data-signup-trigger data-href="/signup/new" data-context="like-shot" href="/signup/new">
                            <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" viewBox="0 0 24 24" role="img" class="icon ">
                                <path
                                    d="m18.199 2.04c-2.606-.284-4.262.961-6.199 3.008-2.045-2.047-3.593-3.292-6.199-3.008-3.544.388-6.321 4.43-5.718 7.96.966 5.659 5.944 9 11.917 12 5.973-3 10.951-6.341 11.917-12 .603-3.53-2.174-7.572-5.718-7.96z" />
                            </svg>
                            <span class="accessibility-text">Like</span>
                        </a>
                    </div>
                </ul>
            </div>
        </div>
    </div>
    <div class="shot-details-container js-shot-details-container" style="visibility: visible;">
        <div class="user-information">
            <a class="hoverable url" rel="contact" :href="'/'+title">
                <span class="display-name">{{title}}</span>
            </a>
            <a class="badge-link" :href="'/'+badge">
                <span class="badge badge-fav">{{badge}}</span>
            </a>
        </div>
        <div class="shot-statistics-container js-shot-statistics">
            <div class="shot-statistic js-shot-likes-container">
                <div class="like-action-16644417  compact-true shot-action">
                    <a class=" tipsy-mobile-disabled stats-action like-shot" rel="no-follow" title="Like this shot" data-signup-trigger data-href="/signup/new" data-context="like-shot" href="/signup/new">
                        <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" viewBox="0 0 24 24" role="img" class="icon fill-current shot-tools-icon">
                            <path
                                d="m18.199 2.04c-2.606-.284-4.262.961-6.199 3.008-2.045-2.047-3.593-3.292-6.199-3.008-3.544.388-6.321 4.43-5.718 7.96.966 5.659 5.944 9 11.917 12 5.973-3 10.951-6.341 11.917-12 .603-3.53-2.174-7.572-5.718-7.96z" />
                        </svg>
                        <span class="accessibility-text">Like</span>
                    </a>
                </div>
                <span class="js-shot-likes-count color-deep-blue-sea-light-20 font-weight-500">{{like}}</span>
            </div>
            <div class="shot-statistic js-shot-views-container">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="11" viewBox="0 0 14 11" fill="none" role="img" class="icon fill-current shot-tools-icon">
                    <path
                        d="M7 3.45833C5.87242 3.45833 4.95833 4.37242 4.95833 5.5C4.95833 6.62758 5.87242 7.54167 7 7.54167C8.12758 7.54167 9.04167 6.62758 9.04167 5.5C9.04167 4.37242 8.12758 3.45833 7 3.45833ZM7 0.25C3.13425 0.25 0 4.625 0 5.5C0 6.375 3.13425 10.75 7 10.75C10.8657 10.75 14 6.375 14 5.5C14 4.625 10.8657 0.25 7 0.25ZM7 8.70833C5.22783 8.70833 3.79167 7.27217 3.79167 5.5C3.79167 3.72783 5.22783 2.29167 7 2.29167C8.77217 2.29167 10.2083 3.72783 10.2083 5.5C10.2083 7.27217 8.77217 8.70833 7 8.70833Z" />
                </svg>
                <span class="js-shot-views-count color-deep-blue-sea-light-20 font-weight-500">{{view}}</span>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default {
    name:'Card',
    props: {
        image: String,
        tagline: String,
        title: String,
        like: String,
        view: String,
        badge: String,
    }
}
</script>