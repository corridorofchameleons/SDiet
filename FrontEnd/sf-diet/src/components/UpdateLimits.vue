<script setup>
import {onMounted, ref} from 'vue'
import axios from 'axios';

axios.defaults.withCredentials = true

const data = ref({
    user: null,
    protein: null,
    fats: null,
    carbohydrates: null,
    calories: null
})

async function getLimits() {
    const tmp_data = await axios.get("http://localhost:8000/limits")
    const result = tmp_data.data
    if (result.length === 1) {
        data.value.protein = result[0].protein
        data.value.fats = result[0].fats
        data.value.carbohydrates = result[0].carbohydrates
        data.value.calories = result[0].calories
    }
}

function saveLimits() {
    axios.post("http://localhost:8000/limits",
    {
        "user_id": data.value.user,
        "protein": data.value.protein,
        "fats": data.value.fats,
        "carbohydrates": data.value.carbohydrates,
        "calories": data.value.calories
    })
    .then((response) => {
        if (response.status === 200) {
            window.alert("По-моему, сохранилось")
        }
    })
    .catch((error) => {
        console.log(error)
    })
}

onMounted(() => {
    getLimits()
})
</script>

<template>
    <h2>Введите минимальное количество</h2>
    <form>
        <div class="form-row">
            <label for="protein">Белки: </label>
            <input v-model="data.protein" type="number" name="protein">
        </div>
        <div class="form-row">
            <label for="fats">Жиры: </label>
            <input v-model="data.fats" type="number" name="fats">
        </div>
        <div class="form-row">
            <label for="carbs">Углеводы: </label>
            <input v-model="data.carbohydrates" type="number" name="carbs">
        </div>
        <div class="form-row">
            <label for="calories">Калории: </label>
            <input v-model="data.calories" type="number" name="calories">
        </div>
        <button type="submit" @click.prevent="saveLimits">Сохранить</button>
    </form>
</template>

<style scoped>
form, h2 {
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
input {
    display: block;
    width: 50px;
}
button {
    margin-top: 5px;
    font-size: 1em;
}
p {
    color: red;
}
</style>