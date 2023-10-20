<script setup>
import { ref } from 'vue'

const btns = ref([
    { num: 1, b_name: 'Внести данные', b_link: 'add_data' },
    { num: 2, b_name: 'Изменить лимиты', b_link: 'update_limits' },
    { num: 3, b_name: 'Выйти', b_link: 'logout'},
])
</script>

<template>
<div class="wrapper">
    <div class="nav-bar-wrapper">
        <router-link v-for="btn in btns" :key="btn.num"
            :to="{name: btn.b_link }"
            class="link"
            active-class="active-link"
            >{{ btn.b_name }}</router-link>
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
    margin: 0 10px 0 0;
    font-size: 1.2em;
    border-right: 2px solid white;
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