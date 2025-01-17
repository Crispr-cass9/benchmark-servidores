<script setup lang="ts">
import { ref } from 'vue';
import ResultadosBenchmark from './components/ResultadosBenchmark.vue';
import type { benchmark_data } from './interface';

  const peticiones = ref<benchmark_data[]>([]);
  async function pedir_datos(enlace:string, cantidad_peticiones:string, concurrencia:string, cantidad_pruebas:string){
    const peticion = await fetch('http://127.0.0.1:5000/ejecutar-pruebas', {
      method:'POST',
      headers: {
      'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        'enlace': enlace, 
        'cantidad_peticiones': cantidad_peticiones,
        'concurrencia': concurrencia,
        'cantidad_pruebas': cantidad_pruebas
      })
    })
    console.log(peticion);
    
    const data = await peticion.json()
    console.log(data);
    peticiones.value = data
    return data
  }

  const entrada_enlace = ref<string>('')
  const entrada_cantidad_peticiones = ref<string>('')
  const entrada_concurrencia = ref<string>('')
  const entrada_cantidad_pruebas = ref<string>('')
</script>

<template>
<header>

  <div id="logo-nav">
    <h2>Benchmarking</h2>
    <nav>
      <a href="#">Features</a>
      <a href="#">Pricing</a>
      <a href="#">Resources</a>
    </nav>

  </div>

  <div id="usuario-entrada">
    <a href="#">Login</a>
    <a href="#">Sign Up</a>
  </div>
</header>  

<div id="seccion-principal">

  <div id="texto">
    
    <h2 id="titulo">More than <br>benchmark</h2>
    
    <p id="contenido">Benchmark your servers and receive optimization advice from professionals.</p>
    
    <button>Get Started</button>

  </div>


  <img src="./img/illustration-working.svg" alt="">

</div>

