<script setup lang="ts">
  import type { benchmark_data } from '@/interface';
import { defineProps } from 'vue';
  // import {Chart as ChartJS,
  //   Title,
  //   Tooltip,
  //   Legend,
  //   BarElement,
  //   CategoryScale,
  //   LinearScale
  // } from 'chart.js'

  // import { Bar } from 'vue-chartjs'

  // ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

  defineProps<{ peticion: benchmark_data }>();


</script>

<template>
  <div id="contenedor-tarjeta">
    <h2><span class="texto-bold">Prueba Número: </span> {{ peticion["Orden Peticion"] }}</h2>
    <h3><span class="texto-bold">Tiempo tomado: </span> {{ peticion["Time taken for tests"] }}</h3>
    <h3><span class="texto-bold">Solicitudes Completadas: </span> {{ peticion["Complete requests"] }}</h3>
    <h3><span class="texto-bold">Solicitudes fallidas: </span> {{ peticion["Failed requests"] }}</h3>
    <h3><span class="texto-bold">Total transferido: </span> {{ peticion["Total transferred"] }}</h3>
    <h3><span class="texto-bold">HTML transferido: </span> {{ peticion["HTML transferred"] }}</h3>
    <h3><span class="texto-bold">Peticiones atendidas por segundo:</span> {{ peticion["Requests per second"] }}</h3>
    <h3><span class="texto-bold">Tiempo por peticion individual:</span> {{ peticion["Time per request"] }}</h3>
    <h3><span class="texto-bold">Kbytes recibidos por segundo:</span> {{ peticion["Transfer rate"] }}</h3>

  </div>
</template>

<style scoped lang="sass">

  h2
    letter-spacing: 2px
    font-size: 25px
    margin-bottom: 20px

  .texto-bold
    font-weight: 800
    color: rgba(0, 0, 0, 0.5)

  h3
    font-weight: 800


</style>
