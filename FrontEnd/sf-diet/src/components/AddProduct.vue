<script setup>
import { ref, reactive, onMounted } from 'vue'
import axios from 'axios'
import router from '@/router'

const cats = ref(null)

const product = reactive({
    name: null,
    protein: null,
    fats: null, 
    carbohydrates: null,
    calories: null,
    cat: null
})

onMounted(getCats)

async function getCats() {
    const res = await fetch("http://localhost:8000/products/")
    cats.value = await res.json()
}

function addP() {
    product.calories = product.fats * 9.3 + product.carbohydrates * 4.2 + product.protein * 4.2
    axios.post("http://localhost:8000/products/add_product", {
        "name": product.name,
        "protein": product.protein,
        "fats": product.fats, 
        "carbohydrates": product.carbohydrates,
        "calories": product.calories,
        "category": product.cat
    })
    .then(function (response) {
        window.alert(response.data.status);
    })
}
</script>

<template>
<form class="form">
    <div class="row">
        <p>Выберите категорию: </p>
        <select required v-model="product.cat">
            <option 
                v-for="c in cats" :key="c.id"
                :value="c.id"
            >{{ c.name.replaceAll('_', ' ') }}</option>
        </select>
    </div>
    <div class="row">
    <p >Введите наименование: </p>
        <input v-model="product.name" required class="name">

    </div>
    <div class="row">
    <p>Введите белки: </p>
        <input type="number" min="0" max="100" v-model="product.protein" required>

    </div>
    <div class="row">
    <p>Введите жиры: </p>
        <input type="number" min="0" max="100" v-model="product.fats" required>

    </div>
    <div class="row">
    <p>Введите углеводы: </p>
        <input type="number" min="0" max="100" v-model="product.carbohydrates" required>

    </div>
    <button type="submit" @click.prevent="addP">Добавить</button>
</form>   
<a @click="router.push({name: 'products'})">Назад к таблицам</a> 
</template>
    
<style scoped>
select, input {
    height: 25px;
}
.form {
    margin: 20px;
}
.row { 
    font-size: 1.2em;
    display: flex; 
    flex-direction: row; 
}
.row select, .row input {
    font-size: 1em;
    margin: 10px;
}
.row p {
    width: 250px;
}
.row input {
    width: 50px;
}
input.name {
    width: 500px;
}
button {
    margin-top: 20px;
    font-size: 1.2em;
}
a {
    margin-left: 20px;
    text-decoration: underline;
}
</style>