<div id="contenedor-fondo-color">

  <div id="seccion-input">

    <div id="contenedor-input-btn">
      <input  v-model="entrada_enlace" id="entrada-enlace" type="text" placeholder="Enlace del servidor">
      <input  v-model="entrada_cantidad_peticiones" id="entrada-link" type="text" placeholder="N° de peticiones">
      <input  v-model="entrada_concurrencia" id="entrada-link" type="text" placeholder="N° de concurrencia">
      <input  v-model="entrada_cantidad_pruebas" id="entrada-link" type="text" placeholder="N° de pruebas">
      <button @click="pedir_datos(entrada_enlace, entrada_cantidad_peticiones, entrada_concurrencia, entrada_cantidad_pruebas)">Shorten It!</button>
    </div>
    <h3 class="error">Este es un error de referencia</h3>
    
  </div>

  <div id="seccion-links-acortados" v-for="(resultado, index) in peticiones" :key = 'index'>
    <ResultadosBenchmark :peticion="resultado"></ResultadosBenchmark>
  </div>

  <div id="seccion-estadisticas-avanzadas">
    <h3>Advanced estatistics</h3>
    <h4>Track how your links are performing across the web with our advanced stadistics dashboard.</h4>  
  </div>


  <div id="seccion-tarjetas">

    <hr>
    
    <div class="contenedor-tarjeta">
    
      <div class="circulo">
        <img class="icono-tarjeta" src="./img/icon-brand-recognition.svg" alt="">
      </div>
    
      <h3 class="titulo-tarjeta">Accede a tus datos</h3>
      
      <p>Todos tus benchmark son almacenados en una base de datos para que puedas acceder a ellos en un futuro
      </p>
    
    </div>

    <div class="contenedor-tarjeta">
    
      <div class="circulo">
        <img class="icono-tarjeta" src="./img/icon-detailed-records.svg" alt="">
      </div>
    
      <h3 class="titulo-tarjeta">Detailed Records</h3>
      
      <p>Gain insights into who is clicking your links. Knowing when and where 
        people engage with your content helps inform better decisions.
      </p>
    
    </div>

    <div class="contenedor-tarjeta">
    
      <div class="circulo">
        <img class="icono-tarjeta" src="./img/icon-fully-customizable.svg" alt="">
      </div>
    
      <h3 class="titulo-tarjeta">Fully Customizable</h3>
      
      <p>
        Improve brand awareness and content discoverability through customizable links, supercharging audience engagement.
      </p>
    
    </div>

  </div>

  <div id="seccion-boost">

    <h2>Boost your links today</h2>
    <button>Get Started</button>

  </div>

  <footer>
    <h2>Shortly</h2>

    <div id="contenedor-nav-footer-redes">

      <nav>

        <div class="submenu">
          <h4>Features</h4>
          <a href="#">Link shortening</a>
          <a href="#">Branded Links</a>
          <a href="#">Analytics</a>
        </div>

        <div class="submenu">
          <h4>Resources</h4>
          <a href="#">Blog</a>
          <a href="#">Developers</a>
          <a href="#">Support</a>
        </div>

        <div class='submenu'>
          <h4>Company</h4>
          <a href="#">About</a>
          <a href="#">Our Team</a>
          <a href="#">Careers</a>
          <a href="#">Contact</a>
        </div>
      </nav>

      <div id="contenedor-redes">
        
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"><path fill="#FFF" d="M22.675 0H1.325C.593 0 0 .593 0 1.325v21.351C0 23.407.593 24 1.325 24H12.82v-9.294H9.692v-3.622h3.128V8.413c0-3.1 1.893-4.788 4.659-4.788 1.325 0 2.463.099 2.795.143v3.24l-1.918.001c-1.504 0-1.795.715-1.795 1.763v2.313h3.587l-.467 3.622h-3.12V24h6.116c.73 0 1.323-.593 1.323-1.325V1.325C24 .593 23.407 0 22.675 0z"/></svg>

        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="20"><path fill="#FFF" d="M24 2.557a9.83 9.83 0 01-2.828.775A4.932 4.932 0 0023.337.608a9.864 9.864 0 01-3.127 1.195A4.916 4.916 0 0016.616.248c-3.179 0-5.515 2.966-4.797 6.045A13.978 13.978 0 011.671 1.149a4.93 4.93 0 001.523 6.574 4.903 4.903 0 01-2.229-.616c-.054 2.281 1.581 4.415 3.949 4.89a4.935 4.935 0 01-2.224.084 4.928 4.928 0 004.6 3.419A9.9 9.9 0 010 17.54a13.94 13.94 0 007.548 2.212c9.142 0 14.307-7.721 13.995-14.646A10.025 10.025 0 0024 2.557z"/></svg>

        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"><path fill="#FFF" d="M12 0C5.373 0 0 5.372 0 12c0 5.084 3.163 9.426 7.627 11.174-.105-.949-.2-2.405.042-3.441.218-.937 1.407-5.965 1.407-5.965s-.359-.719-.359-1.782c0-1.668.967-2.914 2.171-2.914 1.023 0 1.518.769 1.518 1.69 0 1.029-.655 2.568-.994 3.995-.283 1.194.599 2.169 1.777 2.169 2.133 0 3.772-2.249 3.772-5.495 0-2.873-2.064-4.882-5.012-4.882-3.414 0-5.418 2.561-5.418 5.207 0 1.031.397 2.138.893 2.738a.36.36 0 01.083.345l-.333 1.36c-.053.22-.174.267-.402.161-1.499-.698-2.436-2.889-2.436-4.649 0-3.785 2.75-7.262 7.929-7.262 4.163 0 7.398 2.967 7.398 6.931 0 4.136-2.607 7.464-6.227 7.464-1.216 0-2.359-.631-2.75-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146C9.57 23.812 10.763 24 12 24c6.627 0 12-5.373 12-12 0-6.628-5.373-12-12-12z"/></svg>

        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"><path fill="#FFF" d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>

      </div>

    </div>


    <div class="attribution">
      Challenge by <a href="https://www.frontendmentor.io?ref=challenge" target="_blank">Frontend Mentor</a>. 
      Coded by <a href="#">Your Name Here</a>.
    </div>
  </footer>



