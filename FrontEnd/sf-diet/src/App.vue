<script setup>
import PageHeader from '@/components/PageHeader.vue'
import PageFooter from '@/components/PageFooter.vue'

</script>

<template>
  <header>
    <PageHeader/>
  </header>
  <body>
    <div class="content">
      <router-view/>
    </div>
  </body>
  <footer>
    <PageFooter/>
  </footer>
</template>

<style>
header, body, footer {
  margin: 0 auto;
  width: 1138px;
}
body {
  min-height: 800px;
}

</style>
