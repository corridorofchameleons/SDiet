<script setup>
import PageHeader from '@/components/PageHeader.vue';
import PageFooter from '@/components/PageFooter.vue'
</script>

<template>
  <header>
    <PageHeader/>
  </header>
  <body>
    <router-view/>
  </body>
  <footer>
    <PageFooter/>
  </footer>
</template>

<style>
header, footer {
  margin-left: 8px;
  width: 1138px;
}
body {
  min-height: 800px;
}
</style>
