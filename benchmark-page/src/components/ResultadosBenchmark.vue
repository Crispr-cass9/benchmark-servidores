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
    <h2>Prueba Número: {{ peticion["Orden Peticion"] }}</h2>
    <h3>Tiempo tomado: {{ peticion["Time taken for tests"] }}</h3>
    <h3>Solicitudes Completadas: {{ peticion["Complete requests"] }}</h3>
    <h3>Solicitudes fallidas: {{ peticion["Failed requests"] }}</h3>
    <h3>Total transferido: {{ peticion["Total transferred"] }}</h3>
    <h3>HTML transferido: {{ peticion["HTML transferred"] }}</h3>
    <h3>Peticiones atendidas por segundo: {{ peticion["Requests per second"] }}</h3>
    <h3>Tiempo por peticion individual: {{ peticion["Time per request"] }}</h3>
    <h3>Kbytes recibidos por segundo: {{ peticion["Transfer rate"] }}</h3>

  </div>
</template>

<style scoped>

</style>
