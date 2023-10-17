<script setup>
import {ref} from 'vue'
import axios from 'axios';

const login_form = ref({username: null, password: null})

function logIn() {
    let status
    let text

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
    status = response.status
    console.log(status + " OK")
    console.log(document.cookie)
})
.catch((error) => {
    status = error.response.status
    text = error.response.data.detail
    console.log("status: ", status, error.response.data.detail)
    window.alert('По-моему, у нас рекламная пауза\nСтатус ' + text)
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
        <button @click.prevent="logIn">Войти</button>
    </form>
</template>

<style scoped>

</style>