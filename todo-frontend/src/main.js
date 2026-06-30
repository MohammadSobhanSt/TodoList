import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

axios.defaults.baseURL = "127.0.0.1:8000"

createApp(App).use(axios).mount('#app')
