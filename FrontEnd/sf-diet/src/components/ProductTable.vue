<script setup>
import router from '@/router';
import { onMounted, ref, watch } from 'vue'
import axios from 'axios'

// const props = defineProps({
//   catname: String,
// })
let parameters = {
    'page': 0,
    'sort': '',
    'search': ''
}

const cat = ref(null)
const pages = ref(null)
const table_data = ref(null)


onMounted(() => {
    cat.value = router.currentRoute.value.params.id
    getTable()
})

watch(
    () => router.currentRoute.value,
    () => {
        cat.value = router.currentRoute.value.params.id
        getTable()
    }
)


async function getTable() {
    if (cat.value) {
        const res = await axios.get("http://localhost:8000/products/" + cat.value, {
            params: {
                page: router.currentRoute.value.query.page,
                sort: router.currentRoute.value.query.sort,
                search: router.currentRoute.value.query.search,
            }
        })
        const res_data = res.data
        table_data.value = res_data[1].products
        pages.value = res_data[0].pages
        }
}

function get_query({sr=parameters.sort, pg=parameters.page, srch=parameters.search}) {
    router.push({ query: { sort: sr, page: pg, search: srch } })
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
                <button @click="() => {
                    parameters.sort = 'protein-asc'
                    get_query({ sr: 'protein-asc' })}">&uArr;</button>
                <button @click="() => {
                    parameters.sort = 'protein-desc'
                    get_query({ sr: 'protein-desc' })}">&dArr;</button></div>
                </div></th>
            <th><div style="display: flex; justify-content: space-around;"><p>Ж</p>
                <div class="btns">
                <button @click="() => {
                    parameters.sort = 'fats-asc'
                    get_query({ sr: 'fats-asc' })}">&uArr;</button>
                <button @click="() => {
                    parameters.sort = 'fats-desc'
                    get_query({ sr: 'fats-desc'})}">&dArr;</button></div>
                </div></th>
            <th><div style="display: flex; justify-content: space-around;"><p>У</p>
                <div class="btns">
                <button @click="() => {
                    parameters.sort = 'carbohydrates-asc'
                    get_query({ sr: 'carbohydrates-asc'})}">&uArr;</button>
                <button @click="() => {
                    parameters.sort = 'carbohydrates-desc'
                    get_query({ sr: 'carbohydrates-desc'})}">&dArr;</button></div>
                </div></th>
            <th><div style="display: flex; justify-content: space-around;"><p>К</p>
                <div class="btns">
                <button @click="() => {
                    parameters.sort = 'calories-asc'
                    get_query({ sr: 'calories-asc'})}">&uArr;</button>
                <button @click="() => {
                    parameters.sort = 'calories-desc'
                    get_query({ sr: 'calories-desc'})}">&dArr;</button></div>
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
    <div class="pagination">
        <button v-for="p in pages" :key="p"
            class="page"
            @click="() => {
                parameters.page = p
                get_query({pg: p})
            }"
        >{{ p + 1 }}</button> 
    </div>
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
.pagination {
    margin: 10px;
    font-size: 1.5em;
    text-align: center;
}
.page {
    margin: 5px;
}
</style>