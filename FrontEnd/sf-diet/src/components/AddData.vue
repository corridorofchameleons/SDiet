<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios';
import router from '@/router';
// import router from '@/router';

axios.defaults.withCredentials = true


const date = ref(null)
const history = ref(null)
const limits = ref({
    protein: null,
    fats: null,
    carbohydrates: null,
    calories: null
})

const rows = ref([])
const total_initial = ref(null)
const total = ref({
    p: 0,
    f: 0,
    c: 0,
    cal: 0
})
const tmp_data = ref(null)
let curid = null

function setDate() {
    const d = new Date()
    const day = ("0" + d.getDate()).slice(-2)
    const month = ("0" + (d.getMonth() + 1)).slice(-2)
    const year = d.getFullYear()
    date.value = year + "-" + month + "-" + day
}

async function getHistory() {
    const res = await axios.get("http://localhost:8000/records", 
    {
        params: {
            date: date.value
        },
    })

    .catch((error) => {
        // if (error.response.status === 401) {
            // router.push({name: 'login'})
        // }
        window.alert(error.message)
        router.push({name: 'login'})
    })

    if (res) {
        history.value = res.data

        total_initial.value = {
            p: 0,
            f: 0,
            c: 0,
            cal: 0
        }

        let p = 0, f = 0, c = 0, cal = 0

        for (let i=0; i < history.value.length; i++) {
            p += parseFloat(history.value[i].protein)
            f += parseFloat(history.value[i].fats)
            c += parseFloat(history.value[i].carbohydrates)
            cal += parseFloat(history.value[i].calories)
        }

        total_initial.value.p += p
        total_initial.value.f += f
        total_initial.value.c += c
        total_initial.value.cal += cal
        setTotal()}
}

async function getLimits() {
    const res = await axios.get("http://localhost:8000/limits")
    limits.value.protein = res.data.protein
    limits.value.fats = res.data.fats
    limits.value.carbohydrates = res.data.carbohydrates
    limits.value.calories = res.data.calories
    console.log(limits.value)
}

function addProduct(id) {
    rows.value.push({id: id, 
                name: '',
                amt: null,
                protein: 0,
                fats: 0, 
                carbohydrates: 0,
                calories: 0,
                p: 0,
                f: 0, 
                c: 0,
                cal: 0,
                to_be_added: false,
                to_be_shown: true
                })
}

function removeProduct(id) {
    rows.value[id].to_be_shown = false
    rows.value[id].to_be_added = false
    setTotal()
}

async function getData(id) {
    const res = await axios.get("http://localhost:8000/products/product_list", {
        params: {
            search: rows.value[id].name
        }
    })
    tmp_data.value = res.data

    showList()
    }

function showList() {
    const div = document.getElementById("list")
    div.style.display = "flex"
}

function setValue(row) {
    rows.value[curid].to_be_added = true 
    rows.value[curid].name = row.name 
    rows.value[curid].protein = row.protein 
    rows.value[curid].fats = row.fats
    rows.value[curid].carbohydrates = row.carbohydrates
    rows.value[curid].calories = row.calories 

    setAmount()
    killList()
    tmp_data.value = null
}

function killList() {
    const div = document.getElementById("list")
    div.style.display = "none"
}

function setAmount() {
    rows.value[curid].p = (rows.value[curid].protein * rows.value[curid].amt / 100).toFixed(1) 
    rows.value[curid].f = (rows.value[curid].fats * rows.value[curid].amt / 100).toFixed(1)
    rows.value[curid].c = (rows.value[curid].carbohydrates * rows.value[curid].amt / 100).toFixed(1)
    rows.value[curid].cal = (rows.value[curid].calories * rows.value[curid].amt / 100).toFixed(0)

    setTotal()
}