</div>
</template>

<style scoped lang="sass">
// Colores 

$Cyan: hsl(180, 66%, 49%)
$Dark-Violet: hsl(257, 27%, 26%)
$Red: hsl(0, 87%, 67%)
$Gray: hsl(0, 0%, 75%)
$Grayish-Violet: hsl(257, 7%, 63%)
$Very-Dark-Blue: hsl(255, 11%, 22%)
$Very-Dark-Violet: hsl(260, 8%, 14%)

// Variable para controlar el padding de los laterales

$espacio-lateral: 250px

@mixin generic-btn($border-radius, $font-size)
    background-color: $Cyan
    padding: 7px 18px
    border-radius: $border-radius
    color: white  
    transition: background-color .2s ease-in-out
    border: none
    font-weight: 800
    letter-spacing: 1px
    font-size: $font-size
    cursor: pointer


    &:hover
        background-color:  hsl(180, 66%, 65%)
    

*
    margin: 0
    padding: 0
    box-sizing: border-box
    font-family: "Poppins", sans-serif
    color: $Very-Dark-Blue

body
    display: flex
    flex-direction: column
    align-items: center

header
    height: 85px
    width: 100%
    display: flex
    flex-direction: row
    padding: 0 $espacio-lateral
    align-items: center
    justify-content: space-between

#logo-nav
    display: flex
    flex-direction: row
    gap: 45px


    h2
        color: $Very-Dark-Blue
        font-size: 40px

    nav
        display: flex
        flex-direction: row
        align-items: center
        justify-content: center
        gap: 20px
        
        a
            text-decoration: none
            font-size: 20px
            color: $Grayish-Violet
            font-weight: 700
            letter-spacing: 1px
            transition: color .2s ease-in-out

            &:hover
                color: $Dark-Violet

#usuario-entrada
    
    display: flex
    flex-direction: row
    gap: 30px
    align-items: center

    a
        text-decoration: none
        font-size: 20px
        color: $Grayish-Violet
        font-weight: 700
        letter-spacing: 1px
    
    a:nth-child(1)
        transition: color .2s ease-in-out

        &:hover
            color: $Dark-Violet

    a:nth-child(2)
        background-color: $Cyan
        padding: 7px 18px
        border-radius: 50px
        color: white  
        transition: background-color .2s ease-in-out

        &:hover
            background-color:  hsl(180, 66%, 65%) 

#seccion-principal
    display: flex
    flex-direction: row
    justify-content: space-between
    align-items: center
    padding: 50px 0 0 $espacio-lateral
    overflow: hidden
    width: 100%

    img
        position: relative
        right: -70px


#texto
    display: flex
    flex-direction: column
    width: 33%
    min-width: 550px

    #titulo
        font-size: 70px
        font-weight: 800
        line-height: 80px
    
    #contenido
        font-size: 20px
        color: $Gray
        font-weight: 700
        margin: 5px 0 30px 0

    button
        @include generic-btn(50px, 20px)
        width: 200px

#contenedor-fondo-color
    width: 100%
    display: flex
    flex-direction: column
    align-items: center
    margin-top: 200px
    background-color: #f0f1f6
        
#seccion-input
    background-image: url('./img/bg-shorten-desktop.svg')
    background-repeat: no-repeat
    background-size: cover
    background-color: $Dark-Violet
    height: fit-content
    display: flex
    flex-direction: column
    justify-content: center
    align-items: center
    width: calc( 100vw - $espacio-lateral*2 )
    height: 20vh
    border-radius: 15px
    position: relative
    margin-top: -100px

#contenedor-input-btn
    width: 95%
    display: flex
    gap: 40px
    height: fit-content
    flex-direction: row
    justify-content: center
    align-items: center

    input
        border: none
        outline: none
        height: 60px
        border-radius: 10px
        width: 80%
        padding: 0 30px
        font-size: 20px

    button
        @include generic-btn(10px, 20px)
        height: 100%
        width: 15%
    
