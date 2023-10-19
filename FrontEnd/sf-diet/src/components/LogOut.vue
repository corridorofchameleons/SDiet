<script setup>
import axios from 'axios';
import router from '@/router';
import { onMounted } from 'vue';

axios.defaults.withCredentials = true

onMounted(() => {
    axios.post('http://localhost:8000/auth/jwt/logout')
    .then((response) => {
    if (response.status === 204) {
        console.log('logout successful')
        router.push({name: 'login'})
    }
    })
    .catch((error) => {
        console.log('something went wrong', error)
    })
})
</script>