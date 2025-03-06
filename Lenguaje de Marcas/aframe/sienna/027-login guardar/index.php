<?php 
    // Archivo principal que contiene las llamadas a los componentes y la carga del contenido aframe en formato estático html
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Sienna</title>
    <script src="https://aframe.io/releases/1.6.0/aframe.min.js"></script>
    <script src="https://unpkg.com/aframe-physics-system-fork/dist/aframe-physics-system.min.js"></script>
    <link rel="stylesheet" href="estilo/estilo.css">
  </head>
  <body>
    <div id="instruction">Click to enter VR / Engage Pointer Lock</div>
     
    <?php include "componentes/login/login.php"; ?>
    
    <?php include "componentes/guardar/guardar.php"; ?>

	 with "shadow" attribute and physics with "physics" -->
    <a-scene shadow="type: pcfsoft" physics="gravity: -9.8;">
      <a-assets>
        <!-- Define mixins for box materials -->
        <a-mixin
          id="material1"
          material="src: img/bloque.jpg; color: #ffcccc;"
        ></a-mixin>
        <a-mixin
          id="material2"
          material="src: img/bloque.jpg; color: #ccffcc;"
        ></a-mixin>
        <a-mixin
          id="material3"
          material="src: img/bloque.jpg; color: #ccccff;"
        ></a-mixin>
      </a-assets>

      <!-- Sky -->
      <a-sky color="#ECECEC"></a-sky>

      <!-- Directional "Sun" Light -->
      <!-- castShadow must be true to project shadows -->
      <a-entity
        light="type: directional; intensity: 1; castShadow: true"
        position="10 15 10"
      ></a-entity>

      <!-- Optional: Ambient light for a bit of global illumination -->
      <a-entity
        light="type: ambient; intensity: 0.3"
      ></a-entity>

      <!-- Player Rig -->
      <a-entity
        id="player"
        dynamic-body="mass: 5; shape: box;"
        position="0 1 0"
        wasd-controls
        look-controls
      >
        <!-- The camera -->
        <a-entity id="camera" camera>
          <a-cursor
            id="cursor"
            fuse="false"
            raycaster="objects: .clickable"
            material="color: black; shader: flat"
            geometry="primitive: ring; radiusInner: 0.005; radiusOuter: 0.01"
          ></a-cursor>
        </a-entity>
      </a-entity>
    </a-scene>

   <script src="codigo/codigo.js"></script>
  </body>
</html>