<script setup>
import router from '@/router'

</script>

<template>
    <header>
        <h1 @click="router.push({name: 'home'})">SFDiet</h1>
        <div class="links">
            <a @click="router.push({name: 'login'})">Логин</a>
            <a @click="router.push({name: 'account'})">Аккаунт</a>
            <a @click="router.push({name: 'products'})">Справочник</a>
        </div>
    </header>
</template>

<style scoped>
* {
    width: auto;
    padding: 20px;
    background-color: black;
    color: white;
}
header {
    position: relative;
}
.links {
    font-size: 1.5em;
    position: absolute;
    bottom: 0;
    right: 0;
}
a, a label, h1, h1 label {
    cursor: pointer;
}
</style>