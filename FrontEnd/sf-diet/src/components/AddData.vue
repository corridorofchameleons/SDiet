<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios';

const date = ref(new Date())
const rows = ref([])
const total = ref({
    p: 0,
    f: 0,
    c: 0,
    cal: 0
})
const tmp_data = ref(null)
let curid = null


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
                to_be_added: true
                })
}

function removeProduct(id) {
    rows.value[id].to_be_added = false
    setTotal()

    // let cnt = 0
    // for (let i=0; i < rows.value.length; i++) {
    //     if (rows.value[i].to_be_added) {
    //         cnt++
    //     }
    // }
    // if (cnt === 0) {addProduct(0)}
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

    for (let i=0; i < rows.value.length; i++) {
        if (rows.value[i].to_be_added) {
            p += parseFloat(rows.value[i].p)
            f += parseFloat(rows.value[i].f)
            c += parseFloat(rows.value[i].c)
            cal += parseFloat(rows.value[i].cal)
        }
    }

    total.value.p = p.toFixed(1)
    total.value.f = f.toFixed(1)
    total.value.c = c.toFixed(1)
    total.value.cal = cal.toFixed(0)
}

onMounted(() => {
    addProduct(0)
})

</script>

<template>
<div class="wrapper">
    <input v-model="date" 
        type="date" 
        class="date" 
        placeholder="DD-MM-YYYY"
        @input="() => {console.log(date)}">
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
        <tr v-for="row in rows" :key="row.id">
            <td v-if="row.to_be_added" >
                <input v-model="rows[row.id].name" @input="getData(row.id)" @focus="() => {
                        curid = row.id
                        // showList()
                    }" 
                    type="text" class="name" required>
            </td>
            <td v-if="row.to_be_added" >
                <input v-model="rows[row.id].amt" 
                    @focus="() => {
                        curid = row.id
                    }"
                    @input="setAmount"
                    type="number" step="0.1" min="0" class="amount" required>
            </td>
            <td v-if="row.to_be_added" ><input v-model="rows[row.id].p" type="number" min="0" class="calculation" readonly></td>
            <td v-if="row.to_be_added" ><input v-model="rows[row.id].f" type="number" min="0" class="calculation" readonly></td>
            <td v-if="row.to_be_added" ><input v-model="rows[row.id].c" type="number" min="0" class="calculation" readonly></td>
            <td v-if="row.to_be_added" ><input v-model="rows[row.id].cal" type="number" min="0" class="calculation" readonly></td>
            <button v-if="row.to_be_added" @click.prevent="removeProduct(row.id)"
                class="del-btn"
                >X</button>
        </tr>
        </tbody>
        <tfoot>
        <tr>
            <td colspan="2" class="empty"></td>
            <td><input v-model="total.p" type="number" min="0" class="calculation total" readonly></td>
            <td><input v-model="total.f" type="number" min="0" class="calculation total" readonly></td>
            <td><input v-model="total.c" type="number" min="0" class="calculation total" readonly></td>
            <td><input v-model="total.cal" type="number" min="0" class="calculation total" readonly></td>
        </tr>
        </tfoot>
    </table>
    <button class="save-btn">Сохранить</button>
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