function setTotal() {
    let p = 0, f = 0, c = 0, cal = 0

    const p_total = document.getElementById("p-total")
    const f_total = document.getElementById("f-total")
    const c_total = document.getElementById("c-total")
    const cal_total = document.getElementById("cal-total")

    for (let i=0; i < rows.value.length; i++) {
        if (rows.value[i].to_be_added) {
            p += parseFloat(rows.value[i].p)
            f += parseFloat(rows.value[i].f)
            c += parseFloat(rows.value[i].c)
            cal += parseFloat(rows.value[i].cal)
        }
    }

    total.value.p = (parseFloat(total_initial.value.p) + parseFloat(p)).toFixed(0)
    total.value.f = (parseFloat(total_initial.value.f) + parseFloat(f)).toFixed(0)
    total.value.c = (parseFloat(total_initial.value.c) + parseFloat(c)).toFixed(0)
    total.value.cal = (parseFloat(total_initial.value.cal) + parseFloat(cal)).toFixed(0)

    if (limits.value.protein && limits.value.protein > total.value.p) {
        p_total.style.backgroundColor = 'rgba(235, 50, 50, .3)'
    }
    else {p_total.style.backgroundColor = 'rgba(50, 235, 50, .3)'}
    if (limits.value.fats && limits.value.fats > total.value.f) {
        f_total.style.backgroundColor = 'rgba(235, 50, 50, .3)'
    }
    else {f_total.style.backgroundColor = 'rgba(50, 235, 50, .3)'}
    if (limits.value.carbohydrates && limits.value.carbohydrates > total.value.c) {
        c_total.style.backgroundColor = 'rgba(235, 50, 50, .3)'
    }
    else {c_total.style.backgroundColor = 'rgba(50, 235, 50, .3)'}
    if (limits.value.calories && limits.value.calories > total.value.cal) {
        cal_total.style.backgroundColor = 'rgba(235, 50, 50, .3)'
    }
    else {cal_total.style.backgroundColor = 'rgba(50, 235, 50, .3)'}
}

function addRecord() {
    let records = []
    for (let i=0; i < rows.value.length; i++) {
        if (rows.value[i].to_be_added) {
            records.push({
                "user_id": 0,
                "date": date.value,
                "name": rows.value[i].name,
                "weight": rows.value[i].amt,
                "protein": rows.value[i].p,
                "fats": rows.value[i].f,
                "carbohydrates": rows.value[i].c,
                "calories": rows.value[i].cal
                })
        }
    }
    axios.post("http://localhost:8000/records/", records)
    rows.value = []
    getHistory()
    addProduct(0)
    router.push({name: 'add_data'})
}

function deleteRecord(id) {
    axios.delete("http://localhost:8000/records/" + id)
    getHistory()
    router.push({name: 'add_data'})
}

// function reLoad() {
//     location.reload()
// }

onMounted(() => {
    addProduct(0)
    setDate()
    getHistory()
    getLimits()
})

</script>

