import axios from 'axios';

export default defineNuxtPlugin(nuxtApp => {
  nuxtApp.provide('axios', axios.create({
    baseURL: 'http://127.0.0.1:8000' 
  }));
});
