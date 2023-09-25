<script setup>
import router from '@/router';
import { onMounted, ref, watch } from 'vue'

// const props = defineProps({
//   catname: String,
// })

const cat = ref(null)
const table_data = ref(null)

onMounted(() => {
    cat.value = router.currentRoute.value.params.id
    getTable()
})

watch(
    () => router.currentRoute.value.params.id,
    () => {
        cat.value = router.currentRoute.value.params.id
        getTable()
    }
)

async function getTable(pars='') {
    if (cat.value) {
        console.log(pars)
        const res = await fetch("http://localhost:8000/products/" + cat.value + pars)
        table_data.value = await res.json()}
}

</script>

<template>
    <div v-if="table_data">
    <table class="table">
        <!-- <thead><th colspan="5" class="t-head">{{ catname.replaceAll('_', ' ') || '<название категории>' }}</th></thead> -->
        <tr>
            <th>Наименование</th>
            <th><div style="display: flex; justify-content: space-around;"><p>Б</p>
                <div class="btns">
                <button @click="router.push({ query: { sort: 'protein-asc' }}), getTable('?sort=protein-asc')">&uArr;</button>
                <button @click="router.push({ query: { sort: 'protein-desc' }}), getTable('?sort=protein-desc')">&dArr;</button></div>
                </div></th>
            <th><div style="display: flex; justify-content: space-around;"><p>Ж</p>
                <div class="btns">
                <button @click="router.push({ query: { sort: 'fats-asc' }}), getTable('?sort=fats-asc')">&uArr;</button>
                <button @click="router.push({ query: { sort: 'fats-desc' }}), getTable('?sort=fats-desc')">&dArr;</button></div>
                </div></th>
            <th><div style="display: flex; justify-content: space-around;"><p>У</p>
                <div class="btns">
                <button @click="router.push({ query: { sort: 'carbs-asc' }}), getTable('?sort=carbohydrates-asc')">&uArr;</button>
                <button @click="router.push({ query: { sort: 'carbs-desc' }}), getTable('?sort=carbohydrates-desc')">&dArr;</button></div>
                </div></th>
            <th><div style="display: flex; justify-content: space-around;"><p>К</p>
                <div class="btns">
                <button @click="router.push({ query: { sort: 'calories-asc' }}), getTable('?sort=calories-asc')">&uArr;</button>
                <button @click="router.push({ query: { sort: 'calories-desc' }}), getTable('?sort=calories-desc')">&dArr;</button></div>
                </div></th>
        </tr>
        <tbody>
        <tr v-for="r in table_data" :key="r.id">
            <td>{{ r.name }}</td>
            <td class="val-td">{{ r.protein.toFixed(1) }}</td>
            <td class="val-td">{{ r.fats.toFixed(1) }}</td>
            <td class="val-td">{{ r.carbohydrates.toFixed(1) }}</td>
            <td class="val-td">{{ r.calories.toFixed(1) }}</td>
        </tr>
        </tbody>
    </table>
</div>
</template>

<style scoped>
.table {
    width: 800px;
}
.table button {
    background-color: rgb(0, 44, 65);
    color: white;
    border: none;
}
.btns {
    display: flex;
    flex-direction: column;
    justify-content: center;
}
tbody tr:nth-child(odd) {
    background-color: #dddddd;
}

tbody tr:nth-child(even) {
    background-color: #caebff;
}

th, td {
    text-align: left;
    padding: 3px;
    padding-left: 8px;
}
th {
    background-color: rgb(0, 44, 65);
    color: white;
    font-size: 1.2em;
}
.t-head {
    background-color: white;
    color: black;
    font-size: 1.5em;
}
.val-td {
    width: 75px;
}
</style>