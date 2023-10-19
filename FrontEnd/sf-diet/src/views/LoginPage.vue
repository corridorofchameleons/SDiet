<script setup>
import {ref} from 'vue'
import axios from 'axios';
import router from '@/router';

const login_form = ref({username: null, password: null})
const bad_credentials = ref(false)

function logIn() {

    axios.post(
    'http://localhost:8000/auth/jwt/login',
    login_form.value,
    {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
    },
)
.then((response) => {
    console.log(response.status + " OK")
    if (response.status === 204) {
        router.push({name: 'account'})
    }
})
.catch((error) => {
    console.log(error)
    // window.alert('По-моему, у нас рекламная пауза\nСтатус ' + text)
    bad_credentials.value = true
    })
}

</script>

<template>
    <h1>Login</h1>
    <form>
        <div class="form-row">
            <label for="email">Email: </label>
            <input v-model="login_form.username" type="text" name="email">
        </div>
        <div class="form-row">
            <label for="password">Пароль: </label>
            <input v-model="login_form.password" type="password" name="password">
        </div>
        <p v-if="bad_credentials">Неверные имя пользователя и/или пароль</p>
        <button @click.prevent="logIn">Войти</button>
    </form>
</template>

<style scoped>
form, h1, p {
    margin: 10px;
}
.form-row {
    display: flex;
    margin-bottom: 5px;
}
.form-row label {
    display: block;
    min-width: 75px;
}
button {
    margin-top: 5px;
    font-size: 1em;
}
p {
    color: red;
}
</style>