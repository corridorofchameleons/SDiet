<script setup>
import { onMounted, ref } from 'vue'
import ProductTable from './ProductTable.vue';

const cats = ref(null)
const cat_name = ref('')

onMounted(getCats)

async function getCats() {
    const res = await fetch("http://localhost:8000/products/")
    cats.value = await res.json()
}

// function setCat(val) {
//     cat_name.value = val
// }

</script>

<template>
<div class="wrapper">
    <div class="nav-bar-wrapper">
        <h2 class="cats">Категории</h2>
        <router-link v-for="d in cats" :key="d.id"
            :to="{name: 'products_table', 
            params: { id: d.id }, props: true }"
            class="link" 
            active-class="active-link"
        >
            {{ d.name.replaceAll('_', ' ') }}
        </router-link>
    </div>
    <div class="content">
        <ProductTable 
            :catname="cat_name"
        />
    </div>
</div>
</template>

<style scoped>
.wrapper {
    width: auto;
    display: flex;
    padding: 5px;
    background-color: rgb(238, 250, 255);
}
.nav-bar-wrapper {
    display: flex;
    flex-direction: column;
    padding: 0 15px 0 0;
    margin: 5px 10px 5px 0;
    margin-top: 0;
    font-size: 1.2em;
}
.cats {
    margin-top: 0;
    padding-left: 10px;
}
.link {
    margin: 2px;
    padding: 2px 10px;
    color: black;
    text-decoration: none;
    background-color: rgb(228, 228, 228);
    border-radius: 2px;
}
.active-link {
    background-color: white;
}
.link:hover {
    background-color: rgb(255, 255, 255);
}
</style>