.error
    position: absolute
    color: red
    font-weight: 400
    font-size: 20px
    left: 4%
    bottom: 15%
    display: none   

#seccion-links-acortados
    width: 100%
    padding: 0 $espacio-lateral
    height: fit-content

    .contenedor-link-acortado
        width: 100%
        margin-top: 50px
        display: flex
        flex-direction: row
        align-items: center
        justify-content: space-between
        padding: 0 30px
        height: 70px
        background-color: white
        border-radius: 10px

    .link-original
        font-size: 20px
        font-weight: 500
        letter-spacing: 1px

    .resultado-copiar
        display: flex
        flex-direction: row
        height: 100%
        gap: 40px
        align-items: center

        .link-acortado
            font-size: 20px
            color: $Cyan
            font-weight: 700

        .btn-copiar
            background-color: $Cyan
            height: 70%
            width: 80px
            border-radius: 10px
            border: none
            color: white
            font-weight: 800
            font-size: 18px
            letter-spacing: 1px
            cursor: pointer


#seccion-estadisticas-avanzadas
    margin-top: 15vh
    width: 100%
    padding: 0 $espacio-lateral
    display: flex
    flex-direction: column
    align-items: center

    h3
        text-align: center
        font-size: 50px
        margin-bottom: 10px

    h4
        text-align: center
        font-size: 23px
        color: $Gray
        width: 50%  
        margin-bottom: 20px
        line-height: 35px
        font-weight: 500


#seccion-tarjetas
    display: flex
    flex-direction: row
    justify-content: center
    align-items: center
    height: 50vh
    width: 100%
    gap: 30px

    hr
        width: 60%
        border: solid $Cyan 4px
        border-radius: 10px
        position: absolute

    .contenedor-tarjeta
        background-color: white
        width: 20%
        aspect-ratio: 4/3
        position: relative
        z-index: 10
        padding: 30px
    
    .circulo
        width: 80px
        aspect-ratio: 1/1
        border-radius: 50%
        display: flex
        justify-content: center
        align-items: center
        background-color: $Dark-Violet
        position: absolute
        top: -15%

    .titulo-tarjeta
        margin: 40px 0 20px 0
        font-size: 22px
        letter-spacing: 1px
    
    p
        letter-spacing: 1px
        color: $Gray
        font-weight: 700
        font-size: 17px
        line-height: 25px

    .contenedor-tarjeta:nth-child(4)
        margin-top: 100px

    .contenedor-tarjeta:nth-child(2)
        margin-bottom: 100px
    
#seccion-boost
    width: 100%
    height: 300px
    background-image: url('./img/bg-boost-desktop.svg')
    background-repeat: no-repeat
    background-size: cover
    background-color: $Dark-Violet
    display: flex
    flex-direction: column
    align-items: center
    justify-content: center

    h2
        font-size: 50px
        font-weight: 800
        color: white
        letter-spacing: 1px
        text-shadow: 4px 4px 4px black
    
    button
        @include generic-btn(40px, 25px)
        margin-top: 30px
    
footer
    width: 100vw
    height: 30vh
    background-color: $Very-Dark-Violet
    display: flex
    flex-direction: row
    padding: 60px $espacio-lateral 0 $espacio-lateral
    justify-content: space-between

    h2
        font-size: 50px
        text-shadow: 4px 4px 4px black
        color: white


#contenedor-nav-footer-redes
    display: flex
    flex-direction: row
    gap: 120px

    nav
        display: flex
        flex-direction: row
        gap: 60px

        .submenu
            display: flex
            flex-direction: column
            gap: 15px

            h4
                color: white
                font-size: 20px
            
            a
                color: $Gray
                text-decoration: none
                transition: color .1s ease-in-out

                &:hover
                    color: $Cyan
#contenedor-redes
    display: flex
    flex-direction: row
    gap: 30px

    svg
        
        cursor: pointer

        path
            width: 40px !important
            height: 40px !important
            transition: fill .1s ease-in-out

        &:hover path
            fill: $Cyan
            
    
    
.attribution
    display: none
        
</style>