<template>
<div class="wrapper">
    <input v-model="date" 
        type="date" 
        class="date" 
        placeholder="DD-MM-YYYY"
        @input="() => {getHistory()}">
    <button type="submit" @click.prevent="addProduct(rows.length)" class="add-btn">+</button>

    <form>
    <table>
        <thead>
        <tr class="head">
            <th>Наименование</th>
            <th>Вес</th>
            <th>Белки</th>
            <th>Жиры</th>
            <th>Углеводы</th>
            <th>Калории</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="row in history" :key="row.id">
            <td>
                <input v-model="row.name"
                    type="text" class="name" disabled>
            </td>
            <td>
                <input v-model="row.amt" 
                    type="number" step="0.1" min="0" class="amount" disabled>
            </td>
            <td><input v-model="row.protein" type="number" min="0" class="calculation" readonly></td>
            <td><input v-model="row.fats" type="number" min="0" class="calculation" readonly></td>
            <td><input v-model="row.carbohydrates" type="number" min="0" class="calculation" readonly></td>
            <td><input v-model="row.calories" type="number" min="0" class="calculation" readonly></td>
            <button class="del-btn" @click.prevent="deleteRecord(row.id)">Х</button>
        </tr>
        <tr v-for="row in rows" :key="row.id">
            <td v-if="row.to_be_shown" >
                <input v-model="rows[row.id].name" @input="getData(row.id)" @focus="() => {
                        curid = row.id
                        // showList()
                    }" 
                    type="text" class="name" required>
            </td>
            <td v-if="row.to_be_shown" >
                <input v-model="rows[row.id].amt" 
                    @focus="() => {
                        curid = row.id
                    }"
                    @input="setAmount"
                    type="number" step="0.1" min="0" class="amount" required>
            </td>
            <td v-if="row.to_be_shown" ><input v-model="rows[row.id].p" type="number" min="0" class="calculation" readonly></td>
            <td v-if="row.to_be_shown" ><input v-model="rows[row.id].f" type="number" min="0" class="calculation" readonly></td>
            <td v-if="row.to_be_shown" ><input v-model="rows[row.id].c" type="number" min="0" class="calculation" readonly></td>
            <td v-if="row.to_be_shown" ><input v-model="rows[row.id].cal" type="number" min="0" class="calculation" readonly></td>
            <button v-if="row.to_be_shown" @click.prevent="removeProduct(row.id)"
                class="del-btn"
                >X</button>
        </tr>
        </tbody>
        <tfoot>
        <tr>
            <td colspan="2" class="empty">Всего</td>
            <td><input id="p-total" v-model="total.p" type="number" min="0" class="calculation total" readonly></td>
            <td><input id="f-total" v-model="total.f" type="number" min="0" class="calculation total" readonly></td>
            <td><input id="c-total" v-model="total.c" type="number" min="0" class="calculation total" readonly></td>
            <td><input id="cal-total" v-model="total.cal" type="number" min="0" class="calculation total" readonly></td>
        </tr>
        <tr>
            <td colspan="2" class="empty">Цель</td>
            <td><input v-model="limits.protein" type="number" class="calculation total limits" readonly></td>
            <td><input v-model="limits.fats" type="number" class="calculation total limits" readonly></td>
            <td><input v-model="limits.carbohydrates" type="number" class="calculation total limits" readonly></td>
            <td><input v-model="limits.calories" type="number" class="calculation total limits" readonly></td>
        </tr>
        </tfoot>
    </table>
    <button class="save-btn" @click.prevent="() => {
        addRecord()
        // reLoad()
        }">Сохранить</button>
    </form>

    <div class="list" id="list">
        <a @click="killList">Закрыть</a>
        <button v-for="row in tmp_data" :key="row.id"
            @click="setValue(row)"
        >
            {{ row.name }}
        </button>
    </div>
</div>
</template>

<style scoped>
.date {
    height: 20px;
    margin: 0 0 10px 4px;
    width: 100px;
}
.title {
    position: relative;
}
.wrapper {
    display: flex;
    flex-flow: column;
}
input {
    font-size: 1em;
}
th {
    text-align: left;
}
td {
    text-align: right;
}

.name {
    min-width: 250px;
}
.amount, .calculation, th {
    width: 100px;
}
th:first-of-type {
    width: 250px;
}
.calculation {
    border: none;
    text-align: right;
}
.total {
    font-weight: bold;
}
.empty {
    font-weight: bold;
    font-size: 1em;
    padding-right: 6px;
    background-color: unset;
}
.add-btn {
    width: 40px;
    margin: 4px 0 10px 4px;
    font-size: 1.5em;
    font-weight: bold;
    color: rgb(47, 255, 92);
    background-color: white;
    border: 1.5px solid black;
    border-radius: 5px;
}
.del-btn {
    font-size: 1em;
    font-weight: bold;
    color: rgb(252, 45, 45);
    margin-top: 4px;
    background-color: unset;
    border: none;
}
.save-btn {
    font-size: 1em;
    margin: 10px 0 0 4px;
}
.list {
    display: none;
    flex-flow: column;
    position: relative;
    top: -60px;
    left: 2px;
    width: 500px;
}
.list a {
    font-size: 0.9em;
    padding: 0 0 2px 5px;
    color: rgb(9, 106, 197);
    text-decoration: underline;
    background-color: white;
}
.list button {
    text-align: left;
    border: none;
    background-color: white;
}
.list button:hover {
    background-color: rgb(175, 175, 175);
}
input:focus {
    outline: none;
}

</style>