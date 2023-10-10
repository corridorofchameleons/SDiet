<script setup>
import { onMounted, ref } from 'vue'

const rows = ref([])

function addProduct(id) {
    rows.value.push({id: id, 
                name: '',
                amt: 0,
                protein: 0,
                fats: 0, 
                carbohydrates: 0,
                calories: 0,
                to_be_added: true
                })
    console.log(rows.value)
}

function removeProduct(id) {
    rows.value[id].to_be_added = false
    console.log(rows.value)
}

onMounted(() => {
    addProduct(0)
})

</script>

<template>
<div class="wrapper">
    <form>
    <table>
        <thead>
        <tr>
            <th>Наименование</th>
            <th>Количество</th>
            <th>Белки</th>
            <th>Жиры</th>
            <th>Углеводы</th>
            <th>Калории</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="row in rows" :key="row.id">
            <td v-if="row.to_be_added" >
                <input v-model="rows[row.id].name" type="text" class="name" required>
            </td>
            <td v-if="row.to_be_added" >
                <input v-model="rows[row.id].amt" type="number" min="0" class="amount" required initial="8">
            </td>
            <td v-if="row.to_be_added" ><input type="number" min="0" class="calculation" readonly></td>
            <td v-if="row.to_be_added" ><input type="number" min="0" class="calculation" readonly></td>
            <td v-if="row.to_be_added" ><input type="number" min="0" class="calculation" readonly></td>
            <td v-if="row.to_be_added" ><input type="number" min="0" class="calculation" readonly></td>
            <button v-if="row.to_be_added" @click.prevent="removeProduct(row.id)">Удалить</button>
        </tr>
        </tbody>
        <tfoot>
        <tr>
            <td colspan="2" class="empty"></td>
            <td>б</td>
            <td>ж</td>
            <td>у</td>
            <td>к</td>
        </tr>
        </tfoot>
    </table>
    <div class="btns">
        <button type="subnit" @click.prevent="addProduct(rows.length)">Добавить</button>
        <button>Сохранить</button>
    </div>
    </form>

</div>
</template>

<style scoped>
input {
    font-size: 1.1em;
}
th {
    text-align: left;
}
td {
    text-align: right;
}
tfoot td {
    font-weight: bold;
    padding-right: 5px;
    background-color: white;
}
.name {
    width: 250px;
}
.amount, .calculation {
    width: 100px;
}
.calculation {
    border: none;
}
.empty {
    background-color: unset;
}
.btns {
    margin: 3px;
}
.btns button {
    margin-right: 3px;
}
</style>