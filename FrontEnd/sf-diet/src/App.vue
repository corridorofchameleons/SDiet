<script setup>
import PageHeader from '@/components/PageHeader.vue';
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
  margin-left: 8px;
  width: 1138px;
}
body {
  min-height: 800px;
}
.content {
  margin-left: 8px;
}
</style>
