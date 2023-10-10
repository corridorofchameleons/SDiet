<script setup>
import router from '@/router/index.js'
import { ref } from 'vue'

const btns = ref([
    { num: 1, b_name: 'Внести данные', b_link: 'add_data' },
])
</script>

<template>
<div class="wrapper">
    <div class="nav-bar-wrapper">
        <a v-for="btn in btns" :key="btn.num"
            @click="router.push({name: btn.b_link })"
            class="link"
            >{{ btn.b_name }}</a>
    </div>
    <div class="content">
        <RouterView/>
    </div>
</div>
</template>

<style scoped>
.wrapper {
    width: auto;
    min-height: 800px;
    display: flex;
    padding: 5px;
    background-color: rgb(238, 250, 255);
}
.nav-bar-wrapper {
    display: flex;
    flex-direction: column;
    padding: 0 15px 0 0;
    margin: 5px 10px 5px 0;
    margin-top: 0;
    font-size: 1.2em;
}
.cats {
    margin-top: 0;
    padding-left: 10px;
}
.link {
    margin: 2px;
    padding: 2px 10px;
    color: black;
    text-decoration: none;
    background-color: rgb(228, 228, 228);
    border-radius: 2px;
}
.active-link {
    background-color: white;
}
.link:hover {
    background-color: rgb(255, 255, 255);
}
</style>