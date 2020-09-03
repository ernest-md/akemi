<template >
  <!-- Carrito -->
  <div id="carrito">
    <ul class="nav flex-column ml-n2 mt-3 mb-2">
      <li class="nav-item m-n2">
        <a class="nav-link text-white" href="#">Cart</a>
      </li>
      <li class="nav-item m-n2">
        <a id="item" class="nav-link text-white-50" href="#">{{ items }} Items</a>
      </li>
      <li class="nav-item m-n2">
        <a id="price" class="nav-link text-white-50" href="#">{{ total }} €</a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    items: {
      type: Number
    },

    total: {
      type: Number
    }
  }
};
</script>



<style>
</style>