<template>
    <div id="wrap" style="margin-top: 20px;">
        
        <div class="js-toasty-sign-up-container"></div>
        <div class="filter-subnav container-fluid">
            <div class="filter-subnav-inner flex flex-row items-center justify-between">
                <div class="filter-views js-shot-views">
                    <span class="btn-dropdown btn-dropdown-neue">
                        <a class="form-btn outlined btn-dropdown-link" data-track-sub-nav href="#"
                            data-dropdown-state="closed">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                                fill="none" role="img" class="icon btn-dropdown-caret">
                                <path
                                    d="M21.5265 8.77171C22.1578 8.13764 22.1578 7.10962 21.5265 6.47555C20.8951 5.84148 19.8714 5.84148 19.24 6.47555L11.9999 13.7465L4.75996 6.47573C4.12858 5.84166 3.10492 5.84166 2.47354 6.47573C1.84215 7.10979 1.84215 8.13782 2.47354 8.77188L10.8332 17.1671C10.8408 17.1751 10.8486 17.183 10.8565 17.1909C11.0636 17.399 11.313 17.5388 11.577 17.6103C11.5834 17.6121 11.5899 17.6138 11.5964 17.6154C12.132 17.7536 12.7242 17.6122 13.1435 17.1911C13.1539 17.1807 13.1641 17.1702 13.1742 17.1596L21.5265 8.77171Z" />
                            </svg>
                            <span>Popular</span>
                    </a>
                    <div class="btn-dropdown-options">
                        <ul>
                            <li class="popular active" id="popular-btn">
                                <a data-track-view="Popular" href="/shots/popular">Popular</a>
                            </li>
                            <li class id="recent-btn">
                                <a data-track-view="New &amp; Noteworthy" href="/shots/recent">New &amp;
                                        Noteworthy</a>
                            </li>
                            <li class="rule"></li>
                            <li class>
                                <a data-track-view="Goods for Sale" href="/shots/goods">Goods for Sale</a>
                            </li>
                        </ul>
                    </div>
                    </span>
                </div>
                <div class="filter-categories js-filter-categories js-shot-categories">
                    <span class="scroll scroll-backward">
                        <a class="d-none" href="#">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                                fill="none" role="img" class="icon ">
                                <path
                                    d="M21.5265 8.77171C22.1578 8.13764 22.1578 7.10962 21.5265 6.47555C20.8951 5.84148 19.8714 5.84148 19.24 6.47555L11.9999 13.7465L4.75996 6.47573C4.12858 5.84166 3.10492 5.84166 2.47354 6.47573C1.84215 7.10979 1.84215 8.13782 2.47354 8.77188L10.8332 17.1671C10.8408 17.1751 10.8486 17.183 10.8565 17.1909C11.0636 17.399 11.313 17.5388 11.577 17.6103C11.5834 17.6121 11.5899 17.6138 11.5964 17.6154C12.132 17.7536 12.7242 17.6122 13.1435 17.1911C13.1539 17.1807 13.1641 17.1702 13.1742 17.1596L21.5265 8.77171Z" />
                            </svg>
                        </a>
                    </span>
                    <span class="scroll scroll-forward">
                        <a class="d-none" href="#">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                                fill="none" role="img" class="icon ">
                                <path
                                    d="M21.5265 8.77171C22.1578 8.13764 22.1578 7.10962 21.5265 6.47555C20.8951 5.84148 19.8714 5.84148 19.24 6.47555L11.9999 13.7465L4.75996 6.47573C4.12858 5.84166 3.10492 5.84166 2.47354 6.47573C1.84215 7.10979 1.84215 8.13782 2.47354 8.77188L10.8332 17.1671C10.8408 17.1751 10.8486 17.183 10.8565 17.1909C11.0636 17.399 11.313 17.5388 11.577 17.6103C11.5834 17.6121 11.5899 17.6138 11.5964 17.6154C12.132 17.7536 12.7242 17.6122 13.1435 17.1911C13.1539 17.1807 13.1641 17.1702 13.1742 17.1596L21.5265 8.77171Z" />
                            </svg>
                        </a>
                    </span>
                    <ul>
                        <li class="category sets-path active">
                            <a title="All" data-param="category" data-track-sub-nav="true" href="/shots/popular/">All</a>
                        </li>
                        <li class="category sets-path ">
                            <a title="I" data-param="category" data-value="i" data-track-sub-nav="true" href="/i">I</a>
                        </li>
                        <li class="category sets-path ">
                            <a title="You" data-param="category" data-value="you" data-track-sub-nav="true" href="/you">You</a>
                        </li>
                    </ul>
                </div>
                <div class="filter-settings js-shot-settings">
                    <a class="form-btn outlined filters-toggle-btn filters-active empty" data-name="Filters" data-track-sub-nav="true" href="#" data-dropdown-state="open">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" role="img" class="icon filter-icon icon-14">
                            <path fill-rule="evenodd" clip-rule="evenodd"
                                d="M0 6C0 5.17157 0.671573 4.5 1.5 4.5H22.5C23.3284 4.5 24 5.17157 24 6C24 6.82843 23.3284 7.5 22.5 7.5H1.5C0.671573 7.5 0 6.82843 0 6ZM3 12C3 11.1716 3.67157 10.5 4.5 10.5H19.5C20.3284 10.5 21 11.1716 21 12C21 12.8284 20.3284 13.5 19.5 13.5H4.5C3.67157 13.5 3 12.8284 3 12ZM7.5 16.5C6.67157 16.5 6 17.1716 6 18C6 18.8284 6.67157 19.5 7.5 19.5H16.5C17.3284 19.5 18 18.8284 18 18C18 17.1716 17.3284 16.5 16.5 16.5H7.5Z" />
                        </svg>
                        <span class="meatball">0</span>
                        <span class="label" title="Filters">Filters</span>
                    </a>
                </div>
            </div>
            <div class="shot-filters    " style="display: block;">
                <form class="gen-form with-messages shot-filters-form goods-search flex-ns" action="/" accept-charset="UTF-8" method="get">
                    <input name="utf8" type="hidden" value="✓">
                    <fieldset class="find-shots-tag">
                        <a class="clear-filter d-none" data-param="tag" href="/shots/filters">Clear</a>
                        <label>Tags</label>
                        <div class="input-with-icon">
                            <input type="search" name="tag" id="tag" value data-name="Tag" data-track-filter="true" autocomplete="off">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none" role="img" class="icon ">
                                <path fill-rule="evenodd" clip-rule="evenodd"
                                    d="M10.6002 12.0498C9.49758 12.8568 8.13777 13.3333 6.66667 13.3333C2.98477 13.3333 0 10.3486 0 6.66667C0 2.98477 2.98477 0 6.66667 0C10.3486 0 13.3333 2.98477 13.3333 6.66667C13.3333 8.15637 12.8447 9.53194 12.019 10.6419C12.0265 10.6489 12.0338 10.656 12.0411 10.6633L15.2935 13.9157C15.6841 14.3063 15.6841 14.9394 15.2935 15.33C14.903 15.7205 14.2699 15.7205 13.8793 15.33L10.6269 12.0775C10.6178 12.0684 10.6089 12.0592 10.6002 12.0498ZM11.3333 6.66667C11.3333 9.244 9.244 11.3333 6.66667 11.3333C4.08934 11.3333 2 9.244 2 6.66667C2 4.08934 4.08934 2 6.66667 2C9.244 2 11.3333 4.08934 11.3333 6.66667Z" />
                            </svg>
                        </div>
                    </fieldset>
                    <fieldset class="find-shots-timeframe">
                        <input type="hidden" name="timeframe" id="timeframe" value class="filter-timeframe">
                        <a class="clear-filter d-none" data-param="timeframe" href="/shots/filters">Clear</a>
                        <label>Timeframe</label>
                        <span class="btn-dropdown btn-dropdown-neue">
                            <a class="form-btn outlined btn-dropdown-link" href="#" data-name="Timeframe"
                                data-track-filter data-dropdown-state="closed">
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                                    fill="none" role="img" class="icon btn-dropdown-caret">
                                    <path
                                        d="M21.5265 8.77171C22.1578 8.13764 22.1578 7.10962 21.5265 6.47555C20.8951 5.84148 19.8714 5.84148 19.24 6.47555L11.9999 13.7465L4.75996 6.47573C4.12858 5.84166 3.10492 5.84166 2.47354 6.47573C1.84215 7.10979 1.84215 8.13782 2.47354 8.77188L10.8332 17.1671C10.8408 17.1751 10.8486 17.183 10.8565 17.1909C11.0636 17.399 11.313 17.5388 11.577 17.6103C11.5834 17.6121 11.5899 17.6138 11.5964 17.6154C12.132 17.7536 12.7242 17.6122 13.1435 17.1911C13.1539 17.1807 13.1641 17.1702 13.1742 17.1596L21.5265 8.77171Z" />
                                </svg>
                                <span data-prompt="Now" data-fade-default="true" class="default-option">
                                    Now
                                </span>
                        </a>
                        <div class="btn-dropdown-options sets-querystring">
                            <ul>
                                <li class="default-filter-option active">
                                    <a href="?timeframe=">
                                            Now
                                        </a>
                                </li>
                                <li data-value="week" class="timeframe-week "><a href="?timeframe=week">This Past
                                            Week</a></li>
                                <li data-value="month" class="timeframe-month "><a href="?timeframe=month">This Past
                                            Month</a></li>
                                <li data-value="year" class="timeframe-year "><a href="?timeframe=year">This Past
                                            Year</a></li>
                                <li data-value="ever" class="timeframe-all-time "><a href="?timeframe=ever">All
                                            Time</a></li>
                                <li data-value="now" class="d-none timeframe-now "><a href="?timeframe=now">Now</a>
                                </li>
                            </ul>
                        </div>
                        </span>
                    </fieldset>
                </form>
            </div>
        </div>
        <div id="wrap-inner" class="flushed">
            <div id="content" role="main">
                <div id="main" class="main-full">
                    <ol class="js-thumbnail-grid shots-grid group container-fluid is-scrolled">
                        <li v-for="data in cardData" :id="data.id" :key="data.id" :data-thumbnail-id="data.id" class="shot-thumbnail js-thumbnail shot-thumbnail-container      " data-ad-data data-boost-id data-is-boost-fallback>
                            <Card 
                                v-bind:image="data.image" 
                                :tagline="data.tagline" 
                                :title="data.title" 
                                :badge="data.badge" 
                                :like="data.like" 
                                :view="data.view"/> 
                        </li>
                    </ol>
                    <div id="boosted-shots-app"></div>
                    <div class="infinite shot-grid-width container-fluid infinite-login-actions" style>
                        <a class="form-sub sign-up-to-continue" data-signup-trigger="true" data-href="/signup/new" data-context="homepage-load-more" href="/signup/new">Sign up to continue</a>
                        <a href="/session/new">or sign in</a>
                    </div>
                    <div class="loading-more" style="display: none;">
                        <span class="processing">Loading more…</span>
                    </div>
                    <div class="back-to-top" style="display: block;">
                        <a href="#">
                            <img width="50" height="50" class="lazyloading-hidden lazyloaded" alt="Back to top" src="../images/back-to-top.png">
                        </a>
                    </div>
                </div>
            </div>
        </div>
        <div>
            {{data}}
        </div>
    </div>
</template>

<script>
import Card from './Card.vue'
// import { kfc } from './kfc.js'
// import { shawarma } from './shawarma.js'

// 'cardData': [
//     {
//         'id':0,
//         'image': kfc,
//         'tagline': "KFC, who doesn't like it?",
//         'title': "KFC",
//         'badge': "FAV",
//         'like': "1k",
//         'view': "10k",
//     },
//     {
//         'id':1,
//         'image': shawarma,
//         'tagline': "Shawarma, hmm?",
//         'title': "Shawarma",
//         'badge': "UH",
//         'like': "1",
//         'view': "1k",
//     },
// ],

export default {
    name: 'Main',
    beforeMount() {
        this.getData();
    },
    data(){
        return {
            'cardData': []
        }
    },
    methods: {
        async getData(){
            const res = await fetch('http://SERVER_ADDRESS:SERVER_PORT/api/v1/backend/retrieve',{
                method: 'GET',
                  headers: {
                        'Content-Type': 'application/json',
                    },
            });
            const result = await res.json();
            this.cardData = result.data;
        }
    },
    components: {
        Card,
    }
}
</script>