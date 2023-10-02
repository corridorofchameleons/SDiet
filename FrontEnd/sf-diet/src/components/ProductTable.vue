<script setup>
import router from '@/router'
import { onMounted, ref, watch,reactive } from 'vue'
import axios from 'axios'

const page = reactive({num: 0})
const search = ref('')
const sorting = reactive({sort: ''})
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

function get_query() {
    router.push({ query: { sort: sorting.sort, page: page.num, search: search.value } })
}
function kill_query() {
    page.num = 0
    sorting.sort = ''
    search.value = ''
    router.push({ query: { sort: sorting.sort, page: page.num, search: search.value } })
}
</script>

<template>
    <div class="search">
        <input v-model="search"
            id="s-input"
            placeholder="Поиск"
            @input="get_query"
        >
        <button type="submit"
            @click="kill_query"
        >
            Сбросить поиск
        </button>
        <button class="add-btn"
        @click="router.push({name: 'add_product'})"
    >
        Добавить продукт
        </button>
    </div>

    <div v-if="table_data">
    <table class="table">
        <!-- <thead><th colspan="5" class="t-head">{{ catname.replaceAll('_', ' ') || '<название категории>' }}</th></thead> -->
        <tr>
            <th>Наименование</th>
            <th><div style="display: flex; justify-content: space-around;"><p>Б</p>
                <div class="btns">
                <button @click="() => {
                    sorting.sort = 'protein-asc'
                    get_query()}">&uArr;</button>
                <button @click="() => {
                    sorting.sort = 'protein-desc'
                    get_query()}">&dArr;</button></div>
                </div></th>
            <th><div style="display: flex; justify-content: space-around;"><p>Ж</p>
                <div class="btns">
                <button @click="() => {
                    sorting.sort = 'fats-asc'
                    get_query()}">&uArr;</button>
                <button @click="() => {
                    sorting.sort = 'fats-desc'
                    get_query()}">&dArr;</button></div>
                </div></th>
            <th><div style="display: flex; justify-content: space-around;"><p>У</p>
                <div class="btns">
                <button @click="() => {
                    sorting.sort = 'carbohydrates-asc'
                    get_query()}">&uArr;</button>
                <button @click="() => {
                    sorting.sort = 'carbohydrates-desc'
                    get_query()}">&dArr;</button></div>
                </div></th>
            <th><div style="display: flex; justify-content: space-around;"><p>К</p>
                <div class="btns">
                <button @click="() => {
                    sorting.sort = 'calories-asc'
                    get_query()}">&uArr;</button>
                <button @click="() => {
                    sorting.sort = 'calories-desc'
                    get_query()}">&dArr;</button></div>
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
    <div v-if="pages.length > 1" class="pagination">
        <p class="page">Страница: </p>
        <button class="page"
            @click="() => {
                if (page.num > 1) {
                    page.num -= 1
                    get_query()
                }
            }"
        >&lt;</button>
        <button v-for="p in pages" :key="p"
            class="page"
            @click="() => {
                page.num = p
                get_query()
            }"
        >{{ p + 1 }}</button> 
        <button class="page"
            @click="() => {
                if (page.num < pages.length - 1) {
                    page.num += 1
                    get_query()
                }
            }">&gt;</button>
    </div>
    </div>
</template>

<style scoped>
.search {
    float: left;
}
.add-btn {
    margin-left: 200px;
}
.search input, .search button {
    font-size: 1.1em;
    margin: 15px 5px 15px 5px;
}
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
    display: flex;
    justify-content: center;
    margin: 10px;
    font-size: 1.3em;
    text-align: center;
}
.page {
    margin: 5px;
    height: 25px;
    border: none;
}
button.page {
    font-size: 1em;
    background-color: rgb(255, 255, 255);
    border-radius: 3px;
    font-weight: bold;
}
button.page:active {
    background-color: rgb(37, 37, 37);
}
</style>