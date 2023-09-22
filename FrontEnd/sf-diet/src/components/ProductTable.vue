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

async function getTable() {
    if (cat.value) {
        const res = await fetch("http://localhost:8000/products/" + cat.value)
        table_data.value = await res.json()}
}

</script>

<template>
    <div v-if="table_data">
    <table class="table">
        <!-- <thead><th colspan="5" class="t-head">{{ catname.replaceAll('_', ' ') || '<название категории>' }}</th></thead> -->
        <tr>
            <th>Наименование</th>
            <th>Б</th>
            <th>Ж</th>
            <th>У</th>
            <th>Ккал</th>
        </tr>
        <tbody>
        <tr v-for="r in table_data" :key="r.id">
            <td>{{ r.name }}</td>
            <td class="val-td">{{ r.protein.toFixed(1) }}</td>
            <td class="val-td">{{ r.fats.toFixed(1) }}</td>
            <td class="val-td">{{ r.carbohydrates.toFixed(1) }}</td>
            <td class="val-td">{{ (r.fats * 9.3 + r.protein * 4.2 + r.carbohydrates * 4.2).toFixed(1) }}</td>
        </tr>
        </tbody>
    </table>
</div>
</template>

<style scoped>
.table {
    width: 800px;
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
    width: 70px;
}
</style>